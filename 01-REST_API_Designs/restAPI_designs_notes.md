# Chapter 1: REST API designs
REST (Representational State Transfer) is an architectural style for designing web services. A REST API exposes resources over the web using standard HTTP methods.
In REST, everything is a resource. A user, an order, a product, a session — all resources. Every resource has a URL (its identity). You interact with resources using HTTP methods. The server sends back a representation of the resource (usually JSON).

**Instead of calling functions like**:
```
createUser()
deleteProduct()
getOrders()
```

REST exposes resources using URLs:
```
/users
/products
/orders
```
Clients interact with these resources using HTTP methods.
**Example**:
GET    /users/5
POST   /users
PUT    /users/5
DELETE /users/5

## REST API Constraints

Roy Fielding defined 6 constraints. If an API satisfies these constraints, it is considered RESTful.
1. **Client-Server Constraint**:
    The client and server should be completely separate.
    The client handles:
    - UI
    - User interaction

    The server handles:
    - Database
    - Business logic
    - Authentication

    Neither should depend on each other internally.

    **Example**: The frontend only knows 
    `GET /users/5`
    It doesn't know SQL queries, Database schema, Internal code

    **Benefits**:
    - Independent development
    - Easier maintenance
    - Easy frontend replacement
    - Scalability

2. **Stateless Constraint**:
    Every request from the client must contain all information needed to process it. The server does not remember previous requests.
    **Example**: 
    Request 1:
    ```
    GET /profile
    Authorization: Bearer XYZ
    ```
    Server responds.
    Request 2:
    ```
    GET /orders
    Authorization: Bearer XYZ
    ```
    Server responds.

    The server does not remember Request 1. It treats Request 2 as a brand-new request.
    Every request contains:
    - Authorization Token
    - Language
    - Headers
    - Parameters

3. **Cacheable Constraint**:
    Servers should indicate whether responses can be cached. Caching avoids unnecessary repeated requests.
    **Example**:
    Client request: `GET /products`
    Server returns: `Cache-Control: max-age=600`
    Meaning: Store this response for 10 minutes. Future requests can use the cached response instead of contacting the server.

    **Benefits**:
    - Faster applications
    - Reduced server load
    - Better scalability
    - Lower bandwidth usage

