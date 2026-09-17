---
source: https://qlik.dev/manage/automate/identity-provider-create/
last_updated: 2026-01-19T14:21:00Z
---

# Create identity providers

## Example creation requests

These examples illustrate how to create identity providers. For more information,
see the [Identity providers API reference](https://qlik.dev/apis/rest/identity-providers/)
or [Identity providers in Qlik Cloud](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-create-idp-configuration.htm)
on Qlik Help.

> **Note:** You will need to update the examples on this page to match your identity provider configuration, in particular, the
> fields you intend to map into claims.

### JWT

<details>
  <summary>JWT IdP</summary>

  Create a JWT IdP. Note that the `pem` must be on a single line without any line breaks
  (the displayed example has been shortened).

  For information on how to do this manually,
  review the [Create Signed Tokens for JWT Authorization tutorial](/authenticate/jwt/create-signed-tokens-for-jwt-authorization/).

  ```bash
  curl -L "https://mytenant.eu.qlikcloud.com/api/v1/identity-providers" ^
  -H "Content-Type: application/json" ^
  -H "Authorization: Bearer <ACCESS_TOKEN>" ^
  -d "{
      \"tenantIds\": [
          \"BL4tTJ4S7xrHTcq0zQxQrJ5qB1_Q6cSo\"
      ],
      \"provider\": \"external\",
      \"protocol\": \"jwtAuth\",
      \"interactive\": false,
      \"active\": true,
      \"description\": \"Auth for my web app\",
      \"options\": {
          \"jwtLoginEnabled\": true,
          \"issuer\": \"myorganization.com\",
          \"staticKeys\": [
              {
                  \"pem\": \"-----BEGIN CERTIFICATE-----MIIFwzCCA6ugAwIBAgIUY2166Gzw/yzoXgTTXogqjWeWsCUwDQYJKoZIhvcNAQELBQAwcTELMAkGA1UEBhMCR0IxDzANBgNVBAgMBkxvbmRvbjEPMA0GA1UEBwwGTG9uZG9uMQ0wCwYDVQQKDARRbGlrMQ0wCwYDVQQLDARRbGlrMQ0wCwYDVQQDDARRbGlrMRMwEQYJKoZIhvcNAQkBFgRRbGlrMB4XDTIyMDUxODEzMzMx-----END CERTIFICATE-----\",
                  \"kid\": \"myorganization20240205\"
              }
          ]
      }
  }"
  ```

  To create this using the `Create JWT Identity Provider` block in the Qlik Platform
  Operations connector in Qlik Automate, copy and paste this code into a workspace
  to add the block:

  ```json
  {"blocks":[{"id":"4D668B90-65CD-46C6-9DE5-047B597CBAAF","type":"EndpointBlock","disabled":false,"name":"CreateJWTIdentityProvider","displayName":"Qlik Platform Operations - Create JWT Identity Provider","comment":"","childId":null,"inputs":[{"id":"a4444590-1fb9-11ed-bd30-956b614a1313","value":"mytenant.eu.qlikcloud.com","type":"string","structure":{}},{"id":"b6137520-1fbd-11ed-b178-73e57788c51f","value":"-----BEGIN CERTIFICATE-----MIIFwzCCA6ugAwIBAgIUY2166Gzw/yzoXgTTXogqjWeWsCUwDQYJKoZIhvcNAQELBQAwcTELMAkGA1UEBhMCR0IxDzANBgNVBAgMBkxvbmRvbjEPMA0GA1UEBwwGTG9uZG9uMQ0wCwYDVQQKDARRbGlrMQ0wCwYDVQQLDARRbGlrMQ0wCwYDVQQDDARRbGlrMRMwEQYJKoZIhvcNAQkBFgRRbGlrMB4XDTIyMDUxODEzMzMx-----END CERTIFICATE-----","type":"longtext","structure":{}},{"id":"be815d80-1fbd-11ed-8b5f-7dd058ec3767","value":"myorganization20240205","type":"string","structure":{}},{"id":"5d63fa10-1fbe-11ed-9033-5f8daf6b2b4e","value":"myorganization.com","type":"string","structure":{}},{"id":"38f81ad0-9cc0-11ed-a6c7-89c189cfbe31","value":"Auth for my web app","type":"string","structure":{}},{"id":"443172a0-9cc0-11ed-b12b-755bd4ec9f2f","value":null,"type":"string","structure":{}}],"settings":[{"id":"datasource","value":"cccc14a0-d233-11ed-b0d0-33e7e8bc635b","type":"select","structure":{}},{"id":"blendr_on_error","value":"stop","type":"select","structure":{}},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":{}}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":-753,"y":100,"datasourcetype_guid":"c7e48240-e0f2-11ec-ada1-d5ef75014b77","endpoint_guid":"a42eaaf0-1fb9-11ed-91f8-355a98a8e3f6","endpoint_role":"create"}],"variables":[]}
  ```
</details>

### OIDC

<details>
  <summary>Microsoft Entra ID (Azure AD - non-SCIM)</summary>

  Creates an interactive OIDC IdP for Microsoft Entra ID (Azure AD). Ensure that the mapped claims match
  the desired values from your IdP.

  For information on how to do this manually,
  review [How To: Configure Qlik Sense Enterprise SaaS to use Azure AD as an IdP](https://community.qlik.com/t5/Official-Support-Articles/How-To-Configure-Qlik-Sense-Enterprise-SaaS-to-use-Azure-AD-as/ta-p/1704442).

  ```bash
  curl -L "https://mytenant.eu.qlikcloud.com/api/v1/identity-providers" ^
  -H "Content-Type: application/json" ^
  -H "Authorization: Bearer <ACCESS_TOKEN>" ^
  -H "Accept: application/json" ^
  -d "{
      \"tenantIds\": [
          \"BL4tTJ4S7xrHTcq0zQxQrJ5qB1_Q6cSo\"
      ],
      \"provider\": \"azureAD\",
      \"protocol\": \"OIDC\",
      \"interactive\": true,
      \"options\": {
          \"discoveryUrl\": \"https://login.microsoftonline.com/c21eeb5f-f5a6-44e8-a997-123f2f7a123c/v2.0/.well-known/openid-configuration\",
          \"clientId\": \"76d2ce8f-630b-4e5a-904b-a0d6a53aabc2\",
          \"clientSecret\": \"thisisyourappregistrationsecret\",
          \"realm\": \"mydomain\",
          \"claimsMapping\": {
              \"client_id\": [
                  \"client_id\"
              ],
              \"email\": [
                  \"email\"
              ],
              \"groups\": [
                  \"groups\"
              ],
              \"name\": [
                  \"name\"
              ],
              \"picture\": [
                  \"picture\"
              ],
              \"sub\": [
                  \"sub\"
              ]
          },
          \"emailVerifiedAlwaysTrue\": true,
          \"useClaimsFromIdToken\": true,
          \"blockOfflineAccessScope\": false
      },
      \"description\": \"Azure AD deployed via API call\",
      \"skipVerify\": true
  }"
  ```

  To create this using the `Create OIDC Identity Provider` block in the Qlik Platform
  Operations connector in Qlik Automate, copy and paste this code into a workspace
  to add the block:

  ```json
  {"blocks":[{"id":"2E0FA0FC-3E53-4FE2-8E8F-0D12C937AA19","type":"EndpointBlock","disabled":false,"name":"CreateInteractiveIdentityProvider","displayName":"Qlik Platform Operations - Create Interactive Identity Provider","comment":"","childId":"4D668B90-65CD-46C6-9DE5-047B597CBAAF","inputs":[{"id":"73f441c0-1fc2-11ed-8591-5f09098e0d84","value":"mytenant.eu.qlikcloud.com","type":"string","structure":{}},{"id":"1f5641f0-1fc6-11ed-95e1-e5b91a91e8d9","value":"azureAD","type":"string","structure":{}},{"id":"74262860-1fc2-11ed-b3a2-f38dfe17f29d","value":"https://login.microsoftonline.com/c21eeb5f-f5a6-44e8-a997-123f2f7a123c/v2.0/.well-known/openid-configuration","type":"string","structure":{}},{"id":"7813e6a0-1fc6-11ed-850f-fbd8bf087080","value":"76d2ce8f-630b-4e5a-904b-a0d6a53aabc2","type":"string","structure":{}},{"id":"83dbdca0-1fc6-11ed-b7e9-cf844ebe61cf","value":"thisisyourappregistrationsecret","type":"string","structure":{}},{"id":"30836510-1fc6-11ed-a560-9174ff134e41","value":"Azure AD deployed via API call","type":"string","structure":{}},{"id":"42699cb0-1fc6-11ed-b630-3f767948dcd6","value":"4854c0e0-1fc6-11ed-b910-1d264b935638","type":"select","displayValue":"true","structure":{}},{"id":"a6e4a3c0-1fc6-11ed-97ec-f5a6e3101608","value":"mydomain","type":"string","structure":{}},{"id":"fd76d6e0-1fcb-11ed-b7a0-793303a38143","value":"05214ae0-1fcc-11ed-94db-e5bdf7818efc","type":"select","displayValue":"true","structure":{}}],"settings":[{"id":"datasource","value":"cccc14a0-d233-11ed-b0d0-33e7e8bc635b","type":"select","structure":{}},{"id":"blendr_on_error","value":"stop","type":"select","structure":{}},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":{}}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":-349,"y":153,"datasourcetype_guid":"c7e48240-e0f2-11ec-ada1-d5ef75014b77","endpoint_guid":"73d15050-1fc2-11ed-8977-a90e9b97955a","endpoint_role":"create"}],"variables":[]}
  ```

  Note that if you intend to customize the claim mappings in Qlik Automate,
  you need to use the `Raw API Request` block.
</details>
