import requests
from bs4 import BeautifulSoup
from sample_data import SAMPLE_DATA


def fetch_offers(energy_type: str, postal_code: str, consumption: float):
    """Attempt to fetch offers from Check24.

    If fetching fails, return sample data instead.
    """
    # Map energy type to url parameter (placeholder example)
    energy_map = {
        "Electricity": "strom",
        "Gas": "gas",
    }
    try:
        url = "https://www.check24.de/contract/energy/api"  # not actual endpoint
        params = {
            "type": energy_map.get(energy_type, "strom"),
            "zipcode": postal_code,
            "consumption": consumption,
        }
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        offers = []
        # Actual scraping logic would parse soup for offer data
        # This placeholder returns an empty list as parsing depends on page layout
        return offers
    except Exception as exc:
        print(f"Could not fetch offers from Check24: {exc}")
        return SAMPLE_DATA.get(energy_type, [])

