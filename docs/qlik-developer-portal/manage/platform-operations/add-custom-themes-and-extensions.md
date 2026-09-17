---
source: https://qlik.dev/manage/platform-operations/add-custom-themes-and-extensions/
last_updated: 2025-07-08T16:09:30Z
---

# Add custom themes and extensions to a tenant

## Add custom themes and extensions to a tenant

Qlik Sense applications have several extensible capabilities available that you can
use to customize the end user experience. Themes and visualization extensions
allow creators to customize the styling and provide custom visualizations that
work natively with Qlik Sense applications.

To use these themes and extensions on a tenant, you can upload
a zip file containing a manifest and the contents of the theme / extension to
the tenant.

In this tutorial, you will learn how to export these assets from a source tenant
and deploy them to a target tenant.

For more information about creating themes, see [Custom themes](https://qlik.dev/extend/create-custom-themes)

## Prerequisites

- You have reviewed previous tutorials in the [Platform Operations series](https://qlik.dev/manage/platform-operations/overview),
  as this tutorial assumes your knowledge of concepts and steps covered earlier.
- zip files containing a theme or extension to upload to the source
  tenant. Examples assets are available ([https://github.com/qlik-oss/qlik-cloud-examples/tree/main/qlik.dev/tutorials/platform-operations/deployment-assets](https://github.com/qlik-oss/qlik-cloud-examples/tree/main/qlik.dev/tutorials/platform-operations/deployment-assets)).
- cURL for running the inline examples.

## Variable substitution

Throughout this tutorial, variables will be used to communicate value placement.
The variable substitution format is `<VARIABLE_NAME>`. Here is a list of
commonly referred to variables.

| Variable                | Description                                                                                                                                                                                                           |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<SOURCE_TENANT>`       | The URL for the tenant that you are exporting assets from. Equivalent to `tenant.region.qlikcloud.com`.                                                                                                               |
| `<SOURCE_ACCESS_TOKEN>` | A bearer token for authorizing `https` requests to the `<SOURCE_TENANT>`. See the [Create a tenant tutorial](https://qlik.dev/manage/platform-operations/create-a-tenant) for guidance on how to generate this token. |
| `<TARGET_TENANT>`       | The URL for the tenant that you are importing assets to. Equivalent to `tenant.region.qlikcloud.com`.                                                                                                                 |
| `<TARGET_ACCESS_TOKEN>` | A bearer token for authorizing `https` requests to the `<TARGET_TENANT>`. See the [Create a tenant tutorial](https://qlik.dev/manage/platform-operations/create-a-tenant) for guidance on how to generate this token. |
| `<THEME_ID>`            | The ID of the theme on the `<SOURCE_TENANT>`.                                                                                                                                                                         |
| `<EXTENSION_ID>`        | The ID of the extension on the `<SOURCE_TENANT>`.                                                                                                                                                                     |
| `<CSP_ID>`              | The ID of the content security policy template on the `<SOURCE_TENANT>`, if required for an extension.                                                                                                                |

## 1: Upload a theme

Themes can be exported and imported to a tenant using the [Themes API](https://qlik.dev/apis/rest/themes).
If your theme exists on the source tenant, you can export it using:

```bash
curl -L -X GET "https://<SOURCE_TENANT>/api/v1/themes/<THEME_ID>/file" ^
-H "Authorization: Bearer <SOURCE_ACCESS_TOKEN>"
```

An archive (.zip) of the theme is sent in the response body, which you can then import
into the target tenant.

```bash
curl -X POST "https://<SOURCE_TENANT>/api/v1/themes" ^
-H "Authorization: Bearer <TARGET_ACCESS_TOKEN>" ^
-H "Content-Type: multipart/form-data" ^
-F "file=@\"<PATH_TO_ZIP_FILE>\""
```

The JSON object response from the API will return metadata describing the
theme on the tenant.

```json
{
    "id": "N6-6O32350hidIaxsq8sbCKSUZCOVuUN",
    "tenantId": "BL4tTJ4S7xrHTcq0zQxQrJ5qB1_Q6cSo",
    "userId": "637390ec6541614d3a88d6c1",
    "name": "My custom theme",
    "type": "theme",
    "qextFilename": "my-custom-theme",
    "qextVersion": "1.0.0",
    "description": "My first...",
    "version": "1.0.0",
    "author": "Qlik",
    "tags": [],
    "file": {
        "contentType": "application/zip",
        "contentLength": 657,
        "md5": "97fbc3e0770153c089b825a09d007a6b",
        "fileId": "L5UnSi2ThqrlS_Lj51YlQEhE1lwG6IEs",
        "originalname": "my-custom-theme.zip"
    },
    "createdAt": "2022-12-20T12:38:23.528Z",
    "updatedAt": "2022-12-20T12:38:23.528Z"
}
```

## 2: Upload an extension

> **Note:** Visualization extensions you upload to a tenant may have resources like images or code hosted externally.
> If your extension requires a content security policy directive, follow the directions in the [next section](#3-configure-content-security-policy-csp).

Extensions can be exported and imported to a tenant using the [Extensions API](https://qlik.dev/apis/rest/extensions).
If your extension exists on the source tenant, you can export it using:

```bash
curl -L -X GET "https://<SOURCE_TENANT>/api/v1/extensions/<EXTENSION_ID>/file" ^
-H "Authorization: Bearer <SOURCE_ACCESS_TOKEN>"
```

An archive (.zip) of the extension is sent in the response body, which you can then
import into the target tenant.

```bash
curl -X POST "https://<TARGET_TENANT>/api/v1/extensions" ^
-H "Authorization: Bearer <TARGET_ACCESS_TOKEN>" ^
-H "Content-Type: multipart/form-data" ^
-F "file=@\"<PATH_TO_ZIP_FILE>\""
```

The JSON object response from the API will return metadata describing the
extension on the tenant.

```json
{
  "id": "-N5F29rjbeGdXmTbj3CnZGiSkojZHl20",
  "tenantId": "BL4tTJ4S7xrHTcq0zQxQrJ5qB1_Q6cSo",
  "userId": "637390ec6541614d3a88d6c1",
  "name": "hello",
  "type": "visualization",
  "qextFilename": "hello",
  "qextVersion": "0.1.0",
  "loadpath": "hello",
  "description": "",
  "version": "1.0.0",
  "icon": "extension",
  "tags": [],
  "preview": "",
  "bundled": false,
  "supernova": true,
  "file": {
      "contentType": "application/zip",
      "contentLength": 1442,
      "md5": "fca23ff8bbb6c71c18a9d94e0c0f231a",
      "fileId": "cYuCMk1z9DULFaOcquCH9bnjKAZPPD14",
      "originalname": "hello-ext.zip"
  },
  "createdAt": "2022-12-20T17:41:20.518Z",
  "updatedAt": "2022-12-20T17:41:20.518Z"
}
```

## 3: Configure content security policy (CSP)

> **Note:** Configuration of a CSP is only required if your extension utilizes external
> (not bundled in the extension archive) assets.

Qlik Cloud uses content security policy directives to allow content from
external sources to work in end user browsers. Check with your extension provider
to confirm if there are external references in the extension code requiring a
CSP directive. For more information, see
[Managing Content Security Policy](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-content-security-policy.htm)
on Qlik Help.

Adding a custom security policy directive is possible using
the [CSP origins API](https://qlik.dev/apis/rest/csp-origins/#post-api-v1-csp-origins).
In the payload of the request, you can specify any number of directives to
support for an identified origin. However, you may apply only one domain origin
to a CSP entry. This request will allow images, scripts, and CSS files from the
origin domain to render in the browser.

If you already have an existing CSP definition on your source tenant, you can
return the configuration:

```bash
curl -L -X GET "https://<SOURCE_TENANT>/api/v1/csp-origins/<CSP_ID>" ^
-H "Authorization: Bearer <SOURCE_ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json"
```

To then create a new CSP on a target tenant using the definition returned from
the source tenant:

```bash
curl -X POST "https://<TARGET_TENANT>/api/v1/csp-origins" ^
-H "Authorization: Bearer <TARGET_ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-d "{ 
    \"origin\": \"<CONTENT_DOMAIN>\", 
    \"name\": \"<CSP_CONFIG_NAME>\", 
    \"description\": \"<DESCRIPTION>\", 
    \"imgSrc\": true, 
    \"scriptSrc\": true, 
    \"styleSrc\": true 
}"
```

The JSON object response shows the same information as the request with an `id`
and dates for creation and modification.

```json
{
  "id": "<CSP_ENTRY_ID>",
  "origin": "<CONTENT_DOMAIN>",
  "name": "<CSP_CONFIG_NAME>",
  "description": "<DESCRIPTION>",
  "imgSrc": true,
  "scriptSrc": true,
  "styleSrc": true,
  "createdDate": "2022-07-01T17:20:31.641Z",
  "modifiedDate": "2022-07-01T17:20:31.641Z"
}
```

## Next steps

Now that you have themes and extensions on your tenant, you
can [apply branding to your tenant](https://qlik.dev/manage/platform-operations/brand-a-tenant).
