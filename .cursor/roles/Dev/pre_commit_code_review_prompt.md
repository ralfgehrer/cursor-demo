# Pre-Commit Code Review

Please review the provided code changes before I commit them, focusing on:

## Review Criteria
- Code quality and adherence to our style guidelines
- Potential bugs or edge cases
- Performance considerations
- Security vulnerabilities
- Test coverage
- Documentation completeness

## Output Format
Provide a structured review with:
1. Overall assessment
2. Critical issues that must be fixed
3. Recommendations for improvements (optional)
4. A checklist of items to verify before commit

## Example
```
## Code Review Results

### Overall Assessment
The changes look generally good but have 2 critical issues to address.

### Critical Issues
1. Missing input validation for user-provided data on line 45
2. Potential memory leak in useEffect (missing dependency array)

### Recommendations
- Consider extracting the form logic into a custom hook
- Add more descriptive variable names in the processing function

### Pre-Commit Checklist
- [ ] Fix input validation
- [ ] Fix useEffect dependency array
- [ ] Run linter
- [ ] Run unit tests
- [ ] Verify the component works in development environment
```