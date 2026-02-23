# Secure Development Practices

This file outlines secure development practices for handling sensitive information such as access tokens, passwords, and API keys in automation and MCP workflows.

---

## Key Principles
- **Never hardcode secrets in code or markdown files.**
- Use environment variables for local development.
- For production, use secret managers (Azure Key Vault, AWS Secrets Manager, HashiCorp Vault, etc.).
- Add `.env` and any secret files to `.gitignore`.
- Rotate credentials regularly.
- Use least-privilege access for all service accounts.
- Review and audit access permissions periodically.

---

## Example: Using Environment Variables in Python

```python
import os
JIRA_SERVER = os.environ['JIRA_SERVER']
JIRA_USER = os.environ['JIRA_USER']
JIRA_API_TOKEN = os.environ['JIRA_API_TOKEN']
```

---

## References
- [OWASP Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices/)
- [12 Factor App: Config](https://12factor.net/config)
- [GitHub: Keeping your secrets safe](https://docs.github.com/en/actions/security-guides/encrypted-secrets)

---

## Checklist
- [ ] No secrets in code or markdown
- [ ] `.env` and secret files in `.gitignore`
- [ ] Use secret managers for production
- [ ] Regularly rotate and audit credentials
