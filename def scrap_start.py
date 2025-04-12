def scrap_start (link):

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8" }
    with requests.Session() as session:
        response = session.get(link, headers=headers)
        response.raise_for_status()
        R = response.content

    tree = html.fromstring(R)
    return tree