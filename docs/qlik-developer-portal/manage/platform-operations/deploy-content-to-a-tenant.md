---
source: https://qlik.dev/manage/platform-operations/deploy-content-to-a-tenant/
last_updated: 2025-07-08T16:09:30Z
---

# Deploy a Qlik Sense application to a tenant

## Deploy a Qlik Sense application to a tenant

In this tutorial, you are going to learn how to deploy a Qlik Sense application
to a target tenant by exporting the application from a source tenant, and
importing it to the target tenant. This guide is part
of the Platform Operations path for creating and configuring target tenants to
support embedded analytics in host applications like other SaaS software or
enterprise applications.

## Code examples

Complete script examples for deploying Qlik content using qlik-cli, curl,
Python, and API collections are available
in the [Qlik Cloud Examples GitHub repository](https://github.com/qlik-oss/qlik-cloud-examples/tree/main/qlik.dev/tutorials/platform-operations).

## Prerequisites

- You have reviewed previous tutorials in
  the [Platform Operations series](https://qlik.dev/manage/platform-operations/overview),
  as this tutorial assumes your knowledge of concepts and steps covered earlier.
- You have the `id` of an app on your source tenant that you want to deploy to
  your target tenant. This should be located in a personal or shared space, not
  a managed space.
- You have a basic understanding of Qlik Cloud and its access control rules for
  creating content and managing spaces.
- You have a basic understanding of Qlik Sense applications and their
  composition on local file storage.
- cURL for running the inline examples.

> **Note:** The cURL examples in this tutorial show the command syntax for Windows Command Prompt.
> If you are using another command line interface, different syntax may be required for line continuation.
> You may also need to adjust the number and type of quotes surrounding the parameters and their values.

## Variable substitution

Throughout this tutorial, variables will be used to communicate value placement.
The variable substitution format is `<VARIABLE_NAME>`. Here is a list of
variables referred to in this tutorial.

| Variable                | Description                                                                                                                                                                            |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<SOURCE_TENANT>`       | The domain for the initial tenant created during account onboarding. Equivalent to `tenanthostname.<REGION>.qlikcloud.com`.                                                            |
| `<TARGET_TENANT>`       | The domain for the new tenant that this tutorial will create. Equivalent to `tenanthostname.<REGION>.qlikcloud.com`.                                                                   |
| `<REGION>`              | The region identifier for the Qlik Cloud region that you're sending requests to. Examples include `ap` for Australia, `eu` for Ireland, `sg` for Singapore and `us` for North America. |
| `<CLIENT_ID>`           | The client ID for an OAuth client, specific to the region you're sending requests to.                                                                                                  |
| `<CLIENT_SECRET>`       | The client secret for the specific OAuth `<CLIENT_ID>`.                                                                                                                                |
| `<SOURCE_ACCESS_TOKEN>` | A bearer token for authorizing `https` requests to the `<SOURCE_TENANT>`.                                                                                                              |
| `<TARGET_ACCESS_TOKEN>` | A bearer token for authorizing `https` requests to the `<TARGET_TENANT>`.                                                                                                              |
| `<APP_NAME>`            | The name of the app that you're deploying from the source to target tenant.                                                                                                            |
| `<SOURCE_APP_ID>`       | The Qlik Cloud `id` for the app `<APP_NAME>` in a shared space on the `<SOURCE_TENANT>`.                                                                                               |
| `<STAGED_APP_ID>`       | The Qlik Cloud `id` for the app `<APP_NAME>` in the shared space on the `<TARGET_TENANT>`.                                                                                             |
| `<PUBLISHED_APP_ID>`    | The Qlik Cloud `id` for the app `<APP_NAME>` in the managed space on the `<TARGET_TENANT>`.                                                                                            |
| `<SHARED_SPACE_ID>`     | The Qlik Cloud `id` for the shared space on the `<TARGET_TENANT>`.                                                                                                                     |
| `<MANAGED_SPACE_ID>`    | The Qlik Cloud `id` for the managed space on the `<TARGET_TENANT>`.                                                                                                                    |
| `<TEMP_CONTENT_ID>`     | A Qlik Cloud `id` provided by the export endpoint to allow the user to download a copy of the app binary.                                                                              |

## 1 Export a Qlik Sense application from the source tenant

Exporting Qlik Sense applications from a tenant requires:

- The Qlik Sense application `id`.
- The export request.
- Downloading the app when it is ready for export.

### The Qlik Sense application ID

The [Items API](https://qlik.dev/apis/rest/items) returns a list of content on your Qlik Cloud tenant.
As this list includes more than just applications, the
API may return multiple `id` values for some content types.
In this case, you want to look for the `resourceId` attribute, as this identifies
the `app id`, rather than the `id` attribute, which identifies the `item id`.

To find the correct `id`, send a request for information about the application
to the API:

```bash
curl -X GET "https://<SOURCE_TENANT>/api/v1/items?name=<APP_NAME>" ^
-H "Authorization: Bearer <SOURCE_ACCESS_TOKEN>" ^
-H "Accept: application/json" ^
-H "Content-Type: application/json"
```

The result is a JSON object containing any Qlik Sense applications where the name
of the app contains `<APP_NAME>`. The `resourceId` value refers to the `app id`:

```json
{
  "data":[
    {
      "name":"<APP_NAME>",
      "id":"62d94c3eba245043962cc861",
      "resourceId":"<SOURCE_APP_ID>",
      ...
    }
  ]
}
```

Keep a note of `resourceId` for use as `<SOURCE_APP_ID>` in the following commands.

### Export the application

Exporting a Qlik Sense application invokes a backend service that bundles the
domain model, business logic, metadata, and data (optional) into a file so that
it can be downloaded from Qlik Cloud.
The [`/export`](https://qlik.dev/apis/rest/apps#%23%2Fentries%2Fapps%2F-appId%2Fexport-post)
endpoint of the Apps API requires the application's
unique identifier as a path parameter in the URL. Add the `-v` option to
display the response headers, as this is where the file ID will be returned.

> **Note:** Applications can only be exported from personal or shared spaces.
> It is not possible to export an app from a managed space via this method.
> Additionally, although the `bot user` has tenant administrator privileges on the tenant, you must add the `bot user`
> to the space with at least edit access rights before you can export content from that space.

```bash
curl -L -X POST -v "https://<SOURCE_TENANT>/api/v1/apps/<SOURCE_APP_ID>/export" ^
-H "Content-Type: application/octet-stream" ^
-H "Authorization: Bearer <SOURCE_ACCESS_TOKEN>"
```

The result is a list of response headers:

```bash
...
< HTTP/1.1 201 Created
< Date: Mon, 02 May 2022 12:27:43 GMT
< Content-Type: application/json; charset=UTF-8
< Content-Length: 0
< Connection: keep-alive
< Location: /api/v1/temp-contents/<TEMP_CONTENT_ID>
< Strict-Transport-Security: max-age=15724800; includeSubDomains
< Cache-Control: no-store
< Pragma: no-cache
...
```

From the response, take note of the `Location` header, this is where the
exported app will be made available for download.

> **Note:** Refer to the `export_app()` function in [tenant\_deploy\_content.sh](https://github.com/qlik-oss/qlik-cloud-examples/blob/main/qlik.dev/tutorials/platform-operations/curl-bash/tenant_deploy_content.sh)
> script for an example of how to extract the `Location` header and use it to build the URL to download the exported
> app.

The next step is to send a GET request to the `Temporary Contents` service with
the file `<TEMP_CONTENT_ID>` appended to the URL. If your app name contains only
filesystem-friendly characters, then you can use this to name the downloaded file.

```bash
curl -L --output "<APP_NAME>.qvf" ^
 -X GET "https://<SOURCE_TENANT>/api/v1/temp-contents/<TEMP_CONTENT_ID>" ^
 -H "Authorization: Bearer <SOURCE_ACCESS_TOKEN>" ^
 -H "Content-Type: application/octet-stream"
```

The result is a list of file download stats:

```bash
%    Total %    Received % Xferd  Average Speed    Time    Time     Time    Current
                                  Dload   Upload   Total   Spent    Left    Speed
100  224k  100  224k     0    0   371k      0 --:--:--  --:--:--  --:--:--   372k

```

The response indicates that the application was downloaded to the folder
specified in the request.

## 2 Deploy the application to the shared space

You can now deploy your application to the shared space in your target tenant.
Once it's there, you can publish it to your managed space. You will need the
`<SHARED_SPACE_ID>` that you received when you created it.
For more information, see [Create the shared space](https://qlik.dev/manage/platform-operations/configure-a-tenant#create-the-shared-space).

Here's a curl example that shows you how to deploy the application. The `<SHARED_SPACE_ID>`
is included as a query parameter with the command. Autoreplace of apps in shared
spaces is not supported, so each run will create a new copy of the application.
For more information, see the [App import endpoint description](https://qlik.dev/apis/rest/apps/#post-api-v1-apps-import).

```bash
curl -L -X POST "https://<TARGET_TENANT>/api/v1/apps/import?spaceId=<SHARED_SPACE_ID>" ^
-H "Content-Type: application/octet-stream" ^
-H "Authorization: Bearer <TARGET_ACCESS_TOKEN>" ^
--data-binary "@<APP_NAME>.qvf"
```

The result is a JSON object showing the space attributes, and application
privileges and permissions for the user:

```json
{
  "attributes": {
    "id": "<STAGED_APP_ID>",
    "name": "<APP_NAME>",
    "description": "",
    "thumbnail": "",
    "lastReloadTime": "2022-03-31T12:58:33.479Z",
    "createdDate": "2022-04-29T15:48:12.294Z",
    "modifiedDate": "2022-04-29T15:48:13.216Z",
    "owner": "qlikbot\\00cbb22c600e823ed278d5e3d976f85a",
    "ownerId": "kqJvzqkdKhBfWc6aoSe_vQmHkcvipDkV",
    "dynamicColor": "",
    "published": false,
    "publishTime": "",
    "custom": {},
    "hasSectionAccess": false,
    "encrypted": true,
    "originAppId": "",
    "isDirectQueryMode": false,
    "spaceId": "<SHARED_SPACE_ID>",
    "_resourcetype": "app"
  },
  "privileges": [
    "read",
    "update",
    "delete",
    "reload",
    "export",
    "duplicate",
    "change_owner",
    "change_space",
    "export_reduced",
    "source"
  ],
  "create": [
    {
      "resource": "sheet",
      "canCreate": true
    },
    {
      "resource": "bookmark",
      "canCreate": true
    },
    {
      "resource": "snapshot",
      "canCreate": true
    },
    {
      "resource": "story",
      "canCreate": true
    },
    {
      "resource": "dimension",
      "canCreate": true
    },
    {
      "resource": "measure",
      "canCreate": true
    },
    {
      "resource": "masterobject",
      "canCreate": true
    },
    {
      "resource": "variable",
      "canCreate": true
    }
  ]
}
```

Note that the name of the app returned in `<APP_NAME>` will match the name of
the app from the source tenant. Keep a record of the app `id` as `<STAGED_APP_ID>`
as you may need this later for republishing the app.

## 3 Publish the application to the managed space

The next step is to publish your application from the shared space to the
managed space so that your end users can access it. You will need the
`<MANAGED_SPACE_ID>` that you received when you created the managed space.
See [Create the managed space](https://qlik.dev/manage/platform-operations/configure-a-tenant#create-the-managed-space) for details.

The commands for the initial publish and any subsequent republishes of the
application are different. The desired outcome when pushing updated versions of
the app into the managed space is usually for the currently published copy to be
replaced by the new version - this has several benefits including:

- The app `id` and URL doesn't change, removing complexity with any embedding or
  integrations you've deployed
- The app maintains any end-user created content such as bookmarks, sheets,
  stories, etc
- There is no need to handle deletes of old or redundant content

This means that your application must verify whether an existing application
exists prior to the publish action, and adjust the publish command accordingly.

### Verify whether an application has been previously published

The method that you use for checking whether a published version of an app
already exists in the managed space on the target tenant depends on your
development workflow. If you change the `id` of your source app during the
process, then you should use the application name approach, but if you change
your application name during development then you should use the application ID
approach.

If you are following this tutorial and using the examples as they are written,
then either approach can be used.

Once you've determined whether the application already exists in the managed
space, you can proceed
to either [Publishing a new application to a managed space](#publishing-a-new-application-to-a-managed-space),
or [Republishing an application to a managed space](#republishing-an-application-to-a-managed-space).

#### Application name approach

If you keep the `<APP_NAME>` the same
throughout the deployment (for example, it remains the same in the source
tenant, and in the shared and managed space in the target tenant) then you can
do a search on the `<APP_NAME>` via
the [Items API](https://qlik.dev/apis/rest/items/#%23%2Fentries%2Fv1%2Fitems-get):

```bash
curl -L -X GET "https://<TARGET_TENANT>/api/v1/items?resourceType=app&spaceId=<MANAGED_SPACE_ID>&name=<APP_NAME>" ^
-H "Authorization: Bearer <TARGET_ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json"
```

The JSON response will return any matching apps, which in most deployment
patterns will return just the app you are searching for, or no apps if the app
doesn't exist:

```json
{
  "data": [
      {
        "name": "<APP_NAME>",
        "spaceId": "<MANAGED_SPACE_ID>",
        "resourceType": "app",
        "resourceId": "<PUBLISHED_APP_ID>",
        "id": "62d94c3eba245043962cc861",
        "resourceAttributes": {
          "_resourcetype": "app",
          "originAppId": "<STAGED_APP_ID>",
          ...
        }
      }
  ]
}
```

However, if you change the name of the app between deployment steps, or have
multiple apps with similar names in each space, then you will need to use a
different approach, using the metadata stored on the published app in the
managed space.

#### Application ID approach

When the application name doesn't remain constant during the deployment process,
you can look at the `originAppId` of any apps present in the managed space via
the [Items API](https://qlik.dev/apis/rest/items/#%23%2Fentries%2Fv1%2Fitems-get).
You will need to create logic to search the response for any apps where the
`originAppId` matches the `resourceId` of the app that you imported to the
shared space in step 2 (referred to in the tutorial as `<STAGED_APP_ID>`).
A working sample of this logic can be found in the
`publish_app` method in the [platform operations example](https://github.com/qlik-oss/qlik-cloud-examples/blob/68ccf2adee994425b48c8bb548b790e0d07ebf0a/qlik.dev/tutorials/platform-operations/sdk-python/tenant_deploy_content.py#L93).

In this example, you do not specify an `<APP_NAME>` value, which results in all
apps in the space being returned:

```bash
curl -L -X GET"https://<TARGET_TENANT>/api/v1/items?resourceType=app&spaceId=<MANAGED_SPACE_ID>" ^
-H "Authorization: Bearer <TARGET_ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json"
```

The JSON response will return any apps found in the managed space:

```json
{
  "data": [
    {
      "name": "<APP_NAME>",
      "spaceId": "<MANAGED_SPACE_ID>",
      "resourceType": "app",
      "resourceId": "<PUBLISHED_APP_ID>",
      "id": "62d94c3eba245043962cc861",
      "resourceAttributes": {
        "_resourcetype": "app",
        "originAppId": "<STAGED_APP_ID>",
        ...
      }
    }
  ]
}
```

### Publishing a new application to a managed space

For the first publish of the app, you will set several key attributes and land
the app in the managed space.

> **Note:** There can be timing issues when creating a space and then immediately trying to publish to it.
> You may have to implement your own sleep statements and retries, an example with a one second delay can be found in
> the platform-operations example during [the verify step](https://github.com/qlik-oss/qlik-cloud-examples/blob/59ea35fb02a05db13fad757a5e0d048dc4782772/qlik.dev/tutorials/platform-operations/sdk-python/tenant_deploy_content.py).

```bash
curl -L -X POST "https://<TARGET_TENANT>/api/v1/apps/<STAGED_APP_ID>/publish" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json" ^
-H "Authorization: Bearer <TARGET_ACCESS_TOKEN>" ^
-d "{\"spaceId\":\"<MANAGED_SPACE_ID>\", \"attributes\": {\"name\":\"<APP_NAME>\", \"description\":\"\"}}"
```

The result is a JSON object showing the application attributes, and application
privileges and permissions for the user:

```json
{
  "attributes": {
    "id": "<PUBLISHED_APP_ID>",
    "name": "<APP_NAME>",
    "description": "",
    "thumbnail": "",
    "lastReloadTime": "2020-01-07T13:48:25.755Z",
    "createdDate": "2022-04-29T17:49:23.637Z",
    "modifiedDate": "2022-04-29T17:49:25.387Z",
    "owner": "qlikbot\\00cbb22c600e823ed278d5e3d976f85a",
    "ownerId": "kqJvzqkdKhBfWc6aoSe_vQmHkcvipDkV",
    "dynamicColor": "",
    "published": false,
    "publishTime": "2022-04-29T17:49:23.633Z",
    "custom": {},
    "hasSectionAccess": false,
    "encrypted": true,
    "originAppId": "<STAGED_APP_ID>",
    "isDirectQueryMode": false,
    "spaceId": "<MANAGED_SPACE_ID>",
    "_resourcetype": "app"
  },
  "privileges": [
    "read",
    "update",
    "delete",
    "reload",
    "export",
    "exportdata",
    "publish",
    "duplicate",
    "change_owner",
    "change_space",
    "export_reduced",
    "source"
  ],
  "create": [
    {
      "resource": "sheet",
      "canCreate": true
    },
    {
      "resource": "bookmark",
      "canCreate": true
    },
    {
      "resource": "snapshot",
      "canCreate": true
    },
    {
      "resource": "story",
      "canCreate": true
    },
    {
      "resource": "dimension",
      "canCreate": true
    },
    {
      "resource": "measure",
      "canCreate": true
    },
    {
      "resource": "masterobject",
      "canCreate": true
    },
    {
      "resource": "variable",
      "canCreate": true
    },
    {
      "resource": "folderconnection",
      "canCreate": true
    },
    {
      "resource": "internetconnection",
      "canCreate": true
    }
  ]
}
```

The response indicates that the application has been successfully published
to the managed space in the target tenant. Keep a note of the app `id` for the
published app as `<PUBLISHED_APP_ID>` as this will make republishing easier.

### Republishing an application to a managed space

For updates of an application that's already published to a managed space,
you will use a `PUT` request rather than a `POST` request, providing the
`<PUBLISHED_APP_ID>` of the existing published app and a `checkOriginAppId` value of
`false`, which skips validation that the source app is the same as when the app
was originally published.

Although the `checkOriginAppId` validation is important when making updates
through the user interface, removing it allows you to leverage a wider variety
of development workflows which don't require maintaining the same application
`id` in the shared space. Changes to the application `id` commonly happen when
you leverage third party repositories and version control solutions during your
development process.

```bash
curl -L -X PUT "https://<TARGET_TENANT>/api/v1/apps/<STAGED_APP_ID>/publish" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json" ^
-H "Authorization: Bearer <TARGET_ACCESS_TOKEN>" ^
-d "{\"targetId\": \"<PUBLISHED_APP_ID>\",\"checkOriginAppId\": false}"
```

The result is a JSON object showing the application attributes, and application
privileges and permissions for the user:

```json
{
  "attributes":
  {
    "id": "<PUBLISHED_APP_ID>",
    "name": "<APP_NAME>",
    "description": "",
    "thumbnail": "",
    "lastReloadTime": "2020-01-07T13:48:25.755Z",
    "createdDate": "2022-04-29T17:49:23.637Z",
    "modifiedDate": "2022-04-29T17:49:25.387Z",
    "owner": "qlikbot\\00cbb22c600e823ed278d5e3d976f85a",
    "ownerId": "kqJvzqkdKhBfWc6aoSe_vQmHkcvipDkV",
    "dynamicColor": "",
    "published": false,
    "publishTime": "2022-07-22T19:08:54.886Z",
    "custom": {},
    "hasSectionAccess": false,
    "encrypted": true,
    "originAppId": "<STAGED_APP_ID>",
    "isDirectQueryMode": false,
    "spaceId": "<MANAGED_SPACE_ID>",
    "_resourcetype": "app"
  },
  ...
}
```

The response indicates that the application has been successfully republished
to the managed space in the target tenant.

## Next steps

Now that you have a Qlik Sense app on your tenant, you
can [add custom themes
and extensions](https://qlik.dev/manage/platform-operations/add-custom-themes-and-extensions).
