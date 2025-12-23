from abc import ABC, abstractmethod
from typing import List
from core.models import CarListing


class BaseAgent(ABC):
    @abstractmethod
    def fetch_listings(self) -> List[CarListing]:
        """Fetch car listings from a specific source"""
        pass
