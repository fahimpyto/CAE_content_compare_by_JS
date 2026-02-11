from bs4 import BeautifulSoup


def normalize_html(tag):
    return " ".join(str(tag).split())


def get_all_tags(html: str):
    soup = BeautifulSoup(html, "html.parser")

    if not soup.body:
        return []

    tags = []
    for tag in soup.body.find_all(True):
        tags.append(normalize_html(tag))

    return tags


def unique_keep_order(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def compare_html(with_js_html: str, without_js_html: str):
    with_tags = unique_keep_order(get_all_tags(with_js_html))
    without_tags = unique_keep_order(get_all_tags(without_js_html))

    with_set = set(with_tags)
    without_set = set(without_tags)

    missing = [tag for tag in with_tags if tag not in without_set]
    extra = [tag for tag in without_tags if tag not in with_set]

    return missing, extra


def generate_terminal_report(missing, extra):
    lines = []

    lines.append("=" * 70)
    lines.append("MISSING HTML in WithJS file")
    lines.append("=" * 70)
    lines.append("")

    if missing:
        for i, tag in enumerate(missing, 1):
            lines.append(f"[{i}] {tag}")
            lines.append("")
    else:
        lines.append("Nothing Missing ✅")
        lines.append("")

    lines.append("=" * 70)
    lines.append("EXTRA HTML in WithoutJS File")
    lines.append("=" * 70)
    lines.append("")

    if extra:
        for i, tag in enumerate(extra, 1):
            lines.append(f"[{i}] {tag}")
            lines.append("")
    else:
        lines.append("Nothing Extra ✅")
        lines.append("")

    lines.append("=" * 70)
    lines.append("SUMMARY")
    lines.append("=" * 70)
    lines.append(f"Missing Count: {len(missing)}")
    lines.append(f"Extra Count  : {len(extra)}")

    return "\n".join(lines)
