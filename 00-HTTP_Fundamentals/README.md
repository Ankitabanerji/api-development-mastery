# Chapter 1 - HTTP Fundamentals

> A complete guide to understanding the foundation of API development.

---

## 📖 Overview

Every modern API communicates using the **HTTP (HyperText Transfer Protocol)**.

Understanding HTTP is the first and most important step toward becoming a backend or API developer because every REST API, GraphQL API, and web service is built on top of HTTP.

This repository contains detailed notes, examples, interview questions, and practical knowledge about HTTP Fundamentals.

---

# 📚 Topics Covered

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

---

# What is HTTP?

HTTP (HyperText Transfer Protocol) is a request-response protocol used for communication between a client and a server over TCP/IP.

Example:

```
Browser  -------- Request -------->  Server

Browser  <------- Response --------- Server
```

Example:

You visit

```
https://github.com
```

Your browser sends a request.

GitHub server processes it.

GitHub sends back HTML, CSS, JavaScript, and images.

---

# Client and Server

Client

- Browser
- Mobile App
- React App
- Angular App
- Postman

Server

- FastAPI
- Flask
- Django
- Node.js
- Spring Boot

Example

```
React App

      |

HTTP Request

      |

FastAPI Backend

      |

Database
```

---

# Stateless Nature of HTTP

HTTP is Stateless.

Each request is completely independent.

The server does not remember previous requests unless we use

- JWT Tokens
- Cookies
- Sessions

---

# Anatomy of a URL

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

---

# HTTP Methods

## GET

Retrieve data.

Example

```
GET /users
```

CRUD

```
Read
```

---

## POST

Create new data.

Example

```
POST /users
```

CRUD

```
Create
```

---

## PUT

Replace an entire resource.

Example

```
PUT /users/5
```

---

## PATCH

Update selected fields.

Example

```
PATCH /users/5
```

---

## DELETE

Delete a resource.

Example

```
DELETE /users/5
```

---

## HEAD

Returns only headers.

Useful for checking whether a resource exists.

---

## OPTIONS

Returns supported HTTP methods.

Mostly used during CORS preflight requests.

---

## TRACE

Echoes the received request.

Used for diagnostics.

---

## CONNECT

Creates a secure tunnel through a proxy.

Used mainly for HTTPS.

---

# Safe Methods

Safe methods never modify server data.

Examples

- GET
- HEAD
- OPTIONS
- TRACE

---

# Unsafe Methods

Methods that modify server state.

Examples

- POST
- PUT
- PATCH
- DELETE

---

# Idempotent Methods

Calling multiple times gives the same final result.

Examples

- GET
- PUT
- DELETE
- HEAD
- OPTIONS

Example

```
DELETE /users/5
```

Calling it ten times still results in

```
User does not exist.
```

---

# Non-Idempotent Methods

Examples

- POST

Example

```
POST /users
```

Calling multiple times creates multiple users.

---

# HTTP Request Structure

```
POST /users HTTP/1.1

Host: api.example.com

Content-Type: application/json

Authorization: Bearer <token>

{
   "name":"Ankita"
}
```

Components

- Request Line
- Headers
- Blank Line
- Body

---

# HTTP Response Structure

```
HTTP/1.1 200 OK

Content-Type: application/json

{
    "id":1,
    "name":"Ankita"
}
```

Components

- Status Line
- Response Headers
- Blank Line
- Response Body

---

# HTTP Status Codes

## 1xx

Informational

Example

```
100 Continue
```

---

## 2xx

Success

Examples

```
200 OK

201 Created

204 No Content
```

---

## 3xx

Redirection

Examples

```
301 Moved Permanently

302 Found
```

---

## 4xx

Client Errors

Examples

```
400 Bad Request

401 Unauthorized

403 Forbidden

404 Not Found

409 Conflict

429 Too Many Requests
```

---

## 5xx

Server Errors

Examples

```
500 Internal Server Error

502 Bad Gateway

503 Service Unavailable

504 Gateway Timeout
```

---

# 401 vs 403

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

---

# Common HTTP Headers

## Request Headers

```
Content-Type

Accept

Authorization

Cache-Control
```

---

## Response Headers

```
Content-Type

Location

Retry-After

X-RateLimit-Limit

X-RateLimit-Remaining
```

---

# Real-world Example

User logs into an application.

```
POST /login
```

↓

Server verifies credentials.

↓

Returns

```
JWT Token
```

↓

Client stores token.

↓

Future requests

```
Authorization: Bearer <token>
```

---

# Author

**Ankita Banerji**

Learning API Development from fundamentals to advanced production-level concepts.
