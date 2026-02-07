# imports
from playwright.sync_api import sync_playwright

# data
url = "https://gimbalsinsider.com/"

# main_ function
def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)
        context_1 = browser.new_context()
        page_1 = context_1.new_page()
        page_1.goto(url , wait_until = "networkidle")
        html_1 = page_1.content()

        # saving html file with js
        with open("output_withJS.html", "w" , encoding="utf-8") as f:
            f.write(html_1)

        context_1.close()

        context_2 = browser.new_context(java_script_enabled = False)
        page_2 = context_2.new_page()
        page_2.goto(url, wait_until = "networkidle")
        html_2 = page_2.content()

        with open("output_withoutJS.html", "w", encoding= "utf-8") as f:
            f.write(html_2)

        context_2.close()
        browser.close()

if __name__ == "__main__":
    main()

