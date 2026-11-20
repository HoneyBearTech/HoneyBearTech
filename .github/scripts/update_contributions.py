#!/usr/bin/env python3
"""Rewrite the open-source contributions block in README.md.

Lists the latest pull requests GH_USER opened against repositories
they do not own. Uses only the standard library.
"""
import json
import os
import re
import sys
import urllib.parse
import urllib.request

START = "<!-- CONTRIBUTIONS:START -->"
END = "<!-- CONTRIBUTIONS:END -->"
RECENT = 10

USER = os.environ.get("GH_USER", "HoneyBearTech")
TOKEN = os.environ.get("GITHUB_TOKEN", "")


def search(query):
    items, page = [], 1
    while True:
        url = "https://api.github.com/search/issues?" + urllib.parse.urlencode(
            {"q": query, "per_page": 100, "page": page, "sort": "created", "order": "desc"}
        )
        req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
        if TOKEN:
            req.add_header("Authorization", f"Bearer {TOKEN}")
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.load(resp)
        items += data["items"]
        if len(items) >= data["total_count"] or not data["items"] or page >= 10:
            return items
        page += 1


def status(pr):
    if pr["pull_request"].get("merged_at"):
        return "merged"
    return pr["state"]  # "open" or "closed"


ICON = {"merged": "🟣 Merged", "open": "🟢 Open", "closed": "⚪ Closed"}


def render(prs):
    lines = ["<details>", f"<summary><b>Latest {RECENT} pull requests</b></summary>", ""]
    for pr in prs[:RECENT]:
        repo = pr["repository_url"].split("/repos/", 1)[1]
        title = pr["title"].replace("|", "\\|").replace("<", "&lt;")
        lines.append(f"- {ICON[status(pr)]} · [{title}]({pr['html_url']}) — `{repo}`")
    lines += ["", "</details>"]
    return "\n".join(lines)


def main(path):
    prs = search(f"is:pr author:{USER} -user:{USER}")
    block = f"{START}\n{render(prs)}\n{END}"
    with open(path, encoding="utf-8") as f:
        text = f.read()
    pattern = re.compile(re.escape(START) + ".*?" + re.escape(END), re.S)
    if not pattern.search(text):
        sys.exit(f"markers not found in {path}")
    new = pattern.sub(lambda _: block, text)
    if new != text:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new)
        print(f"updated {path}: {len(prs)} pull requests")
    else:
        print("no changes")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "README.md")
