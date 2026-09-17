---
source: https://qlik.dev/extend/extensions/extension-api/build-extension/qvalueexpression/
last_updated: 2026-06-29T09:07:47+02:00
---

# qValueExpression

An expression value is an expression that returns a single numeric value.

Example:

```json
fields : {
    qValueExpression : "=Count (DISTINCT $Field)"
}
```

## Properties

For a complete description of the `qValueExpression` properties,
see the [Qlik Sense Engine (qix) API documentation](https://qlik.dev/apis/json-rpc/qix/schemas/#valueexpression).

## Learn more

- [Generic object in visualization extensions](https://qlik.dev/extend/extensions/extension-api/build-extension/generic-object-viz-extension/)
