import os
import csv
from datetime import datetime
from urllib.parse import urlparse


def make_safe_filename(url: str) -> str:
    parsed = urlparse(url)

    domain = parsed.netloc.replace("www.", "")
    path = parsed.path.strip("/").replace("/", "_")

    if path:
        return f"{domain}_{path}"
    return domain


def ensure_unique_filename(filepath: str) -> str:
    if not os.path.exists(filepath):
        return filepath

    base, ext = os.path.splitext(filepath)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    return f"{base}_{timestamp}{ext}"


def build_output_paths(url: str, output_folder="output"):
    base_name = make_safe_filename(url)

    withjs_file = os.path.join(output_folder, f"{base_name}_withJS.html")
    withoutjs_file = os.path.join(output_folder, f"{base_name}_withoutJS.html")

    withjs_file = ensure_unique_filename(withjs_file)
    withoutjs_file = ensure_unique_filename(withoutjs_file)

    return withjs_file, withoutjs_file


def write_file(filepath: str, content: str):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)


def save_csv_log(url: str, withjs_path: str, withoutjs_path: str, report_path: str, csv_file: str):
    file_exists = os.path.exists(csv_file)

    with open(csv_file, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["url", "withJS_file_path", "withoutJS_file_path", "report_file_path"])

        writer.writerow([url, withjs_path, withoutjs_path, report_path])


def save_terminal_report(url: str, output_folder: str, report_text: str) -> str:
    base_name = make_safe_filename(url)

    report_file = os.path.join(output_folder, f"{base_name}_compare_report.txt")
    report_file = ensure_unique_filename(report_file)

    with open(report_file, "w", encoding="utf-8") as f:
        f.write(report_text)

    return report_file
def is_url_already_scraped(url: str, csv_file: str) -> bool:
    if not os.path.exists(csv_file):
        return False

    with open(csv_file, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader, None)  # skip header

        for row in reader:
            if row and row[0].strip().rstrip("/") == url.strip().rstrip("/"):
                return True

    return False
