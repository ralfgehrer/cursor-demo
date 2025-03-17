# Cursor Project Overview for [Project Name]

This document serves as the primary reference guide for using Cursor effectively within our project. It outlines available project-specific prompts, documentation references, and best practices.

## Documentation References @Doc

The following documentation sources need to be added to your Cursor's @Docs reference settings for optimal AI assistance:

- **Alembic** - https://alembic.sqlalchemy.org/en/latest/



Add these references as described [here](https://docs.cursor.com/context/@-symbols/@-docs).

## Available Prompt Templates

### For Developers
- **[@.cursor/roles/Dev/create_component.md](./../roles/Dev/create_component.md)** - Creates standardized UI components
  - *Example:* `@.cursor/roles/Dev/create_component.md Create a data table with pagination`
- **[@.cursor/roles/Dev/create_endpoint.md](./../roles/Dev/create_endpoint.md)** - Implements RESTful API endpoints
  - *Example:* `@.cursor/roles/Dev/create_endpoint.md Create GET /users/:id endpoint`
- **[@.cursor/roles/Dev/optimize_query.md](./../roles/Dev/optimize_query.md)** - Optimizes database queries
  - *Example:* `@.cursor/roles/Dev/optimize_query.md Analyze and improve this query`
- **[@.cursor/roles/Dev/lint_fix.md](./../roles/Dev/lint_fix.md)** - Auto-fix linting issues
- **[@.cursor/roles/Dev/pre_commit_check.md](./../roles/Dev/pre_commit_check.md)** - Pre-commit validation

### For QA Engineers
- **[@.cursor/roles/QA/generate_unit_tests.md](./../roles/QA/generate_unit_tests.md)** - Creates comprehensive unit tests
  - *Example:* `@.cursor/roles/QA/generate_unit_tests.md @src/utils/validation.js`
- **[@.cursor/roles/QA/generate_e2e_tests.md](./../roles/QA/generate_e2e_tests.md)** - Creates E2E test scenarios
  - *Example:* `@.cursor/roles/QA/generate_e2e_tests.md for the login flow`
- **[@.cursor/roles/QA/create_test_mocks.md](./../roles/QA/create_test_mocks.md)** - Generates test fixtures and mocks
  - *Example:* `@.cursor/roles/QA/create_test_mocks.md for UserService`

### For Architects
- **[@.cursor/roles/Architect/code_review.md](./../roles/Architect/code_review.md)** - Performs in-depth code review
  - *Example:* `@.cursor/roles/Architect/code_review.md @src/components/Payment.jsx`
- **[@.cursor/roles/Architect/performance_review.md](./../roles/Architect/performance_review.md)** - Analyzes performance bottlenecks
  - *Example:* `@.cursor/roles/Architect/performance_review.md for this component`
- **[@.cursor/roles/Architect/refactor_plan.md](./../roles/Architect/refactor_plan.md)** - Creates refactoring strategies
  - *Example:* `@.cursor/roles/Architect/refactor_plan.md Decouple these classes`
- **[@.cursor/roles/Architect/architecture_review.md](./../roles/Architect/architecture_review.md)** - Review architectural decisions

## How to Use These Resources

1. In Cursor Chat, reference documentation with `@` symbol:
```
@.cursor/doc/PRD.md Help me implement the user authentication feature
```

2. Combine multiple references for context-rich responses:
```
@.cursor/doc/PRD.md @AuthService.ts Help me write unit tests for the login flow
```

3. Use role-specific prompts for standardized workflows:
```
@.cursor/roles/QA/generate_unit_tests.md @UserProfile.tsx
```