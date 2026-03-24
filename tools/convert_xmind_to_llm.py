from __future__ import annotations

import json
import sys
import zipfile
from pathlib import Path
import xml.etree.ElementTree as ET


NS = {"x": "urn:xmind:xmap:xmlns:content:2.0"}


def clean_text(text: str | None) -> str:
    return " ".join((text or "").replace("\r", " ").replace("\n", " ").split())


def parse_topic(topic: ET.Element) -> dict:
    node = {
        "title": clean_text(topic.findtext("x:title", default="", namespaces=NS)),
        "children": [],
        "callouts": [],
    }

    children = topic.find("x:children", NS)
    if children is None:
        return node

    for topics in children.findall("x:topics", NS):
        topic_type = topics.get("type", "attached")
        for child in topics.findall("x:topic", NS):
            parsed = parse_topic(child)
            if topic_type == "callout":
                node["callouts"].append(parsed)
            else:
                node["children"].append(parsed)
    return node


def topic_to_markdown(node: dict, depth: int = 0) -> list[str]:
    indent = "  " * depth
    lines = [f"{indent}- {node['title']}"]

    for callout in node.get("callouts", []):
        callout_title = callout["title"]
        lines.append(f"{indent}  - 注释: {callout_title}")
        for child in callout.get("children", []):
            lines.extend(topic_to_markdown(child, depth + 2))

    for child in node.get("children", []):
        lines.extend(topic_to_markdown(child, depth + 1))
    return lines


def build_markdown(data: dict, source_name: str) -> str:
    lines = [
        f"# {source_name}",
        "",
        "## LLM-Readable Outline",
        "",
        f"- Source file: `{source_name}`",
        f"- Sheet title: {data['sheet_title']}",
        f"- Root topic: {data['root']['title']}",
        "",
        "## Tree",
        "",
    ]
    lines.extend(topic_to_markdown(data["root"]))
    lines.append("")
    return "\n".join(lines)


def convert_xmind(path: Path) -> tuple[dict, str]:
    with zipfile.ZipFile(path) as zf:
        root = ET.fromstring(zf.read("content.xml"))

    sheet = root.find("x:sheet", NS)
    if sheet is None:
        raise ValueError("No sheet found in XMind file")

    topic = sheet.find("x:topic", NS)
    if topic is None:
        raise ValueError("No root topic found in XMind file")

    data = {
        "source_file": path.name,
        "sheet_title": clean_text(sheet.findtext("x:title", default="", namespaces=NS)),
        "root": parse_topic(topic),
    }
    return data, build_markdown(data, path.name)


def resolve_source(cwd: Path) -> Path:
    if len(sys.argv) > 1:
        candidate = Path(sys.argv[1])
        return candidate if candidate.is_absolute() else cwd / candidate

    candidates = [
        cwd / "01-5why原因要求示例-为什么我会拖延 本月学习任务？.xmind",
        cwd / "来源" / "01-5why原因要求示例-为什么我会拖延 本月学习任务？.xmind",
        cwd / "来源" / "原生文件" / "01-5why原因要求示例-为什么我会拖延 本月学习任务？.xmind",
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate

    matches = list(cwd.rglob("*.xmind"))
    if len(matches) == 1:
        return matches[0]
    raise FileNotFoundError("Unable to locate a single XMind source file")


def main() -> None:
    cwd = Path.cwd()
    source = resolve_source(cwd)
    data, markdown = convert_xmind(source)

    json_path = cwd / f"{source.stem}.llm.json"
    markdown_path = cwd / f"{source.stem}.llm.md"

    json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    markdown_path.write_text(markdown, encoding="utf-8")

    print(f"Wrote: {markdown_path.name}")
    print(f"Wrote: {json_path.name}")


if __name__ == "__main__":
    main()
