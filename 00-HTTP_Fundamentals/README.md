# Chapter 0 - HTTP Fundamentals

## 📚 Topics Covered

- Overview
- What is HTTP?
- Client-Server Architecture
- Stateless Communication
- Anatomy of a URL
- HTTP Methods
- Safe vs Unsafe Methods
- Idempotent vs Non-Idempotent Methods
- HTTP Request Structure
- HTTP Response Structure
- HTTP Status Codes
- Important HTTP Headers
- Real-world API Examples
- Interview Questions


## 📖 Overview

Every modern API communicates using the **HTTP (HyperText Transfer Protocol)**.

Understanding HTTP is the first and most important step toward becoming a backend or API developer because every REST API, GraphQL API, and web service is built on top of HTTP.

This repository contains detailed notes, examples, interview questions, and practical knowledge about HTTP Fundamentals.

## What is HTTP?

**HTTP (HyperText Transfer Protocol)** is a request-response protocol used for communication between a client and a server over TCP/IP.

```
    Browser  -------- Request -------->  Server

    Browser  <------- Response --------- Server
```

**Example**:

    You visit `https://github.com`

    - Your browser sends a request.
    - GitHub server processes it.
    - GitHub sends back HTML, CSS, JavaScript, and images.

## Client and Server Architecture

It is a software architecture in which clients request services or resources, and a server processes those requests and returns the appropriate response over a network.

**Client**: The application or device that initiates a request (e.g., a web browser, mobile app, or desktop application).
**Server**: A centralized system that receives requests, executes business logic, accesses databases if needed, and sends back responses.
**Communication**: Typically happens using protocols such as HTTP/HTTPS, TCP/IP, or WebSocket.
**Example**:
When you open a website:
- Your browser (client) sends a request to the web server.
- The server processes the request, retrieves data from the database if necessary.
- The server sends the webpage or data back to the browser.
- The browser displays the result.

## Stateless Nature of HTTP

HTTP is Stateless.
Each request is completely independent.
The server does not remember previous requests unless we use
- JWT Tokens
- Cookies
- Sessions

## Anatomy of a URL

Example

```
https://api.github.com:443/users/ankita/repos?sort=stars&page=1
```

Components

| Part | Example |
|-------|----------|
| Scheme | https |
| Host | api.github.com |
| Port | 443 |
| Path | /users/ankita/repos |
| Query Parameters | sort=stars&page=1 |
| Fragment | #section |

> **NOTES**: What's the difference between a path parameter and a query parameter?
- Path params identify a resource (/users/123). 
- Query params filter or modify (?sort=asc).

## HTTP Methods
HTTP methods tell the server what action you want to perform.

| Method |	What it does |	Example |
|--------|---------------|----------|
| GET | Fetch existing data | GET /users/5 |
| POST | Create a new resource | POST /users |
| PUT | Replace the entire resource | PUT /users/5 |
| PATCH | Update only selected fields	| PATCH /users/5 |
| DELETE | Delete a resource	| DELETE /users/5 |
| HEAD | Get headers without the body	| HEAD /report.pdf |
| OPTIONS | Discover allowed methods	| OPTIONS /users |
| TRACE | Echo the request for diagnostics	| TRACE /users |
| CONNECT | Create a proxy tunnel	Used by proxies | for HTTPS |

## HTTP Methods Cheat Sheet

| HTTP Method | Purpose | CRUD Operation | Safe | Idempotent | Request Body | Common Status Codes | Real-World Example |
|-------------|---------|----------------|------|------------|--------------|---------------------|-------------------|
| **GET** | Retrieve data from the server | Read | ✅ Yes | ✅ Yes | ❌ No | `200`, `304`, `404` | Get user profile |
| **POST** | Create a new resource | Create | ❌ No | ❌ No | ✅ Yes | `201`, `200`, `400`, `409` | Create a new user |
| **PUT** | Replace an entire resource | Update | ❌ No | ✅ Yes | ✅ Yes | `200`, `201`, `204`, `404` | Update all details of a user |
| **PATCH** | Partially update a resource | Update | ❌ No | Usually ✅* | ✅ Yes | `200`, `204`, `400`, `404` | Update only the email address |
| **DELETE** | Remove a resource | Delete | ❌ No | ✅ Yes | Usually No | `200`, `202`, `204`, `404` | Delete a user |
| **HEAD** | Retrieve only headers (no response body) | Read | ✅ Yes | ✅ Yes | ❌ No | `200`, `404` | Check if a file exists |
| **OPTIONS** | Return supported HTTP methods for a resource | N/A | ✅ Yes | ✅ Yes | ❌ No | `200`, `204` | Browser CORS preflight request |
| **TRACE** | Echo back the received request for debugging | N/A | ✅ Yes | ✅ Yes | ❌ No | `200` | Diagnostic testing (rarely enabled) |
| **CONNECT** | Establish a tunnel to another server (usually HTTPS via proxy) | N/A | ❌ No | ❌ No | No | `200` | HTTPS proxy connection |

