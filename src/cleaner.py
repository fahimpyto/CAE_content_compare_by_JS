from bs4 import BeautifulSoup as bs

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
        as_attr = link.get("as")

        if rel and "stylesheet" in rel:
            link.decompose()
        elif rel and "preload" in rel and as_attr == "style":
            link.decompose()
    #  remove preload scripts 
        if rel and "preload" in rel and as_attr == "script":
            link.decompose()

    # inline css removing
    for tag in soup.find_all(True):
        if tag.has_attr("style"):
            del tag["style"]

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(str(soup))
    print(f" Clean file saved: {output_file} ")