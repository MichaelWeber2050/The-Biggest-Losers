import requests

# Define a function to search for podcasts in a given city
def search_podcasts(city):
    # Set the search parameters
    url = "https://api.spotify.com/v1/search"
    query = f"q=sports&market=US&type=show&limit=1&offset=0&include_external=audio&locale=en-US&q=city:{city}"
    headers = {"Authorization": "Bearer <YOUR_ACCESS_TOKEN>"}
    
    # Send the API request and get the response
    response = requests.get(f"{url}?{query}", headers=headers)
    
    # Parse the response and return the show ID of the top sports podcast in the city
    if response.status_code == 200:
        data = response.json()
        if len(data["shows"]["items"]) > 0:
            return data["shows"]["items"][0]["id"]
    
    # Return None if no podcast was found or there was an error
    return None

# Define a list of cities with NFL franchises
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Philadelphia", "Phoenix", "San Antonio", "San Diego", "Dallas", "San Jose", "Austin", "Jacksonville", "Fort Worth", "Columbus", "San Francisco", "Charlotte", "Indianapolis", "Seattle", "Denver", "Washington", "Boston", "Nashville", "El Paso", "Detroit", "Memphis", "Portland", "Oklahoma City", "Las Vegas", "Louisville", "Baltimore", "Milwaukee", "Albuquerque", "Tucson", "Fresno", "Mesa", "Sacramento", "Atlanta", "Kansas City", "Colorado Springs", "Miami", "Raleigh", "Omaha", "Long Beach", "Virginia Beach", "Oakland", "Minneapolis", "Tulsa", "Wichita", "New Orleans", "Arlington"]

# Loop through the cities and search for their top sports podcast
for city in cities:
    show_id = search_podcasts(city)
    if show_id:
        print(f"The top sports podcast in {city} is: https://open.spotify.com/show/{show_id}")
    else:
        print(f"No sports podcast was found in {city}.")
