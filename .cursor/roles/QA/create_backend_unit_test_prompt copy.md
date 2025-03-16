# Unit Test Creation Template

This template helps create comprehensive unit tests for Python functions and classes.

## Function/Class to Test
```python
# Paste the function or class to test here
```

## Test Requirements
- Test all function parameters and return values
- Cover edge cases and error conditions
- Use mocks for external dependencies
- Aim for high code coverage
- Follow pytest conventions

## Example Test Structure
```python
import pytest
from unittest.mock import MagicMock, patch

def test_function_name_scenario_being_tested():
    # ARRANGE - Set up test data and mocks
    
    # ACT - Call the function being tested
    
    # ASSERT - Verify the expected outcomes
    
    # Clean up if needed

def test_function_name_error_case():
    # Test error handling
    
    # ...
```

## Additional Testing Tips
- Use parametrized tests for multiple similar test cases
- Test both success and failure paths
- Mock external services and dependencies
- Consider using fixtures for common setup
- Add docstrings to explain complex test scenarios