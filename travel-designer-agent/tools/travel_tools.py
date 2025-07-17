from agents import function_tool

@function_tool
def get_flights(origin: str, destination: str, date: str) -> dict:
    """Mock flight lookup between two cities"""
    return {"origin": origin,
            "destination": destination,
            "price": "$400",
            "airline": "SkyJet",
            "date": date}

@function_tool
def suggest_hotels(name: str, stars: int = 3) -> list:
    """Mock hotel suggestions based on destination"""
    return [
        {"name": name, "stars": stars, "price": "$120/night"},
        {"name": name, "stars": stars, "price": "$95/night"},
    ]
