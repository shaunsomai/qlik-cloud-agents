# ODAG links

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Create, manage, and retrieve on-demand analytics generation links between selection and template applications.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/analytics/odag-links`](#get-apianalyticsodag-links) | A Link object defines an on-demand data navigation path between a selection Analytics Application and a template Analytics Application including the set of properties that control how that data access occurs and under what conditions access is permitted. The set of links returned by this method have properties that match the combination of conditions defined by any supplied query parameters. |
| `POST` | [`/api/analytics/odag-links`](#post-apianalyticsodag-links) | Creates a new link that enables ODAG navigation from a designated selection Analytics Application to a generated Analytics Application that is created by copying the designated template Analytics Application, injecting values for bind variables harvested from the selection Analytics Application and dynamically loaded with data using those bindings. The Bindings will be initialized by searching the load script of the template Analytics Application for patterns of the form `$(od_FIELDNAME)[M-N]` where `FIELDNAME` is the name of a field in the model of the selection Analytics Application and the optional pattern `[M-N]` identifies the lower bound `M` and the upper bound `N` for the number of values for that field which must be in the active selection state of the selection Analytics Application for binding to occur.  The active selection state defaults to `selected` (i.e. green) unless the `od` prefix is immediately followed by some combination of the letters `s`, `o`, or `x`, in that order, specifically designating the `selected`, `optional` (i.e. white) and/or `excluded` (i.e. gray) groups of values to be harvested from the selection Analytics Application's selection state. The bindings in the `bindings` array in the request payload override the properties of the corresponding field bindings found in the script of the template Analytics Application. |
| `GET` | [`/api/analytics/odag-links/{linkId}`](#get-apianalyticsodag-linkslinkid) | Retrieves details of a specific ODAG link, including bindings, properties, status, and template Analytics Application charts. Use this to review link configuration or verify permissions before generating Analytics Applications. |
| `PUT` | [`/api/analytics/odag-links/{linkId}`](#put-apianalyticsodag-linkslinkid) | Modifies ODAG link configuration including bindings, properties, status, and template Analytics Application reference. You can re-scan the template Analytics Application script to auto-detect binding patterns or override specific settings. If `statusSetting` is provided, the request updates only the link status (other payload fields are not applied). |
| `GET` | [`/api/analytics/odag-links/{linkId}/requests`](#get-apianalyticsodag-linkslinkidrequests) | Retrieves all Analytics Application generation requests for a specific ODAG link, with optional filtering by pending status (`pending`), selection Analytics Application (`selectionAppId`), sheet context (`selectionAppSheet`), or client context (`clientContextHandle`). Use this to track generation history or monitor in-flight requests. |
| `POST` | [`/api/analytics/odag-links/{linkId}/requests`](#post-apianalyticsodag-linkslinkidrequests) | Submits a new Analytics Application generation request with the current selection state from a selection Analytics Application. The request is validated against link properties before queuing.  On success, returns a request object that you must monitor for completion using the status endpoint.  Validation failures return detailed error information. |
| `GET` | [`/api/analytics/odag-links/cancreate`](#get-apianalyticsodag-linkscancreate) | Checks whether the current user has permission to create new ODAG links. Optionally verify permissions for a specific template Analytics Application or selection Analytics Application context. Returns a boolean indicating create permission status. |
| `POST` | [`/api/analytics/odag-links/selection-app-link-usages`](#post-apianalyticsodag-linksselection-app-link-usages) | Registers the current set of ODAG links referenced by a selection Analytics Application and returns only those links the current user can access. Call this when a selection Analytics Application is opened or after modifying its ODAG link references. The response is an array of objects, where the `id` identifies the requested link and `link` contains the link state when accessible. Use `GET /analytics/odag-links/{linkId}` for full details. |

## API Reference

### GET /api/analytics/odag-links

A Link object defines an on-demand data navigation path between a selection Analytics Application and a template Analytics Application including the set of properties that control how that data access occurs and under what conditions access is permitted. The set of links returned by this method have properties that match the combination of conditions defined by any supplied query parameters.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `includeCharts` | boolean | No | Determines whether master charts of the template Analytics Application are included in the response. |
| `selectionAppID` | string | No | Filter the list by the selection Analytics Application ID. |
| `type` | string | No | The type of the links to query. Defaults to `link`. Enum: "link", "view", "all" |
| `optOwner` | string | No | Use `optOwner` to filter results by link owner user ID. If supplied, only links owned by that user are returned. If not supplied, returns all links the current user can access. |

#### Responses

##### 200

ODAG links retrieved successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `name` | string | Yes | The name of a link. |
| `owner` | object | Yes | Condensed state of a user returned in state of ownable ODAG entities (for example, a link or request). |
| `status` | string | Yes | The current status of a link. Enum: "active", "disabled", "decommissioned", "incomplete" |
| `bindings` | object[] | No | A collection of Bindings.  Note that there can be multiple bindings having the same `templateAppFieldName` in a binding collection to denote different usages of the field's selection state in the context of the data prep logic but they all must have the same value for their `range` property. |
| `privileges` | string[] | No |  |
| `properties` | object | Yes | The complete set of possible properties for a link and their associated user context/value pairings. |
| `rowEstExpr` | string | Yes | The measure expression to be evaluated in the context of the selection Analytics Application for the link that estimates the number of records that will be qualified by the primary load query of the template Analytics Application. This expression must be valid in the context of the selection Analytics Application fields and update whenever the selection state of the selection Analytics Application changes. |
| `createdDate` | string | Yes |  |
| `dynamicView` | boolean | No | When `true`, the ODAG link is treated as a dynamic view. |
| `templateApp` | object | Yes | Condensed state of an Analytics Application returned in `state` for Link, LinkUsage, Request, and ODAG Apps GET calls. |
| `modifiedDate` | string | No |  |
| `sourceLinkId` | string | No | The ID of the original link this was copied from. Present only on deep-copied links. |
| `includeScript` | boolean | No | Set to `true` to include the generated Analytics Application load script in the generated Analytics Application. The default value is `false`. |
| `modifiedByUser` | object | No | Condensed state of a user returned in state of ownable ODAG entities (for example, a link or request). |
| `genAppAccessible` | boolean | No | Only returned on `LinkGet` and set to `true` if user will have access to an Analytics Application generated by this link. |
| `templateAppChartObjects` | object[] | No |  |

<details>
<summary>Properties of `owner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The system-assigned ID for a user |
| `name` | string | Yes |  |
| `subject` | string | Yes | Identity subject used for identity mapping. |
| `tenantid` | string | Yes | Tenant identifier. |

</details>

<details>
<summary>Properties of `bindings`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `range` | object | No | The lower and upper bound for the permitted number of values that must exist in the selection Analytics Application's source parameter in order for this binding to be valid (and permit an ODAG Request to be submitted. If this property is not supplied, there is no constraint on either the lower or upper bound. To indicate that an exact number of selections are required, use the same number for both the lower and upper bound. |
| `formatting` | object | No | A property value that describes the formatting of field values in a Binding. This is currently only settable in the template Analytics Application script and not when creating or updating a Link. |
| `numericOnly` | boolean | No | Set to `true` to indicate that only numeric values from the selection Analytics Application source parameter should be used. The default value for this property, if left unspecified, is `false`. This is currently only settable in the template Analytics Application script and not when creating or updating a Link. |
| `selectionStates` | string | No | A combination of the letters `S` and/or `O` to indicate which values from the selection states `selected` or `optional` in the hypercube of the selection Analytics Application to harvest as bind values to inject into the script of the template Analytics Application at ODAG request submission time. This is currently only settable in the template Analytics Application script and not when creating or updating a Link. |
| `selectAppParamName` | string | No | The path (or name) of the selection Analytics Application field, variable, or property to obtain the list of values for this binding. |
| `selectAppParamType` | string | Yes | The different kinds of selection Analytics Application parameters whose values can be bound to the script of template Analytics Applications when generating new Analytics Applications. Note that `Exclude` is used to specifically prevent fields defined as optional bind parameters in the template Analytics Application script from being bound (these must either not have the optional quantity constraint specifiers or have a minimum quantity of 0). Enum: "Field", "Variable", "Property", "Exclude", "BDI" |
| `templateAppVarName` | string | Yes |  |

<details>
<summary>Properties of `range`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `lowerBound` | integer | No |  |
| `upperBound` | integer | No |  |

</details>

<details>
<summary>Properties of `formatting`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `quote` | string | No | The character to use for quote wrapping each of the bound values when formatting the source values associated with this binding.  If this property is not supplied, a single quote character (`'`) will be used by default.  Use an empty string to suppress quote wrapping the values. |
| `delimiter` | string | No | The character to use as a separator between two (or more) bound values when formatting the source values associated with this binding.  If this property is not supplied, a comma character will be used by default.  Use an empty string to indicate that no separator character should be used. |

</details>

</details>

<details>
<summary>Properties of `properties`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `disable` | object[] | No | Set to `true` to temporarily disable the use of this Link to generate Analytics Applications. |
| `menuLabel` | object[] | No | The default label to use for this Link in the context of the selection Analytics Application's ODAG navigation menu. |
| `genAppName` | object[] | No | An object that defines how to compute the name to use for the generated Analytics Application. |
| `genAppLimit` | object[] | No | The limit to the number of Analytics Applications generated using this specific Link that can exist, and still not deleted, before the policy defined by the `limitPolicy` property (configured separately via LinkPropertiesV2.limitPolicy) is applied. If no `limitPolicy` is defined, the `Restrict` policy is assumed. If there is no value for this property applicable to the current user, there is no limit to the number of Analytics Applications that can be generated from this link for the user.  The count of the current number of Analytics Applications is based on just those Analytics Applications generated by the current user (and still in existence) for this specific link. The minimum value for `limit` is `1`. |
| `limitPolicy` | object[] | No | The action to take when the limit to the maximum number of generated Analytics Applications is reached. |
| `rowEstRange` | object[] | Yes | A link property that defines a value range that the evaluated value of the row estimate measure must fall within in order to allow submissions of a request for the link. |
| `targetSheet` | object[] | No | An optional property that a Link creator can specify to cause the client to navigate to a specific sheet in the generated Analytics Application when opening the generated Analytics Application from the selection Analytics Application's navpoint panel. |
| `appOpenMethod` | object[] | No | Sets the default method by which the newly generated Analytics Application is displayed when opened. The default is `Tab` to open a new tab in the same browser.  Note that not all devices permit both methods so the chosen behavior may not apply if it is not supported on the user's device or browser. |
| `appRetentionTime` | object[] | No | A string that defines the length of time that a generated Analytics Application should be allowed to exist before it is automatically purged.  The format must be in either ISO 8601 duration format or the text `unlimited`. |
| `overrideGenAppLimit` | object[] | No | The limit to the number of Analytics Applications generated can be overridden using this specific Link that can exist, and still not deleted. The default value for this property is `false`. If this property value is set to `true`, then the `limit` value in `genAppLimit` is ignored. |

<details>
<summary>Properties of `disable`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `disable` | boolean | Yes |  |

</details>

<details>
<summary>Properties of `menuLabel`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `label` | string | Yes |  |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |

</details>

<details>
<summary>Properties of `genAppName`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `params` | string[] | No | One of the allowed variables that, when evaluated at ODAG Request execution time, can be used to compute a part of a generated Analytics Application's name. Enum: "templateAppName", "userId", "curYear", "curMonth", "curDay", "curHr", "curMin", "curSec" |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `formatString` | string | Yes | A string containing the base text of the name to use for the generated Analytics Application and optionally any number of placeholder patterns of the form `{N}` where `N` is an integer greater than or equal to `0`. The integer identifies the offset in the `params` array of an `AppNameParameterV2` to evaluate at ODAG Request execution time to compute a fragment of the generated Analytics Application's name and insert it at the same position as its corresponding `{N}` placeholder. |

</details>

<details>
<summary>Properties of `genAppLimit`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `limit` | integer | Yes |  |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |

</details>

<details>
<summary>Properties of `limitPolicy`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `limitPolicy` | string | Yes | Enum: "Restrict", "AutoDelete" |

</details>

<details>
<summary>Properties of `rowEstRange`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `lowBound` | integer | No | The minimum value for the row estimate to enable usage of the link to perform an ODAG request.  If the row estimate expression evaluates to a number lower than this value, the user will be prevented from submitting an ODAG request for this link.  If this value is not supplied, no minimum is required. |
| `highBound` | integer | Yes | The maximum value for the row estimate to enable usage of the link. If the row estimate expression evaluates to a value larger than this value, the user will be prevented from submitting an ODAG request for this link. |

</details>

<details>
<summary>Properties of `targetSheet`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `sheetId` | string | Yes | The ID of the sheet to first navigate to when opening the generated Analytics Application from the selection Analytics Application. |
| `sheetName` | string | No | An optional, read-only property that is returned when retrieving a link if the `targetSheet` setting exists for the current user in the link's `properties` set and the sheet with that ID exists in the link's `templateApp`. |

</details>

<details>
<summary>Properties of `appOpenMethod`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `openMethod` | string | Yes | Enum: "Tab", "Window" |

</details>

<details>
<summary>Properties of `appRetentionTime`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `retentionTime` | string | Yes |  |

</details>

<details>
<summary>Properties of `overrideGenAppLimit`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `overrideGenAppLimit` | boolean | No |  |

</details>

</details>

<details>
<summary>Properties of `templateApp`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The system-assigned ID for an Analytics Application. |
| `name` | string | Yes | The name of an Analytics Application. |

</details>

<details>
<summary>Properties of `modifiedByUser`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The system-assigned ID for a user |
| `name` | string | Yes |  |
| `subject` | string | Yes | Identity subject used for identity mapping. |
| `tenantid` | string | Yes | Tenant identifier. |

</details>

##### 403

Forbidden.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error entry within an error response. |
| `traceId` | string | No | A unique ID of the trace which the error occurred in. Makes it possible to locate involved services and find log messages from the time of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | A unique code used to identify the template form of the message in i18n tables (language independent). |
| `meta` | object | No | Additional metadata associated with an error. |
| `title` | string | No |  |
| `detail` | string | No | The message describing the error. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `statusCode` | integer | No | The HTTP status code for the error. Generally speaking, the following codes have these meanings: `200` - Success, `201` - Success (object created), `400` - Error with user input, `403` - Authorization error (user lacks permission), `404` - Object not found, `409` - Attempt to change an object using an obsolete last ModifiedDate. |

</details>

</details>

##### 404

