# Notifications

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Notifications is the resource representing the various notifications that notification-prep can render

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/notifications`](#get-apiv1notifications) |  |

## API Reference

### GET /api/v1/notifications

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `locale` | string | No | If present, idenfies the language of the returned 'friendlyName' property. |
| `manageableInHub` | string | No | If present, represents the 'manageableInHub' value to filter by. Enum: true, false |
| `subscribable` | string | No | If present, represents the 'subscribable' value to filter by. Enum: true, false |

#### Responses

##### 200

Request completed successfully. See Results for ResultDetail on each notification.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `notifications` | object[] | Yes | list of notifications |

<details>
<summary>Properties of `notifications`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `transports` | string[] | Yes | Type of Transport e.g. Email, Notification, Slack message etc... |
| `isSubscribable` | boolean | Yes | Indicates if the notification can be subscribed to by users.  If true, the object will also contain 'subscriptionInfo' object |
| `presentationInfo` | object | No | Object containing information pertaining to the presentaion of a notification in the UI |
| `subscriptionInfo` | object | No | Object indicating what properties to use to subscribe to this notification via the 'Subscriptions' service.  For info about its properties, refer to the Subscription sevice's API doc. |
| `isManageableInHub` | boolean | No | Indicates if the notification can be managed in the hub. If true, the object will also contain 'subscriptionInfo' object and a 'presentationInfo' object with a non-empty scopes array. |
| `notificationNamePattern` | string | Yes | Notification name pattern that will trigger this notification e.g resource.action |

<details>
<summary>Properties of `presentationInfo`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `scopes` | string[] | No | Information about the scopes to which this notification applies.  Helps determine the placement of the notification in the UI |
| `friendlyName` | string | No | Localized, human-readable string representing the name of the notification suitable to use in a UI |
| `scopeFriendlyNames` | object | No | Friendly name to be displayed for each scope. |

</details>

<details>
<summary>Properties of `subscriptionInfo`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `action` | string | Yes |  |
| `target` | string | No |  |
| `resourceId` | string | No |  |
| `resourceType` | string | Yes |  |
| `resourceSubType` | string | No |  |

</details>

</details>

##### default

Request error. See Errors.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The error code. |
| `title` | string | Yes | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/notifications` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/notifications',
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
# qlik-cli has not implemented support for GET /api/v1/notifications yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/notifications" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "notifications": [
    {
      "transports": [
        "string"
      ],
      "isSubscribable": true,
      "presentationInfo": {
        "scopes": [
          "string"
        ],
        "friendlyName": "string",
        "scopeFriendlyNames": {}
      },
      "subscriptionInfo": {
        "action": "string",
        "target": "string",
        "resourceId": "string",
        "resourceType": "string",
        "resourceSubType": "string"
      },
      "isManageableInHub": true,
      "notificationNamePattern": "string"
    }
  ]
}
```

---
