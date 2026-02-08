from playwright.sync_api import sync_playwright


def scrape_html_with_js(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        context = browser.new_context(java_script_enabled=True)
        page = context.new_page()

        page.goto(url, wait_until="networkidle")
        html = page.content()

        context.close()
        browser.close()

        return html


def scrape_html_without_js(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        context = browser.new_context(java_script_enabled=False)
        page = context.new_page()

        page.goto(url, wait_until="networkidle")
        html = page.content()

        context.close()
        browser.close()

        return html