ODAG not enabled or access denied.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error entry within an error response. |
| `traceId` | string | No | A unique ID of the trace which the error occurred in. Makes it possible to locate involved services and find log messages from the time of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | A unique code used to identify the template form of the message in i18n tables (language independent). |
| `meta` | object | No | Additional metadata associated with an error. |
| `title` | string | No |  |
| `detail` | string | No | The message describing the error. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `statusCode` | integer | No | The HTTP status code for the error. Generally speaking, the following codes have these meanings: `200` - Success, `201` - Success (object created), `400` - Error with user input, `403` - Authorization error (user lacks permission), `404` - Object not found, `409` - Attempt to change an object using an obsolete last ModifiedDate. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/analytics/odag-links` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/analytics/odag-links',
  {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for GET /api/analytics/odag-links yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/analytics/odag-links" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
[
  {
    "id": "string",
    "name": "ODAG Link name",
    "owner": {
      "id": "wcgIs6wGcDdyzep9QmyopWvNH1FJTOhh",
      "name": "string",
      "subject": "string",
      "tenantid": "string"
    },
    "status": "active",
    "bindings": [
      {
        "range": {
          "lowerBound": 42,
          "upperBound": 42
        },
        "formatting": {
          "quote": "'",
          "delimiter": ","
        },
        "numericOnly": false,
        "selectionStates": "string",
        "selectAppParamName": "string",
        "selectAppParamType": "Field",
        "templateAppVarName": "string"
      }
    ],
    "privileges": [
      "string"
    ],
    "properties": {
      "disable": [
        {
          "context": "string",
          "disable": true
        }
      ],
      "menuLabel": [
        {
          "label": "string",
          "context": "string"
        }
      ],
      "genAppName": [
        {
          "params": [
            "templateAppName"
          ],
          "context": "string",
          "formatString": "string"
        }
      ],
      "genAppLimit": [
        {
          "limit": 42,
          "context": "string"
        }
      ],
      "limitPolicy": [
        {
          "context": "string",
          "limitPolicy": "Restrict"
        }
      ],
      "rowEstRange": [
        {
          "context": "string",
          "lowBound": 42,
          "highBound": 42
        }
      ],
      "targetSheet": [
        {
          "context": "string",
          "sheetId": "string",
          "sheetName": "string"
        }
      ],
      "appOpenMethod": [
        {
          "context": "string",
          "openMethod": "Tab"
        }
      ],
      "appRetentionTime": [
        {
          "context": "string",
          "retentionTime": "string"
        }
      ],
      "overrideGenAppLimit": [
        {
          "context": "string",
          "overrideGenAppLimit": false
        }
      ]
    },
    "rowEstExpr": "string",
    "createdDate": "2025-11-11T13:45:30Z",
    "dynamicView": true,
    "templateApp": {
      "id": "string",
      "name": "appname"
    },
    "modifiedDate": "2025-11-11T13:45:30Z",
    "sourceLinkId": "string",
    "includeScript": false,
    "modifiedByUser": {
      "id": "wcgIs6wGcDdyzep9QmyopWvNH1FJTOhh",
      "name": "string",
      "subject": "string",
      "tenantid": "string"
    },
    "genAppAccessible": true,
    "templateAppChartObjects": [
      {}
    ]
  }
]
```

---

### POST /api/analytics/odag-links

Creates a new link that enables ODAG navigation from a designated selection Analytics Application to a generated Analytics Application that is created by copying the designated template Analytics Application, injecting values for bind variables harvested from the selection Analytics Application and dynamically loaded with data using those bindings. The Bindings will be initialized by searching the load script of the template Analytics Application for patterns of the form `$(od_FIELDNAME)[M-N]` where `FIELDNAME` is the name of a field in the model of the selection Analytics Application and the optional pattern `[M-N]` identifies the lower bound `M` and the upper bound `N` for the number of values for that field which must be in the active selection state of the selection Analytics Application for binding to occur.  The active selection state defaults to `selected` (i.e. green) unless the `od` prefix is immediately followed by some combination of the letters `s`, `o`, or `x`, in that order, specifically designating the `selected`, `optional` (i.e. white) and/or `excluded` (i.e. gray) groups of values to be harvested from the selection Analytics Application's selection state. The bindings in the `bindings` array in the request payload override the properties of the corresponding field bindings found in the script of the template Analytics Application.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `includeCharts` | boolean | No | Determines whether master charts of the template Analytics Application are included in the response. |

#### Request Body

**Required**

A JSON payload containing the content for a new ODAG link.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | The name of a link. |
| `bindings` | object[] | No | A collection of Bindings.  Note that there can be multiple bindings having the same `templateAppFieldName` in a binding collection to denote different usages of the field's selection state in the context of the data prep logic but they all must have the same value for their `range` property. |
| `properties` | object | No | The complete set of possible properties for a link and their associated user context/value pairings. |
| `rowEstExpr` | string | No | The measure expression to be evaluated in the context of the selection Analytics Application for the link that estimates the number of records that will be qualified by the primary load query of the template Analytics Application. This expression must be valid in the context of the selection Analytics Application fields and update whenever the selection state of the selection Analytics Application changes. |
| `dynamicView` | boolean | No | When `true`, the ODAG link is treated as a dynamic view. Analytics Application retention time is overridden to `24 hours` and the maximum number of generated Analytics Applications is set to `1`. |
| `templateApp` | string | No | The system-assigned ID for an Analytics Application. |
| `selectionApp` | string | Yes | The system-assigned ID for an Analytics Application. |
| `includeScript` | boolean | No | Set to `true` to include the generated Analytics Application load script in the generated Analytics Application. The default value is `false`. |
| `statusSetting` | string | No | The requested status transition to apply to a Link. New links are always created with status `active`; `statusSetting` is ignored. When updating a Link, if `statusSetting` is provided, the request updates the Link's `status` only (other fields in the payload are not applied). If omitted, the Link's status is not changed. `statusSetting` is an action, and it maps to the resulting `status`: - `activate` sets `status` to `active`. - `disable` sets `status` to `disabled`. - `decommission` sets `status` to `decommissioned`. If `statusSetting` has an unsupported value, the request returns an error and the Link is not updated. Links with status `decommissioned` cannot change status. Enum: "activate", "disable", "decommission" |

<details>
<summary>Properties of `bindings`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `range` | object | No | The lower and upper bound for the permitted number of values that must exist in the selection Analytics Application's source parameter in order for this binding to be valid (and permit an ODAG Request to be submitted. If this property is not supplied, there is no constraint on either the lower or upper bound. To indicate that an exact number of selections are required, use the same number for both the lower and upper bound. |
| `formatting` | object | No | A property value that describes the formatting of field values in a Binding. This is currently only settable in the template Analytics Application script and not when creating or updating a Link. |
| `numericOnly` | boolean | No | Set to `true` to indicate that only numeric values from the selection Analytics Application source parameter should be used. The default value for this property, if left unspecified, is `false`. This is currently only settable in the template Analytics Application script and not when creating or updating a Link. |
| `selectionStates` | string | No | A combination of the letters `S` and/or `O` to indicate which values from the selection states `selected` or `optional` in the hypercube of the selection Analytics Application to harvest as bind values to inject into the script of the template Analytics Application at ODAG request submission time. This is currently only settable in the template Analytics Application script and not when creating or updating a Link. |
| `selectAppParamName` | string | No | The path (or name) of the selection Analytics Application field, variable, or property to obtain the list of values for this binding. |
| `selectAppParamType` | string | Yes | The different kinds of selection Analytics Application parameters whose values can be bound to the script of template Analytics Applications when generating new Analytics Applications. Note that `Exclude` is used to specifically prevent fields defined as optional bind parameters in the template Analytics Application script from being bound (these must either not have the optional quantity constraint specifiers or have a minimum quantity of 0). Enum: "Field", "Variable", "Property", "Exclude", "BDI" |
| `templateAppVarName` | string | Yes |  |

<details>
<summary>Properties of `range`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `lowerBound` | integer | No |  |
| `upperBound` | integer | No |  |

</details>

<details>
<summary>Properties of `formatting`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `quote` | string | No | The character to use for quote wrapping each of the bound values when formatting the source values associated with this binding.  If this property is not supplied, a single quote character (`'`) will be used by default.  Use an empty string to suppress quote wrapping the values. |
| `delimiter` | string | No | The character to use as a separator between two (or more) bound values when formatting the source values associated with this binding.  If this property is not supplied, a comma character will be used by default.  Use an empty string to indicate that no separator character should be used. |

</details>

</details>

<details>
<summary>Properties of `properties`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `disable` | object[] | No | Set to `true` to temporarily disable the use of this Link to generate Analytics Applications. |
| `menuLabel` | object[] | No | The default label to use for this Link in the context of the selection Analytics Application's ODAG navigation menu. |
| `genAppName` | object[] | No | An object that defines how to compute the name to use for the generated Analytics Application. |
| `genAppLimit` | object[] | No | The limit to the number of Analytics Applications generated using this specific Link that can exist, and still not deleted, before the policy defined by the `limitPolicy` property (configured separately via LinkPropertiesV2.limitPolicy) is applied. If no `limitPolicy` is defined, the `Restrict` policy is assumed. If there is no value for this property applicable to the current user, there is no limit to the number of Analytics Applications that can be generated from this link for the user.  The count of the current number of Analytics Applications is based on just those Analytics Applications generated by the current user (and still in existence) for this specific link. The minimum value for `limit` is `1`. |
| `limitPolicy` | object[] | No | The action to take when the limit to the maximum number of generated Analytics Applications is reached. |
| `rowEstRange` | object[] | Yes | A link property that defines a value range that the evaluated value of the row estimate measure must fall within in order to allow submissions of a request for the link. |
| `targetSheet` | object[] | No | An optional property that a Link creator can specify to cause the client to navigate to a specific sheet in the generated Analytics Application when opening the generated Analytics Application from the selection Analytics Application's navpoint panel. |
| `appOpenMethod` | object[] | No | Sets the default method by which the newly generated Analytics Application is displayed when opened. The default is `Tab` to open a new tab in the same browser.  Note that not all devices permit both methods so the chosen behavior may not apply if it is not supported on the user's device or browser. |
| `appRetentionTime` | object[] | No | A string that defines the length of time that a generated Analytics Application should be allowed to exist before it is automatically purged.  The format must be in either ISO 8601 duration format or the text `unlimited`. |
| `overrideGenAppLimit` | object[] | No | The limit to the number of Analytics Applications generated can be overridden using this specific Link that can exist, and still not deleted. The default value for this property is `false`. If this property value is set to `true`, then the `limit` value in `genAppLimit` is ignored. |

<details>
<summary>Properties of `disable`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `disable` | boolean | Yes |  |

</details>

<details>
<summary>Properties of `menuLabel`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `label` | string | Yes |  |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |

</details>

<details>
<summary>Properties of `genAppName`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `params` | string[] | No | One of the allowed variables that, when evaluated at ODAG Request execution time, can be used to compute a part of a generated Analytics Application's name. Enum: "templateAppName", "userId", "curYear", "curMonth", "curDay", "curHr", "curMin", "curSec" |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `formatString` | string | Yes | A string containing the base text of the name to use for the generated Analytics Application and optionally any number of placeholder patterns of the form `{N}` where `N` is an integer greater than or equal to `0`. The integer identifies the offset in the `params` array of an `AppNameParameterV2` to evaluate at ODAG Request execution time to compute a fragment of the generated Analytics Application's name and insert it at the same position as its corresponding `{N}` placeholder. |

</details>

<details>
<summary>Properties of `genAppLimit`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `limit` | integer | Yes |  |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |

</details>

<details>
<summary>Properties of `limitPolicy`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `limitPolicy` | string | Yes | Enum: "Restrict", "AutoDelete" |

</details>

<details>
<summary>Properties of `rowEstRange`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `lowBound` | integer | No | The minimum value for the row estimate to enable usage of the link to perform an ODAG request.  If the row estimate expression evaluates to a number lower than this value, the user will be prevented from submitting an ODAG request for this link.  If this value is not supplied, no minimum is required. |
| `highBound` | integer | Yes | The maximum value for the row estimate to enable usage of the link. If the row estimate expression evaluates to a value larger than this value, the user will be prevented from submitting an ODAG request for this link. |

</details>

<details>
<summary>Properties of `targetSheet`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `sheetId` | string | Yes | The ID of the sheet to first navigate to when opening the generated Analytics Application from the selection Analytics Application. |
| `sheetName` | string | No | An optional, read-only property that is returned when retrieving a link if the `targetSheet` setting exists for the current user in the link's `properties` set and the sheet with that ID exists in the link's `templateApp`. |

</details>

<details>
<summary>Properties of `appOpenMethod`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `openMethod` | string | Yes | Enum: "Tab", "Window" |

</details>

<details>
<summary>Properties of `appRetentionTime`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `retentionTime` | string | Yes |  |

</details>

<details>
<summary>Properties of `overrideGenAppLimit`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `overrideGenAppLimit` | boolean | No |  |

</details>

</details>

#### Responses

##### 201

ODAG link created successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `name` | string | Yes | The name of a link. |
| `owner` | object | Yes | Condensed state of a user returned in state of ownable ODAG entities (for example, a link or request). |
| `status` | string | Yes | The current status of a link. Enum: "active", "disabled", "decommissioned", "incomplete" |
| `bindings` | object[] | No | A collection of Bindings.  Note that there can be multiple bindings having the same `templateAppFieldName` in a binding collection to denote different usages of the field's selection state in the context of the data prep logic but they all must have the same value for their `range` property. |
| `privileges` | string[] | No |  |
| `properties` | object | Yes | The complete set of possible properties for a link and their associated user context/value pairings. |
| `rowEstExpr` | string | Yes | The measure expression to be evaluated in the context of the selection Analytics Application for the link that estimates the number of records that will be qualified by the primary load query of the template Analytics Application. This expression must be valid in the context of the selection Analytics Application fields and update whenever the selection state of the selection Analytics Application changes. |
| `createdDate` | string | Yes |  |
| `dynamicView` | boolean | No | When `true`, the ODAG link is treated as a dynamic view. |
| `templateApp` | object | Yes | Condensed state of an Analytics Application returned in `state` for Link, LinkUsage, Request, and ODAG Apps GET calls. |
| `modifiedDate` | string | No |  |
| `sourceLinkId` | string | No | The ID of the original link this was copied from. Present only on deep-copied links. |
| `includeScript` | boolean | No | Set to `true` to include the generated Analytics Application load script in the generated Analytics Application. The default value is `false`. |
| `modifiedByUser` | object | No | Condensed state of a user returned in state of ownable ODAG entities (for example, a link or request). |
| `genAppAccessible` | boolean | No | Only returned on `LinkGet` and set to `true` if user will have access to an Analytics Application generated by this link. |
| `templateAppChartObjects` | object[] | No |  |

