import os
from urllib.parse import urlparse
from src.scraper import scrape_html
from src.cleaner import clean_html

url = input("Type URL (with https:) : ")

parsed = urlparse(url)

domain = parsed.netloc.replace("www.", "")
path = parsed.path.strip("/").replace("/", "_")


if path:
    folder_name = f"{domain}_{path}"
else:
    folder_name = domain

raw_folder = os.path.join("raw", folder_name)
cleaned_folder = os.path.join("cleaned", folder_name)

os.makedirs(raw_folder, exist_ok=True)
os.makedirs(cleaned_folder, exist_ok=True)


def main():
    #  WITH JS -
    html_js = scrape_html(url, js_enabled=True)
    raw_file_js = os.path.join(raw_folder, "output_withJS.html")
    cleaned_file_js = os.path.join(cleaned_folder, "output_withJS_clean.html")

    with open(raw_file_js, "w", encoding="utf-8") as f:
        f.write(html_js)

    clean_html(raw_file_js, cleaned_file_js)

    #  WITHOUT JS 
    html_nojs = scrape_html(url, js_enabled=False)
    raw_file_nojs = os.path.join(raw_folder, "output_withoutJS.html")
    cleaned_file_nojs = os.path.join(cleaned_folder, "output_withoutJS_clean.html")

    with open(raw_file_nojs, "w", encoding="utf-8") as f:
        f.write(html_nojs)

    clean_html(raw_file_nojs, cleaned_file_nojs)

    print(f"Work Done! Saved in raw/{folder_name} and cleaned/{folder_name}")


if __name__ == "__main__":
    main()
