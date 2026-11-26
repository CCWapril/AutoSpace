import csv
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
NOTES = ROOT / "notes"
SOURCE_PAGE = "https://iwiki.woa.com/p/4017698622"
GENERATED_ON = "2026-11-25"
SEED_FILES = ["seed_llm.json", "seed_recommendation.json", "seed_multimodal.json", "seed_scaling.json"]
CATEGORY_FILES = {
    "大语言模型": "大语言模型.md",
    "推荐系统": "推荐系统.md",
    "多模态": "多模态.md",
    "Scaling Up": "Scaling-Up.md",
}
CSV_FIELDS = [
    "key", "name", "title_zh", "title_en", "organizations", "first_submitted",
    "arxiv_url", "official_url", "categories", "diagram_urls", "notes",
    "application_notes", "authors", "venue", "verification", "source_page",
]


def append_unique(items, value):
    if value and value not in items:
        items.append(value)


def load_and_merge():
    merged = {}
    order = []
    for filename in SEED_FILES:
        seeds = json.loads((DATA / filename).read_text(encoding="utf-8"))
        for seed in seeds:
            key = seed["key"]
            if key not in merged:
                merged[key] = dict(seed)
                merged[key]["categories"] = []
                merged[key]["diagrams"] = []
                merged[key]["note_list"] = []
                merged[key]["take_list"] = []
                order.append(key)
            record = merged[key]
            append_unique(record["categories"], seed.get("cat", ""))
            for image in seed.get("img", []):
                append_unique(record["diagrams"], image)
            append_unique(record["note_list"], seed.get("note", ""))
            append_unique(record["take_list"], seed.get("take", ""))
            for field in ("name", "zh", "en", "org", "date", "ref"):
                if not record.get(field) and seed.get(field):
                    record[field] = seed[field]
    return [merged[key] for key in order]


def enrich(records, metadata):
    output = []
    missing_metadata = []
    for record in records:
        key = record["key"]
        is_arxiv = bool(re.fullmatch(r"\d{4}\.\d{5}", key))
        meta = metadata.get(key, {}) if is_arxiv else {}
        if is_arxiv and not meta:
            missing_metadata.append(key)
        title_en = meta.get("title_en") or record.get("en") or "待补充"
        title_zh = record.get("zh") or "待翻译"
        date = (meta.get("published") or "")[:10] or record.get("date") or "待核验"
        arxiv_url = meta.get("arxiv_url", "") if is_arxiv else ""
        official_url = record.get("ref", "")
        if not arxiv_url and not official_url:
            paper_link = ""
        else:
            paper_link = arxiv_url or official_url
        venue = meta.get("journal_ref") or meta.get("comment") or ""
        verification = (
            "英文标题、首次提交日期和 arXiv 链接已核验；机构按原页面或补充检索结果整理"
            if is_arxiv else
            "正式标题和官方链接已整理；未确认 arXiv 条目；日期与机构按标注来源保留"
        )
        output.append({
            "key": key,
            "name": record.get("name") or key,
            "title_zh": title_zh,
            "title_en": title_en,
            "organizations": record.get("org") or "原页面未标注",
            "first_submitted": date,
            "arxiv_url": arxiv_url,
            "official_url": official_url,
            "paper_link": paper_link,
            "categories": record["categories"],
            "diagram_urls": record["diagrams"],
            "notes": "；".join(record["note_list"]) or "原页面未提供说明笔记。",
            "application_notes": "；".join(record["take_list"]),
            "authors": meta.get("authors", []),
            "venue": venue,
            "verification": verification,
            "source_page": SOURCE_PAGE,
        })
    if missing_metadata:
        raise RuntimeError("Missing arXiv metadata: " + ", ".join(missing_metadata))
    return output


def csv_row(record):
    return {
        "key": record["key"],
        "name": record["name"],
        "title_zh": record["title_zh"],
        "title_en": record["title_en"],
        "organizations": record["organizations"],
        "first_submitted": record["first_submitted"],
        "arxiv_url": record["arxiv_url"],
        "official_url": record["official_url"],
        "categories": " | ".join(record["categories"]),
        "diagram_urls": " | ".join(record["diagram_urls"]),
        "notes": record["notes"],
        "application_notes": record["application_notes"],
        "authors": "; ".join(record["authors"]),
        "venue": record["venue"],
        "verification": record["verification"],
        "source_page": record["source_page"],
    }