<details>
<summary>Properties of `owner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The system-assigned ID for a user |
| `name` | string | Yes |  |
| `subject` | string | Yes | Identity subject used for identity mapping. |
| `tenantid` | string | Yes | Tenant identifier. |

</details>

<details>
<summary>Properties of `bindings`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `range` | object | No | The lower and upper bound for the permitted number of values that must exist in the selection Analytics Application's source parameter in order for this binding to be valid (and permit an ODAG Request to be submitted. If this property is not supplied, there is no constraint on either the lower or upper bound. To indicate that an exact number of selections are required, use the same number for both the lower and upper bound. |
| `formatting` | object | No | A property value that describes the formatting of field values in a Binding. This is currently only settable in the template Analytics Application script and not when creating or updating a Link. |
| `numericOnly` | boolean | No | Set to `true` to indicate that only numeric values from the selection Analytics Application source parameter should be used. The default value for this property, if left unspecified, is `false`. This is currently only settable in the template Analytics Application script and not when creating or updating a Link. |
| `selectionStates` | string | No | A combination of the letters `S` and/or `O` to indicate which values from the selection states `selected` or `optional` in the hypercube of the selection Analytics Application to harvest as bind values to inject into the script of the template Analytics Application at ODAG request submission time. This is currently only settable in the template Analytics Application script and not when creating or updating a Link. |
| `selectAppParamName` | string | No | The path (or name) of the selection Analytics Application field, variable, or property to obtain the list of values for this binding. |
| `selectAppParamType` | string | Yes | The different kinds of selection Analytics Application parameters whose values can be bound to the script of template Analytics Applications when generating new Analytics Applications. Note that `Exclude` is used to specifically prevent fields defined as optional bind parameters in the template Analytics Application script from being bound (these must either not have the optional quantity constraint specifiers or have a minimum quantity of 0). Enum: "Field", "Variable", "Property", "Exclude", "BDI" |
| `templateAppVarName` | string | Yes |  |

<details>
<summary>Properties of `range`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `lowerBound` | integer | No |  |
| `upperBound` | integer | No |  |

</details>

<details>
<summary>Properties of `formatting`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `quote` | string | No | The character to use for quote wrapping each of the bound values when formatting the source values associated with this binding.  If this property is not supplied, a single quote character (`'`) will be used by default.  Use an empty string to suppress quote wrapping the values. |
| `delimiter` | string | No | The character to use as a separator between two (or more) bound values when formatting the source values associated with this binding.  If this property is not supplied, a comma character will be used by default.  Use an empty string to indicate that no separator character should be used. |

</details>

</details>

<details>
<summary>Properties of `properties`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `disable` | object[] | No | Set to `true` to temporarily disable the use of this Link to generate Analytics Applications. |
| `menuLabel` | object[] | No | The default label to use for this Link in the context of the selection Analytics Application's ODAG navigation menu. |
| `genAppName` | object[] | No | An object that defines how to compute the name to use for the generated Analytics Application. |
| `genAppLimit` | object[] | No | The limit to the number of Analytics Applications generated using this specific Link that can exist, and still not deleted, before the policy defined by the `limitPolicy` property (configured separately via LinkPropertiesV2.limitPolicy) is applied. If no `limitPolicy` is defined, the `Restrict` policy is assumed. If there is no value for this property applicable to the current user, there is no limit to the number of Analytics Applications that can be generated from this link for the user.  The count of the current number of Analytics Applications is based on just those Analytics Applications generated by the current user (and still in existence) for this specific link. The minimum value for `limit` is `1`. |
| `limitPolicy` | object[] | No | The action to take when the limit to the maximum number of generated Analytics Applications is reached. |
| `rowEstRange` | object[] | Yes | A link property that defines a value range that the evaluated value of the row estimate measure must fall within in order to allow submissions of a request for the link. |
| `targetSheet` | object[] | No | An optional property that a Link creator can specify to cause the client to navigate to a specific sheet in the generated Analytics Application when opening the generated Analytics Application from the selection Analytics Application's navpoint panel. |
| `appOpenMethod` | object[] | No | Sets the default method by which the newly generated Analytics Application is displayed when opened. The default is `Tab` to open a new tab in the same browser.  Note that not all devices permit both methods so the chosen behavior may not apply if it is not supported on the user's device or browser. |
| `appRetentionTime` | object[] | No | A string that defines the length of time that a generated Analytics Application should be allowed to exist before it is automatically purged.  The format must be in either ISO 8601 duration format or the text `unlimited`. |
| `overrideGenAppLimit` | object[] | No | The limit to the number of Analytics Applications generated can be overridden using this specific Link that can exist, and still not deleted. The default value for this property is `false`. If this property value is set to `true`, then the `limit` value in `genAppLimit` is ignored. |

<details>
<summary>Properties of `disable`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `disable` | boolean | Yes |  |

</details>

<details>
<summary>Properties of `menuLabel`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `label` | string | Yes |  |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |

</details>

<details>
<summary>Properties of `genAppName`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `params` | string[] | No | One of the allowed variables that, when evaluated at ODAG Request execution time, can be used to compute a part of a generated Analytics Application's name. Enum: "templateAppName", "userId", "curYear", "curMonth", "curDay", "curHr", "curMin", "curSec" |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `formatString` | string | Yes | A string containing the base text of the name to use for the generated Analytics Application and optionally any number of placeholder patterns of the form `{N}` where `N` is an integer greater than or equal to `0`. The integer identifies the offset in the `params` array of an `AppNameParameterV2` to evaluate at ODAG Request execution time to compute a fragment of the generated Analytics Application's name and insert it at the same position as its corresponding `{N}` placeholder. |

</details>

<details>
<summary>Properties of `genAppLimit`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `limit` | integer | Yes |  |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |

</details>

<details>
<summary>Properties of `limitPolicy`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `limitPolicy` | string | Yes | Enum: "Restrict", "AutoDelete" |

</details>

<details>
<summary>Properties of `rowEstRange`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `lowBound` | integer | No | The minimum value for the row estimate to enable usage of the link to perform an ODAG request.  If the row estimate expression evaluates to a number lower than this value, the user will be prevented from submitting an ODAG request for this link.  If this value is not supplied, no minimum is required. |
| `highBound` | integer | Yes | The maximum value for the row estimate to enable usage of the link. If the row estimate expression evaluates to a value larger than this value, the user will be prevented from submitting an ODAG request for this link. |

</details>

<details>
<summary>Properties of `targetSheet`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `sheetId` | string | Yes | The ID of the sheet to first navigate to when opening the generated Analytics Application from the selection Analytics Application. |
| `sheetName` | string | No | An optional, read-only property that is returned when retrieving a link if the `targetSheet` setting exists for the current user in the link's `properties` set and the sheet with that ID exists in the link's `templateApp`. |

</details>

<details>
<summary>Properties of `appOpenMethod`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `openMethod` | string | Yes | Enum: "Tab", "Window" |

</details>

<details>
<summary>Properties of `appRetentionTime`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `retentionTime` | string | Yes |  |

</details>

<details>
<summary>Properties of `overrideGenAppLimit`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `overrideGenAppLimit` | boolean | No |  |

</details>

</details>

<details>
<summary>Properties of `templateApp`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The system-assigned ID for an Analytics Application. |
| `name` | string | Yes | The name of an Analytics Application. |

</details>

<details>
<summary>Properties of `modifiedByUser`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The system-assigned ID for a user |
| `name` | string | Yes |  |
| `subject` | string | Yes | Identity subject used for identity mapping. |
| `tenantid` | string | Yes | Tenant identifier. |

</details>

##### 400

Invalid link payload (see detailed error).

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error entry within an error response. |
| `traceId` | string | No | A unique ID of the trace which the error occurred in. Makes it possible to locate involved services and find log messages from the time of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | A unique code used to identify the template form of the message in i18n tables (language independent). |
| `meta` | object | No | Additional metadata associated with an error. |
| `title` | string | No |  |
| `detail` | string | No | The message describing the error. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `statusCode` | integer | No | The HTTP status code for the error. Generally speaking, the following codes have these meanings: `200` - Success, `201` - Success (object created), `400` - Error with user input, `403` - Authorization error (user lacks permission), `404` - Object not found, `409` - Attempt to change an object using an obsolete last ModifiedDate. |

</details>

</details>

##### 403

Forbidden.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error entry within an error response. |
| `traceId` | string | No | A unique ID of the trace which the error occurred in. Makes it possible to locate involved services and find log messages from the time of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | A unique code used to identify the template form of the message in i18n tables (language independent). |
| `meta` | object | No | Additional metadata associated with an error. |
| `title` | string | No |  |
| `detail` | string | No | The message describing the error. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `statusCode` | integer | No | The HTTP status code for the error. Generally speaking, the following codes have these meanings: `200` - Success, `201` - Success (object created), `400` - Error with user input, `403` - Authorization error (user lacks permission), `404` - Object not found, `409` - Attempt to change an object using an obsolete last ModifiedDate. |

</details>

</details>

##### 404

Invalid referenced object ID (see detailed error message).

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error entry within an error response. |
| `traceId` | string | No | A unique ID of the trace which the error occurred in. Makes it possible to locate involved services and find log messages from the time of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | A unique code used to identify the template form of the message in i18n tables (language independent). |
| `meta` | object | No | Additional metadata associated with an error. |
| `title` | string | No |  |
| `detail` | string | No | The message describing the error. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `statusCode` | integer | No | The HTTP status code for the error. Generally speaking, the following codes have these meanings: `200` - Success, `201` - Success (object created), `400` - Error with user input, `403` - Authorization error (user lacks permission), `404` - Object not found, `409` - Attempt to change an object using an obsolete last ModifiedDate. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/analytics/odag-links` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/analytics/odag-links',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      name: 'ODAG Link name',
      bindings: [
        {
          range: {
            lowerBound: 42,
            upperBound: 42,
          },
          formatting: {
            quote: "'",
            delimiter: ',',
          },
          numericOnly: false,
          selectionStates: 'string',
          selectAppParamName: 'string',
          selectAppParamType: 'Field',
          templateAppVarName: 'string',
        },
      ],
      properties: {
        disable: [
          { context: 'string', disable: true },
        ],
        menuLabel: [
          { label: 'string', context: 'string' },
        ],
        genAppName: [
          {
            params: ['templateAppName'],
            context: 'string',
            formatString: 'string',
          },
        ],
        genAppLimit: [
          { limit: 42, context: 'string' },
        ],
        limitPolicy: [
          {
            context: 'string',
            limitPolicy: 'Restrict',
          },
        ],
        rowEstRange: [
          {
            context: 'string',
            lowBound: 42,
            highBound: 42,
          },
        ],
        targetSheet: [
          {
            context: 'string',
            sheetId: 'string',
            sheetName: 'string',
          },
        ],
        appOpenMethod: [
          {
            context: 'string',
            openMethod: 'Tab',
          },
        ],
        appRetentionTime: [
          {
            context: 'string',
            retentionTime: 'string',
          },
        ],
        overrideGenAppLimit: [
          {
            context: 'string',
            overrideGenAppLimit: false,
          },
        ],
      },
      rowEstExpr: 'string',
      dynamicView: true,
      templateApp: 'string',
      selectionApp: 'string',
      includeScript: false,
      statusSetting: 'activate',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/analytics/odag-links yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/analytics/odag-links" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"name":"ODAG Link name","bindings":[{"range":{"lowerBound":42,"upperBound":42},"formatting":{"quote":"'\''","delimiter":","},"numericOnly":false,"selectionStates":"string","selectAppParamName":"string","selectAppParamType":"Field","templateAppVarName":"string"}],"properties":{"disable":[{"context":"string","disable":true}],"menuLabel":[{"label":"string","context":"string"}],"genAppName":[{"params":["templateAppName"],"context":"string","formatString":"string"}],"genAppLimit":[{"limit":42,"context":"string"}],"limitPolicy":[{"context":"string","limitPolicy":"Restrict"}],"rowEstRange":[{"context":"string","lowBound":42,"highBound":42}],"targetSheet":[{"context":"string","sheetId":"string","sheetName":"string"}],"appOpenMethod":[{"context":"string","openMethod":"Tab"}],"appRetentionTime":[{"context":"string","retentionTime":"string"}],"overrideGenAppLimit":[{"context":"string","overrideGenAppLimit":false}]},"rowEstExpr":"string","dynamicView":true,"templateApp":"string","selectionApp":"string","includeScript":false,"statusSetting":"activate"}'
```

**Example Response:**

```json
{
  "id": "string",
  "name": "ODAG Link name",
  "owner": {
    "id": "wcgIs6wGcDdyzep9QmyopWvNH1FJTOhh",
    "name": "string",
    "subject": "string",
    "tenantid": "string"
  },
  "status": "active",
  "bindings": [
    {
      "range": {
        "lowerBound": 42,
        "upperBound": 42
      },
      "formatting": {
        "quote": "'",
        "delimiter": ","
      },
      "numericOnly": false,
      "selectionStates": "string",
      "selectAppParamName": "string",
      "selectAppParamType": "Field",
      "templateAppVarName": "string"
    }
  ],
  "privileges": [
    "string"
  ],
  "properties": {
    "disable": [
      {
        "context": "string",
        "disable": true
      }
    ],
    "menuLabel": [
      {
        "label": "string",
        "context": "string"
      }
    ],
    "genAppName": [
      {
        "params": [
          "templateAppName"
        ],
        "context": "string",
        "formatString": "string"
      }
    ],
    "genAppLimit": [
      {
        "limit": 42,
        "context": "string"
      }
    ],
    "limitPolicy": [
      {
        "context": "string",
        "limitPolicy": "Restrict"
      }
    ],
    "rowEstRange": [
      {
        "context": "string",
        "lowBound": 42,
        "highBound": 42
      }
    ],
    "targetSheet": [
      {
        "context": "string",
        "sheetId": "string",
        "sheetName": "string"
      }
    ],
    "appOpenMethod": [
      {
        "context": "string",
        "openMethod": "Tab"
      }
    ],
    "appRetentionTime": [
      {
        "context": "string",
        "retentionTime": "string"
      }
    ],
    "overrideGenAppLimit": [
      {
        "context": "string",
        "overrideGenAppLimit": false
      }
    ]
  },
  "rowEstExpr": "string",
  "createdDate": "2025-11-11T13:45:30Z",
  "dynamicView": true,
  "templateApp": {
    "id": "string",
    "name": "appname"
  },
  "modifiedDate": "2025-11-11T13:45:30Z",
  "sourceLinkId": "string",
  "includeScript": false,
  "modifiedByUser": {
    "id": "wcgIs6wGcDdyzep9QmyopWvNH1FJTOhh",
    "name": "string",
    "subject": "string",
    "tenantid": "string"
  },
  "genAppAccessible": true,
  "templateAppChartObjects": [
    {}
  ]
}
```

---

### GET /api/analytics/odag-links/{linkId}

Retrieves details of a specific ODAG link, including bindings, properties, status, and template Analytics Application charts. Use this to review link configuration or verify permissions before generating Analytics Applications.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `linkId` | string | Yes | The ID of the link. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `includeCharts` | boolean | No | Determines whether master charts of the template Analytics Application are included in the response. |

#### Responses

##### 200

