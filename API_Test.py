import http.client

conn = http.client.HTTPSConnection("local-business-data.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "37cde39179msh1fe7b3eb3112f2bp1d96c4jsn555548034447",
    'x-rapidapi-host': "local-business-data.p.rapidapi.com"
}

conn.request("GET", "/search?query=Hoteles%20en%20Durango%20Francisco%2C%20USA&limit=20&lat=37.359428&lng=-121.925337&zoom=13&language=en&region=us&extract_emails_and_contacts=false", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))