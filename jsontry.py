import requests
import json


response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
data = response.json()

print(f"Type: {type(data)}")       
print(f"Keys: {data.keys()}")
print(f"Title: {data['title']}")
print(f"Body: {data['body'][:50]}")


response = requests.get("https://jsonplaceholder.typicode.com/posts")
posts = response.json()

print(f"\nTotal: {len(posts)}")
print(f"First post: {posts[0]['title'][:40]}")
print(f"Last post:  {posts[-1]['title'][:40]}")



response = requests.get("https://jsonplaceholder.typicode.com/users/1")
user = response.json()

print(f"\nName    : {user['name']}")
print(f"Email   : {user['email']}")
print(f"City    : {user['address']['city']}")      
print(f"Company : {user['company']['name']}")    



new_post = {
    "title":  "Learning AI Engineering",
    "body":   "Python, APIs, LLMs, RAG...",
    "userId": 1
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=new_post
)

print(f"\nCreated Status: {response.status_code}") 
print(f"Created Post: {response.json()}")


posts = requests.get("https://jsonplaceholder.typicode.com/posts").json()

with open("posts.json", "w") as f:
    json.dump(posts, f, indent=4)

print(f"\nSaved {len(posts)} posts to posts.json!")



with open("posts.json", "r") as f:
    loaded = json.load(f)

print(f"Loaded {len(loaded)} posts from file!")
print(f"First title: {loaded[0]['title'][:40]}")