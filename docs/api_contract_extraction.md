# API Contract Extraction

## Goal
Understand and document API contracts using OpenAPI/Swagger from public APIs. This step ensures you know what endpoints, methods, schemas, and validation rules are available for testing and automation.

## Steps
1. Choose a public API with an OpenAPI/Swagger spec (e.g., [JSONPlaceholder](https://jsonplaceholder.typicode.com/), [GitHub API](https://docs.github.com/en/rest/reference)).
2. Locate the OpenAPI/Swagger documentation for the API.
3. Review the endpoints and HTTP methods available.
4. For each endpoint, document:
   - URL
   - HTTP method
   - Request parameters and schema
   - Response schema and status codes
   - Authentication requirements (if any)
   - Validation rules and error codes
5. Summarize your findings in a table or bullet list.
6. Save your analysis in this file for traceability.


## JSONPlaceholder API Contract Example

JSONPlaceholder is a free, fake REST API for testing and prototyping. It provides endpoints for posts, comments, users, and more.

### Endpoints
| Endpoint     | Method | Request Schema         | Response Schema        | Auth | Notes                  |
|--------------|--------|-----------------------|------------------------|------|------------------------|
| /posts       | GET    | None                  | Array of Post objects  | None | Get all posts          |
| /posts/{id}  | GET    | None                  | Single Post object     | None | Get a post by ID       |
| /posts       | POST   | PostCreate (title, body, userId) | Post object | None | Create a new post      |
| /posts/{id}  | PUT    | PostUpdate (title, body, userId) | Post object | None | Update a post          |
| /posts/{id}  | DELETE | None                  | Empty                  | None | Delete a post          |

### What Each Column Means
- **Endpoint:** The URL path for the API resource (e.g., /posts).
- **Method:** The HTTP method (GET, POST, PUT, DELETE) used to interact with the endpoint.
- **Request Schema:** The structure of data you send to the API (e.g., fields required to create a post).
- **Response Schema:** The structure of data returned by the API (e.g., a Post object or array of posts).
- **Auth:** Whether authentication is required (JSONPlaceholder does not require auth).
- **Notes:** Additional info about the endpoint’s purpose or behavior.

### Example: Creating a Post
- **Endpoint:** /posts
- **Method:** POST
- **Request Schema:**
   - title (string)
   - body (string)
   - userId (integer)
- **Response Schema:**
   - id (integer)
   - title (string)
   - body (string)
   - userId (integer)

### Why This Matters
Understanding the API contract helps you:
- Know what data you can send and receive
- Design tests for each endpoint and scenario
- Identify required vs optional fields
- Check validation rules and error handling
- Ensure your automation matches the API’s structure

## Further Reading
- [OpenAPI Specification](https://swagger.io/specification/)
- [JSONPlaceholder API Docs](https://jsonplaceholder.typicode.com/)

---

> Proceed to Test Coverage Review after completing your API contract extraction.
