# core/orchestrator.py
from agents.yad2_agent import Yad2Agent
from core.filters import matches_requirements
from services.email_service import send_email

def run(requirements, user_email):
    agents = [Yad2Agent()]

    for agent in agents:
        listings = agent.fetch_listings()
        for car in listings:
            if matches_requirements(car, requirements):
                send_email(
                    user_email,
                    "🚗 נמצאה מודעה מתאימה!",
                    f"{car.title}\nמחיר: {car.price}\n{car.link}"
                )
