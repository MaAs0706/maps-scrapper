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

def get_coordinate(place_name):
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": place_name,
        "key": API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()

    print(f"Status: {data['status']}")  # add this line
    print(f"Full response: {data}") 
    
    if data["results"]:
        location = data["results"][0]["geometry"]["location"]
        lat = location["lat"]
        lng = location["lng"]
        return f"{lat},{lng}"
    else:
        print(f"Could not find the location for {place_name}. Please check the name and try again.")
        return None


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

place_name = input("Enter a location : ")
place_type = input("Enter a business type (e.g., restaurant, doctor, gym, lawyer): ")
location = get_coordinate(place_name)
if location:
    results = find_no_website(
        location=location,
        radius=5000,
        place_type=place_type
    )

    print(f"\n🎯 Found {len(results)} businesses without a website!\n")
    for b in results:
      print(f"Name    : {b['name']}")
      print(f"Phone   : {b['phone']}")
      print(f"Rating  : {b['rating']} ⭐ ({b['reviews']} reviews)")
      print(f"Address : {b['address']}")
      print("-" * 40)

    save_to_csv(results)