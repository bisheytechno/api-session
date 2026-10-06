import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")
print(f"Total posts: {len(response.json())}")

params = {"userId": 1}

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params=params
)

print(f"Status: {response.status_code}")
print(f"User 1 posts: {len(response.json())}")

for post in response.json():
    print(f"→ {post['title'][:40]}")