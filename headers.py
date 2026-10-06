import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(f"Status: {response.status_code}")

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/1",
    headers=headers
)

print(f"Status with headers: {response.status_code}")

print(f"\nResponse Headers:")
print(f"Content-Type : {response.headers['Content-Type']}")
print(f"Server       : {response.headers['Server']}")

API_KEY = "cbscscfeuihfian"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/1",
    headers=headers
)

print(f"\nWith Auth Status: {response.status_code}")