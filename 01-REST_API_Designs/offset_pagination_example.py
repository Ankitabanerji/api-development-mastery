# Real API call:
# GET /orders?page=3&limit=10

# Python code (client side):

import requests

def get_all_orders():
    all_orders = []
    page = 1
    limit = 10

    while True:
        response = requests.get(
            "https://api.shop.com/orders",
            params={"page": page, "limit": limit}
        )
        data = response.json()
        orders = data["data"]
        all_orders.extend(orders)

        # Stop when we've fetched all pages
        if page >= data["pagination"]["total_pages"]:
            break
        page += 1

    return all_orders

# What the response looks like:

# {
#   "data": [ {"id": 21}, {"id": 22}, ... ],
#   "pagination": {
#     "page": 3,
#     "limit": 10,
#     "total": 85,
#     "total_pages": 9
#   }
# }
