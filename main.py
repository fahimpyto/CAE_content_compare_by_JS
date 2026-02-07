# imports
from playwright.sync_api import sync_playwright
import os
from bs4 import BeautifulSoup as bs


# data
url = "https://gimbalsinsider.com/"

# Folder structure
raw_folder = "raw"
cleaned_folder = "cleaned"

os.makedirs(raw_folder, exist_ok=True)
os.makedirs(cleaned_folder, exist_ok=True)

# data_clean Function
def clean_html(input_file, output_file):
    with open(input_file,"r", encoding="utf-8") as f:
        soup = bs(f, "lxml")

    # script tag removing
    for script in soup.find_all("script"):
        script.decompose()

    # style tag removig
    for style in soup.find_all("style"):
        style.decompose()

    # css link removing
    for link in soup.find_all("link"):
        rel = link.get("rel")
        if rel and "stylesheet" in rel:
            link.decompose()

    # inline css removing
    for tag in soup.find_all(True):
        if tag.has_attr("style"):
            del tag["style"]

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(str(soup))
    print(f" Clean file saved: {output_file} ")

# main_ function
def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)
        context_1 = browser.new_context()
        page_1 = context_1.new_page()
        page_1.goto(url , wait_until = "networkidle")
        html_1 = page_1.content()
        raw_file_1 = os.path.join(raw_folder, "output_withJS.html")
        cleaned_file_1 = os.path.join(cleaned_folder,"output_withJS_clean.html")

        # saving html file with js
        with open(raw_file_1, "w" , encoding="utf-8") as f:
            f.write(html_1)

        clean_html(raw_file_1, cleaned_file_1)

        context_1.close()

        context_2 = browser.new_context(java_script_enabled = False)
        page_2 = context_2.new_page()
        page_2.goto(url, wait_until = "networkidle")
        html_2 = page_2.content()
        raw_file_2  = os.path.join(raw_folder, "output_withoutJS.html")
        cleaned_file_2 = os.path.join(cleaned_folder, "output_withoutJS_clean.html")


        with open(raw_file_2, "w", encoding= "utf-8") as f:
            f.write(html_2)

        clean_html(raw_file_2, cleaned_file_2)

        context_2.close()
        browser.close()
        print("Work Done!")

if __name__ == "__main__":
    main()

