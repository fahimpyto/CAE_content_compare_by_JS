import os
from src.scraper import scrape_html_with_js, scrape_html_without_js
from src.cleaner import clean_html_string
from src.comparer import compare_html, generate_terminal_report
from src.utils import build_output_paths, write_file, save_csv_log, save_terminal_report, is_url_already_scraped


def main():
    url = input("Type URL (with https:) : ").strip()
    url = url.rstrip("/")

    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)
    csv_file = "database.csv"
    if is_url_already_scraped(url, csv_file):
        print("\n⚠️ This URL already scraped. Skipping scraping.")
        return

    withjs_path, withoutjs_path = build_output_paths(url, output_folder)

    # scrape html
    html_js = scrape_html_with_js(url)
    html_nojs = scrape_html_without_js(url)

    # clean html
    clean_js = clean_html_string(html_js)
    clean_nojs = clean_html_string(html_nojs)

    # save clean html
    write_file(withjs_path, clean_js)
    write_file(withoutjs_path, clean_nojs)

    # compare
    missing, extra = compare_html(clean_js, clean_nojs)

    # generate terminal report text
    report_text = generate_terminal_report(missing, extra)

    # save same terminal output into txt
    report_path = save_terminal_report(url, output_folder, report_text)

    # save csv
    
    save_csv_log(url, withjs_path, withoutjs_path, report_path, csv_file)

    print("\n✅ Report Saved:", report_path)


if __name__ == "__main__":
    main()
