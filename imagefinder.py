AIzaSyBrWFYAQsLica1GXPmxUudAsODPCupiHZ8

import requests

api_key = "AIzaSyBrWFYAQsLica1GXPmxUudAsODPCupiHZ8"
cse_id = "f6df8f5a4eb1c406c"
query = "Your search query"

url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cse_id}&q={query}&searchType=image"

response = requests.get(url)
data = response.json()

# Extract and process the image results from the 'items' field in the 'data' JSON response.
