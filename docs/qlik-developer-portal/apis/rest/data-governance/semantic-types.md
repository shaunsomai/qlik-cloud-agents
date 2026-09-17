# Semantic types

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

The Semantic types API enables you to manage semantic type definitions programmatically.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `POST` | [`/api/data-governance/semantic-types/actions/export`](#post-apidata-governancesemantic-typesactionsexport) | Exports semantic types from the current tenant as a downloadable JSON file. Supports optional filtering by type IDs, category, creator, or search term.  Without filters, all types (user-created and Qlik defaults) are exported. |
| `POST` | [`/api/data-governance/semantic-types/actions/import`](#post-apidata-governancesemantic-typesactionsimport) | Imports semantic types from a JSON file. Supports Qlik Cloud format (`QlikSemanticTypesExport`) and Talend legacy format (`DQDictionaryImportExport`). Format is auto-detected from the `exportFormat` field in the payload. |

## API Reference

### POST /api/data-governance/semantic-types/actions/export

Exports semantic types from the current tenant as a downloadable JSON file. Supports optional filtering by type IDs, category, creator, or search term.  Without filters, all types (user-created and Qlik defaults) are exported.


- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `ids` | string[] | No | List of semantic type IDs to export. When provided, only these types are included. |
| `types` | string[] | No | Filter by semantic type categories. Supports multiple values for OR logic. When provided, only types matching the specified categories are included.  Enum: "REGEX", "DICTIONARY", "COMPOUND" |
| `search` | string | No | Case-insensitive substring search on label and description fields. Returns only semantic types where the label or description contains the search term. Special regex characters are automatically escaped for literal matching. Maximum length: 500 characters. Empty string returns no results. |
| `createdBy` | string | No | Filter by creator user ID. When provided, only types created by this user are included. |

#### Responses

##### 200

Export file containing the requested semantic types.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `version` | string | Yes | Schema version for forward compatibility. |
| `exportFormat` | string | Yes | Format identifier for auto-detection on import. Enum: "QlikSemanticTypesExport" |
| `exportedCount` | integer | No | Total number of semantic types included in this export. Helps API consumers quickly determine export size without parsing the entire array. |
| `semanticTypes` | object[] | Yes | A semantic type in the export file, stripped of internal fields. |

<details>
<summary>Properties of `semanticTypes`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | Yes | Enum: "REGEX", "DICTIONARY", "COMPOUND" |
| `label` | string | Yes |  |
| `config` | object | Yes |  |
| `activated` | boolean | Yes |  |
| `defaultId` | string | No | Identifier of the parent default semantic type (Qlik-provisioned). Null for user-created types. Used for identity preservation during cross-tenant import and as fallback for COMPOUND children resolution when labels differ across tenants. |
| `description` | string | No |  |
| `useForValidation` | boolean | Yes |  |

<details>
<summary>Properties of `config`</summary>

**One of:**

**Option 1:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `SemanticTypeRegex` | object | No | A semantic type for words matching a regex pattern |

<details>
<summary>Properties of `SemanticTypeRegex`</summary>

_Properties truncated due to depth limit._

</details>

**Option 2:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `SemanticTypeDictionary` | object | No | A semantic type for words matching a value in the list of values |

<details>
<summary>Properties of `SemanticTypeDictionary`</summary>

_Properties truncated due to depth limit._

</details>

**Option 3:**

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `ExportSemanticTypeCompound` | object | No | COMPOUND config in the export file. Children are represented as enriched references with label and parentId for cross-tenant resolution, instead of raw IDs which are tenant-specific. |

<details>
<summary>Properties of `ExportSemanticTypeCompound`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 400

The request is in incorrect format.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 401

User does not have valid authentication credentials.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 403

User does not have access to the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 500

Internal Server Error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 503

Requested service is not available.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/data-governance/semantic-types/actions/export` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/data-governance/semantic-types/actions/export',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      ids: [
        '3b179e2b028c4306ab108b68116ae639',
        '4d237dd47e594f789617041b0d09c66f',
      ],
      types: ['REGEX', 'DICTIONARY'],
      search: 'email',
      createdBy:
        '712020:291adc5e-c210-408b-a43a-776448c35ef4',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/data-governance/semantic-types/actions/export yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/data-governance/semantic-types/actions/export" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"ids":["3b179e2b028c4306ab108b68116ae639","4d237dd47e594f789617041b0d09c66f"],"types":["REGEX","DICTIONARY"],"search":"email","createdBy":"712020:291adc5e-c210-408b-a43a-776448c35ef4"}'
```

**Example Response:**

```json
{
  "version": "1.0",
  "exportFormat": "QlikSemanticTypesExport",
  "exportedCount": 42,
  "semanticTypes": [
    {
      "type": "REGEX",
      "label": "string",
      "config": {
        "validationContent": "ANY_CHARACTER",
        "validationPattern": "^(\\\\S+)\\\\s+(\\\\S+)$"
      },
      "activated": true,
      "defaultId": "string",
      "description": "string",
      "useForValidation": true
    }
  ]
}
```

---

### POST /api/data-governance/semantic-types/actions/import

Imports semantic types from a JSON file. Supports Qlik Cloud format (`QlikSemanticTypesExport`) and Talend legacy format (`DQDictionaryImportExport`). Format is auto-detected from the `exportFormat` field in the payload.

**Conflict handling** is controlled by the `skipConfirmation` flag and the optional `conflictResolutions` array:

- **Preview** (`skipConfirmation` false/absent, no `conflictResolutions`):
  the file is analysed but nothing is imported. Returns `200` with a
  per-type conflict/summary body. Re-submit with `skipConfirmation=true`
  or `conflictResolutions` to actually apply the import.


- **One-shot** (`skipConfirmation=true`, no `conflictResolutions`):
  if real conflicts or in-file duplicates exist, returns `200` with the
  conflict body and imports nothing; otherwise the import is applied and
  `201` is returned with the import report.


- **Resolved** (`conflictResolutions` provided): the import is applied using
  the per-label strategies, falling back to `defaultConflictStrategy`
  (defaults to `SKIP`) for unlisted labels. Returns `201` in both cases
  (conflicts present or not), with the import report.


Import is best-effort: each type is processed independently. Failures are logged in the response report without blocking other types.


- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Required**

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `file` | object | Yes | The export file payload as-is. Format is detected from the `exportFormat` field. Accepts `QlikSemanticTypesExport` (Qlik native) or `DQDictionaryImportExport` (Talend legacy). |
| `skipConfirmation` | boolean | No | Controls preview vs. one-shot import when no `conflictResolutions` are supplied. When `false` (default) the call is a **preview**: the file is analysed and a per-type conflict/summary body is returned (HTTP 200) without importing anything. When `true` the import is attempted **one-shot**: if real conflicts or in-file duplicates exist the conflict body is returned (HTTP 200) and nothing is imported; otherwise all types are imported (HTTP 201). Ignored when `conflictResolutions` are provided (those always apply the import). |
| `conflictResolutions` | object[] | No | Per-type conflict resolution. Each entry maps a conflicting label to its strategy. Labels not listed fall back to `defaultConflictStrategy`. Omit entirely (or send `null`) on the first call to trigger conflict detection. Sending an array — even an empty one — applies the import, using `defaultConflictStrategy` for every conflict not listed. |
| `defaultConflictStrategy` | string | No | Fallback strategy applied to conflicting types not listed in `conflictResolutions`. Defaults to `SKIP`.  Enum: "OVERWRITE", "SKIP", "KEEP_BOTH" |

<details>
<summary>Properties of `conflictResolutions`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `label` | string | Yes | Label of the conflicting semantic type. |
| `strategy` | string | Yes | `OVERWRITE`: replace the existing type with the version from the file. `SKIP`: keep the existing type unchanged, do not import. `KEEP_BOTH`: keep the existing type and create the version from the file with a deduplicated label.  Enum: "OVERWRITE", "SKIP", "KEEP_BOTH" |

</details>

#### Responses

##### 200

Nothing was imported. The body is an `ImportConflictResponse`:
- when `skipConfirmation=true` but real conflicts or in-file
  duplicates exist — nothing was imported;

- when `skipConfirmation` is false/absent (preview) — nothing was
  imported. Re-submit with `skipConfirmation=true` or
  `conflictResolutions` to apply.


**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes |  |
| `types` | object[] | Yes | Every type from the import file with its status. `CONFLICT` types include a `diff` showing field-level differences. `ERROR` types include an `error` message describing the validation failure. `DUPLICATE` types are either repeated labels within the same file, or types whose definition is identical to one already in the tenant (auto-skipped, no conflict resolution needed). |
| `message` | string | Yes |  |

<details>
<summary>Properties of `types`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `diff` | object | No | Field-by-field comparison between the type from the import file and the existing type in the tenant. Only present when status is `CONFLICT`. Each field shows the value from the file and the existing value so the user can make an informed OVERWRITE / SKIP / KEEP_BOTH decision. |
| `type` | string | Yes | Category of the semantic type. Enum: "REGEX", "DICTIONARY", "COMPOUND" |
| `error` | string | No | Human-readable error message. Only present when status is `ERROR`. |
| `label` | string | Yes | Label of the semantic type. |
| `status` | string | Yes | `NEW`: no type with this label exists in the tenant. `CONFLICT`: a type with this label already exists but differs from the imported version. `ERROR`: the type has a validation error (missing field, invalid regex, etc.). `DUPLICATE`: the type is a duplicate — either another type with the same label appears earlier in the import file, or the imported type is identical to an existing type in the tenant (all user-visible fields match; auto-skipped with no conflict resolution needed).  Enum: "NEW", "CONFLICT", "ERROR", "DUPLICATE" |
| `errorCode` | string | No | Machine-readable error code. Only present when status is `ERROR`. Enum: "IMPORT_REGEX_PATTERN_MISSING", "IMPORT_REGEX_PATTERN_TOO_LONG", "IMPORT_REGEX_PATTERN_INVALID", "IMPORT_DICTIONARY_VALUES_MISSING", "IMPORT_DICTIONARY_VALUE_BLANK", "IMPORT_COMPOUND_CHILDREN_MISSING", "IMPORT_COMPOUND_CHILDREN_NOT_FOUND" |

<details>
<summary>Properties of `diff`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `config` | object | No | Type-specific config differences. Only the fields relevant to the type's category are present (REGEX → validationContent/validationPattern, DICTIONARY → validationCriteria/values, COMPOUND → children), and only when they differ. |
| `category` | object | No | A single field difference between the file value and the existing type. |
| `activated` | object | No | A single field difference between the file value and the existing type. |
| `description` | object | No | A single field difference between the file value and the existing type. |
| `useForValidation` | object | No | A single field difference between the file value and the existing type. |

<details>
<summary>Properties of `config`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `category`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `activated`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `description`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `useForValidation`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 201

Import applied. The report contains summary counts and a detailed error list for any types that could not be processed. Returned in both the no-conflict case and when `conflictResolutions` were provided (regardless of whether conflicts were present).


**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | Error detail for a single semantic type that could not be imported. |
| `summary` | object | Yes | Aggregate counts and per-status label details for the import result. Each status group includes a count and the list of affected type labels. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Application error code identifying the failure reason. |
| `label` | string | Yes | Label of the semantic type that failed. |
| `message` | string | Yes | Human-readable error description in English. |

</details>

<details>
<summary>Properties of `summary`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errored` | object | Yes | Count and affected types for one import outcome. |
| `skipped` | object | Yes | Count and affected types for one import outcome. |
| `updated` | object | Yes | Count and affected types for one import outcome. |
| `duplicates` | object | Yes | Count and affected types for one import outcome. |
| `totalCreated` | object | Yes | Count and affected types for one import outcome. |

<details>
<summary>Properties of `errored`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `count` | integer | Yes | Number of types in this category. |
| `items` | object[] | Yes | Affected semantic types paired with their persisted resource id. Ids are present for created, updated, skipped and duplicate outcomes, and null for errored types that were never persisted. |
| `labels` | string[] | Yes | Labels of the affected semantic types. |

<details>
<summary>Properties of `items`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `skipped`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `count` | integer | Yes | Number of types in this category. |
| `items` | object[] | Yes | Affected semantic types paired with their persisted resource id. Ids are present for created, updated, skipped and duplicate outcomes, and null for errored types that were never persisted. |
| `labels` | string[] | Yes | Labels of the affected semantic types. |

<details>
<summary>Properties of `items`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `updated`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `count` | integer | Yes | Number of types in this category. |
| `items` | object[] | Yes | Affected semantic types paired with their persisted resource id. Ids are present for created, updated, skipped and duplicate outcomes, and null for errored types that were never persisted. |
| `labels` | string[] | Yes | Labels of the affected semantic types. |

<details>
<summary>Properties of `items`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `duplicates`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `count` | integer | Yes | Number of types in this category. |
| `items` | object[] | Yes | Affected semantic types paired with their persisted resource id. Ids are present for created, updated, skipped and duplicate outcomes, and null for errored types that were never persisted. |
| `labels` | string[] | Yes | Labels of the affected semantic types. |

<details>
<summary>Properties of `items`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `totalCreated`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `count` | integer | Yes | Number of types in this category. |
| `items` | object[] | Yes | Affected semantic types paired with their persisted resource id. Ids are present for created, updated, skipped and duplicate outcomes, and null for errored types that were never persisted. |
| `labels` | string[] | Yes | Labels of the affected semantic types. |

<details>
<summary>Properties of `items`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 400

Invalid payload — malformed JSON, unknown format, or structural error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 401

User does not have valid authentication credentials.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 403

User does not have access to the resource.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 500

Internal Server Error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

##### 503

Requested service is not available.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No |  |
| `traceId` | string | No |  |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | No |  |
| `title` | string | No |  |
| `detail` | string | No |  |
| `status` | string | No |  |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/data-governance/semantic-types/actions/import` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/data-governance/semantic-types/actions/import',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      file: {
        exportedAt: '2024-01-01T00:00:00Z',
        exportFormat: 'QlikSemanticTypesExport',
        semanticTypes: [],
      },
      skipConfirmation: false,
      conflictResolutions: [
        {
          label: 'Email Address',
          strategy: 'SKIP',
        },
      ],
      defaultConflictStrategy: 'SKIP',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/data-governance/semantic-types/actions/import yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/data-governance/semantic-types/actions/import" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"file":{"exportedAt":"2024-01-01T00:00:00Z","exportFormat":"QlikSemanticTypesExport","semanticTypes":[]},"skipConfirmation":false,"conflictResolutions":[{"label":"Email Address","strategy":"SKIP"}],"defaultConflictStrategy":"SKIP"}'
```

**Example Response:**

```json
{
  "code": "IMPORT_CONFLICT",
  "types": [
    {
      "diff": {
        "config": {
          "values": {},
          "children": {},
          "validationContent": {},
          "validationPattern": {},
          "validationCriteria": {}
        },
        "category": {},
        "activated": {},
        "description": {},
        "useForValidation": {}
      },
      "type": "REGEX",
      "error": "string",
      "label": "string",
      "status": "NEW",
      "errorCode": "IMPORT_REGEX_PATTERN_MISSING"
    }
  ],
  "message": "Conflicts: 2 of 10, Unchanged: 3."
}
```

---
