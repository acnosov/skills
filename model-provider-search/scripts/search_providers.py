#!/usr/bin/env python3
"""
Search models.json for providers offering a specific model.
"""

import json
import sys
import re
import os


def search_providers(file_path, model_pattern):
    """
    Search for providers that offer models matching the given pattern.

    Args:
        file_path: Path to models.json file
        model_pattern: Model name/ID to search for (supports regex-like patterns)

    Returns:
        List of provider model entries with details
    """
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    results = []
    pattern = model_pattern.lower()

    # Normalize pattern to handle variations like k2.5, k2-5, k2p5
    normalized_pattern = pattern.replace(".", "").replace("-", "").replace("p", "")

    for provider_id, provider_data in data.items():
        provider_name = provider_data.get("name", provider_id)
        api = provider_data.get("api", "N/A")
        models = provider_data.get("models", {})

        for model_id, model_info in models.items():
            # Check if model matches the pattern
            id_lower = model_id.lower()
            name_lower = model_info.get("name", "").lower()

            # Normalize id/name for comparison (remove dots, dashes, convert p to nothing)
            id_normalized = id_lower.replace(".", "").replace("-", "").replace("p", "")
            name_normalized = (
                name_lower.replace(".", "").replace("-", "").replace("p", "")
            )

            # Pattern matching: check both exact match and normalized comparison
            is_match = (
                pattern in id_lower
                or pattern in name_lower
                or normalized_pattern in id_normalized
                or normalized_pattern in name_normalized
            )

            if is_match:
                cost = model_info.get("cost", {})
                limit = model_info.get("limit", {})

                results.append(
                    {
                        "provider_name": provider_name,
                        "provider_id": provider_id,
                        "model_id": model_id,
                        "model_name": model_info.get("name", "N/A"),
                        "reasoning": model_info.get("reasoning", False),
                        "tool_call": model_info.get("tool_call", False),
                        "context": limit.get("context", "N/A"),
                        "output": limit.get("output", "N/A"),
                        "cost_in": cost.get("input", "N/A"),
                        "cost_out": cost.get("output", "N/A"),
                    }
                )

    # Sort by provider name
    results.sort(key=lambda x: x["provider_name"])
    return results


def print_table(results):
    """Print results as markdown table."""
    if not results:
        print("No providers found for this model.")
        return

    print(f"Found {len(results)} providers:\n")
    print(
        "| Provider Name | Provider ID | Model ID | Model Name | Reasoning | Tool Call | Context | Output | Cost In | Cost Out |"
    )
    print(
        "|---------------|-------------|----------|------------|-----------|-----------|---------|--------|---------|----------|"
    )

    for r in results:
        print(
            f"| {r['provider_name']} | {r['provider_id']} | {r['model_id']} | {r['model_name']} | {r['reasoning']} | {r['tool_call']} | {r['context']} | {r['output']} | {r['cost_in']} | {r['cost_out']} |"
        )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python search_providers.py <model_pattern>")
        print("Example: python search_providers.py kimi-k2.5")
        sys.exit(1)

    model_pattern = sys.argv[1]

    # XDG Base Directory Specification: default for cache is ~/.cache
    cache_home = os.environ.get("XDG_CACHE_HOME", os.path.expanduser("~/.cache"))
    default_path = os.path.join(cache_home, "opencode", "models.json")

    results = search_providers(default_path, model_pattern)
    print_table(results)
