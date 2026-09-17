---
source: https://qlik.dev/apis/rest/
last_updated: 2026-04-20T13:34:03+01:00
---

# REST APIs

Qlik offers a set of REST APIs to observe and manage a Qlik Cloud tenant. Most of these APIs are
service-oriented and provide a way of configuring most capabilities in a tenant, enabling
programmatic deployments, CI/CD, monitoring, and more.

For access to data in Qlik Sense apps, refer to the [QIX API](https://qlik.dev/apis/json-rpc/).

> **Namespaced APIs:** Namespaced APIs are being introduced to support the growing number of APIs and services in the platform, and to unlock
> versioning support in the future.
>
> This change makes it easier for you to find, understand, and use Qlik APIs by grouping related resources by context and
> standardizing interfaces.
>
> For more information, see [API namespaces](https://qlik.dev/apis/namespaces/) and the [changelog](https://qlik.dev/changelog/).

## What are REST APIs?

REST (Representational State Transfer) is an architectural style for designing networked applications.
Qlik REST APIs use a request-response model where a client sends a request to a service, and the service responds with
the requested resource.

## Direct REST or framework interface?

Direct REST calls and Qlik frameworks access the same underlying platform capabilities.

- Use **direct REST** when you want low-level HTTP control.
- Use `@qlik/api` when you want typed calls and built-in conveniences such as auth helpers, automatic CSRF handling,
  and cache-aware request behavior. See [qlik-api overview](https://qlik.dev/toolkits/qlik-api), [authentication](https://qlik.dev/toolkits/qlik-api/authentication/),
  and [features](https://qlik.dev/toolkits/qlik-api/features/).
- Use `qlik-cli` for shell-native scripting and operational automation. See [qlik-cli](https://qlik.dev/toolkits/qlik-cli/).
- Use **Qlik Automate** for no-code orchestration with platform connectors. See [No-code overview](https://qlik.dev/toolkits/no-code/).
- For assistant-driven workflows, **Qlik MCP access** can be used. See [Qlik MCP server](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikMCP/Qlik-MCP-server.htm).

## Tenant APIs vs. organization APIs

Most Qlik Cloud APIs are tenant APIs.
They operate within the context of a single tenant and use a tenant hostname as the base URL:

```http
https://your-tenant.us.qlikcloud.com/api/<namespace>/<resource>
```

If you need to list tenants across regions and subscriptions in your organization,
see [Organization REST APIs](https://qlik.dev/apis/org-rest/).

The following table summarizes the key differences:

| Aspect       | Tenant APIs                                                                         | Organization APIs                             |
| ------------ | ----------------------------------------------------------------------------------- | --------------------------------------------- |
| **Scope**    | A single tenant                                                                     | All tenants in an organization                |
| **Host**     | `<tenant>.region.qlikcloud.com`                                                     | `console.qlikcloud.com`                       |
| **Auth**     | Tenant OAuth client or API key, Organization OAuth client, or Regional OAuth client | Organization OAuth client                     |
| **Use case** | Manage resources within one tenant                                                  | List tenants across regions and subscriptions |

## Authentication

### Supported authentication methods

Tenant REST APIs support different authentication methods:

- OAuth 2.0: the recommended method for most use cases.
- JSON Web Tokens (JWT): used for legacy embedding solutions where a proxy is in use, or third-party
  cookie blocking isn't a concern.
- API keys: a simple way of providing access to APIs with the same permissions of
  the creating user.

For more information about how to authenticate your requests, see the [Authentication Guide](https://qlik.dev/authenticate).

> **Organization APIs authentication:** Organization APIs use OAuth client credentials. You create an OAuth client in the Cloud Console, then
> exchange its credentials for an access token. For details, see [Organization REST APIs](https://qlik.dev/apis/org-rest/).

### CSRF token

When calling Qlik REST APIs in a browser context, you must send a CSRF token with your request. If the CSRF token is
missing or invalid, the API will reject the request.

The CSRF token is used to prevent cross-site request forgery (CSRF) attacks. These attacks happen when a malicious
website tricks your browser into performing actions, like sending a request, on another website where you're
authenticated, without your consent.

To send the CSRF token, include it in your request using the `qlik-csrf-token` header. For example:

```shell
GET /api/v1/<RESOURCE> HTTP/1.1
Host: <TENANT>.<REGION>.qlikcloud.com
Authorization: Bearer <ACCESS_TOKEN>
qlik-csrf-token: <CSRF_TOKEN>
```

You can retrieve the CSRF token using the [CSRF token API](https://qlik.dev/apis/rest/csrf-token/#get-v1-csrf-token).
The response headers will include the CSRF token.

## Resources and requests

Each resource is exposed by a uniform resource identifier (URI). You can send an HTTP request to the relevant URI to
access a resource.

Each request is made up of the following:

- HTTP method
- URI
- Headers
- Request body

### URI structure

The URI is the path to a resource. The URI is different for each resource, but the structure remains the same for all
tenant-level resources:

```http
https://your-tenant.region.qlikcloud.com/api/v1/resource
```

- `your-tenant` is the hostname of your tenant, generated during tenant creation
  (and cannot be changed), or a custom alias name that you can define.
- `region` is the region where your tenant is deployed, for example `eu` or `us`.
- `resource` is the resource you want to access, which could include query or path parameters.

For example, the URI to retrieve the current user info looks like this:

```http
https://mytenant.us.qlikcloud.com/api/v1/users/me
```

### HTTP methods

Qlik REST APIs use the following HTTP methods:

- `GET`: retrieve a resource.
- `POST`: create a new resource.
- `PUT`: update an existing resource.
- `DELETE`: remove a resource.

### Headers

Commonly used headers are:

- `Authorization`: specifies the token used to authorize the request. Example: `Authorization: Bearer <token>`
- `Content-type`: specifies the format of the request body. Example: `Content-Type: application/json`

## Rate limiting

To ensure fair usage, Qlik implements rate limiting on API requests.
Be sure to handle rate limit errors (`HTTP 429`) in your applications.

For more information, see [Rate limiting](https://qlik.dev/apis/rest/rate-limiting/).

## Pagination

Qlik uses cursor-based pagination to split results into subsets called pages.
After retrieving the first subset of results, you can use the returned `links.next` URL in the response to retrieve
the results from the next page.

For more information, see [Pagination](https://qlik.dev/apis/rest/pagination-sorting-filtering).

## API reference documentation

## Next steps

- Follow step-by-step tutorials to manage data files, data connections, tenants, and more: [Manage Qlik Cloud](https://qlik.dev/manage).
- Get credentials and choose an auth method: see the [Authentication Guide](https://qlik.dev/authenticate) and [Authentication: when to use which method](https://qlik.dev/manage/key-concepts#authentication-when-to-use-which-method).
- Explore the [API reference documentation](#api-reference-documentation).
- Learn about [Organization REST APIs](https://qlik.dev/apis/org-rest/) to list tenants across regions and subscriptions.
- Check the [changelog](https://qlik.dev/changelog/tag/api/) for the latest updates.
- Join the [Qlik Community](https://community.qlik.com/) for support and discussions.
