# sbpro-internetarchive-openlibrary-7cbfb812

A coding-agent eval task from [ugly-studio](https://github.com/Effective-Nihilists). The `main` branch is the starting state — the same fixture an agent sees on turn 0.

**Kind:** `bug-fix`  •  **Tags:** `swe-bench-pro`, `python`, `agentic`

## Prompt

> Read TICKET.md, then explore the codebase and fix the issue. The grader will apply your patch inside the official SWE-bench Pro Docker image and run the tests.

## Success criteria

Edits to source files make the fail_to_pass tests pass without regressing pass_to_pass tests, when applied via the SWE-bench Pro grader. Source: instance_internetarchive__openlibrary-7cbfb812ef0e1f9716e2d6e85d538a96fcb79d13-vfa6ff903cb27f336e17654595dd900fa943dcd91

## Budget

- Max turns: 60
- Max cost (USD): 6
- Timeout: 1800s

## Branches

Each eval run pushes a branch named `<model-slug>-<unix-timestamp>` (e.g. `opus-4-7-1745764987`, `auto-1745765012`). Diff any branch against `main` to see what that model produced.

## Local run

```bash
npm install
npm test  # if defined — see package.json
```

## Grading

If `eval/check.ts` exists, the eval harness runs it after the agent finishes. It returns a deterministic pass/fail scorecard.