Successful response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `name` | string | Yes | The name of a link. |
| `owner` | object | Yes | Condensed state of a user returned in state of ownable ODAG entities (for example, a link or request). |
| `status` | string | Yes | The current status of a link. Enum: "active", "disabled", "decommissioned", "incomplete" |
| `bindings` | object[] | No | A collection of Bindings.  Note that there can be multiple bindings having the same `templateAppFieldName` in a binding collection to denote different usages of the field's selection state in the context of the data prep logic but they all must have the same value for their `range` property. |
| `privileges` | string[] | No |  |
| `properties` | object | Yes | The complete set of possible properties for a link and their associated user context/value pairings. |
| `rowEstExpr` | string | Yes | The measure expression to be evaluated in the context of the selection Analytics Application for the link that estimates the number of records that will be qualified by the primary load query of the template Analytics Application. This expression must be valid in the context of the selection Analytics Application fields and update whenever the selection state of the selection Analytics Application changes. |
| `createdDate` | string | Yes |  |
| `dynamicView` | boolean | No | When `true`, the ODAG link is treated as a dynamic view. |
| `templateApp` | object | Yes | Condensed state of an Analytics Application returned in `state` for Link, LinkUsage, Request, and ODAG Apps GET calls. |
| `modifiedDate` | string | No |  |
| `sourceLinkId` | string | No | The ID of the original link this was copied from. Present only on deep-copied links. |
| `includeScript` | boolean | No | Set to `true` to include the generated Analytics Application load script in the generated Analytics Application. The default value is `false`. |
| `modifiedByUser` | object | No | Condensed state of a user returned in state of ownable ODAG entities (for example, a link or request). |
| `genAppAccessible` | boolean | No | Only returned on `LinkGet` and set to `true` if user will have access to an Analytics Application generated by this link. |
| `templateAppChartObjects` | object[] | No |  |

<details>
<summary>Properties of `owner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The system-assigned ID for a user |
| `name` | string | Yes |  |
| `subject` | string | Yes | Identity subject used for identity mapping. |
| `tenantid` | string | Yes | Tenant identifier. |

</details>

<details>
<summary>Properties of `bindings`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `range` | object | No | The lower and upper bound for the permitted number of values that must exist in the selection Analytics Application's source parameter in order for this binding to be valid (and permit an ODAG Request to be submitted. If this property is not supplied, there is no constraint on either the lower or upper bound. To indicate that an exact number of selections are required, use the same number for both the lower and upper bound. |
| `formatting` | object | No | A property value that describes the formatting of field values in a Binding. This is currently only settable in the template Analytics Application script and not when creating or updating a Link. |
| `numericOnly` | boolean | No | Set to `true` to indicate that only numeric values from the selection Analytics Application source parameter should be used. The default value for this property, if left unspecified, is `false`. This is currently only settable in the template Analytics Application script and not when creating or updating a Link. |
| `selectionStates` | string | No | A combination of the letters `S` and/or `O` to indicate which values from the selection states `selected` or `optional` in the hypercube of the selection Analytics Application to harvest as bind values to inject into the script of the template Analytics Application at ODAG request submission time. This is currently only settable in the template Analytics Application script and not when creating or updating a Link. |
| `selectAppParamName` | string | No | The path (or name) of the selection Analytics Application field, variable, or property to obtain the list of values for this binding. |
| `selectAppParamType` | string | Yes | The different kinds of selection Analytics Application parameters whose values can be bound to the script of template Analytics Applications when generating new Analytics Applications. Note that `Exclude` is used to specifically prevent fields defined as optional bind parameters in the template Analytics Application script from being bound (these must either not have the optional quantity constraint specifiers or have a minimum quantity of 0). Enum: "Field", "Variable", "Property", "Exclude", "BDI" |
| `templateAppVarName` | string | Yes |  |

<details>
<summary>Properties of `range`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `lowerBound` | integer | No |  |
| `upperBound` | integer | No |  |

</details>

<details>
<summary>Properties of `formatting`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `quote` | string | No | The character to use for quote wrapping each of the bound values when formatting the source values associated with this binding.  If this property is not supplied, a single quote character (`'`) will be used by default.  Use an empty string to suppress quote wrapping the values. |
| `delimiter` | string | No | The character to use as a separator between two (or more) bound values when formatting the source values associated with this binding.  If this property is not supplied, a comma character will be used by default.  Use an empty string to indicate that no separator character should be used. |

</details>

</details>

<details>
<summary>Properties of `properties`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `disable` | object[] | No | Set to `true` to temporarily disable the use of this Link to generate Analytics Applications. |
| `menuLabel` | object[] | No | The default label to use for this Link in the context of the selection Analytics Application's ODAG navigation menu. |
| `genAppName` | object[] | No | An object that defines how to compute the name to use for the generated Analytics Application. |
| `genAppLimit` | object[] | No | The limit to the number of Analytics Applications generated using this specific Link that can exist, and still not deleted, before the policy defined by the `limitPolicy` property (configured separately via LinkPropertiesV2.limitPolicy) is applied. If no `limitPolicy` is defined, the `Restrict` policy is assumed. If there is no value for this property applicable to the current user, there is no limit to the number of Analytics Applications that can be generated from this link for the user.  The count of the current number of Analytics Applications is based on just those Analytics Applications generated by the current user (and still in existence) for this specific link. The minimum value for `limit` is `1`. |
| `limitPolicy` | object[] | No | The action to take when the limit to the maximum number of generated Analytics Applications is reached. |
| `rowEstRange` | object[] | Yes | A link property that defines a value range that the evaluated value of the row estimate measure must fall within in order to allow submissions of a request for the link. |
| `targetSheet` | object[] | No | An optional property that a Link creator can specify to cause the client to navigate to a specific sheet in the generated Analytics Application when opening the generated Analytics Application from the selection Analytics Application's navpoint panel. |
| `appOpenMethod` | object[] | No | Sets the default method by which the newly generated Analytics Application is displayed when opened. The default is `Tab` to open a new tab in the same browser.  Note that not all devices permit both methods so the chosen behavior may not apply if it is not supported on the user's device or browser. |
| `appRetentionTime` | object[] | No | A string that defines the length of time that a generated Analytics Application should be allowed to exist before it is automatically purged.  The format must be in either ISO 8601 duration format or the text `unlimited`. |
| `overrideGenAppLimit` | object[] | No | The limit to the number of Analytics Applications generated can be overridden using this specific Link that can exist, and still not deleted. The default value for this property is `false`. If this property value is set to `true`, then the `limit` value in `genAppLimit` is ignored. |

<details>
<summary>Properties of `disable`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `disable` | boolean | Yes |  |

</details>

<details>
<summary>Properties of `menuLabel`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `label` | string | Yes |  |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |

</details>

<details>
<summary>Properties of `genAppName`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `params` | string[] | No | One of the allowed variables that, when evaluated at ODAG Request execution time, can be used to compute a part of a generated Analytics Application's name. Enum: "templateAppName", "userId", "curYear", "curMonth", "curDay", "curHr", "curMin", "curSec" |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `formatString` | string | Yes | A string containing the base text of the name to use for the generated Analytics Application and optionally any number of placeholder patterns of the form `{N}` where `N` is an integer greater than or equal to `0`. The integer identifies the offset in the `params` array of an `AppNameParameterV2` to evaluate at ODAG Request execution time to compute a fragment of the generated Analytics Application's name and insert it at the same position as its corresponding `{N}` placeholder. |

</details>

<details>
<summary>Properties of `genAppLimit`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `limit` | integer | Yes |  |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |

</details>

<details>
<summary>Properties of `limitPolicy`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `limitPolicy` | string | Yes | Enum: "Restrict", "AutoDelete" |

</details>

<details>
<summary>Properties of `rowEstRange`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `lowBound` | integer | No | The minimum value for the row estimate to enable usage of the link to perform an ODAG request.  If the row estimate expression evaluates to a number lower than this value, the user will be prevented from submitting an ODAG request for this link.  If this value is not supplied, no minimum is required. |
| `highBound` | integer | Yes | The maximum value for the row estimate to enable usage of the link. If the row estimate expression evaluates to a value larger than this value, the user will be prevented from submitting an ODAG request for this link. |

</details>

<details>
<summary>Properties of `targetSheet`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `sheetId` | string | Yes | The ID of the sheet to first navigate to when opening the generated Analytics Application from the selection Analytics Application. |
| `sheetName` | string | No | An optional, read-only property that is returned when retrieving a link if the `targetSheet` setting exists for the current user in the link's `properties` set and the sheet with that ID exists in the link's `templateApp`. |

</details>

<details>
<summary>Properties of `appOpenMethod`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `openMethod` | string | Yes | Enum: "Tab", "Window" |

</details>

<details>
<summary>Properties of `appRetentionTime`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `retentionTime` | string | Yes |  |

</details>

<details>
<summary>Properties of `overrideGenAppLimit`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `overrideGenAppLimit` | boolean | No |  |

</details>

</details>

<details>
<summary>Properties of `templateApp`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The system-assigned ID for an Analytics Application. |
| `name` | string | Yes | The name of an Analytics Application. |

</details>

<details>
<summary>Properties of `modifiedByUser`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The system-assigned ID for a user |
| `name` | string | Yes |  |
| `subject` | string | Yes | Identity subject used for identity mapping. |
| `tenantid` | string | Yes | Tenant identifier. |

</details>

##### 403

Forbidden.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error entry within an error response. |
| `traceId` | string | No | A unique ID of the trace which the error occurred in. Makes it possible to locate involved services and find log messages from the time of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | A unique code used to identify the template form of the message in i18n tables (language independent). |
| `meta` | object | No | Additional metadata associated with an error. |
| `title` | string | No |  |
| `detail` | string | No | The message describing the error. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `statusCode` | integer | No | The HTTP status code for the error. Generally speaking, the following codes have these meanings: `200` - Success, `201` - Success (object created), `400` - Error with user input, `403` - Authorization error (user lacks permission), `404` - Object not found, `409` - Attempt to change an object using an obsolete last ModifiedDate. |

</details>

</details>

##### 404

