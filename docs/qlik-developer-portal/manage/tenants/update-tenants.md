---
source: https://qlik.dev/manage/tenants/update-tenants/
last_updated: 2026-04-20T13:34:03+01:00
---

# Configure tenant name and alias

In this tutorial, you are going to learn how to change a tenant name and
alias and retrieve tenant details using Qlik Cloud management APIs.

## Prerequisites

- You have a basic understanding of Qlik Cloud and its access control rules for
  creating content and managing spaces.
- cURL for running the inline examples.

> **Note:** The cURL examples in this topic show the command syntax for Windows Command Prompt.
> If you are using another command line interface, different syntax may be required for line continuation.
> You may also need to adjust the number and type of quotes surrounding the parameters and their values.

## Variable substitution

Throughout this tutorial, variables will be used to communicate value placement.
The variable substitution format is `<VARIABLE_NAME>`. Here is a list of
variables referred to in this tutorial.

| Variable         | Description                                                                                                                                   |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `<TENANT>`       | The URL for the tenant where you are managing groups. Equivalent to `tenanthostname.<REGION>.qlikcloud.com`.                                  |
| `<ACCESS_TOKEN>` | A bearer token for authorizing `https` requests to the `<TENANT>`. For more information, see [Authentication](https://qlik.dev/authenticate). |
| `<TENANT_ID>`    | The unique identifier of the tenant.                                                                                                          |
| `<TENANT_NAME>`  | The name or alias of the tenant.                                                                                                              |
| `<TENANT_ALIAS>` | The alternate alias of the tenant.                                                                                                            |

## Retrieve your tenant ID

To make changes to your tenant, you will need to retrieve the ID of the tenant.
To do this, send a GET request to `<TENANT>/api/v1/tenants/me`.

```bash
curl -L "https://<TENANT>/api/v1/tenants/me" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json"
```

This will redirect you to the information for the current tenant via a `302`
redirect, where the value for `id` is the tenant ID.

## Update the tenant name

You can set a tenant name during the deployment process, for example, to
match your company name or your customer's name. This is displayed in various
user interfaces, notifications, and emails sent by the tenant.

Here's a cURL example that shows you how to update the name of the tenant.

```bash
curl -L -X PATCH "https://<TENANT>/api/v1/tenants/<TENANT_ID>" ^
-H "Content-Type: application/json" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-d "[{\"op\":\"replace\",\"path\":\"/name\",\"value\":\"<TENANT_NAME>\"}]"
```

The response from this request is an `HTTP 204` status code. There are no
additional details provided in the response.

## Update the tenant alias

> **Note:** Setting the alias is not possible in most trial and evaluation versions of Qlik Cloud.

To help you remember the URL of a tenant, you can add an alias of your choosing,
in addition to the system-generated hostname. Your new alias must be specified in
this format:`{user-defined name}.{region}.qlikcloud.com`.

Here is an example of an alias that an OEM might use:
`{oemName}-{customerName}.us.qlikcloud.com` (if the OEM is `ACME` and the customer
is `ABC`, then the alias would be `acme-abc.us.qlikcloud.com`).

> **Note:** It is a good practice to use the tenant hostname instead of the alias name.
>
> In general, only use the alias name for user access, and use the hostname for all system integrations/ orchestration

> activities.

The patch is sent to path `/hostnames/1`, which is always used for the
alias. `/hostnames/0` returns
the system-generated hostname, which cannot be changed.

cURL example to set the alias of the tenant:

```bash
curl -L -X PATCH "https://<TENANT>/api/v1/tenants/<TENANT_ID>" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-d "[{\"op\":\"replace\",\"path\":\"/hostnames/1\",\"value\":\"<TENANT_ALIAS>\"}]"
```

The response from this request is an `HTTP 204` status code. There are no
additional details provided in the response.

You will now be able to access the tenant on both it's original hostname, and the
new alias. If you previously had an alias set, this will be released for use
by other Qlik customers.

## Retrieve tenant details

After you have updated the tenant `name` and `alias`, you can verify
that the values have been changed.

cURL example to get tenant information (you can also
use `<TENANT>/api/v1/tenants/me`):

```bash
curl -L "https://<TENANT>/api/v1/tenants/<TENANT_ID>" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json"
```

The result is a JSON object that shows the updated values for `name` and
`hostname`.

```json
{
    "id": "<TENANT_ID>",
    "name": "<TENANT_NAME>",
    "hostnames": [ "<TENANT_HOSTNAME>", "<TENANT_ALIAS>" ],
    "createdByUser": "",
    "datacenter": "us-east-1",
    "created": "2023-06-05T18:02:18.302Z",
    "lastUpdated": "2023-07-04T16:35:50.499Z",
    "status": "active",
    ...
}
```
