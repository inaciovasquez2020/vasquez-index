"""Static public-site navigation checks; no network or proof assumptions."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
PAGES = ("index.html", "dashboard.html", "publications.html")
PRIVATE = {
    "flagship-lean", "urf-open-review-ledger", "final-wall-fo-k-locality",
    "cycle-local-rigidity", "cyclone-terminal-obstruction",
    "rh-archimedean-kernel-rigidity", "Exchange-Force-Framework",
    "pachner-invariant",
}


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ("a", "link"):
            href = attrs.get("href")
            if href:
                self.urls.append(href)


def test_shared_navigation_and_stylesheet():
    assert (ROOT / "portal.css").is_file()
    for name in PAGES:
        page = (ROOT / name).read_text(encoding="utf-8")
        assert 'href="portal.css"' in page
        assert 'class="portal-nav"' in page
        assert "https://inaciovasquez2020.github.io/" in page
        assert "Publications" in page


def test_links_are_public_and_local_assets_exist():
    for name in PAGES:
        parser = Links()
        parser.feed((ROOT / name).read_text(encoding="utf-8"))
        for href in parser.urls:
            parsed = urlsplit(href)
            if href.startswith("https://github.com/inaciovasquez2020/"):
                repo = parsed.path.split("/")[2]
                assert repo not in PRIVATE, (name, repo)
            if not parsed.scheme and parsed.path and not href.startswith("//"):
                target = (ROOT / name).parent / parsed.path
                assert target.is_file(), (name, href)


def test_status_boundary_is_not_promotion():
    for name in PAGES:
        text = (ROOT / name).read_text(encoding="utf-8")
        assert "not" in text.lower() or "OPEN" in text


if __name__ == "__main__":
    test_shared_navigation_and_stylesheet()
    test_links_are_public_and_local_assets_exist()
    test_status_boundary_is_not_promotion()
    print("PUBLIC_PORTAL_LINKS := PASS")
