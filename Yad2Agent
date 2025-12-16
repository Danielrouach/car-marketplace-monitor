# agents/yad2_agent.py
import requests
from bs4 import BeautifulSoup
from agents.base_agent import BaseAgent
from core.models import CarListing

class Yad2Agent(BaseAgent):

    URL = "https://www.yad2.co.il/vehicles/cars"

    def fetch_listings(self):
        res = requests.get(self.URL, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")

        listings = []
        for ad in soup.select(".feeditem"):
            try:
                price = int(ad.select_one(".price").text.replace(",", ""))
                title = ad.select_one(".title").text
                link = ad.select_one("a")["href"]

                listings.append(
                    CarListing(
                        source="yad2",
                        title=title,
                        price=price,
                        year=0,
                        km=0,
                        link=link
                    )
                )
            except Exception:
                continue

        return listings
