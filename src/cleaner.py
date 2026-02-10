from bs4 import BeautifulSoup as bs


def clean_html_string(html: str) -> str:
    soup = bs(html, "lxml")

    # remove script tags
    for script in soup.find_all("script"):
        script.decompose()

    # remove style tags
    for style in soup.find_all("style"):
        style.decompose()

    # remove css links + preload styles/scripts
    for link in soup.find_all("link"):
        rel = link.get("rel")
        as_attr = link.get("as")

        if rel and "stylesheet" in rel:
            link.decompose()
        elif rel and "preload" in rel and as_attr == "style":
            link.decompose()
        elif rel and "preload" in rel and as_attr == "script":
            link.decompose()

    # remove inline styles
    for tag in soup.find_all(True):
        if tag.has_attr("style"):
            del tag["style"]

    return str(soup)
