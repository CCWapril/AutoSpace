import json
import time
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ARXIV_IDS = [
    "2501.12948", "2503.09516", "2503.05592", "2503.02130", "2505.06708",
    "2509.02017", "2505.17925", "2512.14503", "2508.02751", "2410.21465",
    "2603.25737", "2604.02268", "2604.08539", "2606.19348", "2607.02770",
    "2606.12683", "2606.24597", "2607.15495", "2510.21618", "2510.26692",
    "2603.15031", "2610.21601", "2606.02871", "2611.06483", "2611.01926",
    "2508.15326", "2507.04626", "2504.04237", "2502.18965", "2509.18091",
    "2504.08169", "2510.21714", "2508.14948", "2509.03236", "2506.06913",
    "2511.10138", "2512.07424", "2508.04711", "2509.06887", "2510.26104",
    "2508.15308", "2602.11235", "2602.10016", "2602.11410", "2602.22732",
    "2603.17533", "2603.27538", "2603.02184", "2604.11440", "2604.08933",
    "2605.25749", "2605.05803", "2605.15905", "2605.27441", "2606.03866",
    "2605.24051", "2605.24989", "2606.01396", "2602.15659", "2605.09338",
    "2605.21969", "2606.00422", "2606.31031", "2509.22046", "2606.27243",
    "2502.17494", "2605.29755", "2602.08612", "2609.34552", "2610.32326",
    "2610.32752", "2606.04944", "2511.06374", "2610.22400", "2611.20448",
    "2611.22838", "2611.22788", "2607.24255", "2611.24006", "2611.27514",
    "2511.15122", "2503.07536", "2502.13923", "2603.12793", "2602.10811",
    "2602.12041", "2602.14110", "2602.07520", "2603.03988", "2603.18697",
    "2603.24226", "2604.00590", "2604.08011", "2601.17836", "2604.17878",
    "2605.23191", "2602.09387", "2502.08309", "2606.16838", "2607.28070",
    "2609.03290", "2608.18606", "2608.30251", "2603.21209", "2606.27058",
    "2610.35318", "2610.39426", "2608.27991", "2611.25659",
    "2601.07372", "2411.14199", "2409.18869", "2607.24653",
]

NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom",
}


def fetch_batch(ids):
    url = "https://export.arxiv.org/api/query?id_list=" + ",".join(ids) + "&max_results=" + str(len(ids))
    request = urllib.request.Request(url, headers={"User-Agent": "WorkBuddyPaperKnowledgeBase/1.0"})
    with urllib.request.urlopen(request, timeout=90) as response:
        payload = response.read()
    root = ET.fromstring(payload)
    records = []
    for entry in root.findall("atom:entry", NS):
        entry_id = entry.findtext("atom:id", default="", namespaces=NS)
        arxiv_id = entry_id.rsplit("/", 1)[-1].split("v")[0]
        records.append({
            "arxiv_id": arxiv_id,
            "title_en": " ".join(entry.findtext("atom:title", default="", namespaces=NS).split()),
            "published": entry.findtext("atom:published", default="", namespaces=NS),
            "updated": entry.findtext("atom:updated", default="", namespaces=NS),
            "authors": [a.findtext("atom:name", default="", namespaces=NS) for a in entry.findall("atom:author", NS)],
            "summary": " ".join(entry.findtext("atom:summary", default="", namespaces=NS).split()),
            "primary_category": (entry.find("arxiv:primary_category", NS).attrib.get("term", "") if entry.find("arxiv:primary_category", NS) is not None else ""),
            "comment": entry.findtext("arxiv:comment", default="", namespaces=NS),
            "journal_ref": entry.findtext("arxiv:journal_ref", default="", namespaces=NS),
            "doi": entry.findtext("arxiv:doi", default="", namespaces=NS),
            "arxiv_url": "https://arxiv.org/abs/" + arxiv_id,
        })
    return records


def main():
    records = []
    errors = []
    for start in range(0, len(ARXIV_IDS), 35):
        batch = ARXIV_IDS[start:start + 35]
        try:
            records.extend(fetch_batch(batch))
        except Exception as exc:
            errors.append({"ids": batch, "error": str(exc)})
        if start + 35 < len(ARXIV_IDS):
            time.sleep(3)
    output = {
        "requested_count": len(ARXIV_IDS),
        "fetched_count": len(records),
        "missing_ids": sorted(set(ARXIV_IDS) - {r["arxiv_id"] for r in records}),
        "errors": errors,
        "records": sorted(records, key=lambda r: r["arxiv_id"]),
    }
    destination = Path(__file__).with_name("arxiv_metadata.json")
    destination.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k: output[k] for k in ("requested_count", "fetched_count", "missing_ids", "errors")}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
