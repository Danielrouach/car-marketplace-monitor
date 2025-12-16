# core/filters.py
def matches_requirements(car, req):
    return (
        car.price <= req["max_price"]
        and req["model"].lower() in car.title.lower()
    )