4. **Uniform Interface (Most Important)**:
    This is what makes REST APIs consistent.  It has 4 sub-constraints.
    A. **Resource Identification**:
        Every resource should have a unique URI. Everything is a resource.
        **Example**: 
        ```
        /users/1
        /products/15
        /orders/101
        ```
        Not:
        
        ```
        getUser()
        findOrder()
        ```
    B. **Manipulation Through Representations**:
        Clients modify resources by sending a representation (usually JSON).
        **Example**
        `PUT /users/5`

        Body: 

        ```
        {
            "name":"John",
            "age":28
        }
        ```

        The server updates the resource using this representation.

    C. **Self-Descriptive Messages**:
        Every request and response should contain enough information to be understood independently.
        Headers tell the server/client how to interpret the message.

        **Example**:
        ``
        Content-Type: application/json
        Authorization: Bearer Token
        Accept: application/json
        ```

        Response:
        ```
        HTTP/1.1 200 OK
        Content-Type: application/json
        ```

        The client immediately knows how to process it.

    D. **HATEOAS (Hypermedia As The Engine Of Application State)**:
        Responses include links to possible next actions.
        **Example**:
        `JSON`
        ```
        {
        "id":10,
        "name":"Laptop",
        "links":[
            {
                "rel":"self",
                "href":"/products/10"
            },
            {
                "rel":"reviews",
                "href":"/products/10/reviews"
            },
            {
                "rel":"seller",
                "href":"/users/4"
            }
        ]
        }
        ```
        The client discovers available actions from the response instead of hardcoding every endpoint.
    
5. **Layered System**:
    The client should not know whether it is communicating directly with the application server or through intermediaries.
    Possible layers include:
    - Load balancer
    - API Gateway
    - Reverse Proxy
    - Cache Server
    - Authentication Service

    The client simply calls:
    `GET /users`
    It doesn't know how many layers are involved.

    **Example**:

    Client
    ↓
    API Gateway
    ↓
    Load Balancer
    ↓
    Application Server
    ↓
    Database

6. **Code on Demand (Optional)**:
    The server can send executable code to the client.
    Usually
    - JavaScript
    - WebAssembly

    **Example**
    A browser requests a page:
    ```
    GET /dashboard
    ```
    The server returns:
    ```
    HTML
    CSS
    JavaScript
    ```
    The JavaScript executes in the browser to provide interactive functionality.
    This constraint is optional, unlike the other five.

## URL Design Rules:

1. **Resources and URLs**:
    URLs identify nouns (resources). HTTP methods express verbs (actions).

    WRONG — verb in the URL
    ```
    GET  /getUser/42
    POST /createOrder
    GET  /deleteProduct/5
    POST /updateUserEmail
    ```

    RIGHT — noun in URL, verb is the HTTP method
    ```
    GET    /users/42
    POST   /orders
    DELETE /products/5
    PATCH  /users/42
    ```

    Here's how a REST API for an e-commerce system looks:
    **User API Endpoints**:
    | **Method** | **URL** | **Action** | **Success Response** |
    |--------|-----|--------|------------------|
    | GET | `/users` | List all users (paginated) | `200 OK` |
    | POST | `/users` | Create a new user | `201 Created` + `Location` header |
    | GET | `/users/{id}` | Get one user by ID | `200 OK` |
    | PUT | `/users/{id}` | Replace entire user record | `200 OK` or `204 No Content` |
    | PATCH | `/users/{id}` | Update specific fields | `200 OK` |
    | DELETE | `/users/{id}` | Delete a user | `204 No Content` |

    **Product API Endpoints**:
    | **Method** | **URL** | **Action** | **Success Response** |
    |--------|-----|--------|------------------|
    | GET | `/products` | List products (supports `?category=shoes&sort=price`) | `200 OK` |
    | POST | `/products` | Create a product | `201 Created` |
    | GET | `/products/{id}` | Get one product | `200 OK` |
    | PATCH | `/products/{id}` | Update price, stock, or other fields | `200 OK` |
    | DELETE | `/products/{id}` | Remove a product | `204 No Content` |

    **Order API Endpoints**:
    | **Method** | **URL** | **Action** | **Success Response** |
    |--------|-----|--------|------------------|
    | POST | `/orders` | Place a new order | `201 Created` |
    | GET | `/orders/{id}` | Get order details | `200 OK` |
    | GET | `/users/{id}/orders` | List all orders for a specific user | `200 OK` |
    | GET | `/orders/{id}/items` | Get line items for an order | `200 OK` |
    | PATCH | `/orders/{id}` | Update order status (e.g. cancel) | `200 OK` |

    **Design rule**: Nest resources at most 2 levels deep — /users/{id}/orders is fine. /users/{id}/orders/{oid}/items/{iid}/reviews is too deep. Flatten it to /reviews/{iid} instead.

2. **Request & Response Structure**:
    Every REST API should follow a consistent JSON structure.

    **Successful list response:**
    `GET /products?page=2&per_page=3`
    ```
    {
    "data": [
        { "id": 101, "name": "Running Shoes", "price": 2499 },
        { "id": 102, "name": "Yoga Mat",      "price": 899  },
        { "id": 103, "name": "Water Bottle",  "price": 349  }
    ],
    "pagination": {
        "page": 2,
        "per_page": 3,
        "total": 48,
        "total_pages": 16,
        "next": "/products?page=3&per_page=3",
        "prev": "/products?page=1&per_page=3"
    }
    }
    ```

    **Successful single resource response:**
    `GET /users/42`
    ```
    {
    "data": {
        "id": 42,
        "name": "Ankita",
        "email": "ankita@example.com",
        "created_at": "2024-01-15T10:30:00Z"
    }
    }
    ```

    **Error response — always be consistent:**
    ```
    POST /users  (with missing email field)
    HTTP/1.1 400 Bad Request
    ```

    ```
    {
    "error": {
        "code": "VALIDATION_ERROR",
        "message": "Request body is invalid",
        "details": [
        { "field": "email", "issue": "Email is required" },
        { "field": "name",  "issue": "Name must be at least 2 characters" }
        ]
    }
    }
    ```
    **Mistake**: returning 200 OK with {"success": false, "error": "..."} in the body. The HTTP status code IS the signal — don't bury errors in a 200 body.

3. **Idempotency in Practice — The Idempotency Key**:
    ```
    import requests
    import uuid

    def place_order(user_id, items):
        # Generate a unique key for this specific order attempt
        idempotency_key = str(uuid.uuid4())

        headers = {
            "Authorization": "Bearer <token>",
            "Idempotency-Key": idempotency_key,  # ← the magic
            "Content-Type": "application/json"
        }

        payload = {"user_id": user_id, "items": items}

        # Even if this fires 3 times due to network retries,
        # the server will only create ONE order
        for attempt in range(3):
            try:
                response = requests.post(
                    "https://api.shop.com/orders",
                    json=payload,
                    headers=headers,
                    timeout=5
                )
                if response.status_code in (200, 201):
                    return response.json()
            except requests.Timeout:
                print(f"Attempt {attempt+1} timed out, retrying...")

        raise Exception("Order placement failed after 3 attempts")
    ```
    The server stores (idempotency_key → response) for ~24 hours. If the same key arrives again, it returns the stored response instead of creating a duplicate. This is exactly how Stripe, Razorpay, and Paytm handle payment APIs.

4. **API Versioning**:
    When you change a public API, you can't break existing clients. Versioning is how you manage that evolution.
    | Strategy | Example | Advantages | Disadvantages | Common Usage |
    |----------|---------|--------------|------------------|--------------|
    | **URL Path Versioning** ⭐ *Most Common* | ```http GET /api/v1/users/42 GET /api/v2/users/42 ``` | - Explicit and easy to test in a browser<br>- Easy to route at the load balancer level<br>- Cache-friendly (different URLs) | - Version in URL violates the REST purist view that a URI identifies a resource | Stripe, GitHub, X (Twitter), Razorpay |
    | **Query Parameter** | ```http GET /users/42?version=1 GET /users/42?api-version=2 ``` | - Single URL with optional version parameter<br>- Easy backward compatibility (default to v1) | - Easy to forget the parameter<br>- Pollutes the query string | Microsoft Azure APIs |
    | **Custom Header** | ```http GET /users/42 X-API-Version: 2 ``` | - Keeps the URL clean | - Cannot be tested directly in a browser<br>- Headers are not cached by default | Internal microservices |
    | **Accept Header (Content Negotiation)** | ```http Accept: application/vnd.myapi.v2+json ``` | - Semantically the most RESTful approach | - Very verbose and unfriendly<br>- Hard to test<br>- Lower adoption | GitHub (secondary support) |

    For most REST APIs, **URL Path Versioning** is the preferred approach because it is:
    - Explicit
    - Easy to understand
    - Browser-friendly
    - Cache-friendly
    - Supported by API gateways and load balancers
    - Used by most public APIs

    **Example**

    ```http
    GET /api/v1/users
    GET /api/v2/users
    ```

    **How to deprecate old versions?**
    Suppose our API currently has:
    `/api/v1/users`

    We release a new version:
    `/api/v2/users`

    We don't want to break existing applications immediately because many clients are still using v1. Instead, we:
    - Continue supporting v1 for a period (e.g., 12 months).
    - Tell clients that v1 will be retired.
    - Eventually remove v1 after the announced date.

    The HTTP `Sunset` response header tells clients when an API (or API version) will no longer be available.
    **A client calls**:
    `GET /api/v1/users/42`

    **Your server responds**:
    ```
    HTTP/1.1 200 OK
    Content-Type: application/json
    Sunset: Sat, 31 Dec 2026 00:00:00 GMT

    {
        "id": 42,
        "name": "John Doe"
    }
    ```
    This means: The request still succeeds, but the client is informed that this API version will stop being supported after 31 December 2026. Please migrate before then.

    Many APIs send both a `Deprecation header` and a `Sunset header`.
    ```
    HTTP/1.1 200 OK
    Deprecation: true
    Sunset: Sat, 31 Dec 2026 00:00:00 GMT
    Link: </api/v2/users/42>; rel="successor-version"
    ```

    Here:
    - Deprecation: true → This version is deprecated.
    - Sunset → It will stop working after this date.
    - Link → Points clients to the replacement API version.

5. **Pagination — Three Patterns:**
    Any endpoint that returns a list needs pagination.
     
    - **Offset-based (most common, easiest to implement):**
        ```
        GET /products?offset=20&limit=10
        or
        GET /products?page=3&per_page=10
        ```
        - Simple to implement and understand
        - Problem: 
            The hidden problem:
            ```
            DB has 100 orders. You request page 10 (offset=90).

            Database internally does:
            Scan row 1   → discard
            Scan row 2   → discard
            Scan row 3   → discard
            ...
            Scan row 90  → discard   ← wasted work
            Scan row 91  → return ✓
            Scan row 92  → return ✓
            ...

            As your table grows to 10 million rows,
            offset=9,999,990 scans and discards 10M rows.
            THAT is why offset is slow at scale.
            ```

            The phantom read problem:
            Imagine you have a list of orders in your database, sorted newest first:
            ```
            Position 1  →  Order #5  (newest)
            Position 2  →  Order #4
            Position 3  →  Order #3
            Position 4  →  Order #2
            Position 5  →  Order #1  (oldest)
            ```
            You're showing these to a user, 3 orders per page.

           `Step 1 — User loads Page 1`
            ```
            GET /orders?page=1&limit=3
            → offset=0, fetch 3 rows

            DB returns:
            Position 1 → Order #5  ✓
            Position 2 → Order #4  ✓
            Position 3 → Order #3  ✓
            ```
            User sees: Order 5, Order 4, Order 3. All good.

            `Step 2 — A new order arrives BETWEEN page loads`
            While the user is reading page 1, someone places Order #6 (brand new, goes to the top):
            ```
            Position 1  →  Order #6  ← NEW! just inserted
            Position 2  →  Order #5
            Position 3  →  Order #4
            Position 4  →  Order #3  ← everything shifted DOWN by 1
            Position 5  →  Order #2
            Position 6  →  Order #1
            ```

            Step 3 — User clicks "Next Page" (Page 2)
            ```
            GET /orders?page=2&limit=3
            → offset=3, fetch rows starting from position 4

            DB returns:
            Position 4 → Order #3  ← user already saw this on page 1!
            Position 5 → Order #2
            Position 6 → Order #1
            ```
            The word phantom means ghost — something that appears but shouldn't be there. Order #3 appeared on page 2 like a ghost even though the user already saw it on page 1. It wasn't a real "new" result — it was a duplicate caused by the shift in positions.
            The same problem works in reverse too — if an order gets deleted between page loads, one order silently disappears and the user never sees it. That's the other kind of phantom — a record that should appear but doesn't.

            **Use when:** Data is small, you need "jump to page 5" functionality, admin dashboards, small datasets.
            **Avoid when:** Real-time feeds, large tables (millions of rows), infinite scroll.

    - **Cursor-based (used by Facebook, Twitter, Slack):**
        ```
        GET /posts?limit=10&cursor=eyJpZCI6MTIzfQ==
        # Response includes:
        { "next_cursor": "eyJpZCI6MTMzfQ==", "data": [...] }
        ```

        - The cursor encodes the position (usually a base64-encoded ID or timestamp)
        - Stable even when data changes — no duplicates
        - Can't jump to page 5 directly (no random access)
        - Best for real-time feeds and infinite scroll

        **Use when:** Infinite scroll (Instagram, Twitter), real-time feeds, any large dataset.
        **Avoid when:** User needs to jump to page 5 directly, or needs to know the total count.

    - **Keyset / seek-based (fastest at scale):**
        ```
        GET /orders?after_id=5000&limit=20
        ```
        - Uses the database's indexed column directly — no OFFSET clause
        - SELECT * FROM orders WHERE id > 5000 LIMIT 20
        - Extremely fast even on millions of rows
        - Same limitation as cursor: no random access

    **"Why is offset pagination slow on large tables?"**
    SELECT * FROM orders OFFSET 100000 LIMIT 10 makes the DB scan and discard 100,000 rows.
    With keyset/cursor, it jumps directly to the right index position — O(log n) instead of O(n).

    | Property | Offset Pagination | Cursor Pagination | Keyset Pagination |
    |----------|-------------------|-------------------|-------------------|
    | **Speed on large tables** | Slow — **O(offset)** | Fast — Index-based | Fastest — **O(log n)** |
    | **Stable with inserts/deletes?** | No — duplicates or skipped records possible | Yes — cursor is anchored | Yes — ID/key anchored |
    | **Jump to page N directly** | Yes — `offset = (page - 1) × limit` | No — must walk forward | No — must walk forward |
    | **Know total count** | Easy — `COUNT(*)` query | Hard — expensive query | Hard — expensive query |
    | **Implementation complexity** | Simple | Medium | Medium |
    | **Typical API** | `GET /users?page=3&limit=10` | `GET /users?cursor=abc&limit=10` | `GET /users?after_id=500&limit=10` |
    | **Best use case** | Admin panels, dashboards, small datasets | Social media feeds, infinite scrolling | High-traffic APIs, event logs, audit tables |
    | **Used by** | Most basic REST APIs | Twitter (X), Slack, Meta | Stripe and other high-scale APIs |

6. **HATEOAS — What It Is and Why Most APIs Skip It**
    HATEOAS (Hypermedia As The Engine Of Application State) is the idea that an API response should include links to all possible next actions. The client should never need to hardcode URLs.
    **Example:**
    ```
    GET /orders/99
    ```
    Response:
    ``` 
    {
    "data": {
        "id": 99,
        "status": "pending",
        "total": 1499
    },
    "links": {
        "self":   { "href": "/orders/99",        "method": "GET"    },
        "cancel": { "href": "/orders/99/cancel", "method": "POST"   },
        "pay":    { "href": "/payments",         "method": "POST"   },
        "user":   { "href": "/users/42",         "method": "GET"    }
    }
    }
    ```
    The client reads the links object and knows what it can do next — without any hardcoded URL logic. In theory, the server can change URL structures freely because clients follow links dynamically.
    In practice: most REST APIs don't implement this because it significantly increases response payload size and adds complexity.