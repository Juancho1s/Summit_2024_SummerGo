import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyAcltyE2eVLPdmbaryyk2vyuAmtgdNZoCQ")

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("cual es el top 5 lugares turisticos de durango?")
print(response.text)

