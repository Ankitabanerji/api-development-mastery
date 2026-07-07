# Real API call:
# # First request — no cursor
# GET /posts?limit=3

# # Next request — use cursor from previous response
# GET /posts?limit=3&cursor=eyJpZCI6MTAzfQ==

# Python code (client side):

import requests

def get_all_posts():
    all_posts = []
    cursor = None       # Start with no cursor
    limit = 10

    while True:
        params = {"limit": limit}
        if cursor:
            params["cursor"] = cursor   # Add cursor once we have one

        response = requests.get(
            "https://api.social.com/posts",
            params=params
        )
        data = response.json()
        all_posts.extend(data["data"])

        # Server sends null/None when there are no more pages
        cursor = data.get("next_cursor")
        if not cursor:
            break

    return all_posts

# What the response looks like:

# json{
#   "data": [
#     {"id": 101, "text": "Hello world"},
#     {"id": 102, "text": "REST is fun"},
#     {"id": 103, "text": "Building APIs"}
#   ],
#   "next_cursor": "eyJpZCI6MTAzfQ==",   ← pass this in next request
#   "prev_cursor": null                   ← for going backwards
# }

# // Last page response:
# {
#   "data": [ {"id": 198}, {"id": 199} ],
#   "next_cursor": null    ← null means no more pages
# }

# What's inside a cursor?

import base64, json

# Server encodes the cursor like this:
cursor = base64.b64encode(json.dumps({"id": 103}).encode()).decode()
# "eyJpZCI6IDEwM30="

# Server decodes it on the next request:
decoded = json.loads(base64.b64decode(cursor).decode())
# {"id": 103}
# Then runs: SELECT * FROM posts WHERE id > 103 LIMIT 10
# The client never needs to decode this — it's treated as an opaque string.'
# 'This is intentional: the server can change what's inside the cursor without breaking clients.
