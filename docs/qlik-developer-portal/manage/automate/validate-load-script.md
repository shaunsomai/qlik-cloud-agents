---
source: https://qlik.dev/manage/automate/validate-load-script/
last_updated: 2026-01-19T14:21:00Z
---

# Validate Analytics application load scripts using Apps API

Validate script provides programmatic integrations with a way to validate Qlik Analytics
application load scripts without needing to load that script into an application or run a trial reload.
This allows developers to add simple validation to their deployments to reduce
deployment risk and catch transposition errors.

This feature helps to improve the quality of programmatic deployments by
verifying load script rewrites before they are updated in applications, and reducing
reload failures caused by script issues.

You can validate load scripts using the Apps API by sending a POST request to the `/v1/apps/validatescript`
endpoint with the load script you wish to validate in the payload.

## Benefits

- Early error and warning detection: Catch syntax errors before script execution.
- Streamlined debugging: Simplify the debugging process by identifying issues upfront.

## Examples

Here are some example validation results returned by the endpoint.

### Unexpected token error

```json
{
    "script": "SET Thousand Sep=',';",
  }
```

Will return the error:

```json
"errors" [
  {
    "msg": "Unexpected token: 'Sep', expected: '='",
    "Info": "",
    "Column": 0,
    "line": 0,
    "ch": 0
  }
],
"Warnings": []
```

### Unknown statement error

```json
  {
    "script": "tke val",
  }
```

Will return the error:

```json
"errors" [
  {
    "msg": "Unknown statement: tke val",
    "Info": "",
    "Column": 0,
    "line": 0,
    "ch": 0
  }
],
"Warnings": []
```

The validator also introduces warnings, a new concept in the engine and so far
only one warning is implemented. Warnings indicate potential issues in the script
that do not prevent it from running but may lead to unexpected behavior.

### Warning: Missing 'Then' keyword

```json
{
    "script": "if $(a) >= 0",
  }
```

Will return the warning:

```json
"errors" [],
"Warnings": [
  {
    "msg": "Missing the 'Then' keyword at the end of the if statement.",
    "Info": "Script will work anyway.",
    "Column": 0,
    "line": 0,
    "ch": 0
  }
]
```

For more information, see the [Apps API reference](https://qlik.dev/apis/rest/apps/).
