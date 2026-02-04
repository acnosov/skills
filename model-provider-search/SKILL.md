---
name: model-provider-search
description: Search models.json to find all providers offering a specific AI model. Extracts and displays provider information including model ID, name, costs, context limits, and reasoning or tool call capabilities. Use when user asks to find providers for a model, check who offers a specific model, or search for model availability across providers.
---

# Model Provider Search

## Overview

This skill extracts provider information from `models.json` for a specified AI model, displaying results in a markdown table format with key details: provider name/ID, model ID/name, reasoning/calling capabilities, context/output limits, and pricing info.

## Workflow

When searching for a provider for a model:

1. **Extract model pattern**: Parse the user's request to identify the model name (e.g., "kimi-k2.5", "claude-sonnet-4.5")
2. **Run search script**: Execute `scripts/search_providers.py` with the model pattern
3. **Display results**: The script outputs a formatted markdown table

## Usage

### Direct script execution

Run the search script with the model pattern:

```bash
python scripts/search_providers.py <model-pattern>
```

Examples:
- `python scripts/search_providers.py kimi-k2.5` - Search for Kimi K2.5
- `python scripts/search_providers.py gpt-4o` - Search for GPT-4o
- `python scripts/search_providers.py claude` - Search for any Claude model

### File location

The script searches `/home/ac/.cache/opencode/models.json` by default. This path can be modified in the script if needed.

## Search Logic

The search matches the provided pattern against:
- Model IDs (case-insensitive)
- Model names (case-insensitive)

Results include models where the pattern appears anywhere in the ID or name.

## Output Format

The output is a markdown table with columns:
- Provider Name: Human-readable provider name
- Provider ID: Machine-readable provider identifier
- Model ID: Model identifier used by the provider
- Model Name: Human-readable model name
- Reasoning: Whether the model supports reasoning/chain-of-thought
- Tool Call: Whether the model supports function/tool calling
- Context: Maximum context window size
- Output: Maximum output tokens
- Cost In: Input token cost (per million)
- Cost Out: Output token cost (per million)

## Resources

### scripts/search_providers.py

Executable Python script that performs the search and displays results table. Can be run directly or via Bash tool.