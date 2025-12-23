import requests
from bs4 import BeautifulSoup

from agents.base import BaseAgent
from core.models import CarListing


class Yad2Agent(BaseAgent):
    SOURCE = "yad2"
    URL = "https://www.yad2.co.il/vehicles/cars"

    def fetch_listings(self):
        response = requests.get(self.URL, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        listings = []

        for ad in soup.select(".feeditem"):
            try:
                title = ad.select_one(".title").get_text(strip=True)
                price_text = ad.select_one(".price").get_text(strip=True)
                price = int(price_text.replace(",", "").replace("₪", ""))

                link = ad.select_one("a")["href"]
                if link.startswith("/"):
                    link = f"https://www.yad2.co.il{link}"

                listings.append(
                    CarListing(
                        source=self.SOURCE,
                        title=title,
                        price=price,
                        year=0,
                        km=0,
                        link=link,
                    )
                )
            except Exception:
                continue

        return listings
