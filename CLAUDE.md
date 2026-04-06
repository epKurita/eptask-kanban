# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Project Does

`backlog_to_vibe.py` is a single-file migration utility that fetches open issues from the **Backlog** project management API and exports them to multiple formats for import into **Vibe** (kanban tool).

## Running the Script

```bash
# Activate the virtual environment first
source venv/bin/activate

# Run the migration
python3 backlog_to_vibe.py
```

## Configuration

All configuration is via `.env` in the project root:

```
BACKLOG_BASE_URL=https://<space>.backlog.com
BACKLOG_API_KEY=<your-api-key>
BACKLOG_ASSIGNEE=<userId or display name>   # optional, filters by assignee
BACKLOG_PROJECT_ID=<numeric-id>             # optional, filters by project
```

`BACKLOG_ASSIGNEE` can be either a numeric Backlog user ID or a string userId/name — the script resolves it via `/api/v2/users`.

## Output Files

Running the script produces 6 files in the project root:

| File | Contents |
|---|---|
| `vibe_import.json` | All open tasks as a flat JSON array |
| `vibe_import_parents.json` | Only parent tasks (no `parentIssueId`) |
| `vibe_import_children.json` | Only subtasks (have `parentIssueId`) |
| `vibe_import_grouped.json` | Summary stats + parents + children in one file |
| `vibe_import.md` | All tasks as human-readable markdown |
| `vibe_import_parent_child.md` | Hierarchical markdown (parents then children) |

## Architecture

The script is a linear pipeline:

1. **Config load** — reads `.env` via `python-dotenv`
2. **Assignee resolution** — `resolve_assignee_id()` calls `/api/v2/users` to convert name→numeric ID
3. **Fetch** — `backlog_get_issues()` calls `/api/v2/issues` (max 100, sorted by updated desc)
4. **Filter** — `is_closed_issue()` drops issues with status `closed/完了/処理済み/resolved`
5. **Transform** — `backlog_issue_to_vibe_task()` maps each Backlog issue to a `VibeTask` dataclass; the description field embeds the Backlog metadata as plaintext
6. **Split** — `split_parent_child_tasks()` separates tasks by whether `parent_issue_id` is set
7. **Export** — 4 JSON exporters + 2 markdown exporters write to disk

Exit codes: `0` = success, `1` = missing config, `2–3` = assignee resolution error, `4–5` = issue fetch error.

## Dependencies

```bash
pip install requests python-dotenv
```
