import http.client
import json
from flask import Flask, jsonify, request, make_response  # Import Flask and related modules
from flask_cors import CORS

# Initialize Flask application
app = Flask(__name__)
CORS(app)

@app.route('/lookAround', methods=['POST'])
def findPlaces():
    conn = http.client.HTTPSConnection("local-business-data.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "67f8123be2mshe653493aa87fba4p188bfejsna3a2e349e03e",
        'x-rapidapi-host': "local-business-data.p.rapidapi.com"
    }

    # Retrieve the query from the request body (assuming JSON input)
    query = request.json['query']

    # Perform the GET request to the external API
    conn.request("GET", f"/search-in-area?query={query}&lat=24.043829&lng=-104.627699&zoom=15&limit=&language=en&region=us&extract_emails_and_contacts=false", headers=headers)

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
