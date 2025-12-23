from dataclasses import dataclass


@dataclass
class CarListing:
    source: str
    title: str
    price: int
    year: int
    km: int
    link: str
