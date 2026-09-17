---
source: https://qlik.dev/manage/automate/create-user-with-fetch/
last_updated: 2026-01-19T14:21:00Z
---

# Create a user on the tenant using Fetch API

You can use Fetch API to create users on Qlik Cloud tenants with a
[machine-to-machine (M2M) OAuth client](https://qlik.dev/authenticate/oauth/create/create-oauth-client).

First, make a request to the `oauth/token` endpoint to obtain an access
token. Make sure the M2M client you created is authorized for `admin_classic` or
`admin.users` scopes, so that the access token has the correct access to create
a user.

```javascript
async function getAccessToken() {
  const options = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Accept": "application/json",
    }
    clientId: "<OAUTH_M2M_CLIENT_ID>",
    clientSecret: "<OAUTH_M2M_CLIENT_SECRET>",
    grant_type: "client_credentials",
    scope: "admin.users",
  }

  const response = await fetch("https://<tenant>.<region>.qlikcloud.com/oauth/token", options);
  if(response?.ok){
    const tokenInfo = await response.json();
    return tokenInfo.access_token;
  }

  console.log("Handle the error");
  return null;
}
```

Now, use the access token to create the user. If you want to create an active user
on the tenant, the body of the request to the `users` endpoint must include the
`subject` and `status` properties, with `status` set to *active*. It's good practice
to include the `name` and `email` properties in the request body.

```javascript
const accessToken = await getAccessToken();

const data = {
  subject: "<UNIQUE_NONIDENTIFIABLE_STRING_REPRESENTING_USER>",
  name: "<USER_DISPLAY_NAME>",
  email: "<USER_EMAIL_ADDRESS>",
  status: "active",
};

const options = {
  method: "POST",
  headers: {
    "Content-Type": "application/javascript",
    "Authorization": `Bearer ${accessToken}`
  },
  body: JSON.stringify(data)
}

const response = await fetch("https://<tenant>.<region>.qlikcloud.com/api/v1/users", options);
if(response?.ok) {
  const data = await response.json();
  return data;
}

console.log("Handle the error");
return null;
```

Here's an example of the response:

```json
{
  "id": "TiQ8GPVr8qI714Lp5ChAAFFaU24MJy69",
  "name": "Harold Frompus",
  "email": "harry@example.com",
  "links": {
    "self": {
      "href": "http://<tenant>.<region>.qlikcloud.com/api/v1/users/DKNmFJCNo8SGURUdh2ll--------USER"
    }
  },
}
```

Review the [Create user](https://qlik.dev/apis/rest/users/#post-v1-users) endpoint for further
information about the Users API.
