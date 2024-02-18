import googlemaps
from googlemaps import places
from config import API_KEY

gmaps = googlemaps.Client(key=API_KEY)

def getCoords(place: str):
    result = gmaps.find_place(input=place, input_type="textquery")
    id = result["candidates"][0]["place_id"]
    place_details = gmaps.place(id)

    if place_details and 'geometry' in place_details['result']:
        location = place_details['result']['geometry']['location']
        latitude = location['lat']
        longitude = location['lng']

    print(f"lat:{latitude}, long:{longitude}")
    return (latitude, longitude)


def findallGrocers(coords):
    grocers = gmaps.places_nearby(location=coords, radius=10000, keyword="Grocery store")
    grocers = grocers['results']
    for grocer in grocers:
        name = grocer['name']
        if "Walmart" in name or "Safeway" in name or "Rosauers" in name:
            print("\033[94m", end="")
        print(f"{name} at {grocer['vicinity']}")
        print("\033[39m")
    return grocers


def findCompatibleGrocers(coords):
    grocers = gmaps.places_nearby(location=coords, radius=10000, keyword="Grocery store")
    grocers = grocers['results']
    returnlist = []
    for grocer in grocers:
        name = grocer['name']
        if "Walmart" in name or "Safeway" in name or "Rosauers" in name or "Albertsons":
            print(f"{name} at {grocer['vicinity']}")
            returnlist.append((name, grocer['vicinity']))

        
        


def findGrocersbyQuery(query):
    findallGrocers(getCoords(query))
