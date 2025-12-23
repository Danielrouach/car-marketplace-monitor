from core.models import CarListing


def matches_requirements(car: CarListing, requirements: dict) -> bool:
    if car.price > requirements.get("max_price", float("inf")):
        return False

    model = requirements.get("model")
    if model and model.lower() not in car.title.lower():
        return False

    return True
