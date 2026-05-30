# Repository Instructions

## Shape

- This repo stores agent skills, not an application; each skill lives in its own directory with a required `SKILL.md` and optional `references/`, `scripts/`, and `assets/` resources.
- Root-level skills currently include `go-resty/` and `model-provider-search/`; `.claude/skills/` contains bundled helper skills used while working on this repo.
- Keep detailed API/reference material out of `SKILL.md` when possible; use `references/` and point agents to the exact file to read on demand.

## Verification

- Use `prek run --all-files` as the repository-wide check; this is the only configured hook runner.
- Validate the hook config explicitly with `prek validate-config prek.toml`; plain `prek validate-config` may print `No configs to check` in this repo.
- `prek list` shows the effective hooks, including the commit-message `committed` hook.
- Hooks in `prek.toml` exclude `^\.(claude|opencode|kilo)/`, so edits under `.claude/skills/` are not covered by the normal pre-commit checks.
- Do not add/remove hooks or exclusions in `prek.toml` just to make checks pass; these hooks are intentional, so fix the underlying issue instead.

## Skill Authoring Notes

- Skill frontmatter should include `name` and `description`; names are lowercase kebab-case, and descriptions should say what the skill does and when to use it.
- `.claude/skills/skill-creator/scripts/validate-metadata.py` is currently incomplete: running it raises an `IndentationError`, so do not rely on it until fixed.

## Commit Gotchas

- `prek.toml` enables a `commit-msg` hook from `crate-ci/committed`; use conventional-style commit messages such as `docs: add skill instructions`.
