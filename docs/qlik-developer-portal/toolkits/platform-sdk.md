---
source: https://qlik.dev/toolkits/platform-sdk/
last_updated: 2026-05-27T15:46:17+02:00
---

# Python Platform SDK overview

> **Upcoming deprecation notice:** The Qlik Python Platform SDK is currently in public preview and is planned for deprecation.
> Do not use this SDK for new projects or long-term integrations.
>
> Existing integrations can continue using the SDK.
> A replacement is under development.
>
> Until replacement guidance becomes available, use Qlik APIs directly for new Python developments.

The Qlik Platform SDK is a software development kit available in Python that provide easy to use
interfaces to Qlik Cloud APIs for managing tenants and building data analytics
applications.

With the Platform SDK, you can:

- Access the backend services of your tenants to automate tedious and repetitive
  tasks.
- Build web applications on top of Qlik for managing jobs to be done across
  your analytics landscape.
- Connect to Qlik Sense analytics applications and access data for use in
  embedded applications and machine learning models.
- Create and explore analytics applications programmatically using Qlik's
  unique calculation engine to solve data intensive business problems.

## Get started

> **Warning:** Existing integrations can continue using the SDK during the transition period.
> Do not start new projects with this SDK.

### Prerequisites

- A Qlik Cloud tenant
- [Python](https://www.python.org/downloads/) 3.8 or greater
- Latest version of the [Python SDK](https://pypi.org/project/qlik-sdk/)

### Installation

To install the Python Platform SDK, just use `pip`.

```bash
python3 -m pip install --upgrade qlik-sdk
```

## Authentication

The Platform SDK supports multiple methods for authenticating to Qlik Cloud.

### Using an API Key

An API key is a token representing a user in your tenant. With an API key, a
user can interact with the platform programmatically with the same access
privileges and context they have during interactive sessions through a web
browser. [Follow this guide](https://qlik.dev/authenticate/api-key/generate-your-first-api-key)
to obtain an API key for your tenant.

Once you have an API key, you can connect your backend application to Qlik Cloud
using the Platform SDK to create backend applications.

```python
from qlik_sdk import Auth, AuthType, Config

# Authorization
# Create auth object
config = Config(
    host='<QLIK_TENANT_URL>',
    auth_type=AuthType.APIKey,
    api_key='<API_KEY>',
)

client = Auth(config=config)

# Make REST API call
user_me = client.rest(path='/users/me')
print(user_me.json())
```

### Using Machine-to-Machine OAuth2

OAuth is a standard security protocol for authorization and delegation. It allows third party applications
to access API resources without disclosing the end-user credentials.

For a step-by-step guide on how to create an OAuth client for your tenant,
see [Create an OAuth client](https://qlik.dev/authenticate/oauth/create/create-oauth-client).

```python
from qlik_sdk import Auth, AuthType, Config

# Authorization
# Create auth object
config = Config(
    auth_type=AuthType.OAuth2,
    host='<QLIK_TENANT_URL>',
    client_id='<CLIENT_ID>',
    client_secret='<CLIENT_SECRET>'
)

# Authorisation
client = Auth(config=config)
client.authorize()
```

## Interact with apps

In the following examples, the user only wants to interact with the
`Apps` resource.

```python
from qlik_sdk import Apps, AuthType, Config

apps = Apps(Config(host='<QLIK_TENANT_URL>', auth_type=AuthType.APIKey, api_key='<API_KEY>'))

# app is fetched from the REST /v1/apps/{app_id}
app = apps.get(app_id='<QLIK_APP_ID>')

# opens a websocket connection against the Engine API and gets the app layout
with app.open():
    app_info = app.get_app_layout()
```

## Interceptor

Log requests using interceptors

```python
from qlik_sdk import Apps, AuthType, Config

client = Auth(Config(host='<QLIK_TENANT_URL>', auth_type=AuthType.APIKey, api_key='<API_KEY>'))
user_me = client.rest(path='/users/me')

# request interceptor method
def log_req(req: requests.Request) -> requests.Request:
    print(req)
    return req

# registers an interceptor
client.rpc.interceptors["request"].use(log_req)

app_list = client.rest(path="/items", params={"resourceType":"app", "limit": 100})
```

## Raw calls to backend

```python
import sys
import uuid

from qlik_sdk import Apps, Auth, AuthType, Config

config = Config(
    host='<QLIK_TENANT_URL>', auth_type=AuthType.APIKey, api_key='<API_KEY>'
)

auth = Auth(config)
apps = Apps(config)

session_app_id = "SessionApp_" + str(uuid.uuid1())
session_app = apps.create_session_app(session_app_id)
with session_app.open():
    # create a generic object of a custom type
    properties = {
        "qInfo": {"qType": "custom-object"},
    }

    obj = session_app.create_session_object(properties)

    # set a custom property i.e. a property not defined in GenericObjectProperties
    properties["CustomProperty"] = "custom-property-value"
    obj.set_properties(properties)

    # fetch the properties and validate that the custom property is returned
    new_props = obj.get_properties()
    if new_props.qInfo.qType != "custom-object":
        sys.exit(1)
    if new_props.CustomProperty != "custom-property-value":
        sys.exit(1)

```
