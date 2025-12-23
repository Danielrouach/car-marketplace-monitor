from core.models import CarListing
from core.rules_engine import matches_requirements


def test_matches_requirements_success():
    car = CarListing(
        source="yad2",
        title="Mazda 3 2018",
        price=40000,
        year=2018,
        km=90000,
        link="",
    )

    req = {"model": "mazda", "max_price": 45000}

    assert matches_requirements(car, req)
