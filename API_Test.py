import http.client

conn = http.client.HTTPSConnection("local-business-data.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "37cde39179msh1fe7b3eb3112f2bp1d96c4jsn555548034447",
    'x-rapidapi-host': "local-business-data.p.rapidapi.com"
}

query = ""

conn.request("GET", f"/search?query={query}&limit=10&zoom=2&language=es&region=mx&extract_emails_and_contacts=false", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))


conn.request("GET", "/search-in-area?query=pizza&lat=37.359428&lng=-121.925337&zoom=13&limit=20&language=en&region=us&extract_emails_and_contacts=false", headers=headers)
