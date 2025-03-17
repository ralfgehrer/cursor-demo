# Cursor Project Overview 
This document serves as the primary reference guide for using Cursor effectively within our project. It outlines available project-specific prompts, documentation references, and best practices.

## Documentation References @Doc

The following documentation sources need to be added to your Cursor's @Docs reference settings for optimal AI assistance:

- **Alembic** - https://alembic.sqlalchemy.org/en/latest/



Add these references as described [here](https://docs.cursor.com/context/@-symbols/@-docs).

## Available Prompt Templates

### For Architects
- **[@.cursor/roles/Architekt/create_adr.md](./../roles/Architekt/create_adr.md)** - Creates Architecture Decision Records
  - *Example:* `@.cursor/roles/Architekt/create_adr.md Document our API versioning strategy`
- **[@.cursor/roles/Architekt/design_system_interface.md](./../roles/Architekt/design_system_interface.md)** - Designs clean system interfaces
  - *Example:* `@.cursor/roles/Architekt/design_system_interface.md Design interface between auth and user services`
- **[@.cursor/roles/Architekt/plan_plan_act_pattern.md](./../roles/Architekt/plan_plan_act_pattern.md)** - Creates structured implementation plans
  - *Example:* `@.cursor/roles/Architekt/plan_plan_act_pattern.md Plan the user authentication feature + more contexct`

### For Developers
- **[@.cursor/roles/Dev/code_refactoring_steps.md](./../roles/Dev/code_refactoring_steps.md)** - Improves code quality and maintainability
  - *Example:* `@.cursor/roles/Dev/code_refactoring_steps.md Refactor the user authentication code`
- **[@.cursor/roles/Dev/create_hello_world.md](./../roles/Dev/create_hello_world.md)** - Creates simple starter code
  - *Example:* `@.cursor/roles/Dev/create_hello_world.md Generate a greeting function`
- **[@.cursor/roles/Dev/implement_error_handling.md](./../roles/Dev/implement_error_handling.md)** - Adds robust error handling patterns
  - *Example:* `@.cursor/roles/Dev/implement_error_handling.md Add error handling to API client`
- **[@.cursor/roles/Dev/pre_commit_code_review_prompt.md](./../roles/Dev/pre_commit_code_review_prompt.md)** - Pre-commit validation and review
  - *Example:* `@.cursor/roles/Dev/pre_commit_code_review_prompt.md Review my changes before commit`

### For QA Engineers
- **[@.cursor/roles/QA/create_backend_unit_test_prompt.md](./../roles/QA/create_backend_unit_test_prompt.md)** - Creates backend unit tests
  - *Example:* `@.cursor/roles/QA/create_backend_unit_test_prompt.md @src/services/auth.js`
- **[@.cursor/roles/QA/create_frontend_unit_test_prompt.md](./../roles/QA/create_frontend_unit_test_prompt.md)** - Creates frontend unit tests
  - *Example:* `@.cursor/roles/QA/create_frontend_unit_test_prompt.md @src/components/Login.jsx`
- **[@.cursor/roles/QA/identify_edge_cases.md](./../roles/QA/identify_edge_cases.md)** - Discovers potential edge cases
  - *Example:* `@.cursor/roles/QA/identify_edge_cases.md Find edge cases in the registration flow`
- **[@.cursor/roles/QA/test_strategy.md](./../roles/QA/test_strategy.md)** - Develops comprehensive test strategies
  - *Example:* `@.cursor/roles/QA/test_strategy.md Create test strategy for payment processing`


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