import requests
import csv
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")




def nearby_search(location, radius, place_type):
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": location,
        "radius": radius,
        "type": place_type,
        "key": API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data.get("results", [])


def get_place_details(place_id):
    url = "https://maps.googleapis.com/maps/api/place/details/json"
    params = {
        "place_id": place_id,
        "fields": "name,website,formatted_phone_number,rating,user_ratings_total,formatted_address",
        "key": API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data.get("result", {})


def find_no_website(location, radius, place_type):
    print(f"Searching for {place_type}s near {location}...\n")
    
    places = nearby_search(location, radius, place_type)
    print(f"Found {len(places)} places. Checking each for website...\n")
    
    no_website = []

    for i, place in enumerate(places):
        place_id = place["place_id"]
        details = get_place_details(place_id)

        name    = details.get("name", "N/A")
        website = details.get("website")
        phone   = details.get("formatted_phone_number", "N/A")
        rating  = details.get("rating", "N/A")
        reviews = details.get("user_ratings_total", 0)
        address = details.get("formatted_address", "N/A")

        print(f"[{i+1}/{len(places)}] {name} — {'✅ has website' if website else '❌ no website'}")

        if not website:
            no_website.append({
                "name": name,
                "phone": phone,
                "rating": rating,
                "reviews": reviews,
                "address": address
            })

    return no_website


def save_to_csv(results, filename="results.csv"):
    if not results:
        print("No results to save.")
        return

    keys = results[0].keys()
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(results)

    print(f"\n✅ Saved {len(results)} businesses to {filename}")


results = find_no_website(
    location="10.0261,76.3083",  # Kochi
    radius=5000,                  # 5km
    place_type="doctor"       # try: restaurant, doctor, gym, lawyer
)

print(f"\n🎯 Found {len(results)} businesses without a website!\n")
for b in results:
    print(f"Name    : {b['name']}")
    print(f"Phone   : {b['phone']}")
    print(f"Rating  : {b['rating']} ⭐ ({b['reviews']} reviews)")
    print(f"Address : {b['address']}")
    print("-" * 40)

save_to_csv(results)