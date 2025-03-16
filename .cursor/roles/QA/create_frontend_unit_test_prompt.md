# Unit Test Generation

Please generate comprehensive unit tests for the provided file.

## Test Requirements
- Use Jest and React Testing Library
- Follow AAA pattern (Arrange, Act, Assert)
- Include tests for all public functions/methods
- Cover both success and error scenarios
- Mock external dependencies
- Follow our naming convention: `describe('ComponentName', () => { ... })`
- Group related tests within nested describe blocks
- Use appropriate assertions based on function behavior

## Output Format
Provide a complete test file named [filename].test.[extension]

## Examples
For a component:
```tsx
import { render, screen, fireEvent } from '@testing-library/react';
import { ComponentName } from './ComponentName';

describe('ComponentName', () => {
  it('should render correctly', () => {
    // Arrange
    render(<ComponentName />);
    
    // Act
    const element = screen.getByText('Expected Text');
    
    // Assert
    expect(element).toBeInTheDocument();
  });
  
  // Additional tests...
});