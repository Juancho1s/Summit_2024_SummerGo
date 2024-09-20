import http.client

conn = http.client.HTTPSConnection("local-business-data.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "37cde39179msh1fe7b3eb3112f2bp1d96c4jsn555548034447",
    'x-rapidapi-host': "local-business-data.p.rapidapi.com"
}

query = "Durango_Hotel_Motel"

conn.request("GET", f"/search-in-area?query={query}&lat=37.359428&lng=-121.925337&zoom=13&limit=20&language=en&region=us&extract_emails_and_contacts=false", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))