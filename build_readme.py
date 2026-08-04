import codecs
import email.utils
import json
import os
import pathlib
import re
import time
import urllib.error
import urllib.request
from collections import Counter
from urllib.parse import quote, unquote, urlparse
import xml.etree.ElementTree as ET


ROOT = pathlib.Path(__file__).parent.resolve()
README = ROOT / "README.md"
BLOG_FEED_URL = "https://zcxggmu.github.io/index.xml"
GITHUB_USER = "zcxGGmu"
POST_LIMIT = 5
PR_LIMIT = 6
PROJECT_LIMIT = 6


def replace_chunk(content, marker, chunk, inline=False):
    pattern = re.compile(
        r"<!\-\- {} starts \-\->.*<!\-\- {} ends \-\->".format(marker, marker),
        re.DOTALL,
    )
    if not inline:
        chunk = "\n{}\n".format(chunk)
    replacement = "<!-- {} starts -->{}<!-- {} ends -->".format(
        marker, chunk, marker
    )
    rewritten, count = pattern.subn(replacement, content)
    if count != 1:
        raise RuntimeError(
            f"Expected exactly one {marker!r} marker block, found {count}"
        )
    return rewritten


def fetch_feed_xml(url):
    return fetch_url(url, "application/rss+xml, application/xml;q=0.9, */*;q=0.8")


def fetch_url(url, accept):
    last_error = None
    for attempt in range(3):
        request = urllib.request.Request(
            url,
            headers={
                "User-Agent": "zcxGGmu-profile-readme-updater/1.0",
                "Accept": accept,
            },
        )
        token = os.environ.get("GITHUB_TOKEN")
        if "api.github.com" in url and token:
            request.add_header("Authorization", f"Bearer {token}")
            request.add_header("X-GitHub-Api-Version", "2022-11-28")
        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                return response.read()
        except (TimeoutError, ConnectionError, urllib.error.URLError) as error:
            last_error = error
            if attempt == 2:
                break
            time.sleep(2**attempt)
    raise last_error


def fetch_json(url):
    return json.loads(fetch_url(url, "application/vnd.github+json").decode("utf-8"))


def parse_pub_date(value):
    if not value:
        return ""
    parsed = email.utils.parsedate_to_datetime(value)
    return parsed.date().isoformat()


def escape_markdown(text):
    return text.replace("[", "\\[").replace("]", "\\]")


def title_from_link(link, fallback_title):
    slug = unquote(urlparse(link).path.strip("/").split("/")[-1])
    if not slug:
        return fallback_title

    special_words = {
        "agi": "AGI",
        "ai": "AI",
        "api": "API",
        "cpu": "CPU",
        "deepseek": "DeepSeek",
        "gpu": "GPU",
        "llm": "LLM",
        "llms": "LLMs",
        "riscv": "RISC-V",
    }
    words = [special_words.get(word, word.capitalize()) for word in slug.split("-")]
    return " ".join(word for word in words if word)


def fetch_blog_entries():
    root = ET.fromstring(fetch_feed_xml(BLOG_FEED_URL))
    channel = root.find("channel")
    if channel is None:
        raise RuntimeError("RSS feed did not contain a channel element")

    entries = []
    for item in channel.findall("item")[:POST_LIMIT]:
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        pub_date = parse_pub_date((item.findtext("pubDate") or "").strip())
        if not title or not link:
            continue
        entries.append(
            {
                "title": escape_markdown(title_from_link(link, title)),
                "url": link,
                "published": pub_date,
            }
        )
    if not entries:
        raise RuntimeError("RSS feed did not contain any usable entries")
    return entries


def repo_from_pr(item):
    return item["repository_url"].split("/repos/", 1)[1]


def pr_status(item):
    if item["state"] == "open":
        return "open"
    if item.get("pull_request", {}).get("merged_at"):
        return "merged"
    return "closed"


def status_label(status):
    return {
        "open": "Open",
        "merged": "Merged",
        "closed": "Closed",
    }[status]


def status_badge(status):
    return {
        "open": "🟢",
        "merged": "✅",
        "closed": "⚪",
    }[status]


def fetch_pr_items():
    query = quote(f"type:pr author:{GITHUB_USER}")
    items = []
    page = 1
    total_count = None

    while True:
        url = (
            "https://api.github.com/search/issues"
            f"?q={query}&sort=created&order=desc&per_page=100&page={page}"
        )
        data = fetch_json(url)
        total_count = data["total_count"]
        page_items = data.get("items", [])
        items.extend(page_items)
        if not page_items or len(items) >= total_count:
            break
        page += 1
    return items


def build_pr_activity():
    items = fetch_pr_items()
    status_counts = Counter(pr_status(item) for item in items)
    repo_counts = Counter(repo_from_pr(item) for item in items)
    open_repo_counts = Counter(
        repo_from_pr(item) for item in items if pr_status(item) == "open"
    )

    active_projects = open_repo_counts.most_common(PROJECT_LIMIT)
    if not active_projects:
        active_projects = repo_counts.most_common(PROJECT_LIMIT)

    lines = [
        (
            f"- **Status**: **{len(items)} PRs** across "
            f"**{len(repo_counts)} projects** — "
            f"🟢 {status_counts['open']} open · "
            f"✅ {status_counts['merged']} merged · "
            f"⚪ {status_counts['closed']} closed"
        ),
        "- **Active projects**: "
        + ", ".join(
            f"[{repo}](https://github.com/{repo}) ({count} open)"
            for repo, count in active_projects
        ),
        "- **Latest PRs**:",
    ]

    for item in items[:PR_LIMIT]:
        repo = repo_from_pr(item)
        status = pr_status(item)
        number = item["number"]
        title = escape_markdown(item["title"])
        lines.append(
            f"  - {status_badge(status)} "
            f"[{repo}#{number}]({item['html_url']}) "
            f"— {status_label(status)} — {title}"
        )
    return "\n".join(lines)


def read_text_preserving_bom(path):
    raw = path.read_bytes()
    has_bom = raw.startswith(codecs.BOM_UTF8)
    return raw.decode("utf-8-sig"), has_bom


def write_text_preserving_bom(path, text, has_bom):
    data = text.encode("utf-8")
    if has_bom:
        data = codecs.BOM_UTF8 + data
    path.write_bytes(data)


def main():
    readme_contents, has_bom = read_text_preserving_bom(README)
    rewritten = readme_contents

    try:
        pr_activity_md = build_pr_activity()
        rewritten = replace_chunk(rewritten, "pr_activity", pr_activity_md)
    except Exception as error:
        print(f"WARNING: keeping previous PR activity block: {error}")

    try:
        entries = fetch_blog_entries()
        entries_md = "\n".join(
            "- [{title}]({url}) — {published}".format(**entry) for entry in entries
        )
        rewritten = replace_chunk(rewritten, "blog_posts", entries_md)
    except Exception as error:
        print(f"WARNING: keeping previous blog posts block: {error}")

    write_text_preserving_bom(README, rewritten, has_bom)


if __name__ == "__main__":
    main()
