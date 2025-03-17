# Generate FastAPI pytest for endpoint

Generate a pytest test function for the specified FastAPI endpoint. Follow these guidelines:

1. Use pytest fixtures for database and authentication - reuse exisiting ones or create new fixtures for additional tests
2. Include both successful case and at least one error case
3. Follow our project's existing test patterns
4. Ensure proper validation of response status codes and content

Example: see tests @backend/app/tests/api/routes/test_items.py for @backend/app/api/routes/items.py
