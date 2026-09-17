---
source: https://qlik.dev/apis/event/verify-webhook-signatures-hmac/
last_updated: 2026-01-05T10:08:57Z
---

# Verify webhook signatures using HMAC

## Overview

Qlik Cloud webhooks allow you to subscribe to events and react to changes from your tenant in real time
in your own applications and tooling.
To ensure that webhook payloads are authentic and have not been tampered with, Qlik Cloud signs each webhook request
using HMAC (Hash-based Message Authentication Code).

This tutorial explains what HMAC is, when to use it, and how to verify webhook signatures in JavaScript.

## Prerequisites

Before you begin, ensure you have:

- A webhook registered in Qlik Cloud with a configured secret key
- Your secret key stored securely in an environment variable or secrets management system
- For detailed webhook setup instructions, see [Create and manage webhooks](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-webhooks.htm)
  on Qlik Help

## What is HMAC?

HMAC is a cryptographic technique that combines a secret key with a message to produce a unique fingerprint (digest).
This fingerprint serves as proof that:

- **The message is authentic**. The webhook came from Qlik Cloud, not an imposter
- **The message is unmodified**. The payload has not been altered during transmission

HMAC works by:

- Taking your secret key and the webhook payload
- Applying a hash algorithm (SHA256 in Qlik Cloud's case)
- Producing a unique signature that only someone with the secret key can generate

Even if someone has access to the webhook URL and payload, they cannot forge a valid signature without knowing the
secret key.

## When to use HMAC verification

You should always verify webhook signatures in production environments because:

- Unauthenticated endpoints are vulnerable: Without verification, anyone who knows your webhook URL can send malicious
  payloads
- Man-in-the-middle attacks: Network interception could modify the payload, and signature verification would catch this
- Compliance requirements: Many security frameworks and compliance standards require payload verification

HMAC verification is a critical security control for any system accepting webhooks.

## How to verify HMAC in JavaScript

When Qlik Cloud sends a webhook to your endpoint, it includes a signature in the `Qlik-Signature` header.

Follow these steps to verify the signature.

### Step 1: Set up your webhook with a secret key

When registering a webhook in Qlik Cloud, you provide a secret key.
This same key is used to verify incoming payloads.
Keep this secret key secure and never expose it publicly.

### Step 2: Extract the signature and payload

For each webhook request received, extract:

- The `Qlik-Signature` header value (the signature sent by Qlik Cloud)
- The request body (the webhook payload)

### Step 3: Compute the HMAC

Using Node.js crypto library, compute the HMAC-SHA256 digest of the payload with your secret key:

```javascript
import crypto from "crypto";

// Extract the signature from the header
const header = req.headers['qlik-signature'];

// Use the raw body preserved by middleware
const payload = req.rawBody || Buffer.from(JSON.stringify(req.body));

// Create an HMAC using SHA256 algorithm and your secret key from environment
const hmac = crypto.createHmac('sha256', SECRET_KEY);

// Update the HMAC with the payload
hmac.update(payload);

// Get the digest in hex format (Qlik Cloud sends signatures as hex-encoded)
const computedSignature = hmac.digest('hex');
```

### Step 4: Compare signatures

Compare the computed signature with the one from the header. If they match, the payload is authentic and unmodified:

```javascript
const isValid = (header === computedSignature);

if (isValid) {
  console.log('✓ Webhook signature is valid. Payload is authentic.');
  // Process the webhook event
  return res.status(200).json({ success: true, verified: true });
} else {
  console.log('✗ Webhook signature is invalid. Payload may have been tampered with.');
  // Reject the request
  return res.status(401).json({ error: 'Invalid signature', verified: false });
}
```

<details>
  <summary>
    ## Complete Express.js example
  </summary>

  First, create a `.env` file in your project root with your secret key:

  ```text
  QLIK_WEBHOOK_SECRET=your-webhook-secret-key
  ```

  <Aside type="note">
  The following code uses `dotenv.config()` to automatically load environment variables from your `.env` file.
  This keeps sensitive credentials out of your source code.
  </Aside>

  Then, create your webhook receiver:

  ```javascript
  import express from 'express';
  import crypto from 'crypto';
  import dotenv from 'dotenv';

  dotenv.config();

  const app = express();
  // Load the webhook secret from the .env file
  const SECRET_KEY = process.env.QLIK_WEBHOOK_SECRET;

  // Keep the raw body for HMAC computation
  app.use(express.raw({ type: 'application/json' }));

  // Parse JSON after HMAC verification
  app.use((req, res, next) => {
    if (req.body instanceof Buffer) {
      req.rawBody = req.body;
      req.body = JSON.parse(req.body.toString('utf-8'));
    }
    next();
  });

  app.post('/webhook', (req, res) => {
    const header = req.headers['qlik-signature'];
    const payload = req.rawBody || Buffer.from(JSON.stringify(req.body));

    // Validate header exists
    if (!header || !payload) {
      return res.status(400).json({ error: 'Missing signature or payload' });
    }

    // Create HMAC-SHA256
    const hmac = crypto.createHmac('sha256', SECRET_KEY);
    hmac.update(payload);
    const computedSignature = hmac.digest('hex');

    // Verify signatures match
    const isValid = (header === computedSignature);

    if (isValid) {
      console.log('✓ Webhook signature is valid. Payload is authentic.');
      console.log(`Event type: ${req.body.type}`);
      // Process the webhook event
      return res.status(200).json({ success: true, verified: true });
    } else {
      console.log('✗ Webhook signature is invalid. Payload may have been tampered with.');
      return res.status(401).json({ error: 'Invalid signature', verified: false });
    }
  });

  app.listen(3000, () => {
    console.log('Webhook receiver listening on port 3000');
  });
  ```

</details>

## Key considerations

When it comes to secret key management, keep these best practices in mind:

- **Never hardcode secrets**: Store your secret key in environment variables, secrets management systems, or
  configuration files that are not checked into version control
- **Keep secrets private**: Never share or expose your secret key publicly
- **Rotate periodically**: Consider rotating your secret key periodically for enhanced security

When handling payloads for HMAC computation, consider the following:

- **Use raw payload**: Always compute the HMAC using the raw request body, not a parsed JSON object
- **Consistent encoding**: Ensure the payload is encoded as UTF-8 before hashing
- **Buffer handling**: Convert the payload to a Buffer to ensure consistent binary handling across different
  environments

When dealing with the `Qlik-Signature` header that contains the hex-encoded HMAC-SHA256 digest, make sure to:

- Extract the entire header value as-is
- Compare it directly with your computed hex-encoded signature
- Perform a constant-time comparison (optional but recommended) to prevent timing attacks

## Next steps

- Review the [Qlik Cloud webhooks documentation](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-webhooks.htm)
  for webhook management
- Learn about [Qlik Cloud system events](https://qlik.dev/apis/event/) and available event types
- Explore [Qlik Automate](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/introduction/home-automation.htm)
  for low-code event automation
