import requests

# 1. Basic error handling

url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    data = response.json()
    print(f"Success: {data['title'][:40]}")

except requests.exceptions.Timeout:
    print("Server does not respond — timeout!")

except requests.exceptions.ConnectionError:
    print("No Internet connection")

except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")

except Exception as e:
    print(f"Unknown error: {e}")

# 2. 404 — Not Found
try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/99999",
        timeout=5
    )
    response.raise_for_status()
    print(f"Found: {response.json()}")

except requests.exceptions.HTTPError as e:
    print(f"Not found: {e}")


# 3. Wrong URL — Connection Error
try:
    response = requests.get(
        "https://this-website-does-not-exist.com",
        timeout=5
    )

except requests.exceptions.ConnectionError:
    print("Website does not exist!")

except requests.exceptions.Timeout:
    print("Timeout!")

# 4. Status code manually check

response = requests.get(url)

if response.status_code == 200:
    print(f"\n OK — Data comes!")
    print(response.json()['title'][:40])
elif response.status_code == 404:
    print(" No Data!")
elif response.status_code == 401:
    print("Need API key!")
else:
    print(f"Error: {response.status_code}")