from agents.yad2 import Yad2Agent
from core.rules_engine import matches_requirements
from services.email import send_email


def run(requirements: dict, user_email: str):
    agents = [
        Yad2Agent(),
    ]

    for agent in agents:
        listings = agent.fetch_listings()

        for car in listings:
            if matches_requirements(car, requirements):
                send_email(
                    to=user_email,
                    subject="🚗 נמצאה מודעת רכב מתאימה",
                    body=(
                        f"מקור: {car.source}\n"
                        f"{car.title}\n"
                        f"מחיר: {car.price}\n"
                        f"{car.link}"
                    ),
                )
