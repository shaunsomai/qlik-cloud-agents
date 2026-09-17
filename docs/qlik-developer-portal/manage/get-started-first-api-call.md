---
source: https://qlik.dev/manage/get-started-first-api-call/
last_updated: 2026-04-20T13:34:03+01:00
---

# Your first API call

This quick start gets you from zero to one successful API call to your Qlik Cloud tenant.

## 1. Get credentials

For recommended auth methods and API key security tradeoffs, see
[Authentication: when to use which method](https://qlik.dev/manage/key-concepts#authentication-when-to-use-which-method).

## 2. Set tenant URL and token

- **Tenant URL**: Your tenant has the form `yourtenant.region.qlikcloud.com`
  (for example, `mycompany.us.qlikcloud.com`). Use this as the base for all API requests.
- **Token**: Set your access token (from OAuth SPA flow or API key) in your environment or in Postman as a Bearer token.

## 3. Call an endpoint

Use `GET /api/v1/users/me` to retrieve the current user. Example with cURL
(replace placeholders):

```bash
curl -L "https://<TENANT>/api/v1/users/me" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json"
```

A successful response returns your user information (for `users/me`). If so,
your API setup is working.

## Next steps

- Explore more endpoints: See the [REST API reference](https://qlik.dev/apis/rest/) to discover all available APIs
- Learn key concepts: Understand [tenants, spaces, and data terms](https://qlik.dev/manage/key-concepts)
- Create resources: Follow how-to guides for [creating data files](https://qlik.dev/manage/data-files/create-datafiles) or
  [setting up data connections](https://qlik.dev/manage/data-connections/create-data-connections)
- Before automating at scale: See the [API operations checklist](https://qlik.dev/manage/api-operations-checklist) for essential
  pre-flight checks and best practices
- Deploy at scale: See [Platform Operations](https://qlik.dev/manage/platform-operations/overview) for multitenancy and deployment
  strategies
