# Test Coverage Review

## Goal
Review existing tests and identify gaps using public repo examples. This step ensures you know what is already tested, what needs coverage, and how to prioritize new tests for MCP automation.

## Steps
1. Find a public repo or project that uses JSONPlaceholder or similar APIs for testing (e.g., [jsonplaceholder/tests](https://github.com/typicode/jsonplaceholder)).
2. Review the test files and documentation:
   - What endpoints are covered?
   - What scenarios are tested (success, error, edge cases)?
   - What data is used for testing?
3. Document your findings:
   - List endpoints and scenarios with existing coverage
   - Identify gaps (untested endpoints, missing error cases, etc.)
   - Note any reusable test data or helpers
4. Summarize your review in this file for traceability.


## Example Table
| Endpoint     | Scenario                  | Covered | Notes                        |
|--------------|---------------------------|---------|------------------------------|
| /posts       | GET all posts             | Yes     | Basic retrieval              |
| /posts/{id}  | GET by ID                 | Yes     | Valid/invalid ID             |
| /posts       | POST new post             | Yes     | Valid/invalid data           |
| /posts/{id}  | PUT update post           | No      | Needs coverage               |
| /posts/{id}  | DELETE post               | No      | Needs coverage               |
| /comments    | GET all comments          | Yes     | Basic retrieval              |
| /comments/{id}| GET comment by ID        | No      | Add valid/invalid ID         |
| /comments    | POST new comment          | No      | Add valid/invalid data       |
| /users       | GET all users             | Yes     | Basic retrieval              |
| /users/{id}  | GET user by ID            | No      | Add valid/invalid ID         |
| /users       | POST new user             | No      | Add valid/invalid data       |
| /posts       | GET with query params     | No      | Filter by userId, etc.       |
| /posts/{id}  | PATCH partial update      | No      | Needs coverage               |
| /posts/{id}  | GET after DELETE          | No      | Should return not found      |

## Further Reading
- [pytest Documentation](https://docs.pytest.org/en/latest/)
- [JSONPlaceholder Test Examples](https://github.com/typicode/jsonplaceholder)

---

> Proceed to Test Design & Documentation after completing your test coverage review.
