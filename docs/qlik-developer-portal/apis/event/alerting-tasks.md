---
source: https://qlik.dev/apis/event/alerting-tasks/
last_updated: 2026-09-11T16:13:57Z
---

# Alerting tasks

Events emitted for data alerting task execution, including alert triggers and notifications.

## Table of Contents

### system-events.alerting

- [com.qlik.v1.alerting-task.created](#comqlikv1alerting-taskcreated)
- [com.qlik.v1.alerting-task.deleted](#comqlikv1alerting-taskdeleted)
- [com.qlik.v1.alerting-task.execution-summary.created](#comqlikv1alerting-taskexecution-summarycreated)
- [com.qlik.v1.alerting-task.recipient.removed](#comqlikv1alerting-taskrecipientremoved)
- [com.qlik.v1.alerting-task.task-status.changed](#comqlikv1alerting-tasktask-statuschanged)

## Events published on the `system-events.alerting` channel

### com.qlik.v1.alerting-task.created

**Title:** A data alert has been created

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a new data alert is created. Includes alert configuration, access type, recipients, and trigger settings. Use this to track alert creation and update external monitoring systems.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Unique identifier for the event type. This event indicates that data alert has been created. Metadata: default = "com.qlik.v1.alerting-task.created". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | The unique identifier for the user triggering the event. |
| `authtype` | `string` | No | The type of principal that triggered the occurrence. |
| `tenantid` | `string` | Yes | The unique identifier for the tenant related to the event. |
| `authclaims` | `string` | No | A JSON string representing claims of the principal that triggered the event. |
| `tracestate` | `string` | No | A comma-delimited list of key-value pairs. |
| `traceparent` | `string` | No | Contains a version, trace ID, span ID, and trace options. |
| `data` | `object` | No | Contains the event-specific attributes of the payload. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `alertID` | `string` | No | The identifier of the alert associated with the alerting task. |
| `creatorId` | `string` | No | The identifier of the user who created the alerting task. |
| `accessType` | `string` | No | The type of access associated with the alerting task. Allowed values: SOURCE_ACCESS \| TARGET_ACCESS. |
| `recipients` | `object` | No |  |
| `conditionId` | `string` | No | The identifier of the condition associated with the alerting task. |
| `description` | `string` | No | Description of the alert. |
| `triggerType` | `string` | No | The type of trigger associated with the alerting task. Allowed values: RELOAD \| SCHEDULED. |
| `recipientsCount` | `integer` | No | The number of recipients associated with the alerting task. |
| `alertingTaskStatus` | `string` | No | The status of the alerting task. |
| `alertingTaskEnabled` | `string` | No | Indicates whether the alerting task is enabled or not. |

<details>
<summary>Properties of `recipients`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userIds` | `string[]` | No | The list of user identifiers associated with the alerting task. |

</details>

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2025-01-15T10:43:17Z",
  "type": "com.qlik.v1.alerting-task.created",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "authtype": "User",
  "tenantid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "authclaims": "{\n  \"sub\": \"VZhiEfgW2bLd7HgR-jjzAh6VnicipweT\",\n  \"email\": \"user@example.com\",\n  \"roles\": [\"admin\", \"editor\"]\n}\n",
  "tracestate": "rojo=00f067aa0ba902b7,congo=t61rcWkgMzE",
  "traceparent": "00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01",
  "data": {
    "alertID": "string",
    "creatorId": "string",
    "accessType": "SOURCE_ACCESS",
    "recipients": {
      "userIds": [
        "string"
      ]
    },
    "conditionId": "string",
    "description": "string",
    "triggerType": "RELOAD",
    "recipientsCount": 42,
    "alertingTaskStatus": "string",
    "alertingTaskEnabled": "string"
  }
}
```


### com.qlik.v1.alerting-task.deleted

**Title:** A data alert has been deleted

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a data alert is deleted. Includes the alert identifier, causal action code, and affected recipients. Use this to clean up alert subscriptions and external alert registries.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | The unique identifier for the event type. Metadata: default = "com.qlik.v1.alerting-task.deleted". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | The unique identifier for the user triggering the event. |
| `authtype` | `string` | No | The type of principal that triggered the occurrence. |
| `tenantid` | `string` | Yes | The unique identifier for the tenant related to the event. |
| `authclaims` | `string` | No | A JSON string representing claims of the principal that triggered the event. |
| `tracestate` | `string` | No | A comma-delimited list of key-value pairs. |
| `traceparent` | `string` | No | Contains a version, trace ID, span ID, and trace options. |
| `data` | `object` | No | Contains the event-specific attributes of the payload. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `action` | `string` | No | Action that triggered the deletion. Allowed values: ADMIN_ACTION \| OWNER_ACTION \| APP_DELETED. |
| `alertId` | `string` | No | ID of the alert. |
| `appName` | `string` | No | Name of the app associated with the alerting task. |
| `ownerId` | `string` | No | ID of the owner of the alert. |
| `alertName` | `string` | No | Name of the alert. |
| `description` | `string` | No | Description of the alert. |
| `triggerType` | `string` | No | The type of trigger associated with the alerting task. Allowed values: RELOAD \| SCHEDULED. |
| `recipientIds` | `string[]` | No | IDs of the recipients of the alert. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2025-01-15T10:43:17Z",
  "type": "com.qlik.v1.alerting-task.deleted",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "authtype": "User",
  "tenantid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "authclaims": "{\n  \"sub\": \"VZhiEfgW2bLd7HgR-jjzAh6VnicipweT\",\n  \"email\": \"user@example.com\",\n  \"roles\": [\"admin\", \"editor\"]\n}\n",
  "tracestate": "rojo=00f067aa0ba902b7,congo=t61rcWkgMzE",
  "traceparent": "00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01",
  "data": {
    "action": "ADMIN_ACTION",
    "alertId": "64231b8989790dc11f0c88ee",
    "appName": "string",
    "ownerId": "DRCy6BXc0O4AXNcFVPW-IPsUpbWCgRct",
    "alertName": "test4_new_alert_target_access_2_recipients_manual_trigger",
    "description": "test4_new_alert_target_access_2_recipients_manual_trigger",
    "triggerType": "RELOAD",
    "recipientIds": [
      [
        "DRCy6BXc0O4AXNcFVPW-IPsUpbWCgRct",
        "2rQoqsyhuOH11bzP_tf8xD"
      ]
    ]
  }
}
```


### com.qlik.v1.alerting-task.execution-summary.created

**Title:** A data alert execution summary has been generated

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when an execution summary is generated for a data alert. Includes execution statistics (successful, failed, disabled recipients), overall status, and tracking information. Use this to monitor alert execution health.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | The unique identifier for the event type. Metadata: default = "com.qlik.v1.alerting-task.execution-summary.created". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | The unique identifier for the user triggering the event. |
| `authtype` | `string` | No | The type of principal that triggered the occurrence. |
| `tenantid` | `string` | Yes | The unique identifier for the tenant related to the event. |
| `authclaims` | `string` | No | A JSON string representing claims of the principal that triggered the event. |
| `tracestate` | `string` | No | A comma-delimited list of key-value pairs. |
| `traceparent` | `string` | No | Contains a version, trace ID, span ID, and trace options. |
| `data` | `object` | No | Contains the event-specific attributes of the payload. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `alertId` | `string` | No | The identifier of the alert that the execution summary pertains to. |
| `summary` | `object` | No | The execution summary data. |
| `tracking` | `object` | No | The tracking information for the event. |
| `alertName` | `string` | No | The name of the alert that the execution summary pertains to. |
| `description` | `string` | No | The description of the alert that the execution summary pertains to. |

<details>
<summary>Properties of `summary`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `alertId` | `string` | No | The identifier of the alert that the execution summary pertains to. |
| `ownerId` | `string` | No | The identifier of the owner of the alert. |
| `complete` | `boolean` | No | Whether the execution summary is complete. |
| `tenantId` | `string` | No | The identifier of the tenant that the alert belongs to. |
| `alertName` | `string` | No | The name of the alert that the execution summary pertains to. |
| `accessMode` | `string` | No | The access mode for the alert. Allowed values: SOURCE_ACCESS \| TARGET_ACCESS. |
| `workflowId` | `string` | No | The identifier of the workflow that the alert belongs to. |
| `totalRecipientCount` | `integer` | No | The total number of recipients for the alert. |
| `failedExecutionsCount` | `integer` | No | The number of failed executions for the alert. |
| `disabledRecipientsCount` | `integer` | No | The number of disabled recipients for the alert. |
| `successfulExecutionsCount` | `integer` | No | The number of successful executions for the alert. |
| `failedExecutionsRecipientsInfo` | `object[]` | No | Information about recipients for whom executions failed. |

</details>

<details>
<summary>Properties of `tracking`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `alertId` | `string` | No | The identifier of the alert that the execution summary pertains to. |
| `workflowId` | `string` | No | The identifier of the workflow that the execution summary pertains to. |

</details>

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2025-01-15T10:43:17Z",
  "type": "com.qlik.v1.alerting-task.execution-summary.created",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "authtype": "User",
  "tenantid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "authclaims": "{\n  \"sub\": \"VZhiEfgW2bLd7HgR-jjzAh6VnicipweT\",\n  \"email\": \"user@example.com\",\n  \"roles\": [\"admin\", \"editor\"]\n}\n",
  "tracestate": "rojo=00f067aa0ba902b7,congo=t61rcWkgMzE",
  "traceparent": "00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01",
  "data": {
    "alertId": "62c5b42f53c0b193281aa124",
    "summary": {
      "alertId": "62c5b42f53c0b193281aa124",
      "ownerId": "4--qu5MTAghrqvygydtHSWTSqBWIiBtG",
      "complete": true,
      "tenantId": "ActoyXI9-8Z7H9M8W_JBbVAQvsOmBnle",
      "alertName": "New Terminal Alarm",
      "accessMode": "SOURCE_ACCESS",
      "workflowId": "24db23a7-6a2e-4a5f-8ee3-32fa1935f4f3",
      "totalRecipientCount": 1,
      "failedExecutionsCount": 0,
      "disabledRecipientsCount": 0,
      "successfulExecutionsCount": 1,
      "failedExecutionsRecipientsInfo": [
        {}
      ]
    },
    "tracking": {
      "alertId": "62c5b42f53c0b193281aa124",
      "workflowId": "62c5b42f53c0b193281aa124"
    },
    "alertName": "New Terminal Alarm",
    "description": "string"
  }
}
```


### com.qlik.v1.alerting-task.recipient.removed

**Title:** A data alert has been modified by removing a recipient

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when a recipient is removed from a data alert. Includes the alert identifier, removed recipient, and alert metadata. Use this to revoke alert access.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | The unique identifier for the event type. Metadata: default = "com.qlik.v1.alerting-task.recipient.removed". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | The unique identifier for the user triggering the event. |
| `authtype` | `string` | No | The type of principal that triggered the occurrence. |
| `tenantid` | `string` | Yes | The unique identifier for the tenant related to the event. |
| `authclaims` | `string` | No | A JSON string representing claims of the principal that triggered the event. |
| `tracestate` | `string` | No | A comma-delimited list of key-value pairs. |
| `traceparent` | `string` | No | Contains a version, trace ID, span ID, and trace options. |
| `data` | `object` | No | Contains the event-specific attributes of the payload. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `alertId` | `string` | No | The identifier of the alert the recipient was removed from. |
| `ownerId` | `string` | No | The identifier of the user who owns the alert. |
| `alertName` | `string` | No | The name of the alert the recipient was removed from. |
| `description` | `string` | No | A description of the alert. |
| `recipientId` | `string` | No | The identifier of the recipient that was removed. |

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2025-01-15T10:43:17Z",
  "type": "com.qlik.v1.alerting-task.recipient.removed",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "authtype": "User",
  "tenantid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "authclaims": "{\n  \"sub\": \"VZhiEfgW2bLd7HgR-jjzAh6VnicipweT\",\n  \"email\": \"user@example.com\",\n  \"roles\": [\"admin\", \"editor\"]\n}\n",
  "tracestate": "rojo=00f067aa0ba902b7,congo=t61rcWkgMzE",
  "traceparent": "00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01",
  "data": {
    "alertId": "64233273697940223c2f6993",
    "ownerId": "640239c20ae3db3eb09ffd55",
    "alertName": "test1_new_alert_source_access_2_recipients_manual_trigger",
    "description": "test1_new_alert_source_access_2_recipients_manual_trigger",
    "recipientId": "640239de63f7bc79e4f05915"
  }
}
```


### com.qlik.v1.alerting-task.task-status.changed

**Title:** A data alert status has been modified

**Action:** `send`

**Visibility:** `public`

**Stability:** `stable`

Published when the operational status of a data alert changes (for example, enabled/disabled, error state). Includes the alert, current state, previous state, and cause of the change. Use this to track alert health and implement status-driven workflows.

**Payload**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | The unique identifier for the event type. Metadata: default = "com.qlik.v1.alerting-task.task-status.changed". |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |
| `userid` | `string` | No | The unique identifier for the user triggering the event. |
| `authtype` | `string` | No | The type of principal that triggered the occurrence. |
| `tenantid` | `string` | Yes | The unique identifier for the tenant related to the event. |
| `authclaims` | `string` | No | A JSON string representing claims of the principal that triggered the event. |
| `tracestate` | `string` | No | A comma-delimited list of key-value pairs. |
| `traceparent` | `string` | No | Contains a version, trace ID, span ID, and trace options. |
| `data` | `object` | No | Contains the event-specific attributes of the payload. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cause` | `string` | No | The cause of the alerting task status change. |
| `alertId` | `string` | No | The identifier of the alert that the event pertains to. |
| `oldTask` | `object` | No | The previous state of the alerting task. |
| `ownerId` | `string` | No | The identifier of the owner of the alerting task. |
| `tenantId` | `string` | No | The identifier of the tenant of the alerting task. |
| `alertName` | `string` | No | The name of the alert that the event pertains to. |
| `currentTask` | `object` | No | The current state of the alerting task. |
| `description` | `string` | No | The description of the alerting task. |

<details>
<summary>Properties of `oldTask`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `recipients` | `object[]` | No |  |
| `enabledByUser` | `boolean` | No | Indicates whether the alerting task was enabled by a user. |
| `enabledBySystem` | `boolean` | No | Indicates whether the alerting task was enabled by the system. |
| `alertingTaskErrors` | `object[]` | No | An array of error objects for the alerting task. |

<details>
<summary>Properties of `recipients`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `alertingTaskErrors`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `currentTask`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `recipients` | `object[]` | No |  |
| `enabledByUser` | `boolean` | No | Indicates whether the alerting task was enabled by a user. |
| `enabledBySystem` | `boolean` | No | Indicates whether the alerting task was enabled by the system. |
| `alertingTaskErrors` | `object[]` | No | An array of error objects for the alerting task. |

<details>
<summary>Properties of `recipients`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `alertingTaskErrors`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>


**Example**

```json
{
  "id": "A234-1234-1234",
  "time": "2025-01-15T10:43:17Z",
  "type": "com.qlik.v1.alerting-task.task-status.changed",
  "source": "com.qlik/my-service",
  "specversion": "1.0",
  "datacontenttype": "application/json",
  "userid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "authtype": "User",
  "tenantid": "VZhiEfgW2bLd7HgR-jjzAh6VnicipweT",
  "authclaims": "{\n  \"sub\": \"VZhiEfgW2bLd7HgR-jjzAh6VnicipweT\",\n  \"email\": \"user@example.com\",\n  \"roles\": [\"admin\", \"editor\"]\n}\n",
  "tracestate": "rojo=00f067aa0ba902b7,congo=t61rcWkgMzE",
  "traceparent": "00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01",
  "data": {
    "cause": "string",
    "alertId": "string",
    "oldTask": {
      "recipients": [
        {
          "userId": "string",
          "subscribed": true,
          "enabledByUser": true,
          "enabledBySystem": true,
          "alertingTaskRecipientErrors": [
            {
              "value": "USER_IS_DELETED"
            }
          ]
        }
      ],
      "enabledByUser": true,
      "enabledBySystem": true,
      "alertingTaskErrors": [
        {
          "value": "OWNER_DISABLED"
        }
      ]
    },
    "ownerId": "string",
    "tenantId": "string",
    "alertName": "string",
    "currentTask": {
      "recipients": [
        {
          "userId": "string",
          "subscribed": true,
          "enabledByUser": true,
          "enabledBySystem": true,
          "alertingTaskRecipientErrors": [
            {
              "value": "USER_IS_DELETED"
            }
          ]
        }
      ],
      "enabledByUser": true,
      "enabledBySystem": true,
      "alertingTaskErrors": [
        {
          "value": "OWNER_DISABLED"
        }
      ]
    },
    "description": "string"
  }
}
```


## Schemas

### cloudEventsContextAttributes

CloudEvents Specification JSON Schema.

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifies the event. Metadata: minLength = 1. |
| `time` | `string` | No | Timestamp of when the occurrence happened. Must adhere to RFC 3339. Metadata: minLength = 1, format = "date-time". |
| `type` | `string` | Yes | Describes the type of event related to the originating occurrence. Metadata: minLength = 1. |
| `source` | `string` | Yes | Identifies the context in which an event happened. Metadata: minLength = 1, format = "uri-reference". |
| `specversion` | `string` | Yes | The version of the CloudEvents specification which the event uses. Metadata: minLength = 1. |
| `datacontenttype` | `string` | No | Content type of the data value. Must adhere to RFC 2046 format. Metadata: minLength = 1. |



### cloudEventsQlikExtensionsAttributes

**Type:** `object`

**Properties**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userid` | `string` | No | The unique identifier for the user triggering the event. |
| `authtype` | `string` | No | The type of principal that triggered the occurrence. |
| `tenantid` | `string` | Yes | The unique identifier for the tenant related to the event. |
| `authclaims` | `string` | No | A JSON string representing claims of the principal that triggered the event. |
| `tracestate` | `string` | No | A comma-delimited list of key-value pairs. |
| `traceparent` | `string` | No | Contains a version, trace ID, span ID, and trace options. |


