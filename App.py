from flask import Flask, jsonify, request
import http.client


app = Flask(__name__)

@app.route('/lookAround', methods=['POST'])
def findPlaces():

    conn = http.client.HTTPSConnection("local-business-data.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "37cde39179msh1fe7b3eb3112f2bp1d96c4jsn555548034447",
        'x-rapidapi-host': "local-business-data.p.rapidapi.com"
    }
    query = request.json['query']

    query = ""

    conn.request("GET", f"/search?query={query}&limit=10&zoom=2&language=es&region=mx&extract_emails_and_contacts=false", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

    item = {
        'id': len(items) + 1,
        'name': data['name'],
        'description': data.get('description', '')
    }
    items.append(item)
    return jsonify(item), 201

