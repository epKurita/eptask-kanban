#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import Any, Dict, List, Optional, Tuple

import requests
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")


@dataclass
class VibeTask:
    title: str
    description: str
    source_key: str
    source_url: str
    source_status: str
    priority: str
    assignee: str
    due_date: Optional[str]
    parent_issue_id: Optional[int] = None
    source_issue_id: Optional[int] = None


def backlog_get(
    base_url: str,
    api_key: str,
    endpoint: str,
    params: Optional[Dict[str, Any]] = None,
) -> Any:
    url = f"{base_url.rstrip('/')}{endpoint}"
    merged_params = {"apiKey": api_key}
    if params:
        merged_params.update(params)

    resp = requests.get(url, params=merged_params, timeout=30)
    resp.raise_for_status()
    return resp.json()


def backlog_get_users(base_url: str, api_key: str) -> List[Dict[str, Any]]:
    return backlog_get(base_url, api_key, "/api/v2/users")


def resolve_assignee_id(
    base_url: str,
    api_key: str,
    assignee_raw: str,
) -> Optional[int]:
    """
    assignee_raw が数値ならそのまま使う。
    数値でなければ userId または name から /api/v2/users を引いて解決する。
    """
    assignee_raw = assignee_raw.strip()
    if not assignee_raw:
        return None

    if assignee_raw.isdigit():
        return int(assignee_raw)

    users = backlog_get_users(base_url, api_key)
    lowered = assignee_raw.lower()

    for user in users:
        user_id = str(user.get("userId", "")).strip().lower()
        name = str(user.get("name", "")).strip().lower()
        if lowered == user_id or lowered == name:
            return user.get("id")

    return None


def backlog_get_issues(
    base_url: str,
    api_key: str,
    assignee_id: Optional[int] = None,
    project_id: Optional[int] = None,
    count: int = 100,
) -> List[Dict[str, Any]]:
    params: Dict[str, Any] = {
        "count": count,
        "sort": "updated",
        "order": "desc",
    }

    if assignee_id is not None:
        params["assigneeId[]"] = assignee_id

    if project_id is not None:
        params["projectId[]"] = project_id

    return backlog_get(base_url, api_key, "/api/v2/issues", params=params)


def is_closed_issue(issue: Dict[str, Any]) -> bool:
    status_name = (issue.get("status") or {}).get("name", "").strip().lower()
    closed_names = {
        "closed",
        "完了",
        "処理済み",
        "resolved",
    }
    return status_name in closed_names


def safe_text(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def backlog_issue_to_vibe_task(base_url: str, issue: Dict[str, Any]) -> VibeTask:
    issue_key = safe_text(issue.get("issueKey"))
    summary = safe_text(issue.get("summary"))
    description = safe_text(issue.get("description"))

    status_name = safe_text((issue.get("status") or {}).get("name"))
    priority_name = safe_text((issue.get("priority") or {}).get("name"))
    due_date = issue.get("dueDate")
    source_issue_id = issue.get("id")

    assignee = ""
    assignee_obj = issue.get("assignee")
    if assignee_obj:
        assignee = safe_text(assignee_obj.get("name"))

    parent_issue_id = issue.get("parentIssueId")
    source_url = f"{base_url.rstrip('/')}/view/{issue_key}"

    vibe_description = f"""Backlog Key: {issue_key}
Backlog URL: {source_url}
Assignee: {assignee or "-"}
Priority: {priority_name or "-"}
Status (source): {status_name or "-"}
Due: {due_date or "-"}

Original Description:
{description or "(no description)"}
"""

    return VibeTask(
        title=summary or issue_key,
        description=vibe_description,
        source_key=issue_key,
        source_url=source_url,
        source_status=status_name,
        priority=priority_name,
        assignee=assignee,
        due_date=due_date,
        parent_issue_id=parent_issue_id,
        source_issue_id=source_issue_id,
    )


def split_parent_child_tasks(tasks: List[VibeTask]) -> Tuple[List[VibeTask], List[VibeTask]]:
    parents: List[VibeTask] = []
    children: List[VibeTask] = []

    for task in tasks:
        if task.parent_issue_id is None:
            parents.append(task)
        else:
            children.append(task)

    return parents, children


def export_json(tasks: List[VibeTask], path: Path) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump([asdict(t) for t in tasks], f, ensure_ascii=False, indent=2)


def export_grouped_json(
    all_tasks: List[VibeTask],
    parent_tasks: List[VibeTask],
    child_tasks: List[VibeTask],
    path: Path,
) -> None:
    payload = {
        "summary": {
            "all_count": len(all_tasks),
            "parent_count": len(parent_tasks),
            "child_count": len(child_tasks),
        },
        "parents": [asdict(t) for t in parent_tasks],
        "children": [asdict(t) for t in child_tasks],
    }

    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)


