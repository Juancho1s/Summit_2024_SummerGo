import http.client
import json
from flask import Flask, jsonify, request, make_response  # Import Flask and related modules

# Initialize Flask application
app = Flask(__name__)

@app.route('/lookAround', methods=['POST'])
def findPlaces():
    conn = http.client.HTTPSConnection("local-business-data.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "37cde39179msh1fe7b3eb3112f2bp1d96c4jsn555548034447",
        'x-rapidapi-host': "local-business-data.p.rapidapi.com"
    }

    # Retrieve the query from the request body (assuming JSON input)
    query = request.json['query']

    userData = {
        "places": json.loads(data.decode("utf-8"))['results'],
        "userId": 2,
        "userLikes": "haburguesas, peliculas de terror, Comida china"
    }

    # Perform the GET request to the external API
    conn.request("GET", f"/search-in-area?query={query}&lat=24.043829&lng=-104.627699&zoom=15&limit=10&language=en&region=us&extract_emails_and_contacts=false", headers=headers)

    # Get the response from the API
    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))
    # Decode and parse the response into JSON
    json_data = json.loads(data.decode("utf-8"))

    # Now process the parsed JSON data into the desired format
    aux = [
        {
            "full_address": i.get("full_address"),
            "photos_sample": i.get("photos_sample"),
            "lat": i.get("latitude"),
            "lng": i.get("longitude"),
            "about": i.get("about"),
        } for i in json_data.get("data", [])
    ]

    # Return the filtered data as JSON response
    return make_response(jsonify(aux), 200)

if __name__ == '__main__':
    app.run(debug=True)