> **Note:** `PATCH` is generally considered idempotent **only if** the patch operation itself is designed to be idempotent. The HTTP specification does not require it.

**Safe** — The method does NOT change server state. You can call it 100 times and the data on the server is untouched.
- `SAFE METHODS`: GET, HEAD, OPTION, TRACE
- `UNSAFE METHODS`: POST, PUT, PATCH, DELETE, CONNECT

**Idempotent** — Calling it once vs. calling it 10 times produces the same result.
-`IDEMPOTENT`: GET, PUT, DELETE, HEAD, OPTION, TRACE
- `NON-IDEMPOTENT`: POSAT, CONNECT

## HTTP Request Structure
Every HTTP request has this exact structure:
```
METHOD  /path  HTTP/1.1          ← Request line
Host: api.example.com            ─┐
Content-Type: application/json    │ Headers
Authorization: Bearer <token>    ─┘
                                  ← Blank line (MANDATORY separator)
{                                ─┐
  "name": "Ankita"                │ Body (optional — GET has no body)
}                                ─┘
```
**A real GET request**:
```
GET /users/42 HTTP/1.1
Host: api.github.com
Accept: application/json
Authorization: Bearer ghp_xxxx
```

**A real POST request**:
```
POST /users HTTP/1.1
Host: api.example.com
Content-Type: application/json
Content-Length: 27

{"name": "Ankita", "age": 23}
```

## HTTP Response Structure
The server responds with:

```HTTP/1.1  200  OK                 ← Status line (version · code · reason)
Content-Type: application/json   ─┐
Date: Wed, 02 Jul 2026 10:00:00   │ Response headers
X-RateLimit-Remaining: 58        ─┘
                                  ← Blank line
{                                ─┐
  "id": 42,                       │ Response body
  "name": "Ankita"               ─┘
}
```

## HTTP Status Codes

**1xx**: Informational
Example

```
100 Continue
```

**2xx**: Success
Examples

```
200 OK

201 Created

204 No Content
```

**3xx**: Redirection
Examples

```
301 Moved Permanently

302 Found
```

**4xx**: Client Errors
Examples

```
400 Bad Request

401 Unauthorized

403 Forbidden

404 Not Found

409 Conflict

429 Too Many Requests
```

**5xx**: Server Errors
Examples

```
500 Internal Server Error

502 Bad Gateway

503 Service Unavailable

504 Gateway Timeout
```

## 401 vs 403

401 Unauthorized

```
"I don't know who you are."
```

Authentication required.

---

403 Forbidden

```
"I know who you are, but you cannot access this resource."
```

Authorization failure.


## Common HTTP Headers

**Request Headers**

```
Content-Type: application/json     # Format of the body I'm sending
Accept: application/json           # Format I want back
Authorization: Bearer <token>      # My credentials
Cache-Control: no-cache            # Don't use cached data
```

**Response Headers**

```
Content-Type: application/json     # Format of body being returned
X-RateLimit-Limit: 60             # Max requests per hour
X-RateLimit-Remaining: 58         # How many left
Retry-After: 30                   # Wait 30s before retrying (after 429)
Location: /users/42               # Where the new resource lives (after 201)
```
## Chapter 0 — Summary
| Concept |	What to remember |
| HTTP	|	Stateless request–response protocol over TCP |
| URL	|	scheme + host + port + path + query + fragment |
| Methods	|	GET (read), POST (create), PUT (replace), PATCH (update), DELETE (remove) |
| Safe	|	No side effects — GET only |
| Idempotent	|	Same result on repeat calls — GET, PUT, DELETE |


## Real-world Example

User logs into an application.

```
POST /login
```

↓

Server verifies credentials.

↓

Returns ```JWT Token```

↓

Client stores token.

↓

Future requests ```Authorization: Bearer <token>```


# Author

**Ankita Banerji**

Learning API Development from fundamentals to advanced production-level concepts.