def export_markdown(tasks: List[VibeTask], path: Path) -> None:
    lines: List[str] = ["# Vibe Kanban Import Draft", ""]

    for i, task in enumerate(tasks, start=1):
        parent_info = str(task.parent_issue_id) if task.parent_issue_id is not None else "-"
        lines.extend(
            [
                f"## {i}. {task.title}",
                "",
                f"- Backlog Key: {task.source_key}",
                f"- Backlog URL: {task.source_url}",
                f"- Source Issue ID: {task.source_issue_id or '-'}",
                f"- Parent Issue ID: {parent_info}",
                f"- Status: {task.source_status or '-'}",
                f"- Priority: {task.priority or '-'}",
                f"- Assignee: {task.assignee or '-'}",
                f"- Due: {task.due_date or '-'}",
                "",
                "```text",
                task.description.rstrip(),
                "```",
                "",
            ]
        )

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def export_parent_child_markdown(
    parent_tasks: List[VibeTask],
    child_tasks: List[VibeTask],
    path: Path,
) -> None:
    lines: List[str] = [
        "# Vibe Kanban Import Draft (Parent / Child)",
        "",
        f"- Parent tasks: {len(parent_tasks)}",
        f"- Child tasks: {len(child_tasks)}",
        "",
        "## Parent Tasks",
        "",
    ]

    for task in parent_tasks:
        lines.extend(
            [
                f"### {task.title}",
                f"- Backlog Key: {task.source_key}",
                f"- Source Issue ID: {task.source_issue_id or '-'}",
                f"- Due: {task.due_date or '-'}",
                "",
            ]
        )

    lines.extend(["## Child Tasks", ""])

    for task in child_tasks:
        lines.extend(
            [
                f"### {task.title}",
                f"- Backlog Key: {task.source_key}",
                f"- Source Issue ID: {task.source_issue_id or '-'}",
                f"- Parent Issue ID: {task.parent_issue_id or '-'}",
                f"- Due: {task.due_date or '-'}",
                "",
            ]
        )

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main() -> int:
    base_url = (os.getenv("BACKLOG_BASE_URL") or "").strip()
    api_key = (os.getenv("BACKLOG_API_KEY") or "").strip()
    assignee_raw = (os.getenv("BACKLOG_ASSIGNEE") or "").strip()
    project_id_raw = (os.getenv("BACKLOG_PROJECT_ID") or "").strip()

    if not base_url or not api_key:
        print("ERROR: BACKLOG_BASE_URL and BACKLOG_API_KEY are required.", file=sys.stderr)
        print("Please set them in your .env file.", file=sys.stderr)
        return 1

    assignee_id = None
    if assignee_raw:
        try:
            assignee_id = resolve_assignee_id(base_url, api_key, assignee_raw)
        except requests.HTTPError as e:
            print(f"HTTP ERROR while resolving assignee: {e}", file=sys.stderr)
            if e.response is not None:
                print(e.response.text, file=sys.stderr)
            return 2
        except requests.RequestException as e:
            print(f"REQUEST ERROR while resolving assignee: {e}", file=sys.stderr)
            return 3

        if assignee_id is None:
            print(
                f"WARNING: Could not resolve assignee from BACKLOG_ASSIGNEE={assignee_raw}. "
                "Assignee filter will be ignored.",
                file=sys.stderr,
            )

    project_id = None
    if project_id_raw:
        if project_id_raw.isdigit():
            project_id = int(project_id_raw)
        else:
            print(
                f"WARNING: BACKLOG_PROJECT_ID is not numeric, so it will be ignored: {project_id_raw}",
                file=sys.stderr,
            )

    try:
        issues = backlog_get_issues(
            base_url=base_url,
            api_key=api_key,
            assignee_id=assignee_id,
            project_id=project_id,
            count=100,
        )
    except requests.HTTPError as e:
        print(f"HTTP ERROR: {e}", file=sys.stderr)
        if e.response is not None:
            print(e.response.text, file=sys.stderr)
        return 4
    except requests.RequestException as e:
        print(f"REQUEST ERROR: {e}", file=sys.stderr)
        return 5

    open_issues = [issue for issue in issues if not is_closed_issue(issue)]
    tasks = [backlog_issue_to_vibe_task(base_url, issue) for issue in open_issues]
    parent_tasks, child_tasks = split_parent_child_tasks(tasks)

    export_json(tasks, BASE_DIR / "vibe_import.json")
    export_json(parent_tasks, BASE_DIR / "vibe_import_parents.json")
    export_json(child_tasks, BASE_DIR / "vibe_import_children.json")
    export_grouped_json(
        tasks,
        parent_tasks,
        child_tasks,
        BASE_DIR / "vibe_import_grouped.json",
    )
    export_markdown(tasks, BASE_DIR / "vibe_import.md")
    export_parent_child_markdown(
        parent_tasks,
        child_tasks,
        BASE_DIR / "vibe_import_parent_child.md",
    )

    print(f"Fetched issues: {len(issues)}")
    print(f"Open issues exported: {len(tasks)}")
    print(f"Parent tasks: {len(parent_tasks)}")
    print(f"Child tasks: {len(child_tasks)}")
    print(f"Wrote: {BASE_DIR / 'vibe_import.json'}")
    print(f"Wrote: {BASE_DIR / 'vibe_import_parents.json'}")
    print(f"Wrote: {BASE_DIR / 'vibe_import_children.json'}")
    print(f"Wrote: {BASE_DIR / 'vibe_import_grouped.json'}")
    print(f"Wrote: {BASE_DIR / 'vibe_import.md'}")
    print(f"Wrote: {BASE_DIR / 'vibe_import_parent_child.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
