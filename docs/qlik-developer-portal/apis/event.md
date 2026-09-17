---
source: https://qlik.dev/apis/event/
last_updated: 2026-07-30T17:02:04Z
---

# Qlik Cloud system events

Qlik Cloud system events allow you to subscribe to events and react to changes in real time within your tenant.

> **Migration to a new event format:** Qlik Cloud webhooks will transition legacy event payloads to a new format based on the
> [CloudEvents 1.0.2 specification](https://cloudevents.io/).
>
> Starting on or after November 3, 2025, any event not already CloudEvents-compliant will be sent in a hybrid format
> that includes both legacy and CloudEvents attributes.
> Legacy fields will be deprecated and removed on or after October 6, 2026, as announced in the [changelog](https://qlik.dev/changelog/216-webhooks-legacy-fields-removal/).
>
> If you use webhooks, plan to update your integrations to rely on the CloudEvents attributes (`id`, `source`, `type`,
> `time`, and others) before October 6, 2026.
>
> For more information, see the [Qlik Cloud Webhooks: Migration to new event formats is coming](https://community.qlik.com/t5/Official-Support-Articles/Qlik-Cloud-Webhooks-Migration-to-new-event-formats-is-coming/ta-p/2528660)
> article on Qlik Community.

## Use cases

By using webhooks, the [Audits API](https://qlik.dev/apis/rest/audits), and [Qlik Automate](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/introduction/home-automation.htm),
you can respond instantly to events such as user actions, app changes, or data reloads.

Some use cases include:

- Slack notifications: notify your team whenever a new app is created in Qlik Cloud automatically.
- Welcome emails: send automated welcome emails when new users are added to your tenant.
- Automated updates: update records in an external system automatically when users are removed.

## Event delivery methods

System events can be consumed through two primary methods: webhooks and the [Audits API](https://qlik.dev/apis/rest/audits).

> **Format differences:** The event envelope differs depending on the delivery method (webhooks or Audits API).
> However, the payload contained in the `data` object remains consistent across both methods.
> This ensures that the business logic you build around event data is portable, regardless of how you receive the events.

## Authentication and security

### Secure webhook endpoints

To secure webhook endpoints:

- Use HTTPS: always host your webhook endpoint over HTTPS to encrypt data during transmission.
- Authenticate requests: implement authentication mechanisms to verify that requests are coming from Qlik Cloud.

### Verify webhook payload signature

Qlik Cloud signs webhook payloads using a secret key that you provide during webhook registration.
You should verify the signature to ensure that requests are coming from Qlik Cloud.
To verify webhook signatures:

1. Retrieve the signature from the `Qlik-Signature` header attached to the request.
2. Use your secret key and the request body to compute the HMAC SHA256 hash.
3. Compare the computed HMAC SHA256 hash with the signature from the `Qlik-Signature` header.

If the signatures match, proceed to process the event. If not, reject the request.

Qlik Cloud signs webhook payloads using a secret key that you provide during webhook registration.
You should verify the signature to ensure that requests are coming from Qlik Cloud.

For a detailed guide on how to verify webhook signatures in JavaScript, including code examples and best practices, see
[Verify webhook signatures using HMAC](https://qlik.dev/apis/event/verify-webhook-signatures-hmac/).

## Reference documentation

## Next steps

- [Create a webhook](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-webhooks.htm)
