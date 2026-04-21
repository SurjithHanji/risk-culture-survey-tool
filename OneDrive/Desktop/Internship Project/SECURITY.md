# SECURITY.md

## 1. SQL Injection
- Attack: Malicious SQL queries in input fields
- Impact: Unauthorized database access or data loss
- Mitigation: Use parameterized queries and validation

## 2. Cross-Site Scripting (XSS)
- Attack: Injecting scripts into input fields
- Impact: Stealing user data or session hijacking
- Mitigation: Input sanitisation and escaping output

## 3. Prompt Injection
- Attack: Manipulating AI prompts (e.g., "ignore previous instructions")
- Impact: AI produces unsafe or incorrect output
- Mitigation: Detect and block suspicious patterns

## 4. Rate Limiting Abuse (DoS)
- Attack: Sending too many requests
- Impact: Server overload or crash
- Mitigation: Limit requests using flask-limiter

## 5. Unauthorized Access
- Attack: Accessing APIs without authentication
- Impact: Data exposure or system misuse
- Mitigation: JWT authentication and role-based access control