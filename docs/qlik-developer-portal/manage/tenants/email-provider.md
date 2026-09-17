---
source: https://qlik.dev/manage/tenants/email-provider/
last_updated: 2026-04-20T13:34:03+01:00
---

# Configure tenant email provider

In this tutorial, you are going to learn how to configure a tenant to send
emails with your SMTP email provider using Qlik Cloud management APIs.

The Transport API is the service responsible for managing notification channels
and email configurations for the sending of system notifications,
as well as updates from analytics services in the hub, such as data alerts
and subscriptions.

These notifications provide users with information about events such as failed
reloads, users being added to spaces, data alerts being triggered, and regular
subscription snapshots being sent to subscribers. Note that workflows running
in Qlik Automate (including the report blocks) will use their own
SMTP/email configuration. Only system notifications from Automate
will be sent via the Transport API.

For a description of all endpoints, refer to the [Transports API reference](https://qlik.dev/apis/rest/transports).

## Prerequisites

- You have a basic understanding of Qlik Cloud and its access control rules for
  creating content and managing spaces.
- You have installed cURL to run the inline examples.
- You have configured an SMTP email server or provider, such as:
  - [AWS SES](https://community.qlik.com/t5/Official-Support-Articles/Use-AWS-SES-Simple-Email-Service-as-the-email-provider-for-Qlik/ta-p/2135458)
  - [Mailchimp](https://community.qlik.com/t5/Official-Support-Articles/How-to-use-Mailchimp-bulk-email-service-SMTP-with-Qlik-Cloud/ta-p/2063035)
  - [Sendgrid](https://community.qlik.com/t5/Official-Support-Articles/How-to-use-Sendgrid-bulk-email-service-SMTP-with-Qlik-Cloud/ta-p/2001715)

> **Note:** The cURL examples in this topic show the command syntax for Windows Command Prompt.
> If you are using another command line interface, different syntax may be required for line continuation.
> You may also need to adjust the number and type of quotes surrounding the parameters and their values.

## Variable substitution

Throughout this tutorial, variables will be used to communicate value placement.
The variable substitution format is `<VARIABLE_NAME>`. Here is a list of
variables referred to in this tutorial.

| Variable         | Description                                                                                                                                   |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `<TENANT>`       | The URL for the tenant where you are managing groups. Equivalent to `tenanthostname.region.qlikcloud.com`.                                    |
| `<ACCESS_TOKEN>` | A bearer token for authorizing `https` requests to the `<TENANT>`. For more information, see [Authentication](https://qlik.dev/authenticate). |

## Configure a new email provider

To configure an email provider, patch the tenant. This example is for AWS SES,
where there is a separate username and email address:

```bash
curl -L -X PATCH "https://<TENANT>/api/v1/transports/email-config" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json" ^
-d "[
    {
        \"op\": \"replace\",
        \"path\": \"/serverAddress\",
        \"value\": \"email-smtp.eu-west-2.amazonaws.com\"
    },
    {
        \"op\": \"replace\",
        \"path\": \"/serverPort\",
        \"value\": 2465
    },
    {
        \"op\": \"replace\",
        \"path\": \"/securityType\",
        \"value\": \"SSL/TLS\"
    },
    {
        \"op\": \"replace\",
        \"path\": \"/username\",
        \"value\": \"SKIARX3IRHQ7J3ZLGABC\"
    },
    {
        \"op\": \"replace\",
        \"path\": \"/emailAddress\",
        \"value\": \"qlik@mydomain.com\"
    },
    {
        \"op\": \"replace\",
        \"path\": \"/emailPassword\",
        \"value\": \"YourPasswordHere\"
    }
]"
```

If successful, returns a `204` response with the email provider configuration:

```json
{
    "_id": "64c03b868a37cb93b4529c89",
    "serverAddress": "email-smtp.eu-west-2.amazonaws.com",
    "serverPort": 2465,
    "securityType": "SSL/TLS",
    "emailAddress": "qlik@mydomain.com",
    "modificationTime": "2023-07-25T21:16:38.271Z",
    "tenantId": "BL4tTJ4S7xrHTcq0zQxQrJ5qB1_Q6cSo",
    "isValid": true,
    "authFailures": 0,
    "status": {
        "statusCode": 0,
        "statusReason": "OK"
    },
    "username": "SKIARX3IRHQ7J3ZLGABC",
    "passwordExists": true
}
```

## Retrieve the current email configuration

To retrieve the current email configuration for the tenant:

```bash
curl -L "https://<TENANT>/api/v1/transports/email-config" ^
-H "Authorization: Bearer <ACCESS_TOKEN>"
```

If successful, returns a `200` status, with an example response for AWS
SES:

```json
{
    "_id": "64c03b868a37cb93b4529c89",
    "serverAddress": "email-smtp.eu-west-2.amazonaws.com",
    "serverPort": 2465,
    "securityType": "SSL/TLS",
    "emailAddress": "qlik@mydomain.com",
    "modificationTime": "2023-07-25T21:16:38.271Z",
    "tenantId": "BL4tTJ4S7xrHTcq0zQxQrJ5qB1_Q6cSo",
    "isValid": true,
    "authFailures": 0,
    "status": {
        "statusCode": 0,
        "statusReason": "OK"
    },
    "username": "SKIARX3IRHQ7J3ZLGABC",
    "passwordExists": true
}
```

## Send a test email

To send a test email through the configured provider to verify the service is
working correctly:

```bash
curl -L "https://<TENANT>/api/v1/transports/email-config/actions/send-test-email" ^
-H "Authorization: Bearer <ACCESS_TOKEN>" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json" ^
-d "{
  \"body\": \"This is a test email sent from my tenant.\",
  \"subject\": \"Qlik Cloud Test Email\",
  \"recipient\": \"test@example.com\"
}"
```

If successful, returns a `200` status and the following payload:

```json
{
    "connectionFailed": false,
    "message": "Email sent",
    "smtpResponseCode": 250,
    "accepted": [
        "test@example.com"
    ],
    "rejected": [],
    "success": true
}
```
