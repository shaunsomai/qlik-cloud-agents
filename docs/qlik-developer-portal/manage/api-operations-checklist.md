---
source: https://qlik.dev/manage/api-operations-checklist/
last_updated: 2026-04-20T13:34:03+01:00
---

# API operations checklist

Before you start creating, updating, or deleting resources through APIs, verify these basics in a test flow.

## Prerequisites

- Familiarity with REST APIs and HTTP methods (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`)
- Understanding of [Key concepts](https://qlik.dev/manage/key-concepts) including tenant, space, and data connection fundamentals
- An access token with appropriate permissions for the operations you plan to perform

## API operations best practices

Follow this checklist for safe and reliable automation:

1. **Use a non-production space or tenant for initial validation.**\
   Start with test environments before deploying to production. This lets you verify API
   behavior, error handling, and rollback procedures without risk.

2. **Start with `GET` calls to confirm visibility and identifiers.**\
   Before any `POST`, `PUT`, `PATCH`, or `DELETE` requests, retrieve the IDs of resources
   you plan to modify. This confirms your credentials work and you have the permissions needed.

3. **Confirm your token type and permissions are correct for the action.**\
   Different token types (OAuth SPA, OAuth M2M, API key) have different scopes and lifetimes.
   Verify your token has the required permissions before building automation.

4. **Validate your dependency chain.**\
   Map out the sequence of API calls your script needs. For example: space → data connection
   → app reload → data file. Test each step independently before combining them.

5. **Add retry and pagination handling to scripts.**\
   Use exponential backoff for retries and handle `429` (rate limit) responses. For endpoints
   that return lists, implement pagination to handle large result sets.

6. **Test rollback behavior for critical operations.**\
   Before automating operations like disabling features or reassigning ownership, verify you
   can undo them. Document the rollback steps in your automation.

## Related documentation

For more details on how Manage APIs work, see:

- [REST API fundamentals](https://qlik.dev/apis/rest/)
- [Pagination and filtering](https://qlik.dev/apis/rest/pagination-sorting-filtering)
- [Rate limiting](https://qlik.dev/apis/rest/rate-limiting/)
- [Key concepts](https://qlik.dev/manage/key-concepts)
