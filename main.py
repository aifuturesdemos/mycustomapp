# Secure main.py (template)
import logging
import os
import sys
import requests
from requests.exceptions import RequestException

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

def get_user_input(prompt):
    try:
        user_input = input(prompt)
        # Basic input validation: ensure input is not empty and does not contain dangerous characters
        if not user_input or any(c in user_input for c in [';', '|', '&', '`']):
            raise ValueError('Invalid input detected.')
        return user_input
    except Exception as e:
        logging.error(f"Input error: {e}")
        sys.exit(1)

def fetch_data_from_api(url):
    try:
        # Ensure the URL uses HTTPS
        if not url.lower().startswith('https://'):
            raise ValueError('Only HTTPS URLs are allowed.')
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        logging.error(f"Network error: {e}")
        return None
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return None

def main():
    logging.info("Application started.")
    api_url = get_user_input("Enter the secure API URL (HTTPS only): ")
    data = fetch_data_from_api(api_url)
    if data:
        logging.info(f"Fetched data: {data}")
    else:
        logging.warning("No data fetched.")
    logging.info("Application finished.")

if __name__ == "__main__":
    main()