Invalid link ID (see detailed error).

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error entry within an error response. |
| `traceId` | string | No | A unique ID of the trace which the error occurred in. Makes it possible to locate involved services and find log messages from the time of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | A unique code used to identify the template form of the message in i18n tables (language independent). |
| `meta` | object | No | Additional metadata associated with an error. |
| `title` | string | No |  |
| `detail` | string | No | The message describing the error. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `statusCode` | integer | No | The HTTP status code for the error. Generally speaking, the following codes have these meanings: `200` - Success, `201` - Success (object created), `400` - Error with user input, `403` - Authorization error (user lacks permission), `404` - Object not found, `409` - Attempt to change an object using an obsolete last ModifiedDate. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/analytics/odag-links/{linkId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/analytics/odag-links/{linkId}',
  {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for GET /api/analytics/odag-links/{linkId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/analytics/odag-links/{linkId}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "string",
  "name": "ODAG Link name",
  "owner": {
    "id": "wcgIs6wGcDdyzep9QmyopWvNH1FJTOhh",
    "name": "string",
    "subject": "string",
    "tenantid": "string"
  },
  "status": "active",
  "bindings": [
    {
      "range": {
        "lowerBound": 42,
        "upperBound": 42
      },
      "formatting": {
        "quote": "'",
        "delimiter": ","
      },
      "numericOnly": false,
      "selectionStates": "string",
      "selectAppParamName": "string",
      "selectAppParamType": "Field",
      "templateAppVarName": "string"
    }
  ],
  "privileges": [
    "string"
  ],
  "properties": {
    "disable": [
      {
        "context": "string",
        "disable": true
      }
    ],
    "menuLabel": [
      {
        "label": "string",
        "context": "string"
      }
    ],
    "genAppName": [
      {
        "params": [
          "templateAppName"
        ],
        "context": "string",
        "formatString": "string"
      }
    ],
    "genAppLimit": [
      {
        "limit": 42,
        "context": "string"
      }
    ],
    "limitPolicy": [
      {
        "context": "string",
        "limitPolicy": "Restrict"
      }
    ],
    "rowEstRange": [
      {
        "context": "string",
        "lowBound": 42,
        "highBound": 42
      }
    ],
    "targetSheet": [
      {
        "context": "string",
        "sheetId": "string",
        "sheetName": "string"
      }
    ],
    "appOpenMethod": [
      {
        "context": "string",
        "openMethod": "Tab"
      }
    ],
    "appRetentionTime": [
      {
        "context": "string",
        "retentionTime": "string"
      }
    ],
    "overrideGenAppLimit": [
      {
        "context": "string",
        "overrideGenAppLimit": false
      }
    ]
  },
  "rowEstExpr": "string",
  "createdDate": "2025-11-11T13:45:30Z",
  "dynamicView": true,
  "templateApp": {
    "id": "string",
    "name": "appname"
  },
  "modifiedDate": "2025-11-11T13:45:30Z",
  "sourceLinkId": "string",
  "includeScript": false,
  "modifiedByUser": {
    "id": "wcgIs6wGcDdyzep9QmyopWvNH1FJTOhh",
    "name": "string",
    "subject": "string",
    "tenantid": "string"
  },
  "genAppAccessible": true,
  "templateAppChartObjects": [
    {}
  ]
}
```

---

### PUT /api/analytics/odag-links/{linkId}

Modifies ODAG link configuration including bindings, properties, status, and template Analytics Application reference. You can re-scan the template Analytics Application script to auto-detect binding patterns or override specific settings. If `statusSetting` is provided, the request updates only the link status (other payload fields are not applied).

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `linkId` | string | Yes | The ID of the link. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `includeCharts` | boolean | No | Determines whether master charts of the template Analytics Application are included in the response. |

#### Request Body

**Required**

A JSON payload containing the updated configuration for the ODAG link.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | The name of a link. |
| `ownerId` | string | No | The system-assigned ID for a user |
| `bindings` | object[] | No | A collection of Bindings.  Note that there can be multiple bindings having the same `templateAppFieldName` in a binding collection to denote different usages of the field's selection state in the context of the data prep logic but they all must have the same value for their `range` property. |
| `properties` | object | No | The complete set of possible properties for a link and their associated user context/value pairings. |
| `rowEstExpr` | string | No | The measure expression to be evaluated in the context of the selection Analytics Application for the link that estimates the number of records that will be qualified by the primary load query of the template Analytics Application. This expression must be valid in the context of the selection Analytics Application fields and update whenever the selection state of the selection Analytics Application changes. |
| `dynamicView` | boolean | No | When `true`, the ODAG link is treated as a dynamic view. Analytics Application retention time is overridden to `24 hours` and the maximum number of generated Analytics Applications is set to `1`. |
| `templateApp` | string | No | The system-assigned ID for an Analytics Application. |
| `selectionApp` | string | Yes | The system-assigned ID for an Analytics Application. |
| `includeScript` | boolean | No | Set to `true` to include the generated Analytics Application load script in the generated Analytics Application. The default value is `false`. |
| `statusSetting` | string | No | The requested status transition to apply to a Link. New links are always created with status `active`; `statusSetting` is ignored. When updating a Link, if `statusSetting` is provided, the request updates the Link's `status` only (other fields in the payload are not applied). If omitted, the Link's status is not changed. `statusSetting` is an action, and it maps to the resulting `status`: - `activate` sets `status` to `active`. - `disable` sets `status` to `disabled`. - `decommission` sets `status` to `decommissioned`. If `statusSetting` has an unsupported value, the request returns an error and the Link is not updated. Links with status `decommissioned` cannot change status. Enum: "activate", "disable", "decommission" |

<details>
<summary>Properties of `bindings`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `range` | object | No | The lower and upper bound for the permitted number of values that must exist in the selection Analytics Application's source parameter in order for this binding to be valid (and permit an ODAG Request to be submitted. If this property is not supplied, there is no constraint on either the lower or upper bound. To indicate that an exact number of selections are required, use the same number for both the lower and upper bound. |
| `formatting` | object | No | A property value that describes the formatting of field values in a Binding. This is currently only settable in the template Analytics Application script and not when creating or updating a Link. |
| `numericOnly` | boolean | No | Set to `true` to indicate that only numeric values from the selection Analytics Application source parameter should be used. The default value for this property, if left unspecified, is `false`. This is currently only settable in the template Analytics Application script and not when creating or updating a Link. |
| `selectionStates` | string | No | A combination of the letters `S` and/or `O` to indicate which values from the selection states `selected` or `optional` in the hypercube of the selection Analytics Application to harvest as bind values to inject into the script of the template Analytics Application at ODAG request submission time. This is currently only settable in the template Analytics Application script and not when creating or updating a Link. |
| `selectAppParamName` | string | No | The path (or name) of the selection Analytics Application field, variable, or property to obtain the list of values for this binding. |
| `selectAppParamType` | string | Yes | The different kinds of selection Analytics Application parameters whose values can be bound to the script of template Analytics Applications when generating new Analytics Applications. Note that `Exclude` is used to specifically prevent fields defined as optional bind parameters in the template Analytics Application script from being bound (these must either not have the optional quantity constraint specifiers or have a minimum quantity of 0). Enum: "Field", "Variable", "Property", "Exclude", "BDI" |
| `templateAppVarName` | string | Yes |  |

<details>
<summary>Properties of `range`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `lowerBound` | integer | No |  |
| `upperBound` | integer | No |  |

</details>

<details>
<summary>Properties of `formatting`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `quote` | string | No | The character to use for quote wrapping each of the bound values when formatting the source values associated with this binding.  If this property is not supplied, a single quote character (`'`) will be used by default.  Use an empty string to suppress quote wrapping the values. |
| `delimiter` | string | No | The character to use as a separator between two (or more) bound values when formatting the source values associated with this binding.  If this property is not supplied, a comma character will be used by default.  Use an empty string to indicate that no separator character should be used. |

</details>

</details>

<details>
<summary>Properties of `properties`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `disable` | object[] | No | Set to `true` to temporarily disable the use of this Link to generate Analytics Applications. |
| `menuLabel` | object[] | No | The default label to use for this Link in the context of the selection Analytics Application's ODAG navigation menu. |
| `genAppName` | object[] | No | An object that defines how to compute the name to use for the generated Analytics Application. |
| `genAppLimit` | object[] | No | The limit to the number of Analytics Applications generated using this specific Link that can exist, and still not deleted, before the policy defined by the `limitPolicy` property (configured separately via LinkPropertiesV2.limitPolicy) is applied. If no `limitPolicy` is defined, the `Restrict` policy is assumed. If there is no value for this property applicable to the current user, there is no limit to the number of Analytics Applications that can be generated from this link for the user.  The count of the current number of Analytics Applications is based on just those Analytics Applications generated by the current user (and still in existence) for this specific link. The minimum value for `limit` is `1`. |
| `limitPolicy` | object[] | No | The action to take when the limit to the maximum number of generated Analytics Applications is reached. |
| `rowEstRange` | object[] | Yes | A link property that defines a value range that the evaluated value of the row estimate measure must fall within in order to allow submissions of a request for the link. |
| `targetSheet` | object[] | No | An optional property that a Link creator can specify to cause the client to navigate to a specific sheet in the generated Analytics Application when opening the generated Analytics Application from the selection Analytics Application's navpoint panel. |
| `appOpenMethod` | object[] | No | Sets the default method by which the newly generated Analytics Application is displayed when opened. The default is `Tab` to open a new tab in the same browser.  Note that not all devices permit both methods so the chosen behavior may not apply if it is not supported on the user's device or browser. |
| `appRetentionTime` | object[] | No | A string that defines the length of time that a generated Analytics Application should be allowed to exist before it is automatically purged.  The format must be in either ISO 8601 duration format or the text `unlimited`. |
| `overrideGenAppLimit` | object[] | No | The limit to the number of Analytics Applications generated can be overridden using this specific Link that can exist, and still not deleted. The default value for this property is `false`. If this property value is set to `true`, then the `limit` value in `genAppLimit` is ignored. |

<details>
<summary>Properties of `disable`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `disable` | boolean | Yes |  |

</details>

<details>
<summary>Properties of `menuLabel`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `label` | string | Yes |  |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |

</details>

<details>
<summary>Properties of `genAppName`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `params` | string[] | No | One of the allowed variables that, when evaluated at ODAG Request execution time, can be used to compute a part of a generated Analytics Application's name. Enum: "templateAppName", "userId", "curYear", "curMonth", "curDay", "curHr", "curMin", "curSec" |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `formatString` | string | Yes | A string containing the base text of the name to use for the generated Analytics Application and optionally any number of placeholder patterns of the form `{N}` where `N` is an integer greater than or equal to `0`. The integer identifies the offset in the `params` array of an `AppNameParameterV2` to evaluate at ODAG Request execution time to compute a fragment of the generated Analytics Application's name and insert it at the same position as its corresponding `{N}` placeholder. |

</details>

<details>
<summary>Properties of `genAppLimit`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `limit` | integer | Yes |  |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |

</details>

<details>
<summary>Properties of `limitPolicy`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `limitPolicy` | string | Yes | Enum: "Restrict", "AutoDelete" |

</details>

<details>
<summary>Properties of `rowEstRange`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `lowBound` | integer | No | The minimum value for the row estimate to enable usage of the link to perform an ODAG request.  If the row estimate expression evaluates to a number lower than this value, the user will be prevented from submitting an ODAG request for this link.  If this value is not supplied, no minimum is required. |
| `highBound` | integer | Yes | The maximum value for the row estimate to enable usage of the link. If the row estimate expression evaluates to a value larger than this value, the user will be prevented from submitting an ODAG request for this link. |

</details>

<details>
<summary>Properties of `targetSheet`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `sheetId` | string | Yes | The ID of the sheet to first navigate to when opening the generated Analytics Application from the selection Analytics Application. |
| `sheetName` | string | No | An optional, read-only property that is returned when retrieving a link if the `targetSheet` setting exists for the current user in the link's `properties` set and the sheet with that ID exists in the link's `templateApp`. |

</details>

<details>
<summary>Properties of `appOpenMethod`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `openMethod` | string | Yes | Enum: "Tab", "Window" |

</details>

<details>
<summary>Properties of `appRetentionTime`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `retentionTime` | string | Yes |  |

</details>

<details>
<summary>Properties of `overrideGenAppLimit`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `overrideGenAppLimit` | boolean | No |  |

</details>

</details>

#### Responses

##### 200

ODAG link updated successfully.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `name` | string | Yes | The name of a link. |
| `owner` | object | Yes | Condensed state of a user returned in state of ownable ODAG entities (for example, a link or request). |
| `status` | string | Yes | The current status of a link. Enum: "active", "disabled", "decommissioned", "incomplete" |
| `bindings` | object[] | No | A collection of Bindings.  Note that there can be multiple bindings having the same `templateAppFieldName` in a binding collection to denote different usages of the field's selection state in the context of the data prep logic but they all must have the same value for their `range` property. |
| `privileges` | string[] | No |  |
| `properties` | object | Yes | The complete set of possible properties for a link and their associated user context/value pairings. |
| `rowEstExpr` | string | Yes | The measure expression to be evaluated in the context of the selection Analytics Application for the link that estimates the number of records that will be qualified by the primary load query of the template Analytics Application. This expression must be valid in the context of the selection Analytics Application fields and update whenever the selection state of the selection Analytics Application changes. |
| `createdDate` | string | Yes |  |
| `dynamicView` | boolean | No | When `true`, the ODAG link is treated as a dynamic view. |
| `templateApp` | object | Yes | Condensed state of an Analytics Application returned in `state` for Link, LinkUsage, Request, and ODAG Apps GET calls. |
| `modifiedDate` | string | No |  |
| `sourceLinkId` | string | No | The ID of the original link this was copied from. Present only on deep-copied links. |
| `includeScript` | boolean | No | Set to `true` to include the generated Analytics Application load script in the generated Analytics Application. The default value is `false`. |
| `modifiedByUser` | object | No | Condensed state of a user returned in state of ownable ODAG entities (for example, a link or request). |
| `genAppAccessible` | boolean | No | Only returned on `LinkGet` and set to `true` if user will have access to an Analytics Application generated by this link. |
| `templateAppChartObjects` | object[] | No |  |

<details>
<summary>Properties of `owner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The system-assigned ID for a user |
| `name` | string | Yes |  |
| `subject` | string | Yes | Identity subject used for identity mapping. |
| `tenantid` | string | Yes | Tenant identifier. |

</details>

<details>
<summary>Properties of `bindings`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `range` | object | No | The lower and upper bound for the permitted number of values that must exist in the selection Analytics Application's source parameter in order for this binding to be valid (and permit an ODAG Request to be submitted. If this property is not supplied, there is no constraint on either the lower or upper bound. To indicate that an exact number of selections are required, use the same number for both the lower and upper bound. |
| `formatting` | object | No | A property value that describes the formatting of field values in a Binding. This is currently only settable in the template Analytics Application script and not when creating or updating a Link. |
| `numericOnly` | boolean | No | Set to `true` to indicate that only numeric values from the selection Analytics Application source parameter should be used. The default value for this property, if left unspecified, is `false`. This is currently only settable in the template Analytics Application script and not when creating or updating a Link. |
| `selectionStates` | string | No | A combination of the letters `S` and/or `O` to indicate which values from the selection states `selected` or `optional` in the hypercube of the selection Analytics Application to harvest as bind values to inject into the script of the template Analytics Application at ODAG request submission time. This is currently only settable in the template Analytics Application script and not when creating or updating a Link. |
| `selectAppParamName` | string | No | The path (or name) of the selection Analytics Application field, variable, or property to obtain the list of values for this binding. |
| `selectAppParamType` | string | Yes | The different kinds of selection Analytics Application parameters whose values can be bound to the script of template Analytics Applications when generating new Analytics Applications. Note that `Exclude` is used to specifically prevent fields defined as optional bind parameters in the template Analytics Application script from being bound (these must either not have the optional quantity constraint specifiers or have a minimum quantity of 0). Enum: "Field", "Variable", "Property", "Exclude", "BDI" |
| `templateAppVarName` | string | Yes |  |

<details>
<summary>Properties of `range`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `lowerBound` | integer | No |  |
| `upperBound` | integer | No |  |

</details>

<details>
<summary>Properties of `formatting`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `quote` | string | No | The character to use for quote wrapping each of the bound values when formatting the source values associated with this binding.  If this property is not supplied, a single quote character (`'`) will be used by default.  Use an empty string to suppress quote wrapping the values. |
| `delimiter` | string | No | The character to use as a separator between two (or more) bound values when formatting the source values associated with this binding.  If this property is not supplied, a comma character will be used by default.  Use an empty string to indicate that no separator character should be used. |

</details>

</details>

<details>
<summary>Properties of `properties`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `disable` | object[] | No | Set to `true` to temporarily disable the use of this Link to generate Analytics Applications. |
| `menuLabel` | object[] | No | The default label to use for this Link in the context of the selection Analytics Application's ODAG navigation menu. |
| `genAppName` | object[] | No | An object that defines how to compute the name to use for the generated Analytics Application. |
| `genAppLimit` | object[] | No | The limit to the number of Analytics Applications generated using this specific Link that can exist, and still not deleted, before the policy defined by the `limitPolicy` property (configured separately via LinkPropertiesV2.limitPolicy) is applied. If no `limitPolicy` is defined, the `Restrict` policy is assumed. If there is no value for this property applicable to the current user, there is no limit to the number of Analytics Applications that can be generated from this link for the user.  The count of the current number of Analytics Applications is based on just those Analytics Applications generated by the current user (and still in existence) for this specific link. The minimum value for `limit` is `1`. |
| `limitPolicy` | object[] | No | The action to take when the limit to the maximum number of generated Analytics Applications is reached. |
| `rowEstRange` | object[] | Yes | A link property that defines a value range that the evaluated value of the row estimate measure must fall within in order to allow submissions of a request for the link. |
| `targetSheet` | object[] | No | An optional property that a Link creator can specify to cause the client to navigate to a specific sheet in the generated Analytics Application when opening the generated Analytics Application from the selection Analytics Application's navpoint panel. |
| `appOpenMethod` | object[] | No | Sets the default method by which the newly generated Analytics Application is displayed when opened. The default is `Tab` to open a new tab in the same browser.  Note that not all devices permit both methods so the chosen behavior may not apply if it is not supported on the user's device or browser. |
| `appRetentionTime` | object[] | No | A string that defines the length of time that a generated Analytics Application should be allowed to exist before it is automatically purged.  The format must be in either ISO 8601 duration format or the text `unlimited`. |
| `overrideGenAppLimit` | object[] | No | The limit to the number of Analytics Applications generated can be overridden using this specific Link that can exist, and still not deleted. The default value for this property is `false`. If this property value is set to `true`, then the `limit` value in `genAppLimit` is ignored. |

<details>
<summary>Properties of `disable`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `disable` | boolean | Yes |  |

</details>

<details>
<summary>Properties of `menuLabel`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `label` | string | Yes |  |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |

</details>

<details>
<summary>Properties of `genAppName`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `params` | string[] | No | One of the allowed variables that, when evaluated at ODAG Request execution time, can be used to compute a part of a generated Analytics Application's name. Enum: "templateAppName", "userId", "curYear", "curMonth", "curDay", "curHr", "curMin", "curSec" |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `formatString` | string | Yes | A string containing the base text of the name to use for the generated Analytics Application and optionally any number of placeholder patterns of the form `{N}` where `N` is an integer greater than or equal to `0`. The integer identifies the offset in the `params` array of an `AppNameParameterV2` to evaluate at ODAG Request execution time to compute a fragment of the generated Analytics Application's name and insert it at the same position as its corresponding `{N}` placeholder. |

</details>

<details>
<summary>Properties of `genAppLimit`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `limit` | integer | Yes |  |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |

</details>

<details>
<summary>Properties of `limitPolicy`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `limitPolicy` | string | Yes | Enum: "Restrict", "AutoDelete" |

</details>

<details>
<summary>Properties of `rowEstRange`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `lowBound` | integer | No | The minimum value for the row estimate to enable usage of the link to perform an ODAG request.  If the row estimate expression evaluates to a number lower than this value, the user will be prevented from submitting an ODAG request for this link.  If this value is not supplied, no minimum is required. |
| `highBound` | integer | Yes | The maximum value for the row estimate to enable usage of the link. If the row estimate expression evaluates to a value larger than this value, the user will be prevented from submitting an ODAG request for this link. |

</details>

<details>
<summary>Properties of `targetSheet`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `sheetId` | string | Yes | The ID of the sheet to first navigate to when opening the generated Analytics Application from the selection Analytics Application. |
| `sheetName` | string | No | An optional, read-only property that is returned when retrieving a link if the `targetSheet` setting exists for the current user in the link's `properties` set and the sheet with that ID exists in the link's `templateApp`. |

</details>

<details>
<summary>Properties of `appOpenMethod`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `openMethod` | string | Yes | Enum: "Tab", "Window" |

</details>

<details>
<summary>Properties of `appRetentionTime`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `retentionTime` | string | Yes |  |

</details>

<details>
<summary>Properties of `overrideGenAppLimit`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `context` | string | Yes | An expression based on the usage environment of a Link typically including predicates that test the current user's membership in a group or possession of a user role that when evaluated truthfully enables an applicable value for a Link property. For example, `User_*` indicates that the link property setting applies to all users while `User.name = joe` indicates the rule applies only to a specific user named `joe`. |
| `overrideGenAppLimit` | boolean | No |  |

</details>

</details>

<details>
<summary>Properties of `templateApp`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The system-assigned ID for an Analytics Application. |
| `name` | string | Yes | The name of an Analytics Application. |

</details>

<details>
<summary>Properties of `modifiedByUser`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The system-assigned ID for a user |
| `name` | string | Yes |  |
| `subject` | string | Yes | Identity subject used for identity mapping. |
| `tenantid` | string | Yes | Tenant identifier. |

</details>

##### 403

Forbidden.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error entry within an error response. |
| `traceId` | string | No | A unique ID of the trace which the error occurred in. Makes it possible to locate involved services and find log messages from the time of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | A unique code used to identify the template form of the message in i18n tables (language independent). |
| `meta` | object | No | Additional metadata associated with an error. |
| `title` | string | No |  |
| `detail` | string | No | The message describing the error. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `statusCode` | integer | No | The HTTP status code for the error. Generally speaking, the following codes have these meanings: `200` - Success, `201` - Success (object created), `400` - Error with user input, `403` - Authorization error (user lacks permission), `404` - Object not found, `409` - Attempt to change an object using an obsolete last ModifiedDate. |

</details>

</details>

##### 404

Link not found, ODAG not enabled, or invalid referenced object.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error entry within an error response. |
| `traceId` | string | No | A unique ID of the trace which the error occurred in. Makes it possible to locate involved services and find log messages from the time of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | A unique code used to identify the template form of the message in i18n tables (language independent). |
| `meta` | object | No | Additional metadata associated with an error. |
| `title` | string | No |  |
| `detail` | string | No | The message describing the error. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `statusCode` | integer | No | The HTTP status code for the error. Generally speaking, the following codes have these meanings: `200` - Success, `201` - Success (object created), `400` - Error with user input, `403` - Authorization error (user lacks permission), `404` - Object not found, `409` - Attempt to change an object using an obsolete last ModifiedDate. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PUT /api/analytics/odag-links/{linkId}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/analytics/odag-links/{linkId}',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      name: 'ODAG Link name',
      ownerId: 'wcgIs6wGcDdyzep9QmyopWvNH1FJTOhh',
      bindings: [
        {
          range: {
            lowerBound: 42,
            upperBound: 42,
          },
          formatting: {
            quote: "'",
            delimiter: ',',
          },
          numericOnly: false,
          selectionStates: 'string',
          selectAppParamName: 'string',
          selectAppParamType: 'Field',
          templateAppVarName: 'string',
        },
      ],
      properties: {
        disable: [
          { context: 'string', disable: true },
        ],
        menuLabel: [
          { label: 'string', context: 'string' },
        ],
        genAppName: [
          {
            params: ['templateAppName'],
            context: 'string',
            formatString: 'string',
          },
        ],
        genAppLimit: [
          { limit: 42, context: 'string' },
        ],
        limitPolicy: [
          {
            context: 'string',
            limitPolicy: 'Restrict',
          },
        ],
        rowEstRange: [
          {
            context: 'string',
            lowBound: 42,
            highBound: 42,
          },
        ],
        targetSheet: [
          {
            context: 'string',
            sheetId: 'string',
            sheetName: 'string',
          },
        ],
        appOpenMethod: [
          {
            context: 'string',
            openMethod: 'Tab',
          },
        ],
        appRetentionTime: [
          {
            context: 'string',
            retentionTime: 'string',
          },
        ],
        overrideGenAppLimit: [
          {
            context: 'string',
            overrideGenAppLimit: false,
          },
        ],
      },
      rowEstExpr: 'string',
      dynamicView: true,
      templateApp: 'string',
      selectionApp: 'string',
      includeScript: false,
      statusSetting: 'activate',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/analytics/odag-links/{linkId} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/analytics/odag-links/{linkId}" \
-X PUT \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"name":"ODAG Link name","ownerId":"wcgIs6wGcDdyzep9QmyopWvNH1FJTOhh","bindings":[{"range":{"lowerBound":42,"upperBound":42},"formatting":{"quote":"'\''","delimiter":","},"numericOnly":false,"selectionStates":"string","selectAppParamName":"string","selectAppParamType":"Field","templateAppVarName":"string"}],"properties":{"disable":[{"context":"string","disable":true}],"menuLabel":[{"label":"string","context":"string"}],"genAppName":[{"params":["templateAppName"],"context":"string","formatString":"string"}],"genAppLimit":[{"limit":42,"context":"string"}],"limitPolicy":[{"context":"string","limitPolicy":"Restrict"}],"rowEstRange":[{"context":"string","lowBound":42,"highBound":42}],"targetSheet":[{"context":"string","sheetId":"string","sheetName":"string"}],"appOpenMethod":[{"context":"string","openMethod":"Tab"}],"appRetentionTime":[{"context":"string","retentionTime":"string"}],"overrideGenAppLimit":[{"context":"string","overrideGenAppLimit":false}]},"rowEstExpr":"string","dynamicView":true,"templateApp":"string","selectionApp":"string","includeScript":false,"statusSetting":"activate"}'
```

**Example Response:**

```json
{
  "id": "string",
  "name": "ODAG Link name",
  "owner": {
    "id": "wcgIs6wGcDdyzep9QmyopWvNH1FJTOhh",
    "name": "string",
    "subject": "string",
    "tenantid": "string"
  },
  "status": "active",
  "bindings": [
    {
      "range": {
        "lowerBound": 42,
        "upperBound": 42
      },
      "formatting": {
        "quote": "'",
        "delimiter": ","
      },
      "numericOnly": false,
      "selectionStates": "string",
      "selectAppParamName": "string",
      "selectAppParamType": "Field",
      "templateAppVarName": "string"
    }
  ],
  "privileges": [
    "string"
  ],
  "properties": {
    "disable": [
      {
        "context": "string",
        "disable": true
      }
    ],
    "menuLabel": [
      {
        "label": "string",
        "context": "string"
      }
    ],
    "genAppName": [
      {
        "params": [
          "templateAppName"
        ],
        "context": "string",
        "formatString": "string"
      }
    ],
    "genAppLimit": [
      {
        "limit": 42,
        "context": "string"
      }
    ],
    "limitPolicy": [
      {
        "context": "string",
        "limitPolicy": "Restrict"
      }
    ],
    "rowEstRange": [
      {
        "context": "string",
        "lowBound": 42,
        "highBound": 42
      }
    ],
    "targetSheet": [
      {
        "context": "string",
        "sheetId": "string",
        "sheetName": "string"
      }
    ],
    "appOpenMethod": [
      {
        "context": "string",
        "openMethod": "Tab"
      }
    ],
    "appRetentionTime": [
      {
        "context": "string",
        "retentionTime": "string"
      }
    ],
    "overrideGenAppLimit": [
      {
        "context": "string",
        "overrideGenAppLimit": false
      }
    ]
  },
  "rowEstExpr": "string",
  "createdDate": "2025-11-11T13:45:30Z",
  "dynamicView": true,
  "templateApp": {
    "id": "string",
    "name": "appname"
  },
  "modifiedDate": "2025-11-11T13:45:30Z",
  "sourceLinkId": "string",
  "includeScript": false,
  "modifiedByUser": {
    "id": "wcgIs6wGcDdyzep9QmyopWvNH1FJTOhh",
    "name": "string",
    "subject": "string",
    "tenantid": "string"
  },
  "genAppAccessible": true,
  "templateAppChartObjects": [
    {}
  ]
}
```

---

### GET /api/analytics/odag-links/{linkId}/requests

Retrieves all Analytics Application generation requests for a specific ODAG link, with optional filtering by pending status (`pending`), selection Analytics Application (`selectionAppId`), sheet context (`selectionAppSheet`), or client context (`clientContextHandle`). Use this to track generation history or monitor in-flight requests.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `linkId` | string | Yes | The ID of the link. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `clientContextHandle` | string | No | An opaque handle to a client-side object that contains the reference to the link being used. |
| `pending` | boolean | No | Pass `true` if only pending requests should be returned. |
| `selectionAppId` | string | No | The ID of the selection Analytics Application. |
| `selectionAppSheet` | string | No | The name (or ID) of the sheet to filter qualifying ODAG requests for a selection Analytics Application. |

#### Responses

##### 200

Successful response - see array of requests in response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The system-assigned ID for an ODAG request. |
| `kind` | string | Yes | For links that do not use any partitioning fields, a `single` Analytics Application generation request is created. However, for selection Analytics Applications that designate a set of partitioning fields and the user selects multiple values for any of those partitioning fields, ODAG uses a separate `singlesub` request to generate a separate Analytics Application for each combination of selected partition field values, and tracks the queuing and data load phase of each of those sub-requests separately. Note that `singlesub` requests share the same link ID as their spawning `multiple` parent request. Enum: "single", "multiple", "singlesub" |
| `link` | string | Yes | The system-assigned ID for a link. |
| `owner` | object | Yes | Condensed state of a user returned in state of ownable ODAG entities (for example, a link or request). |
| `state` | string | Yes | The current state of an ODAG request. Enum: "validating", "queued", "invalid", "hold", "loading", "canceled", "failed", "succeeded", "canceling", "canceledAck", "failedAck" |
| `loadState` | object | No | An object that describes the state of a generated Analytics Application's data load operation. In request objects that include this object as an optional property, the property will be missing for `multiple` generation requests (see their sub-requests for their data load information) or for `single` and `singlesub` requests that have not yet reached their `loading` phase. |
| `sheetname` | string | No |  |
| `purgeAfter` | string | No |  |
| `timeToLive` | integer | No | The value of the Link's `appRetentionTime` property at the time the Analytics Application was generated (`0` means no auto-purge). |
| `validation` | string[] | No | A list of validation errors or warnings. |
| `createdDate` | string | Yes |  |
| `targetSheet` | string | No | The ID of the target sheet, taken from the link properties, to navigate to when opening the generated Analytics Application (empty for Analytics Application overview). |
| `templateApp` | string | Yes | The system-assigned ID for an Analytics Application. |
| `actualRowEst` | integer | No | The evaluated value of the Link's `rowEstExpr` measure expression at the time this request was initiated. |
| `errorMessage` | string | No | Detailed message if the request failed. |
| `generatedApp` | object | No | Condensed state of an Analytics Application returned in `state` for Link, LinkUsage, Request, and ODAG Apps GET calls. |
| `modifiedDate` | string | Yes |  |
| `selectionApp` | string | No | The system-assigned ID for an Analytics Application. |
| `curRowEstExpr` | string | No | The Link's `rowEstExpr` property setting at the time this request was initiated. |
| `retentionTime` | integer | No | The remaining time in minutes this request will be retained (0 means kept forever). |
| `parentRequestId` | string | No | The system-assigned ID for an ODAG request. |
| `templateAppName` | string | No | The name of an Analytics Application. |
| `bindingStateHash` | integer | No | A 64-bit hash of the bound field state at the time the request was made. |
| `generatedAppName` | string | No | The name of an Analytics Application. |
| `selectionAppName` | string | No | The name of an Analytics Application. |
| `curRowEstLowBound` | integer | No | The Link's `rowEstRange.lowBound` value for the user at the time this request was initiated. |
| `curRowEstHighBound` | integer | No | The Link's `rowEstRange.highBound` value for the user at the time this request was initiated. |
| `selectionStateHash` | integer | No | A 64-bit hash of the selected field values at the time the request was made. |

<details>
<summary>Properties of `owner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The system-assigned ID for a user |
| `name` | string | Yes |  |
| `subject` | string | Yes | Identity subject used for identity mapping. |
| `tenantid` | string | Yes | Tenant identifier. |

</details>

<details>
<summary>Properties of `loadState`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | No | The completion status of a completed Request. Enum: "pending", "success", "warnings", "failed" |
| `loadHost` | string | Yes | The engine host name used to perform the data load operation for this request. This property will be missing in `multiple` generation requests (see the `loadHost` field of their sub-requests) and will be an empty string on a `single` or `singlesub` request that has not yet reached the `loading` phase. |
| `startedAt` | string | Yes |  |
| `finishedAt` | string | No |  |

</details>

<details>
<summary>Properties of `generatedApp`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The system-assigned ID for an Analytics Application. |
| `name` | string | Yes | The name of an Analytics Application. |

</details>

##### 400

Link not found or ODAG service error (see detailed error).

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error entry within an error response. |
| `traceId` | string | No | A unique ID of the trace which the error occurred in. Makes it possible to locate involved services and find log messages from the time of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | A unique code used to identify the template form of the message in i18n tables (language independent). |
| `meta` | object | No | Additional metadata associated with an error. |
| `title` | string | No |  |
| `detail` | string | No | The message describing the error. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `statusCode` | integer | No | The HTTP status code for the error. Generally speaking, the following codes have these meanings: `200` - Success, `201` - Success (object created), `400` - Error with user input, `403` - Authorization error (user lacks permission), `404` - Object not found, `409` - Attempt to change an object using an obsolete last ModifiedDate. |

</details>

</details>

##### 403

Forbidden.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error entry within an error response. |
| `traceId` | string | No | A unique ID of the trace which the error occurred in. Makes it possible to locate involved services and find log messages from the time of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | A unique code used to identify the template form of the message in i18n tables (language independent). |
| `meta` | object | No | Additional metadata associated with an error. |
| `title` | string | No |  |
| `detail` | string | No | The message describing the error. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `statusCode` | integer | No | The HTTP status code for the error. Generally speaking, the following codes have these meanings: `200` - Success, `201` - Success (object created), `400` - Error with user input, `403` - Authorization error (user lacks permission), `404` - Object not found, `409` - Attempt to change an object using an obsolete last ModifiedDate. |

</details>

</details>

##### 404

ODAG not enabled or access denied.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error entry within an error response. |
| `traceId` | string | No | A unique ID of the trace which the error occurred in. Makes it possible to locate involved services and find log messages from the time of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | A unique code used to identify the template form of the message in i18n tables (language independent). |
| `meta` | object | No | Additional metadata associated with an error. |
| `title` | string | No |  |
| `detail` | string | No | The message describing the error. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `statusCode` | integer | No | The HTTP status code for the error. Generally speaking, the following codes have these meanings: `200` - Success, `201` - Success (object created), `400` - Error with user input, `403` - Authorization error (user lacks permission), `404` - Object not found, `409` - Attempt to change an object using an obsolete last ModifiedDate. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/analytics/odag-links/{linkId}/requests` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/analytics/odag-links/{linkId}/requests',
  {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for GET /api/analytics/odag-links/{linkId}/requests yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/analytics/odag-links/{linkId}/requests" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
[
  {
    "id": "string",
    "kind": "single",
    "link": "string",
    "owner": {
      "id": "wcgIs6wGcDdyzep9QmyopWvNH1FJTOhh",
      "name": "string",
      "subject": "string",
      "tenantid": "string"
    },
    "state": "validating",
    "loadState": {
      "status": "pending",
      "loadHost": "string",
      "startedAt": "2025-11-11T13:45:30Z",
      "finishedAt": "2025-11-11T13:45:30Z"
    },
    "sheetname": "string",
    "purgeAfter": "2025-11-11T13:45:30Z",
    "timeToLive": 42,
    "validation": [
      "string"
    ],
    "createdDate": "2025-11-11T13:45:30Z",
    "targetSheet": "string",
    "templateApp": "string",
    "actualRowEst": 42,
    "errorMessage": "string",
    "generatedApp": {
      "id": "string",
      "name": "appname"
    },
    "modifiedDate": "2025-11-11T13:45:30Z",
    "selectionApp": "string",
    "curRowEstExpr": "string",
    "retentionTime": 42,
    "parentRequestId": "string",
    "templateAppName": "appname",
    "bindingStateHash": 42,
    "generatedAppName": "appname",
    "selectionAppName": "appname",
    "curRowEstLowBound": 42,
    "curRowEstHighBound": 42,
    "selectionStateHash": 42
  }
]
```

---

### POST /api/analytics/odag-links/{linkId}/requests

Submits a new Analytics Application generation request with the current selection state from a selection Analytics Application. The request is validated against link properties before queuing.  On success, returns a request object that you must monitor for completion using the status endpoint.  Validation failures return detailed error information.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `linkId` | string | Yes | The ID of the link. |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `sheetname` | string | No | The name of the sheet from which the request is being made. |
| `actualRowEst` | integer | No | The current row estimate value calculated by the link's `rowEstExpr` property in the context of the selection Analytics Application. |
| `selectionApp` | string | Yes | The system-assigned ID for an Analytics Application. |
| `selectionState` | object[] | No | A collection of FieldSelectionStateV2 objects. |
| `bindSelectionState` | object[] | Yes | A collection of FieldSelectionStateV2 objects. |
| `clientContextHandle` | string | No | An opaque handle to a client-side object that contains the reference to the link being used. |

<details>
<summary>Properties of `selectionState`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `values` | object[] | Yes | The list of values in the selection state for this field. |
| `selectedSize` | integer | No | The actual number of selected values. Not used for `bindSelectionState`. |
| `selectionAppParamName` | string | Yes | The name of a variable or field that corresponds to one or more bindings having a matching `selectAppParamName` used to generate Analytics Applications. |
| `selectionAppParamType` | string | Yes | The different kinds of selection Analytics Application parameters whose values can be bound to the script of template Analytics Applications when generating new Analytics Applications. Note that `Exclude` is used to specifically prevent fields defined as optional bind parameters in the template Analytics Application script from being bound (these must either not have the optional quantity constraint specifiers or have a minimum quantity of 0). Enum: "Field", "Variable", "Property", "Exclude", "BDI" |

<details>
<summary>Properties of `values`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `numValue` | string | No |  |
| `strValue` | string | Yes |  |
| `selStatus` | string | Yes | The valid set of selection states that a specific field value can be in. One of: `S` (selected), `O` (optional), or `X` (excluded). Enum: "S", "O", "X" |

</details>

</details>

<details>
<summary>Properties of `bindSelectionState`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `values` | object[] | Yes | The list of values in the selection state for this field. |
| `selectedSize` | integer | No | The actual number of selected values. Not used for `bindSelectionState`. |
| `selectionAppParamName` | string | Yes | The name of a variable or field that corresponds to one or more bindings having a matching `selectAppParamName` used to generate Analytics Applications. |
| `selectionAppParamType` | string | Yes | The different kinds of selection Analytics Application parameters whose values can be bound to the script of template Analytics Applications when generating new Analytics Applications. Note that `Exclude` is used to specifically prevent fields defined as optional bind parameters in the template Analytics Application script from being bound (these must either not have the optional quantity constraint specifiers or have a minimum quantity of 0). Enum: "Field", "Variable", "Property", "Exclude", "BDI" |

<details>
<summary>Properties of `values`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `numValue` | string | No |  |
| `strValue` | string | Yes |  |
| `selStatus` | string | Yes | The valid set of selection states that a specific field value can be in. One of: `S` (selected), `O` (optional), or `X` (excluded). Enum: "S", "O", "X" |

</details>

</details>

#### Responses

##### 201

Successful response - the request has been queued.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The system-assigned ID for an ODAG request. |
| `kind` | string | Yes | For links that do not use any partitioning fields, a `single` Analytics Application generation request is created. However, for selection Analytics Applications that designate a set of partitioning fields and the user selects multiple values for any of those partitioning fields, ODAG uses a separate `singlesub` request to generate a separate Analytics Application for each combination of selected partition field values, and tracks the queuing and data load phase of each of those sub-requests separately. Note that `singlesub` requests share the same link ID as their spawning `multiple` parent request. Enum: "single", "multiple", "singlesub" |
| `link` | string | Yes | The system-assigned ID for a link. |
| `owner` | object | Yes | Condensed state of a user returned in state of ownable ODAG entities (for example, a link or request). |
| `state` | string | Yes | The current state of an ODAG request. Enum: "validating", "queued", "invalid", "hold", "loading", "canceled", "failed", "succeeded", "canceling", "canceledAck", "failedAck" |
| `loadState` | object | No | An object that describes the state of a generated Analytics Application's data load operation. In request objects that include this object as an optional property, the property will be missing for `multiple` generation requests (see their sub-requests for their data load information) or for `single` and `singlesub` requests that have not yet reached their `loading` phase. |
| `sheetname` | string | No |  |
| `purgeAfter` | string | No |  |
| `timeToLive` | integer | No | The value of the Link's `appRetentionTime` property at the time the Analytics Application was generated (`0` means no auto-purge). |
| `validation` | string[] | No | A list of validation errors or warnings. |
| `createdDate` | string | Yes |  |
| `targetSheet` | string | No | The ID of the target sheet, taken from the link properties, to navigate to when opening the generated Analytics Application (empty for Analytics Application overview). |
| `templateApp` | string | Yes | The system-assigned ID for an Analytics Application. |
| `actualRowEst` | integer | No | The evaluated value of the Link's `rowEstExpr` measure expression at the time this request was initiated. |
| `errorMessage` | string | No | Detailed message if the request failed. |
| `generatedApp` | object | No | Condensed state of an Analytics Application returned in `state` for Link, LinkUsage, Request, and ODAG Apps GET calls. |
| `modifiedDate` | string | Yes |  |
| `selectionApp` | string | No | The system-assigned ID for an Analytics Application. |
| `curRowEstExpr` | string | No | The Link's `rowEstExpr` property setting at the time this request was initiated. |
| `retentionTime` | integer | No | The remaining time in minutes this request will be retained (0 means kept forever). |
| `parentRequestId` | string | No | The system-assigned ID for an ODAG request. |
| `templateAppName` | string | No | The name of an Analytics Application. |
| `bindingStateHash` | integer | No | A 64-bit hash of the bound field state at the time the request was made. |
| `generatedAppName` | string | No | The name of an Analytics Application. |
| `selectionAppName` | string | No | The name of an Analytics Application. |
| `curRowEstLowBound` | integer | No | The Link's `rowEstRange.lowBound` value for the user at the time this request was initiated. |
| `curRowEstHighBound` | integer | No | The Link's `rowEstRange.highBound` value for the user at the time this request was initiated. |
| `selectionStateHash` | integer | No | A 64-bit hash of the selected field values at the time the request was made. |

<details>
<summary>Properties of `owner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The system-assigned ID for a user |
| `name` | string | Yes |  |
| `subject` | string | Yes | Identity subject used for identity mapping. |
| `tenantid` | string | Yes | Tenant identifier. |

</details>

<details>
<summary>Properties of `loadState`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | No | The completion status of a completed Request. Enum: "pending", "success", "warnings", "failed" |
| `loadHost` | string | Yes | The engine host name used to perform the data load operation for this request. This property will be missing in `multiple` generation requests (see the `loadHost` field of their sub-requests) and will be an empty string on a `single` or `singlesub` request that has not yet reached the `loading` phase. |
| `startedAt` | string | Yes |  |
| `finishedAt` | string | No |  |

</details>

<details>
<summary>Properties of `generatedApp`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The system-assigned ID for an Analytics Application. |
| `name` | string | Yes | The name of an Analytics Application. |

</details>

##### 400

The selection Analytics Application was in an invalid state to proceed with this Analytics Application generation (see detailed error).

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error entry within an error response. |
| `traceId` | string | No | A unique ID of the trace which the error occurred in. Makes it possible to locate involved services and find log messages from the time of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | A unique code used to identify the template form of the message in i18n tables (language independent). |
| `meta` | object | No | Additional metadata associated with an error. |
| `title` | string | No |  |
| `detail` | string | No | The message describing the error. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `statusCode` | integer | No | The HTTP status code for the error. Generally speaking, the following codes have these meanings: `200` - Success, `201` - Success (object created), `400` - Error with user input, `403` - Authorization error (user lacks permission), `404` - Object not found, `409` - Attempt to change an object using an obsolete last ModifiedDate. |

</details>

</details>

##### 403

Forbidden.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error entry within an error response. |
| `traceId` | string | No | A unique ID of the trace which the error occurred in. Makes it possible to locate involved services and find log messages from the time of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | A unique code used to identify the template form of the message in i18n tables (language independent). |
| `meta` | object | No | Additional metadata associated with an error. |
| `title` | string | No |  |
| `detail` | string | No | The message describing the error. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `statusCode` | integer | No | The HTTP status code for the error. Generally speaking, the following codes have these meanings: `200` - Success, `201` - Success (object created), `400` - Error with user input, `403` - Authorization error (user lacks permission), `404` - Object not found, `409` - Attempt to change an object using an obsolete last ModifiedDate. |

</details>

</details>

##### 404

Invalid link ID.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error entry within an error response. |
| `traceId` | string | No | A unique ID of the trace which the error occurred in. Makes it possible to locate involved services and find log messages from the time of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | A unique code used to identify the template form of the message in i18n tables (language independent). |
| `meta` | object | No | Additional metadata associated with an error. |
| `title` | string | No |  |
| `detail` | string | No | The message describing the error. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `statusCode` | integer | No | The HTTP status code for the error. Generally speaking, the following codes have these meanings: `200` - Success, `201` - Success (object created), `400` - Error with user input, `403` - Authorization error (user lacks permission), `404` - Object not found, `409` - Attempt to change an object using an obsolete last ModifiedDate. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/analytics/odag-links/{linkId}/requests` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/analytics/odag-links/{linkId}/requests',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      sheetname: 'string',
      actualRowEst: 42,
      selectionApp: 'string',
      selectionState: [
        {
          values: [
            {
              numValue: 'string',
              strValue: 'string',
              selStatus: 'S',
            },
          ],
          selectedSize: 42,
          selectionAppParamName: 'string',
          selectionAppParamType: 'Field',
        },
      ],
      bindSelectionState: [
        {
          values: [
            {
              numValue: 'string',
              strValue: 'string',
              selStatus: 'S',
            },
          ],
          selectedSize: 42,
          selectionAppParamName: 'string',
          selectionAppParamType: 'Field',
        },
      ],
      clientContextHandle: 'string',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/analytics/odag-links/{linkId}/requests yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/analytics/odag-links/{linkId}/requests" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"sheetname":"string","actualRowEst":42,"selectionApp":"string","selectionState":[{"values":[{"numValue":"string","strValue":"string","selStatus":"S"}],"selectedSize":42,"selectionAppParamName":"string","selectionAppParamType":"Field"}],"bindSelectionState":[{"values":[{"numValue":"string","strValue":"string","selStatus":"S"}],"selectedSize":42,"selectionAppParamName":"string","selectionAppParamType":"Field"}],"clientContextHandle":"string"}'
```

**Example Response:**

```json
{
  "id": "string",
  "kind": "single",
  "link": "string",
  "owner": {
    "id": "wcgIs6wGcDdyzep9QmyopWvNH1FJTOhh",
    "name": "string",
    "subject": "string",
    "tenantid": "string"
  },
  "state": "validating",
  "loadState": {
    "status": "pending",
    "loadHost": "string",
    "startedAt": "2025-11-11T13:45:30Z",
    "finishedAt": "2025-11-11T13:45:30Z"
  },
  "sheetname": "string",
  "purgeAfter": "2025-11-11T13:45:30Z",
  "timeToLive": 42,
  "validation": [
    "string"
  ],
  "createdDate": "2025-11-11T13:45:30Z",
  "targetSheet": "string",
  "templateApp": "string",
  "actualRowEst": 42,
  "errorMessage": "string",
  "generatedApp": {
    "id": "string",
    "name": "appname"
  },
  "modifiedDate": "2025-11-11T13:45:30Z",
  "selectionApp": "string",
  "curRowEstExpr": "string",
  "retentionTime": 42,
  "parentRequestId": "string",
  "templateAppName": "appname",
  "bindingStateHash": 42,
  "generatedAppName": "appname",
  "selectionAppName": "appname",
  "curRowEstLowBound": 42,
  "curRowEstHighBound": 42,
  "selectionStateHash": 42
}
```

---

### GET /api/analytics/odag-links/cancreate

Checks whether the current user has permission to create new ODAG links. Optionally verify permissions for a specific template Analytics Application or selection Analytics Application context. Returns a boolean indicating create permission status.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `optDenyIfSelAppNotUpdatable` | boolean | No | When `true`, deny permission if the selection Analytics Application cannot be updated. This parameter is ignored unless `optSelectAppId` is also supplied. |
| `optSelectAppId` | string | No | An optional parameter for specifying the ID of a selection Analytics Application. |
| `optTemplateAppId` | string | No | An optional parameter for specifying the ID of a template Analytics Application. |

#### Responses

##### 200

Successful response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `canCreateLinks` | boolean | No |  |

##### 400

Invalid parameter values (see detailed error).

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error entry within an error response. |
| `traceId` | string | No | A unique ID of the trace which the error occurred in. Makes it possible to locate involved services and find log messages from the time of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | A unique code used to identify the template form of the message in i18n tables (language independent). |
| `meta` | object | No | Additional metadata associated with an error. |
| `title` | string | No |  |
| `detail` | string | No | The message describing the error. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `statusCode` | integer | No | The HTTP status code for the error. Generally speaking, the following codes have these meanings: `200` - Success, `201` - Success (object created), `400` - Error with user input, `403` - Authorization error (user lacks permission), `404` - Object not found, `409` - Attempt to change an object using an obsolete last ModifiedDate. |

</details>

</details>

##### 403

Forbidden.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error entry within an error response. |
| `traceId` | string | No | A unique ID of the trace which the error occurred in. Makes it possible to locate involved services and find log messages from the time of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | A unique code used to identify the template form of the message in i18n tables (language independent). |
| `meta` | object | No | Additional metadata associated with an error. |
| `title` | string | No |  |
| `detail` | string | No | The message describing the error. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `statusCode` | integer | No | The HTTP status code for the error. Generally speaking, the following codes have these meanings: `200` - Success, `201` - Success (object created), `400` - Error with user input, `403` - Authorization error (user lacks permission), `404` - Object not found, `409` - Attempt to change an object using an obsolete last ModifiedDate. |

</details>

</details>

##### 404

ODAG not enabled.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error entry within an error response. |
| `traceId` | string | No | A unique ID of the trace which the error occurred in. Makes it possible to locate involved services and find log messages from the time of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | A unique code used to identify the template form of the message in i18n tables (language independent). |
| `meta` | object | No | Additional metadata associated with an error. |
| `title` | string | No |  |
| `detail` | string | No | The message describing the error. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `statusCode` | integer | No | The HTTP status code for the error. Generally speaking, the following codes have these meanings: `200` - Success, `201` - Success (object created), `400` - Error with user input, `403` - Authorization error (user lacks permission), `404` - Object not found, `409` - Attempt to change an object using an obsolete last ModifiedDate. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/analytics/odag-links/cancreate` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/analytics/odag-links/cancreate',
  {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for GET /api/analytics/odag-links/cancreate yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/analytics/odag-links/cancreate" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "canCreateLinks": true
}
```

---

### POST /api/analytics/odag-links/selection-app-link-usages

Registers the current set of ODAG links referenced by a selection Analytics Application and returns only those links the current user can access. Call this when a selection Analytics Application is opened or after modifying its ODAG link references. The response is an array of objects, where the `id` identifies the requested link and `link` contains the link state when accessible. Use `GET /analytics/odag-links/{linkId}` for full details.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `selAppId` | string | Yes | The ID of a selection Analytics Application. |
| `includeCharts` | boolean | No | When `true`, include master charts from the template Analytics Application in the response. |
| `type` | string | No | The type of the links to query. Defaults to `link`. Enum: "link", "view", "all" |

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `linkList` | string[] | Yes | An array of Link IDs. |

#### Responses

##### 200

Successful response.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The system-assigned ID for a link. |
| `link` | object | No | The full state of a Link. |

<details>
<summary>Properties of `link`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes |  |
| `name` | string | Yes | The name of a link. |
| `owner` | object | Yes | Condensed state of a user returned in state of ownable ODAG entities (for example, a link or request). |
| `status` | string | Yes | The current status of a link. Enum: "active", "disabled", "decommissioned", "incomplete" |
| `bindings` | object[] | No | A collection of Bindings.  Note that there can be multiple bindings having the same `templateAppFieldName` in a binding collection to denote different usages of the field's selection state in the context of the data prep logic but they all must have the same value for their `range` property. |
| `privileges` | string[] | No |  |
| `properties` | object | Yes | The complete set of possible properties for a link and their associated user context/value pairings. |
| `rowEstExpr` | string | Yes | The measure expression to be evaluated in the context of the selection Analytics Application for the link that estimates the number of records that will be qualified by the primary load query of the template Analytics Application. This expression must be valid in the context of the selection Analytics Application fields and update whenever the selection state of the selection Analytics Application changes. |
| `createdDate` | string | Yes |  |
| `dynamicView` | boolean | No | When `true`, the ODAG link is treated as a dynamic view. |
| `templateApp` | object | Yes | Condensed state of an Analytics Application returned in `state` for Link, LinkUsage, Request, and ODAG Apps GET calls. |
| `modifiedDate` | string | No |  |
| `sourceLinkId` | string | No | The ID of the original link this was copied from. Present only on deep-copied links. |
| `includeScript` | boolean | No | Set to `true` to include the generated Analytics Application load script in the generated Analytics Application. The default value is `false`. |
| `modifiedByUser` | object | No | Condensed state of a user returned in state of ownable ODAG entities (for example, a link or request). |
| `genAppAccessible` | boolean | No | Only returned on `LinkGet` and set to `true` if user will have access to an Analytics Application generated by this link. |
| `templateAppChartObjects` | object[] | No |  |

<details>
<summary>Properties of `owner`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The system-assigned ID for a user |
| `name` | string | Yes |  |
| `subject` | string | Yes | Identity subject used for identity mapping. |
| `tenantid` | string | Yes | Tenant identifier. |

</details>

<details>
<summary>Properties of `bindings`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `range` | object | No | The lower and upper bound for the permitted number of values that must exist in the selection Analytics Application's source parameter in order for this binding to be valid (and permit an ODAG Request to be submitted. If this property is not supplied, there is no constraint on either the lower or upper bound. To indicate that an exact number of selections are required, use the same number for both the lower and upper bound. |
| `formatting` | object | No | A property value that describes the formatting of field values in a Binding. This is currently only settable in the template Analytics Application script and not when creating or updating a Link. |
| `numericOnly` | boolean | No | Set to `true` to indicate that only numeric values from the selection Analytics Application source parameter should be used. The default value for this property, if left unspecified, is `false`. This is currently only settable in the template Analytics Application script and not when creating or updating a Link. |
| `selectionStates` | string | No | A combination of the letters `S` and/or `O` to indicate which values from the selection states `selected` or `optional` in the hypercube of the selection Analytics Application to harvest as bind values to inject into the script of the template Analytics Application at ODAG request submission time. This is currently only settable in the template Analytics Application script and not when creating or updating a Link. |
| `selectAppParamName` | string | No | The path (or name) of the selection Analytics Application field, variable, or property to obtain the list of values for this binding. |
| `selectAppParamType` | string | Yes | The different kinds of selection Analytics Application parameters whose values can be bound to the script of template Analytics Applications when generating new Analytics Applications. Note that `Exclude` is used to specifically prevent fields defined as optional bind parameters in the template Analytics Application script from being bound (these must either not have the optional quantity constraint specifiers or have a minimum quantity of 0). Enum: "Field", "Variable", "Property", "Exclude", "BDI" |
| `templateAppVarName` | string | Yes |  |

<details>
<summary>Properties of `range`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `formatting`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `properties`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `disable` | object[] | No | Set to `true` to temporarily disable the use of this Link to generate Analytics Applications. |
| `menuLabel` | object[] | No | The default label to use for this Link in the context of the selection Analytics Application's ODAG navigation menu. |
| `genAppName` | object[] | No | An object that defines how to compute the name to use for the generated Analytics Application. |
| `genAppLimit` | object[] | No | The limit to the number of Analytics Applications generated using this specific Link that can exist, and still not deleted, before the policy defined by the `limitPolicy` property (configured separately via LinkPropertiesV2.limitPolicy) is applied. If no `limitPolicy` is defined, the `Restrict` policy is assumed. If there is no value for this property applicable to the current user, there is no limit to the number of Analytics Applications that can be generated from this link for the user.  The count of the current number of Analytics Applications is based on just those Analytics Applications generated by the current user (and still in existence) for this specific link. The minimum value for `limit` is `1`. |
| `limitPolicy` | object[] | No | The action to take when the limit to the maximum number of generated Analytics Applications is reached. |
| `rowEstRange` | object[] | Yes | A link property that defines a value range that the evaluated value of the row estimate measure must fall within in order to allow submissions of a request for the link. |
| `targetSheet` | object[] | No | An optional property that a Link creator can specify to cause the client to navigate to a specific sheet in the generated Analytics Application when opening the generated Analytics Application from the selection Analytics Application's navpoint panel. |
| `appOpenMethod` | object[] | No | Sets the default method by which the newly generated Analytics Application is displayed when opened. The default is `Tab` to open a new tab in the same browser.  Note that not all devices permit both methods so the chosen behavior may not apply if it is not supported on the user's device or browser. |
| `appRetentionTime` | object[] | No | A string that defines the length of time that a generated Analytics Application should be allowed to exist before it is automatically purged.  The format must be in either ISO 8601 duration format or the text `unlimited`. |
| `overrideGenAppLimit` | object[] | No | The limit to the number of Analytics Applications generated can be overridden using this specific Link that can exist, and still not deleted. The default value for this property is `false`. If this property value is set to `true`, then the `limit` value in `genAppLimit` is ignored. |

<details>
<summary>Properties of `disable`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `menuLabel`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `genAppName`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `genAppLimit`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `limitPolicy`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `rowEstRange`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `targetSheet`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `appOpenMethod`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `appRetentionTime`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `overrideGenAppLimit`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `templateApp`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The system-assigned ID for an Analytics Application. |
| `name` | string | Yes | The name of an Analytics Application. |

</details>

<details>
<summary>Properties of `modifiedByUser`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The system-assigned ID for a user |
| `name` | string | Yes |  |
| `subject` | string | Yes | Identity subject used for identity mapping. |
| `tenantid` | string | Yes | Tenant identifier. |

</details>

</details>

##### 400

Invalid parameter values or link list (see detailed error).

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error entry within an error response. |
| `traceId` | string | No | A unique ID of the trace which the error occurred in. Makes it possible to locate involved services and find log messages from the time of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | A unique code used to identify the template form of the message in i18n tables (language independent). |
| `meta` | object | No | Additional metadata associated with an error. |
| `title` | string | No |  |
| `detail` | string | No | The message describing the error. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `statusCode` | integer | No | The HTTP status code for the error. Generally speaking, the following codes have these meanings: `200` - Success, `201` - Success (object created), `400` - Error with user input, `403` - Authorization error (user lacks permission), `404` - Object not found, `409` - Attempt to change an object using an obsolete last ModifiedDate. |

</details>

</details>

##### 403

Forbidden.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error entry within an error response. |
| `traceId` | string | No | A unique ID of the trace which the error occurred in. Makes it possible to locate involved services and find log messages from the time of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | A unique code used to identify the template form of the message in i18n tables (language independent). |
| `meta` | object | No | Additional metadata associated with an error. |
| `title` | string | No |  |
| `detail` | string | No | The message describing the error. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `statusCode` | integer | No | The HTTP status code for the error. Generally speaking, the following codes have these meanings: `200` - Success, `201` - Success (object created), `400` - Error with user input, `403` - Authorization error (user lacks permission), `404` - Object not found, `409` - Attempt to change an object using an obsolete last ModifiedDate. |

</details>

</details>

##### 404

Invalid selection Analytics Application ID or link ID supplied (see detailed error message).

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | A single error entry within an error response. |
| `traceId` | string | No | A unique ID of the trace which the error occurred in. Makes it possible to locate involved services and find log messages from the time of the error. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No | A unique code used to identify the template form of the message in i18n tables (language independent). |
| `meta` | object | No | Additional metadata associated with an error. |
| `title` | string | No |  |
| `detail` | string | No | The message describing the error. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `statusCode` | integer | No | The HTTP status code for the error. Generally speaking, the following codes have these meanings: `200` - Success, `201` - Success (object created), `400` - Error with user input, `403` - Authorization error (user lacks permission), `404` - Object not found, `409` - Attempt to change an object using an obsolete last ModifiedDate. |

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/analytics/odag-links/selection-app-link-usages` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/analytics/odag-links/selection-app-link-usages',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      linkList: ['string'],
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/analytics/odag-links/selection-app-link-usages yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/analytics/odag-links/selection-app-link-usages" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"linkList":["string"]}'
```

**Example Response:**

```json
[
  {
    "id": "string",
    "link": {
      "id": "string",
      "name": "ODAG Link name",
      "owner": {
        "id": "wcgIs6wGcDdyzep9QmyopWvNH1FJTOhh",
        "name": "string",
        "subject": "string",
        "tenantid": "string"
      },
      "status": "active",
      "bindings": [
        {
          "range": {
            "lowerBound": 42,
            "upperBound": 42
          },
          "formatting": {
            "quote": "'",
            "delimiter": ","
          },
          "numericOnly": false,
          "selectionStates": "string",
          "selectAppParamName": "string",
          "selectAppParamType": "Field",
          "templateAppVarName": "string"
        }
      ],
      "privileges": [
        "string"
      ],
      "properties": {
        "disable": [
          {
            "context": "string",
            "disable": true
          }
        ],
        "menuLabel": [
          {
            "label": "string",
            "context": "string"
          }
        ],
        "genAppName": [
          {
            "params": [
              "templateAppName"
            ],
            "context": "string",
            "formatString": "string"
          }
        ],
        "genAppLimit": [
          {
            "limit": 42,
            "context": "string"
          }
        ],
        "limitPolicy": [
          {
            "context": "string",
            "limitPolicy": "Restrict"
          }
        ],
        "rowEstRange": [
          {
            "context": "string",
            "lowBound": 42,
            "highBound": 42
          }
        ],
        "targetSheet": [
          {
            "context": "string",
            "sheetId": "string",
            "sheetName": "string"
          }
        ],
        "appOpenMethod": [
          {
            "context": "string",
            "openMethod": "Tab"
          }
        ],
        "appRetentionTime": [
          {
            "context": "string",
            "retentionTime": "string"
          }
        ],
        "overrideGenAppLimit": [
          {
            "context": "string",
            "overrideGenAppLimit": false
          }
        ]
      },
      "rowEstExpr": "string",
      "createdDate": "2025-11-11T13:45:30Z",
      "dynamicView": true,
      "templateApp": {
        "id": "string",
        "name": "appname"
      },
      "modifiedDate": "2025-11-11T13:45:30Z",
      "sourceLinkId": "string",
      "includeScript": false,
      "modifiedByUser": {
        "id": "wcgIs6wGcDdyzep9QmyopWvNH1FJTOhh",
        "name": "string",
        "subject": "string",
        "tenantid": "string"
      },
      "genAppAccessible": true,
      "templateAppChartObjects": [
        {}
      ]
    }
  }
]
```

---
