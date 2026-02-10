import os
from src.scraper import scrape_html_with_js, scrape_html_without_js
from src.cleaner import clean_html_string
from src.utils import build_output_paths, write_file, save_csv_log


def main():
    url = input("Type URL (with https:) : ").strip()

    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)

    withjs_path, withoutjs_path = build_output_paths(url, output_folder)

    # scrape html
    html_js = scrape_html_with_js(url)
    html_nojs = scrape_html_without_js(url)

    # clean html (string based)
    clean_js = clean_html_string(html_js)
    clean_nojs = clean_html_string(html_nojs)

    # save only clean output
    write_file(withjs_path, clean_js)
    write_file(withoutjs_path, clean_nojs)

    # csv log
    csv_file =  "database.csv"
    save_csv_log(url, withjs_path, withoutjs_path, csv_file)

    print("\n✅ Work Done!")
    print(f" Clean WITH JS saved: {withjs_path}")
    print(f" Clean WITHOUT JS saved: {withoutjs_path}")
    print(f" CSV log updated: {csv_file}")


if __name__ == "__main__":
    main()
