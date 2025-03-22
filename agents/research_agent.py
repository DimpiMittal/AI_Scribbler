import requests
from bs4 import BeautifulSoup
import logging

class ResearchAgent:
    def __init__(self):
        self.url = "https://trends.google.com/trends/trendingsearches/daily"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        }

    def get_trending_topics(self):
        try:
            response = requests.get(self.url, headers=self.headers, timeout=10)
            
            # Check if request was successful
            if response.status_code != 200:
                logging.error(f"❌ Failed to fetch trends: HTTP {response.status_code}")
                return ["Modern HR Strategies"]

            soup = BeautifulSoup(response.text, 'html.parser')
            topics = [item.text.strip() for item in soup.find_all('div', class_='title')]

            if not topics:
                logging.warning("⚠️ No trending topics found. Returning default topic.")
                return ["Modern HR Strategies"]

            logging.info(f"✅ Successfully fetched {len(topics[:5])} trending HR topics.")
            return topics[:5]

        except requests.exceptions.RequestException as e:
            logging.error(f"❌ Network error while fetching trends: {e}")
        except Exception as e:
            logging.error(f"❌ Unexpected error in fetching trends: {e}")

        return ["Modern HR Strategies"]