def md_cell(value):
    return str(value).replace("|", "\\|").replace("\n", "<br>")


def paper_link(record):
    if record["arxiv_url"]:
        return f"[arXiv:{record['key']}]({record['arxiv_url']})"
    if record["official_url"]:
        return f"[官方链接]({record['official_url']})"
    return "未确认"


def write_csv_and_json(records):
    with (ROOT / "papers.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS)
        writer.writeheader()
        writer.writerows(csv_row(record) for record in records)
    (ROOT / "papers.json").write_text(
        json.dumps([csv_row(record) for record in records], ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def write_index(records):
    lines = [
        "# 论文总索引",
        "",
        f"> 共 {len(records)} 篇唯一论文；日期统一为 arXiv 首次提交时间，非 arXiv 条目使用标注来源时间。",
        "",
        "| 论文 | 中文标题 | 机构 | 时间 | 链接 | 分类 |",
        "|---|---|---|---|---|---|",
    ]
    for record in records:
        lines.append(
            f"| {md_cell(record['name'])} | {md_cell(record['title_zh'])} | "
            f"{md_cell(record['organizations'])} | {md_cell(record['first_submitted'])} | "
            f"{paper_link(record)} | {md_cell(' / '.join(record['categories']))} |"
        )
    (ROOT / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_category_notes(records):
    for category, filename in CATEGORY_FILES.items():
        selected = [record for record in records if category in record["categories"]]
        lines = [
            "---",
            f"title: 论文笔记-{category}",
            f"category: {category}",
            f"source: {SOURCE_PAGE}",
            f"generated: {GENERATED_ON}",
            f"paper_count: {len(selected)}",
            "---",
            "",
            f"# {category}论文笔记",
            "",
            "> 字段说明：英文标题与 arXiv 日期由 arXiv API 核验；中文标题为整理译名；机构以原页面为主，补充检索时已标注。结构图沿用原 iWiki 附件，需要相应内网权限。",
            "",
        ]
        for record in selected:
            lines.extend([
                f"## {record['name']}",
                "",
                f"- **中文标题**：{record['title_zh']}",
                f"- **English Title**：{record['title_en']}",
                f"- **机构**：{record['organizations']}",
                f"- **时间**：{record['first_submitted']}",
                f"- **论文链接**：{paper_link(record)}",
                f"- **分类**：{' / '.join(record['categories'])}",
                f"- **说明笔记**：{record['notes']}",
            ])
            if record["application_notes"]:
                lines.append(f"- **可参考性**：{record['application_notes']}")
            if record["venue"]:
                lines.append(f"- **发表信息（arXiv 元数据）**：{record['venue']}")
            lines.extend(["", "### 结构图", ""])
            if record["diagram_urls"]:
                for index, image in enumerate(record["diagram_urls"], start=1):
                    lines.append(f"![{record['name']}结构图{index}]({image})")
                    lines.append("")
            else:
                lines.extend(["原页面未提供结构图。", ""])
            lines.extend(["---", ""])
        (NOTES / filename).write_text("\n".join(lines), encoding="utf-8")


def write_readme(records):
    counts = Counter(category for record in records for category in record["categories"])
    arxiv_count = sum(bool(record["arxiv_url"]) for record in records)
    no_arxiv = [record["name"] for record in records if not record["arxiv_url"]]
    no_diagram = sum(not record["diagram_urls"] for record in records)
    cross_category = sum(len(record["categories"]) > 1 for record in records)
    lines = [
        "# 论文知识库",
        "",
        f"来源：[iWiki 论文合集]({SOURCE_PAGE})。本知识库将原页面的分类表格整理为可检索、可重建、可持续维护的结构化笔记。",
        "",
        "## 内容概览",
        "",
        f"- 唯一论文：**{len(records)} 篇**；分类归属：**{sum(counts.values())} 条**。",
        f"- arXiv 元数据已核验：**{arxiv_count} 篇**；未确认 arXiv：**{len(no_arxiv)} 篇**。",
        f"- 跨分类论文：**{cross_category} 篇**，已合并主记录并保留多个分类标签。",
        f"- 原页面未提供结构图：**{no_diagram} 篇**，笔记中已明确标记，未用虚构图片补齐。",
        "",
        "| 分类 | 论文数 | 笔记 |",
        "|---|---:|---|",
    ]
    for category, filename in CATEGORY_FILES.items():
        lines.append(f"| {category} | {counts[category]} | [查看](notes/{filename}) |")
    lines.extend([
        "",
        "## 文件说明",
        "",
        "- `INDEX.md`：全量总索引，适合浏览和检索。",
        "- `notes/`：按原页面分类生成的详细笔记，含中英标题、机构、时间、链接、结构图和说明。",
        "- `papers.csv`：结构化主表，UTF-8 BOM，可直接导入表格或知识库工具。",
        "- `papers.json`：与 CSV 等价的结构化数据，适合程序处理。",
        "- `data/seed_*.json`：人工维护的中文译名、机构、笔记和原图链接，是内容维护入口。",
        "- `data/arxiv_metadata.json`：arXiv API 返回的标题、作者、摘要、日期与发表信息。",
        "- `data/fetch_arxiv.py`：批量刷新 arXiv 元数据。",
        "- `data/build_kb.py`：合并种子数据并重新生成所有索引、笔记、CSV 和 JSON。",
        "",
        "## 维护流程",
        "",
        "1. 新增或修改论文时，编辑对应的 `data/seed_*.json`；已有 arXiv ID 的论文无需手抄英文标题和日期。",
        "2. 若新增 arXiv ID，同时加入 `data/fetch_arxiv.py` 的 `ARXIV_IDS`，再运行该脚本。",
        "3. 运行 `python3 data/build_kb.py` 重建知识库；生成文件不要作为长期手工编辑入口。",
        "4. 跨分类重复条目使用同一个 `key`，构建时会自动合并分类、结构图与可参考性笔记。",
        "",
        "## 数据口径与待补项",
        "",
        "- **时间**：arXiv 条目统一使用首次提交日期，不等同于会议录用或期刊发表日期；会议信息保留在各条目的 arXiv 元数据中。",
        "- **中文标题**：为便于检索的整理译名，不视为官方译名。",
        "- **机构**：优先沿用原页面，少数通过官方页面补充；未逐篇从 PDF 首页核验全部作者单位。",
        "- **结构图**：保留原 iWiki 附件 URL，访问需要相应权限；缺失时明确标记。",
        f"- **未确认 arXiv**：{'、'.join(no_arxiv)}。其中 STAR 的原页面信息不足以唯一定位，AdaFedRec 与 ACM 综述保留官方 DOI。",
        "- **笔记深度**：本次是对原合集的忠实结构化整理，不等同于逐篇全文精读；DHEN 等原页面信息较少的条目已保留待补提示。",
        "- **非论文资源**：商推分享链接、强化学习栏目的 YouTube 频道及空白的 MTGR 标题未计入论文数，仍可在源页面查看。",
        "",
    ])
    (ROOT / "README.md").write_text("\n".join(lines), encoding="utf-8")


def validate(records):
    assert len({record["key"] for record in records}) == len(records)
    for record in records:
        for field in ("name", "title_zh", "title_en", "organizations", "first_submitted", "notes"):
            assert record[field], (record["key"], field)
        assert record["categories"], record["key"]
        assert record["paper_link"] or record["key"] == "star-analogical", record["key"]


def main():
    metadata_payload = json.loads((DATA / "arxiv_metadata.json").read_text(encoding="utf-8"))
    metadata = {record["arxiv_id"]: record for record in metadata_payload["records"]}
    records = enrich(load_and_merge(), metadata)
    validate(records)
    write_csv_and_json(records)
    write_index(records)
    write_category_notes(records)
    write_readme(records)
    summary = {
        "unique_papers": len(records),
        "category_memberships": dict(Counter(category for record in records for category in record["categories"])),
        "arxiv_verified": sum(bool(record["arxiv_url"]) for record in records),
        "without_confirmed_arxiv": [record["key"] for record in records if not record["arxiv_url"]],
        "without_diagram": [record["key"] for record in records if not record["diagram_urls"]],
        "cross_category": [record["key"] for record in records if len(record["categories"]) > 1],
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
