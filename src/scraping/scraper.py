from playwright.sync_api import sync_playwright

def scrape_html(url, js_enabled=True):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        context = browser.new_context(java_script_enabled=js_enabled)
        page = context.new_page()

        page.goto(url, wait_until="networkidle")
        html = page.content()

        context.close()
        browser.close()

        return html
