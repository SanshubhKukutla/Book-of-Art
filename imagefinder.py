import requests
from main import get_keywords

api_key = "AIzaSyBrWFYAQsLica1GXPmxUudAsODPCupiHZ8"
search_engine_id = "f6df8f5a4eb1c406c"
query = get_keywords()
num_results = 10

url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={search_engine_id}&q={query}&searchType=image&num={num_results}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for item in data.get("items", []):
        image_link = item.get("link")
        print(image_link)
else:
    print(f"Request failed with status code {response.status_code}")
