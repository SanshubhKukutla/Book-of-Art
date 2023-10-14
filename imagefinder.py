import requests

api_key = 'AIzaSyBrWFYAQsLica1GXPmxUudAsODPCupiHZ8'
search_engine_id = 'f6df8f5a4eb1c406c'
query = 'your search query'

# Define the API endpoint URL
url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={search_engine_id}&q={query}&searchType=image'

# Make the API request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    # Extract and process the image search results from the 'items' field in the JSON response.
    for item in data.get('items', []):
        image_link = item.get('link')
        print(image_link)
else:
    print(f"Request failed with status code {response.status_code}")

