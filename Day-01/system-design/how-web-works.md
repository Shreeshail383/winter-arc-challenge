# How the Web Works — Request Lifecycle

## Overview

When a user enters a URL in a browser, the browser locates the server, establishes a connection, sends an HTTP request, receives a response, and renders the webpage.

**Request lifecycle:**

`URL → DNS → TCP → TLS → HTTP Request → HTTP Response → Browser Rendering`

## 1. URL Parsing
The browser parses the URL into its components: scheme (`https`), hostname (`example.com`), path (`/home`), and optional query parameters.

## 2. DNS Resolution
DNS (Domain Name System) translates the hostname into an IP address so the browser can locate the server. The browser or operating system may use a cached DNS result to avoid another lookup.

## 3. Connection Establishment
For HTTP/1.1 and HTTP/2 over HTTPS, the browser typically establishes a TCP connection with the server. For HTTPS, TLS negotiates encryption and authenticates the server using its certificate.

HTTP/3 uses QUIC over UDP instead of TCP and integrates TLS security into the QUIC handshake.

## 4. HTTP Request
The browser sends an HTTP request containing a method (GET, POST, etc.), path, headers, and, when needed, a body.

Example: `GET /home HTTP/1.1`

The request travels through the network to the web server, potentially passing through a CDN, load balancer, or reverse proxy.

## 5. Server Processing
The server processes the request. It may execute application code, query a database, call another service, or return a cached result.

## 6. HTTP Response
The server returns an HTTP response containing a status code, headers, and an optional body.

Examples:
- `200 OK` — request succeeded.
- `301 Moved Permanently` — redirect.
- `404 Not Found` — resource not found.
- `500 Internal Server Error` — server encountered an error.

## 7. Browser Rendering
The browser processes the HTML and discovers referenced CSS, JavaScript, images, and other resources. It builds the DOM and CSSOM, calculates layout, paints pixels, and executes JavaScript. Additional network requests may be required to load these resources.

## Interview Summary

“When a user enters a URL, the browser parses it and resolves the hostname through DNS. It establishes the required network connection and, for HTTPS, secures it with TLS. The browser sends an HTTP request to the server. The server processes the request and returns an HTTP response. Finally, the browser parses the response, loads dependent resources, executes JavaScript, and renders the page.”

**Key distinction:** DNS finds the server's IP address; TCP or QUIC provides transport; TLS secures the connection; HTTP defines the request and response.