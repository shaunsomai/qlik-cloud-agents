---
source: https://qlik.dev/manage/data-governance/import-export-semantic-types/
last_updated: 2026-09-11T18:31:59+02:00
---

# Import and export semantic types

In this guide, you'll learn how to export and import semantic types using the Semantic Types API.

## Overview

Semantic types describe the type of data found in dataset fields, such as names, ZIP codes, or phone numbers.
They can be used to enhance the data quality of your datasets.
For more information, see [Managing semantic types](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataProducts/Managing-semantic-types.htm)
on Qlik Help.

The [Semantic Types API](https://qlik.dev/apis/rest/data-governance/semantic-types) provides endpoints to export and import
semantic types. Use the API to:

- Export semantic types to save them and reuse them later in the same or another tenant.
- Import semantic types into the same tenant to create new types or update existing definitions, for example to add
  values to a dictionary-based semantic type or change the pattern of a pattern-based semantic type.
- Copy semantic types from a source Qlik Cloud tenant to a target tenant.
- Import semantic types exported from a legacy Talend environment into Qlik Cloud.

To review conflicts before importing, use this workflow:

1. **Preview** the import to see which semantic types are new, conflicting, or cannot be imported.
2. **Resolve conflicts** by choosing strategies for conflicting types, optionally using a default strategy.
3. **Complete the import** by resubmitting the semantic types with your resolutions.

You can also skip the preview and attempt a one-shot import by setting `skipConfirmation` to `true`.

## Before you begin

- You have one of the following subscriptions:
  - Qlik Talend Cloud Enterprise
  - Qlik Talend Cloud Premium
  - Qlik Cloud Analytics Premium
  - Qlik Cloud Analytics Enterprise
  - Qlik Sense Enterprise SaaS
- You have an API key or access token. For more information, see [Authentication](https://qlik.dev/authenticate).
- You have access to the source tenant, where you export the semantic types.
- You have access to the target tenant, where you import the semantic types. The source and target can be the same
  tenant.
- On the source tenant, exporting requires the `semantictype:list` or `admin.semantictype:list` scope.
- On the target tenant, importing requires the `semantictype:create` scope.
  For more information, see [Scopes](https://qlik.dev/manage/access-control/scopes).

> **Note:** Replace everything in `<angle brackets>` with your own values.

## Export semantic types

Export semantic types from the source tenant as a JSON file:

```bash
curl -X POST "https://<SOURCE_TENANT>/api/data-governance/semantic-types/actions/export" \
  -H "Authorization: Bearer <API_KEY>" \
  -H "Content-Type: application/json" \
  -d "{}" \
  --output semantic-types.json
```

The request body is optional. Without filters, the endpoint exports every semantic type in the tenant, including
Qlik-provided default types and user-created types.

To export a subset, pass one or more filters in the request body:

- `ids`: a list of specific semantic type IDs.
- `types`: one or more categories (`REGEX`, `DICTIONARY`, `COMPOUND`).
- `search`: a case-insensitive substring match on label or description.
- `createdBy`: a creator user ID.

The response is a `SemanticTypesExportEnvelope` containing `exportFormat`, `version`, the `semanticTypes` array, and
optionally `exportedCount`.

The `Content-Disposition` header suggests a filename such as `semantic-types-20260604143052.json`.
In this guide, the response is saved as `semantic-types.json`.

You'll use the exported JSON object as the `file` property when importing the semantic types.

## Import semantic types

The import endpoint expects the complete exported JSON object in the required `file` property:

```json
{
  "file": <EXPORTED_FILE_CONTENTS>
}
```

In the examples in this guide, `<EXPORTED_FILE_CONTENTS>` represents the JSON object returned by the export endpoint.

The API supports two import formats:

- Qlik Cloud's `QlikSemanticTypesExport` format.
- The Talend legacy `DQDictionaryImportExport` format.

The format is auto-detected from the `exportFormat` field.

The request behaves differently depending on whether you provide `skipConfirmation` or `conflictResolutions`:

| Request                                                                           | Behavior                                                                                                     |
| --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| `skipConfirmation` is absent or `false` and no `conflictResolutions` are supplied | Preview the import without importing anything.                                                               |
| `conflictResolutions` are supplied, even as an empty array                        | Apply the import. Conflicts not explicitly listed use `defaultConflictStrategy`, which defaults to `SKIP`.   |
| `skipConfirmation` is `true` and no `conflictResolutions` are supplied            | Attempt a one-shot import. If review is required, nothing is imported and the conflict response is returned. |

## Preview the import

Create a preview request by placing the exported JSON object in the `file` property.
Do not include `skipConfirmation` or `conflictResolutions`.

If you're following the examples with curl, you can use [`jq`](https://jqlang.org/) to create the request body from `semantic-types.json`:

```bash
jq '{file: .}' semantic-types.json > import-request.json
```

`jq` is only used here to construct the JSON request body and is not required by the Semantic Types API.
For installation instructions, see [Downloading jq](https://jqlang.org/download/).

Submit the request to the import endpoint:

```bash
curl -X POST "https://<TARGET_TENANT>/api/data-governance/semantic-types/actions/import" \
  -H "Authorization: Bearer <API_KEY>" \
  -H "Content-Type: application/json" \
  --data-binary @import-request.json
```

When `skipConfirmation` is absent or `false` and no `conflictResolutions` are supplied, the call is a preview.
The semantic types are analyzed but nothing is imported.

The response is `200` with an `ImportConflictResponse` listing each semantic type from the `file` property of the
request.
Each semantic type has a `status` of `NEW`, `CONFLICT`, `ERROR`, or `DUPLICATE`.
For example, a conflicting semantic type can return:

```json
{
  "code": "IMPORT_CONFLICT",
  "message": "Conflicts: 1 of 1.",
  "types": [
    {
      "diff": {
        "config": {
          "validationPattern": {
            "existing": "^[A-Z]{3}[0-9]{3}$",
            "fromFile": "^[A-Z]{4}[0-9]{2}$"
          }
        }
      },
      "label": "EMAIL_ADDRESS_SEMANTIC_TYPE",
      "status": "CONFLICT",
      "type": "REGEX"
    }
  ]
}
```

In this example, `EMAIL_ADDRESS_SEMANTIC_TYPE` conflicts with an existing type in the target tenant.

### Understand preview results

The `status` field indicates the outcome for each type:

- `NEW`: no type with this label exists in the tenant.
- `CONFLICT`: a type with this label already exists. The item can include a `diff` showing field-by-field difference
  between `fromFile` and `existing`.
- `ERROR`: the type has an error that prevents it from being imported.
- `DUPLICATE`: either the semantic type is identical to one already in the tenant or `file` contains more than one
  semantic type with the same label.

The API uses the same `DUPLICATE` status for both cases.
The response `message` indicates which case was detected.

For more information about these cases, see [Import behavior and edge cases](#import-behavior-and-edge-cases).

### Resolve conflicts and complete the import

Resubmit the semantic types with `conflictResolutions` to apply the import.

Provide a strategy for the conflicts you want to resolve individually.
Conflicting labels not listed in `conflictResolutions` use `defaultConflictStrategy`, which defaults to `SKIP`.

For example, create a request that overwrites the existing `EMAIL_ADDRESS_SEMANTIC_TYPE` semantic type:

```bash
jq '{
  file: .,
  defaultConflictStrategy: "SKIP",
  conflictResolutions: [
    {
      label: "EMAIL_ADDRESS_SEMANTIC_TYPE",
      strategy: "OVERWRITE"
    }
  ]
}' semantic-types.json > import-request.json
```

Submit the request:

```bash
curl -X POST "https://<TARGET_TENANT>/api/data-governance/semantic-types/actions/import" \
  -H "Authorization: Bearer <API_KEY>" \
  -H "Content-Type: application/json" \
  --data-binary @import-request.json
```

Each strategy resolves a conflict as follows:

- `OVERWRITE`: replace the existing semantic type definition with the version from `file`.
- `SKIP`: keep the existing semantic type unchanged and don't import the version from `file`.
- `KEEP_BOTH`: keep the existing semantic type and import the version from `file` with a modified label so both semantic
  types can exist.

> **Note:** In the Qlik Cloud UI, the equivalent conflict resolution options are  **Ignore**, **Update**, and **Keep both**.
> The API uses `SKIP`, `OVERWRITE`, and `KEEP_BOTH`.

Sending `conflictResolutions`, even an empty array, applies the import immediately. Conflicts not explicitly listed use
`defaultConflictStrategy`, which defaults to `SKIP`.

For example, the following is an applied import, not a preview:

```json
{
  "file": <EXPORTED_FILE_CONTENTS>,
  "conflictResolutions": []
}
```

An applied import returns `201` with an `ImportReport`, including when conflicts were resolved:

```json
{
  "summary": {
    "totalCreated": {
      "count": 3,
      "labels": ["Email Address", "Phone Number", "IBAN"],
      "items": [
        { "label": "Email Address", "id": "abc-1" },
        { "label": "Phone Number", "id": "abc-2" },
        { "label": "IBAN", "id": "abc-3" }
      ]
    },
    "updated": { "count": 0, "labels": [], "items": [] },
    "skipped": { "count": 0, "labels": [], "items": [] },
    "errored": { "count": 0, "labels": [], "items": [] },
    "duplicates": { "count": 0, "labels": [], "items": [] }
  },
  "errors": []
}
```

The report indicates which semantic types were created, updated, skipped, found unchanged, or could not be imported:

- `totalCreated`: semantic types created by the import.
- `updated`: existing semantic types updated using `OVERWRITE`.
- `skipped`: conflicting semantic types kept unchanged using `SKIP`.
- `errored`: semantic types that could not be imported.
- `duplicates`: semantic types in `file` that were identical to semantic types already in the tenant.

> **Note:** Import processing is best-effort. A failure for one semantic type does not prevent other valid semantic types in the
> same applied import from being processed.
>
> Types that could not be imported are reported in `summary.errored` and in the `errors` array.

### Import without preview

You can skip the explicit preview step by setting `skipConfirmation` to `true` and omitting `conflictResolutions`:

```json
{
  "file": <EXPORTED_FILE_CONTENTS>,
  "skipConfirmation": true
}
```

If no conflict resolution is required, the import is applied directly and returns `201`.

If conflicts or duplicate conditions requiring review are detected, the API returns `200` with an
`ImportConflictResponse` and nothing is imported.

## Verify the import

Check the `summary` counts (`totalCreated`, `updated`, `skipped`, `errored`, `duplicates`) and the `errors` array in
`ImportReport` to confirm the outcome of the import.

You can also verify created or updated semantic types in Qlik Cloud: Open **Data Quality**, go to the
**Semantic types** tab, and find the imported semantic type.
For more information, see [Managing semantic types](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataProducts/Managing-semantic-types.htm)
on Qlik Help.

## Import behavior and edge cases

<details>
  <summary>Identical semantic types</summary>

  If a semantic type in `file` is identical to one already in the tenant, the preview returns `DUPLICATE`.

  When the import is applied, the type is not changed and is reported in `summary.duplicates`.
</details>

<details>
  <summary>Duplicate labels</summary>

  If `file` contains multiple semantic types with the same label, preview marks all occurrences as `DUPLICATE`.

  A one-shot import is not applied when these duplicate labels are detected.

  If the import is explicitly applied using `conflictResolutions`, processing remains best-effort.

  If no semantic type with that label already exists in the tenant, the first occurrence can be created and a later
  occurrence fails with `IMPORT_DUPLICATE_LABEL`.

  The failed occurrence is reported in `summary.errored`, not in `summary.duplicates`.
</details>

<details>
  <summary>Compound semantic types</summary>

  A compound semantic type can reference other semantic types as children.

  In the Qlik Cloud export format, the importer resolves each child in three steps: first by `label` against semantic
  types created earlier in the same import batch, then by `label` against existing semantic types in the target tenant,
  and finally by `parentId` as a fallback.

  If a child cannot be resolved by either `label` or `parentId`, the compound semantic type is rejected with
  `IMPORT_COMPOUND_CHILDREN_NOT_FOUND`. Other valid semantic types in the same import continue processing.

  For example:

  ```json
  {
    "code": "IMPORT_COMPOUND_CHILDREN_NOT_FOUND",
    "label": "EXAMPLE_BROKEN_COMPOUND",
    "message": "COMPOUND type 'EXAMPLE_BROKEN_COMPOUND' references missing children: [EXAMPLE_MISSING_CHILD]."
  }
  ``` 
</details>
