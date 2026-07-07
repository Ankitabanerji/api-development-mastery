# Real API call — notice how simple it is:
# # First request
# GET /orders?limit=10

# # Next requests — client passes the last seen ID
# GET /orders?after_id=5090&limit=10
# GET /orders?after_id=5100&limit=10

# Python code (client side):

import requests

def get_all_orders():
    all_orders = []
    after_id = None     # Start from beginning
    limit = 10

    while True:
        params = {"limit": limit}
        if after_id:
            params["after_id"] = after_id   # Pass last seen ID

        response = requests.get(
            "https://api.shop.com/orders",
            params=params
        )
        data = response.json()
        orders = data["data"]

        if not orders:
            break   # Empty page = we're done

        all_orders.extend(orders)

        # The last ID in this page becomes next request's anchor
        after_id = orders[-1]["id"]

    return all_orders

# What the response looks like:

# json
# {
#   "data": [
#     {"id": 5091, "total": 899},
#     {"id": 5092, "total": 1299},
#     ...
#     {"id": 5100, "total": 499}
#   ],
#   "has_more": true
# }
# // Client reads: after_id = 5100 (last item's id)
# // Next call: GET /orders?after_id=5100&limit=10

# Server-side DB query (why it's fast):
# sql
# -- This hits the B-tree index on `id` directly
# -- No scanning, no discarding
# SELECT * FROM orders
# WHERE id > 5090          -- ← index seek: O(log n)
# ORDER BY id ASC
# LIMIT 10;
