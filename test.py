from typing import List, Dict

from src.naturalpy import natural
from pydantic import BaseModel

class Place(BaseModel):
    city: str
    name: str
    highlight: str

@natural
def get_places(country: str, interest: str, number: int = 3) -> List[Place]:
    """
    Tell me the top ${number} places to visit in ${country} which are
    good for a tourist who has an interest in ${interest}. For each,
    include the city, name, and a one-line highlight.
    """

@natural
def analyze_text(text: str, aspects: List[str]) -> Dict[str, float]:
    """
    Analyze the following text: "${text}"

    Give me a sentiment score for each of these aspects:
    ${aspects}

    For each aspect, provide a score between 0 and 1 where 0 is very negative
    and 1 is very positive.
    """

# text = "The service was excellent but the food was mediocre and overpriced."
# aspects = ["service", "food quality", "value"]
#
# analysis = analyze_text(text, aspects)
# print(analysis)

# try:
#     places = get_places("Australia", "adventure")
#     print(places)
# except Exception as e:
#     print("Error:", e)
#
# @natural
# def prime_numbers(n: int) -> List[int]:
#     """
#     Generate a list of prime numbers up to ${n}.
#     """
#
# primes = prime_numbers(50)
# print(primes)

@natural
def generate_ideas(topic: str, count: int) -> List[str]:
    """
    Generate ${count} creative ideas related to ${topic}.
    Each idea should be innovative and practical.
    """

# Call like a normal function
ideas = generate_ideas("sustainable urban gardening", 3)
print(ideas)  # ['Vertical hydroponic systems for balconies', ...]