# fact_lookup.py
# ========================
# AI Chatbot - Fact Lookup
# ========================

import requests
import json
import os
from config import *

CACHE_FILE = os.path.join(DATA_DIR, "fact_cache.json")

# ------------------------
# Load / Save Cache
# ------------------------
def load_cache():
    if not os.path.exists(CACHE_FILE):
        return {}
    try:
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        print("Error loading cache:", e)
        return {}

def save_cache(cache):
    try:
        with open(CACHE_FILE, "w") as f:
            json.dump(cache, f, indent=2)
    except Exception as e:
        print("Error saving cache:", e)

# ------------------------
# Wikipedia Fact Lookup
# ------------------------
def get_fact(topic):
    """
    Fetch a short summary from Wikipedia.
    """
    cache = load_cache()
    topic_lower = topic.lower()
    if topic_lower in cache:
        return cache[topic_lower]

    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic.replace(' ', '_')}"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        if "extract" in data:
            fact = data["extract"][:MAX_TOKENS] + ("..." if len(data["extract"]) > MAX_TOKENS else "")
            cache[topic_lower] = fact
            save_cache(cache)
            return fact
        else:
            return f"Sorry, I couldn't find info on '{topic}'. {SPECIAL_PHRASE}"
    except Exception as e:
        return f"Error fetching fact: {e}. {SPECIAL_PHRASE}"

# ------------------------
# Test Examples
# ------------------------
if __name__ == "__main__":
    examples = ["Python (programming language)", "Black hole", "OpenAI"]
    for topic in examples:
        print(f"Fact for {topic}:")
        print(get_fact(topic))
        print("---")

