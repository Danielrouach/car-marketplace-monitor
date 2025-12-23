# car-marketplace-monitor

#  Car Marketplace Monitor

An extensible, agent-based backend system that monitors public car listings
and notifies users when matching criteria are met.

## Architecture
- Agent-based scraping layer
- Central orchestration engine
- Rule-based matching system
- Pluggable notification services

## Why this project?
This project demonstrates:
- Clean backend architecture
- Abstraction & extensibility
- Legal & ethical data collection
- Event-driven notifications
- Production-oriented design

## Supported Sources
- Yad2 (public listings)
- Additional marketplaces via agent interface

> Social platforms (Facebook / Instagram) are intentionally implemented
> as placeholders due to ToS and API constraints.

## Tech Stack
- Python 3.11
- Requests + BeautifulSoup
- SMTP / Email notifications
- Environment-based configuration

## Run
```bash
pip install -r requirements.txt
python main.py
