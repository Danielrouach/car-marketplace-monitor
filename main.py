from core.orchestrator import run


if __name__ == "__main__":
    requirements = {
        "model": "mazda",
        "max_price": 45000,
    }

    run(requirements, "your_email@gmail.com")
