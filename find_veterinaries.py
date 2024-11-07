import requests

def find_nearby_veterinaries(location, radius=5000, api_key="YOUR_GOOGLE_API_KEY"):
    """
    Find nearby veterinary services based on location.

    Parameters:
    - location (str): The latitude and longitude of the search center in "lat,lng" format.
    - radius (int): The radius to search within in meters (default is 5000).
    - api_key (str): Your Google Places API key.

    Returns:
    - list: A list of dictionaries containing details about each veterinary service.
    """
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        'location': location,
        'radius': radius,
        'type': 'veterinary_care',
        'key': api_key
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data.get("results"):
            return [
                {
                    'name': vet.get('name'),
                    'address': vet.get('vicinity'),
                    'rating': vet.get('rating', 'N/A'),
                    'user_ratings_total': vet.get('user_ratings_total', 0),
                }
                for vet in data['results']
            ]
    else:
        print("Error:", response.status_code, response.text)
    return []
