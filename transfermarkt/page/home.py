from transfermarkt.page.object import PageObject
from transfermarkt.models.domain import Domain

from transfermarkt.page.utils import get_text_from_anchor, get_href_from_anchor


# from transfermarkt.page.utils import get_href_from_anchor, get_text_from_anchor


class HomePage(PageObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.url = "https://www.transfermarkt.com"

        user_agent = "transfermarkt"

        self.headers = {
            'user-agent': user_agent
        }

        self.load()

    def get_domains(self) -> list[Domain]:
        switcher = self.soup.select("div.tm-domainswitcher-box > ul")
        unordered_list = switcher[0]
        items = unordered_list.select("li")

        domains = []
        for item in items:
            name = get_text_from_anchor(item)
            url = get_href_from_anchor(item)

            domain = Domain(name=name, url=url)
            domains.append(domain)

        return domains
