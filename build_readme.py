import codecs
import email.utils
import pathlib
import re
import urllib.request
from urllib.parse import unquote, urlparse
import xml.etree.ElementTree as ET


ROOT = pathlib.Path(__file__).parent.resolve()
README = ROOT / "README.md"
BLOG_FEED_URL = "https://zcxggmu.github.io/index.xml"
POST_LIMIT = 5


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
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "zcxGGmu-profile-readme-updater/1.0",
            "Accept": "application/rss+xml, application/xml;q=0.9, */*;q=0.8",
        },
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        return response.read()


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
    entries = fetch_blog_entries()
    entries_md = "\n".join(
        "- [{title}]({url}) — {published}".format(**entry) for entry in entries
    )
    rewritten = replace_chunk(readme_contents, "blog_posts", entries_md)
    write_text_preserving_bom(README, rewritten, has_bom)


if __name__ == "__main__":
    main()
