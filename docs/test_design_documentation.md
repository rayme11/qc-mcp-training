# Test Design & Documentation

## Goal
Design comprehensive test cases for JSONPlaceholder endpoints and document them clearly. This step ensures you have a structured plan for what to test, how to test, and what results to expect.

## Steps
1. For each endpoint and scenario identified in the coverage review, design test cases:
   - Define test steps
   - Specify input data
   - State expected results
   - Note priorities (critical, normal, edge)
2. Use a template for consistency:
   - Test Case ID
   - Title
   - Endpoint & Method
   - Input Data
   - Expected Result
   - Priority
   - Notes
3. Document your test cases in this file for traceability.

## Example Test Case Template

| Test Case ID | Title                        | Endpoint     | Method | Input Data                | Expected Result         | Priority | Notes           |
|--------------|------------------------------|--------------|--------|--------------------------|------------------------|----------|-----------------|
| TC01         | Get all posts                | /posts       | GET    | None                     | 100 posts returned     | Normal   | Basic retrieval |
| TC02         | Get post by valid ID         | /posts/1     | GET    | id=1                     | Post with id=1         | Critical | Valid ID        |
| TC03         | Get post by invalid ID       | /posts/999   | GET    | id=999                   | 404 Not Found          | Edge     | Invalid ID      |
| TC04         | Create new post              | /posts       | POST   | title, body, userId      | New post created       | Critical | Valid data      |
| TC05         | Create post missing title    | /posts       | POST   | body, userId             | Error, missing title   | Edge     | Invalid data    |
| TC06         | Update post with valid data  | /posts/1     | PUT    | title, body, userId      | Post updated           | Normal   | Valid update    |
| TC07         | Update post with missing body| /posts/1     | PUT    | title, userId            | Error, missing body    | Edge     | Invalid update  |
| TC08         | Delete post by valid ID      | /posts/1     | DELETE | id=1                     | Post deleted           | Critical | Valid delete    |
| TC09         | Delete post by invalid ID    | /posts/999   | DELETE | id=999                   | 404 Not Found          | Edge     | Invalid delete  |
| TC10         | Get comments for post        | /posts/1/comments | GET | id=1                 | Array of comments      | Normal   | Related data    |
| TC11         | Get user by valid ID         | /users/1     | GET    | id=1                     | User with id=1         | Critical | Valid user      |
| TC12         | Get user by invalid ID       | /users/999   | GET    | id=999                   | 404 Not Found          | Edge     | Invalid user    |
| TC13         | Create comment with valid data| /comments   | POST   | name, email, body, postId| New comment created    | Critical | Valid comment   |
| TC14         | Create comment missing email | /comments    | POST   | name, body, postId       | Error, missing email   | Edge     | Invalid comment |
| TC15         | Get posts filtered by userId | /posts?userId=1 | GET | userId=1               | Posts for userId=1     | Normal   | Query param     |
| TC16         | Partial update post (PATCH)  | /posts/1     | PATCH  | title                    | Post updated           | Normal   | Partial update  |
| TC17         | Get post after delete        | /posts/1     | GET    | id=1                     | 404 Not Found          | Edge     | Deleted post    |

## Further Reading
- [Test Design Techniques](https://www.guru99.com/software-testing-techniques.html)
- [API Testing Guide](https://www.postman.com/api-platform/api-testing/)

---

> Proceed to Automation Implementation after completing your test design documentation.
