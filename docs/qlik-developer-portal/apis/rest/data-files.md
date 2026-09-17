# Data files

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Data files represent the flat file storage associated with spaces in your Qlik Cloud tenant. Each space will have a corresponding data files connection, which you can list with data-connections.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `GET` | [`/api/v1/data-files`](#get-apiv1data-files) |  |
| `POST` | [`/api/v1/data-files`](#post-apiv1data-files) |  |
| `GET` | [`/api/v1/data-files/{id}`](#get-apiv1data-filesid) |  |
| `PUT` | [`/api/v1/data-files/{id}`](#put-apiv1data-filesid) |  |
| `DELETE` | [`/api/v1/data-files/{id}`](#delete-apiv1data-filesid) |  |
| `POST` | [`/api/v1/data-files/{id}/actions/change-owner`](#post-apiv1data-filesidactionschange-owner) | This is primarily an admin type of operation.  In general, the owner of a data file or folder is implicitly |
| `POST` | [`/api/v1/data-files/{id}/actions/change-space`](#post-apiv1data-filesidactionschange-space) | This is to allow for a separate admin type of operation that is more global in terms of access in cases |
| `POST` | [`/api/v1/data-files/actions/change-space`](#post-apiv1data-filesactionschange-space) | This is to allow for a separate admin type of operation that is more global in terms of access in cases |
| `POST` | [`/api/v1/data-files/actions/delete`](#post-apiv1data-filesactionsdelete) |  |
| `GET` | [`/api/v1/data-files/connections`](#get-apiv1data-filesconnections) | The non-filtered list contains a set of hardcoded connections, along with one connection per team space that |
| `GET` | [`/api/v1/data-files/connections/{id}`](#get-apiv1data-filesconnectionsid) |  |
| `GET` | [`/api/v1/data-files/quotas`](#get-apiv1data-filesquotas) |  |

## API Reference

### GET /api/v1/data-files

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `allowInternalFiles` | boolean | No | If set to false, do not return data files with internal extensions else return all the data files. |
| `appId` | string | No | Only return files scoped to the specified app.  If this parameter is not specified, only files that are not scoped to any app are returned.  "*" implies all app-scoped files are returned. |
| `baseNameWildcard` | string | No | If present, return only items whose base name matches the given wildcard.  Wildcards include '*' and '?' characters to allow for multiple matches.  The base name is the actual file or folder name without any folder pathing included. |
| `connectionId` | string | No | Return files and folders that reside in the space referenced by the specified DataFiles connection.  If this parameter is not specified, the user's personal space is implied. |
| `excludeFiles` | boolean | No | If set to true, exclude files in the returned list (IE, only return folders).  If false, include files. |
| `excludeSubFolders` | boolean | No | If set to true, exclude folders and files that reside in sub-folders of the root being searched.  If false, include all items in full folder hierarchy that recursively reside under the root.  That is, setting to true results in only the direct children of the root being returned. |
| `folderId` | string | No | If present, return only items which reside under the folder specified by the given ID.  If not present, items that live at the root of the space are returned.  This property is mutually exclusive with 'folderPath'. |
| `folderPath` | string | No | If present, return only items which reside under the specified folder path.  If not present, items that live at the root of the space are returned.  This property is mutually exclusive with 'folderId'. |
| `includeAllSpaces` | boolean | No | If set to true, and connectionId is not specified, return files and folders from all spaces the given user has access to (including the personal space).  If connectionId is specified, this parameter is ignored. |
| `includeFolders` | boolean | No | If set to true, include folders in the returned list.  If false, only return data files. |
| `includeFolderStats` | boolean | No | If set to true, include computed folder statistics for folders in the returned list.  If false, this information is not returned. |
| `limit` | integer | No | If present, the maximum number of data files to return. |
| `name` | string | No | Filter the list of files returned to the given file name. |
| `notOwnerId` | string | No | If present, fetch the data files whose owner is not the specified owner.  If a connectionId is specified in this case, the returned list is constrained to the specified space.  If connectionId is not specified, then the returned list is constrained to the calling user's personal space.  If includeAllSpaces is set to true, and connectionId is not specified, the returned list is from all spaces the given user has access to (including the personal space). |
| `ownerId` | string | No | If present, fetch the data files for the specified owner.  If a connectionId is specified in this case, the returned list is constrained to the specified space.  If connectionId is not specified, then all files owned by the specified user are returned regardless of the personal space that a given file resides in. |
| `page` | string | No | If present, the cursor that starts the page of data that is returned. |
| `sort` | string | No | The name of the field used to sort the result.  By default, the sort order is ascending.  Putting a '+' prefix on the sort field name explicitly indicates ascending sort order.  A '-' prefix indicates a descending sort order. Enum: "name", "+name", "-name", "size", "+size", "-size", "modifiedDate", "+modifiedDate", "-modifiedDate", "folder", "+folder", "-folder", "baseName", "+baseName", "-baseName" |

#### Responses

##### 200

The file list was retrieved.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes | Properties of the uploaded data files. |
| `links` | object | Yes |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID for the file or folder. |
| `qri` | string | No | The QRI generated from the datafile or folder's metadata. |
| `name` | string | Yes | The full name of the file or folder, including any folder path prefix. |
| `size` | integer | Yes | The size of the uploaded file, in bytes.  0 if this item represents a folder |
| `appId` | string | No | If this file or folder is bound to the lifecycle of a specific app, this is the ID of this app. |
| `folder` | boolean | No | Whether or not this given item represents a folder or a file. |
| `actions` | string[] | Yes | The CRUD actions that are allowed on the given data file. Enum: "read", "update", "delete", "list", "change_owner", "change_space" |
| `ownerId` | string | Yes | The 'owner' of a file or folder is the user who last uploaded the item's content. |
| `spaceId` | string | No | If the file or folder was created in a team space, this is the ID of that space. |
| `baseName` | string | No | The name of the file or folder, not including any folder path prefix. |
| `folderId` | string | No | If the file or folder resides in a parent folder, this is the parent folder ID.  If the file or folder does not reside in a parent folder, this value is null. |
| `folderPath` | string | No | If the file or folder resides in a parent folder, this is the parent folder path.  If the file or folder does not reside in a parent folder, this value is null. |
| `createdDate` | string | Yes | The date that the file or folder was created. |
| `folderStats` | object | Yes |  |
| `modifiedDate` | string | No | The date that the updated file or folder was last modified. |
| `contentUpdatedDate` | string | No | If the data file's content was updated, this is the DateTime of the last content update. |

<details>
<summary>Properties of `folderStats`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `totalFileCount` | integer | Yes | The number of data files that reside as direct and indirect children of the given folder and it's sub-folder hierarchy. |
| `directFileCount` | integer | Yes | The number of data files that reside as direct children of the given folder. |
| `totalFolderCount` | integer | Yes | The number of folders that reside as direct and indirect children of the given folder and it's sub-folder hierarchy. |
| `aggregateFileSize` | integer | Yes | The sum of the file sizes, in bytes, of all data files that reside as direct and indirect children of the given folder and it's sub-folder hierarchy. |
| `directFolderCount` | integer | Yes | The number of sub-folders that reside as direct children of the given folder. |
| `totalInternalFileCount` | integer | Yes | The number of 'internal' data files (IE, those that are not visible to end users by default) that reside as direct and indirect children of the given folder and it's sub-folder hierarchy. |
| `directInternalFileCount` | integer | Yes | The number of 'internal' data files (IE, those that are not visible to end users by default) that reside as direct children of the given folder. |
| `totalAppScopedFileCount` | integer | Yes | The number of app-scoped data files that reside as direct and indirect children of the given folder and it's sub-folder hierarchy. |
| `directAppScopedFileCount` | integer | Yes | The number of app-scoped data files that reside as direct children of the given folder. |
| `aggregateInternalFileSize` | integer | Yes | The sum of the file sizes, in bytes, of all internal data files that reside as direct and indirect children of the given folder and it's sub-folder hierarchy. |
| `aggregateAppScopedFileSize` | integer | Yes | The sum of the file sizes, in bytes, of all app-scoped data files that reside as direct and indirect children of the given folder and it's sub-folder hierarchy. |

</details>

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `next` | object | Yes |  |
| `prev` | object | Yes |  |
| `self` | object | Yes |  |

<details>
<summary>Properties of `next`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | The URL for the link. |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | The URL for the link. |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | The URL for the link. |

</details>

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Fine-grained error codes for data-files REST operations.  For operations which do not have a more fine-grained error code, the error code is set to the HTTP status code.<p>Members:</p><ul><li><i>DF-001</i> - The page cursor passed as a parameter to the GET operation is invalid.</li><li><i>DF-002</i> - The sort specification passed as a parameter to the GET operation is invalid.</li><li><i>DF-003</i> - FolderPath and FolderId are mutually exclusive, they cannot both be passed as parameters.</li><li><i>DF-004</i> - The provided FolderPath must be in canonical form.</li><li><i>DF-005</i> - The specified parent folder cannot be found.</li><li><i>DF-006</i> - The specified owner cannot be found.</li><li><i>DF-007</i> - A connection corresponding to the specified space cannot be found.</li><li><i>DF-008</i> - THe specified ID must correspond to a folder, not a file.</li><li><i>DF-009</i> - The specified space cannot be found.</li><li><i>DF-010</i> - The specified file name contains an invalid file extension.</li><li><i>DF-011</i> - The specified file name is missing a file extension.</li><li><i>DF-012</i> - The specified temporary content file could not be found.</li><li><i>DF-013</i> - Access to the specified space is forbidden.</li><li><i>DF-014</i> - The specified connection cannot be found.</li><li><i>DF-015</i> - The provided filename must be in canonical form.</li><li><i>DF-016</i> - The datafile size quota for the given personal space has been exceeded.</li><li><i>DF-017</i> - The specified source file or folder could not be found.</li><li><i>DF-018</i> - The source and target of a datafile operation must either both be folders or both be files, but they are             not.</li><li><i>DF-019</i> - The specified target folder is a child of the specified source folder, which is not allowed.</li><li><i>DF-020</i> - The specified folder does not exist in the specified space.</li><li><i>DF-021</i> - The specified source file or folder is already locked.</li><li><i>DF-022</i> - The automatic creation of a missing parent folder failed.</li><li><i>DF-023</i> - An attempt to lock a parent folder of a given data file item failed.</li><li><i>DF-024</i> - The attempt to copy a source file or folder to a target failed.</li><li><i>DF-025</i> - The specified target file or folder is already locked.</li><li><i>DF-026</i> - The request results in the creation of a folder hierarchy which is beyond the max allowed folder             hierarchy depth.</li></ul> Enum: "HTTP-200", "HTTP-201", "HTTP-204", "HTTP-400", "HTTP-403", "HTTP-404", "HTTP-409", "HTTP-413", "HTTP-423", "HTTP-500", "HTTP-501", "HTTP-503", "DF-001", "DF-002", "DF-003", "DF-004", "DF-005", "DF-006", "DF-007", "DF-008", "DF-009", "DF-010", "DF-011", "DF-012", "DF-013", "DF-014", "DF-015", "DF-016", "DF-017", "DF-018", "DF-019", "DF-020", "DF-021", "DF-022", "DF-023", "DF-024", "DF-025", "DF-026" |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Fine-grained error codes for data-files REST operations.  For operations which do not have a more fine-grained error code, the error code is set to the HTTP status code.<p>Members:</p><ul><li><i>DF-001</i> - The page cursor passed as a parameter to the GET operation is invalid.</li><li><i>DF-002</i> - The sort specification passed as a parameter to the GET operation is invalid.</li><li><i>DF-003</i> - FolderPath and FolderId are mutually exclusive, they cannot both be passed as parameters.</li><li><i>DF-004</i> - The provided FolderPath must be in canonical form.</li><li><i>DF-005</i> - The specified parent folder cannot be found.</li><li><i>DF-006</i> - The specified owner cannot be found.</li><li><i>DF-007</i> - A connection corresponding to the specified space cannot be found.</li><li><i>DF-008</i> - THe specified ID must correspond to a folder, not a file.</li><li><i>DF-009</i> - The specified space cannot be found.</li><li><i>DF-010</i> - The specified file name contains an invalid file extension.</li><li><i>DF-011</i> - The specified file name is missing a file extension.</li><li><i>DF-012</i> - The specified temporary content file could not be found.</li><li><i>DF-013</i> - Access to the specified space is forbidden.</li><li><i>DF-014</i> - The specified connection cannot be found.</li><li><i>DF-015</i> - The provided filename must be in canonical form.</li><li><i>DF-016</i> - The datafile size quota for the given personal space has been exceeded.</li><li><i>DF-017</i> - The specified source file or folder could not be found.</li><li><i>DF-018</i> - The source and target of a datafile operation must either both be folders or both be files, but they are             not.</li><li><i>DF-019</i> - The specified target folder is a child of the specified source folder, which is not allowed.</li><li><i>DF-020</i> - The specified folder does not exist in the specified space.</li><li><i>DF-021</i> - The specified source file or folder is already locked.</li><li><i>DF-022</i> - The automatic creation of a missing parent folder failed.</li><li><i>DF-023</i> - An attempt to lock a parent folder of a given data file item failed.</li><li><i>DF-024</i> - The attempt to copy a source file or folder to a target failed.</li><li><i>DF-025</i> - The specified target file or folder is already locked.</li><li><i>DF-026</i> - The request results in the creation of a folder hierarchy which is beyond the max allowed folder             hierarchy depth.</li></ul> Enum: "HTTP-200", "HTTP-201", "HTTP-204", "HTTP-400", "HTTP-403", "HTTP-404", "HTTP-409", "HTTP-413", "HTTP-423", "HTTP-500", "HTTP-501", "HTTP-503", "DF-001", "DF-002", "DF-003", "DF-004", "DF-005", "DF-006", "DF-007", "DF-008", "DF-009", "DF-010", "DF-011", "DF-012", "DF-013", "DF-014", "DF-015", "DF-016", "DF-017", "DF-018", "DF-019", "DF-020", "DF-021", "DF-022", "DF-023", "DF-024", "DF-025", "DF-026" |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/data-files` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-files',
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
# qlik-cli has not implemented support for GET /api/v1/data-files yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-files" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "ee6a390c-5d33-11e8-9c2d-fa7ae01bbebc",
      "qri": "qri:qdf:space://ooSOGoLLaq7EMaSdSsCiGvLwcd_VAf1oU0mzwSfp_Qs#wME89c8gKu_Tpz8W_a0JKSbKC4hzbNu0NLVgqi2UFS0",
      "name": "some/folder/MyFile.csv",
      "size": 1024,
      "appId": "f34b91a1-0dc3-44ac-a847-51cb84122c84",
      "folder": true,
      "actions": [
        "Read"
      ],
      "ownerId": "lDL4DIINndhL_iJkcbqWyJenuwizP-2D",
      "spaceId": "617979737a9f56e49dea2e6e",
      "baseName": "MyFile.csv",
      "folderId": "ee6a390c-5d33-11e8-9c2d-fa7ae01bbebc",
      "folderPath": "some/folder",
      "createdDate": "2020-07-07T20:52:40.8534780Z",
      "folderStats": {
        "totalFileCount": 50,
        "directFileCount": 50,
        "totalFolderCount": 50,
        "aggregateFileSize": 10000,
        "directFolderCount": 50,
        "totalInternalFileCount": 50,
        "directInternalFileCount": 50,
        "totalAppScopedFileCount": 50,
        "directAppScopedFileCount": 50,
        "aggregateInternalFileSize": 10000,
        "aggregateAppScopedFileSize": 10000
      },
      "modifiedDate": "2020-07-07T20:52:40.8534780Z",
      "contentUpdatedDate": "2020-07-07T20:52:40.8534780Z"
    }
  ],
  "links": {
    "next": {
      "href": "string"
    },
    "prev": {
      "href": "string"
    },
    "self": {
      "href": "string"
    }
  }
}
```

---

### POST /api/v1/data-files

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

**Content-Type:** `multipart/form-data`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `File` | string | No | IFormFile form multipart/form-data |
| `Json` | object | No | See PostDataFileRequest schema which defines request structure.  See PostDataFileRequest model. |

<details>
<summary>Properties of `Json`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | Yes | Name that will be given to the file or folder.  It should be noted that the '/' character in the name indicates a 'path' separator in a logical folder hierarchy for the name.  Names that contain '/'s should be used with the assumption that a logical 'folder hierarchy' is being defined for the full pathname of that file or folder.  IE, a '/' is a significant character in the name. |
| `appId` | string | No | If this file should be bound to the lifecycle of a specific app, this is the ID of this app.  If this request is creating a folder, the specification of an app ID is not allowed. |
| `folder` | boolean | No | If true, a folder will be created.  If false, a file is created. |
| `folderId` | string | No | If the specified file or folder should be moved to become a a sub-item of an existing folder, this is the ID of this parent folder.  Any additional folder path that is present on the Name property will be created as a subfolder hierarchy of this folder.  If the FolderID is null, the file or folder specified in the Name property (including any folder prefix on that name), will be created in the root of the space. |
| `sourceId` | string | No | If a SourceId is specified, this is the ID of the existing data file or folder whose content should be copied into the specified data file or folder.  That is, for a file instead of the file content being specified in the Data element, it is effectively copied from an existing, previously uploaded file.  For a folder, rather than the new folder being empty, it's contents are copied from an existing, previously created folder. |
| `connectionId` | string | No | If present, this is the DataFiles connection that the upload should occur in the context of.  If absent, the default is that the upload will occur in the context of the Personal Space DataFiles connection.  If the DataFiles connection is different from the one specified when the file or folder was last POSTed or PUT, this will result in a logical move of this file or folder into the new space. |
| `tempContentFileId` | string | No | If a TempContentFileId is specified, this is the ID of a previously uploaded temporary content file whose content should be copied into the specified data file.  That is, instead of the file content being specified in the Data element, it is effectively copied from an existing, previously uploaded file.  The expectation is that this file was previously uploaded to the temporary content service, and the ID specified here is the one returned from the temp content upload request.  This option does not apply when POSTing a folder. |

</details>

#### Responses

##### 201

New file or folder was created.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID for the file or folder. |
| `qri` | string | No | The QRI generated from the datafile or folder's metadata. |
| `name` | string | Yes | The full name of the file or folder, including any folder path prefix. |
| `size` | integer | Yes | The size of the uploaded file, in bytes.  0 if this item represents a folder |
| `appId` | string | No | If this file or folder is bound to the lifecycle of a specific app, this is the ID of this app. |
| `folder` | boolean | No | Whether or not this given item represents a folder or a file. |
| `actions` | string[] | Yes | The CRUD actions that are allowed on the given data file. Enum: "read", "update", "delete", "list", "change_owner", "change_space" |
| `ownerId` | string | Yes | The 'owner' of a file or folder is the user who last uploaded the item's content. |
| `spaceId` | string | No | If the file or folder was created in a team space, this is the ID of that space. |
| `baseName` | string | No | The name of the file or folder, not including any folder path prefix. |
| `folderId` | string | No | If the file or folder resides in a parent folder, this is the parent folder ID.  If the file or folder does not reside in a parent folder, this value is null. |
| `folderPath` | string | No | If the file or folder resides in a parent folder, this is the parent folder path.  If the file or folder does not reside in a parent folder, this value is null. |
| `createdDate` | string | Yes | The date that the file or folder was created. |
| `folderStats` | object | Yes |  |
| `modifiedDate` | string | No | The date that the updated file or folder was last modified. |
| `contentUpdatedDate` | string | No | If the data file's content was updated, this is the DateTime of the last content update. |

<details>
<summary>Properties of `folderStats`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `totalFileCount` | integer | Yes | The number of data files that reside as direct and indirect children of the given folder and it's sub-folder hierarchy. |
| `directFileCount` | integer | Yes | The number of data files that reside as direct children of the given folder. |
| `totalFolderCount` | integer | Yes | The number of folders that reside as direct and indirect children of the given folder and it's sub-folder hierarchy. |
| `aggregateFileSize` | integer | Yes | The sum of the file sizes, in bytes, of all data files that reside as direct and indirect children of the given folder and it's sub-folder hierarchy. |
| `directFolderCount` | integer | Yes | The number of sub-folders that reside as direct children of the given folder. |
| `totalInternalFileCount` | integer | Yes | The number of 'internal' data files (IE, those that are not visible to end users by default) that reside as direct and indirect children of the given folder and it's sub-folder hierarchy. |
| `directInternalFileCount` | integer | Yes | The number of 'internal' data files (IE, those that are not visible to end users by default) that reside as direct children of the given folder. |
| `totalAppScopedFileCount` | integer | Yes | The number of app-scoped data files that reside as direct and indirect children of the given folder and it's sub-folder hierarchy. |
| `directAppScopedFileCount` | integer | Yes | The number of app-scoped data files that reside as direct children of the given folder. |
| `aggregateInternalFileSize` | integer | Yes | The sum of the file sizes, in bytes, of all internal data files that reside as direct and indirect children of the given folder and it's sub-folder hierarchy. |
| `aggregateAppScopedFileSize` | integer | Yes | The sum of the file sizes, in bytes, of all app-scoped data files that reside as direct and indirect children of the given folder and it's sub-folder hierarchy. |

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Fine-grained error codes for data-files REST operations.  For operations which do not have a more fine-grained error code, the error code is set to the HTTP status code.<p>Members:</p><ul><li><i>DF-001</i> - The page cursor passed as a parameter to the GET operation is invalid.</li><li><i>DF-002</i> - The sort specification passed as a parameter to the GET operation is invalid.</li><li><i>DF-003</i> - FolderPath and FolderId are mutually exclusive, they cannot both be passed as parameters.</li><li><i>DF-004</i> - The provided FolderPath must be in canonical form.</li><li><i>DF-005</i> - The specified parent folder cannot be found.</li><li><i>DF-006</i> - The specified owner cannot be found.</li><li><i>DF-007</i> - A connection corresponding to the specified space cannot be found.</li><li><i>DF-008</i> - THe specified ID must correspond to a folder, not a file.</li><li><i>DF-009</i> - The specified space cannot be found.</li><li><i>DF-010</i> - The specified file name contains an invalid file extension.</li><li><i>DF-011</i> - The specified file name is missing a file extension.</li><li><i>DF-012</i> - The specified temporary content file could not be found.</li><li><i>DF-013</i> - Access to the specified space is forbidden.</li><li><i>DF-014</i> - The specified connection cannot be found.</li><li><i>DF-015</i> - The provided filename must be in canonical form.</li><li><i>DF-016</i> - The datafile size quota for the given personal space has been exceeded.</li><li><i>DF-017</i> - The specified source file or folder could not be found.</li><li><i>DF-018</i> - The source and target of a datafile operation must either both be folders or both be files, but they are             not.</li><li><i>DF-019</i> - The specified target folder is a child of the specified source folder, which is not allowed.</li><li><i>DF-020</i> - The specified folder does not exist in the specified space.</li><li><i>DF-021</i> - The specified source file or folder is already locked.</li><li><i>DF-022</i> - The automatic creation of a missing parent folder failed.</li><li><i>DF-023</i> - An attempt to lock a parent folder of a given data file item failed.</li><li><i>DF-024</i> - The attempt to copy a source file or folder to a target failed.</li><li><i>DF-025</i> - The specified target file or folder is already locked.</li><li><i>DF-026</i> - The request results in the creation of a folder hierarchy which is beyond the max allowed folder             hierarchy depth.</li></ul> Enum: "HTTP-200", "HTTP-201", "HTTP-204", "HTTP-400", "HTTP-403", "HTTP-404", "HTTP-409", "HTTP-413", "HTTP-423", "HTTP-500", "HTTP-501", "HTTP-503", "DF-001", "DF-002", "DF-003", "DF-004", "DF-005", "DF-006", "DF-007", "DF-008", "DF-009", "DF-010", "DF-011", "DF-012", "DF-013", "DF-014", "DF-015", "DF-016", "DF-017", "DF-018", "DF-019", "DF-020", "DF-021", "DF-022", "DF-023", "DF-024", "DF-025", "DF-026" |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Fine-grained error codes for data-files REST operations.  For operations which do not have a more fine-grained error code, the error code is set to the HTTP status code.<p>Members:</p><ul><li><i>DF-001</i> - The page cursor passed as a parameter to the GET operation is invalid.</li><li><i>DF-002</i> - The sort specification passed as a parameter to the GET operation is invalid.</li><li><i>DF-003</i> - FolderPath and FolderId are mutually exclusive, they cannot both be passed as parameters.</li><li><i>DF-004</i> - The provided FolderPath must be in canonical form.</li><li><i>DF-005</i> - The specified parent folder cannot be found.</li><li><i>DF-006</i> - The specified owner cannot be found.</li><li><i>DF-007</i> - A connection corresponding to the specified space cannot be found.</li><li><i>DF-008</i> - THe specified ID must correspond to a folder, not a file.</li><li><i>DF-009</i> - The specified space cannot be found.</li><li><i>DF-010</i> - The specified file name contains an invalid file extension.</li><li><i>DF-011</i> - The specified file name is missing a file extension.</li><li><i>DF-012</i> - The specified temporary content file could not be found.</li><li><i>DF-013</i> - Access to the specified space is forbidden.</li><li><i>DF-014</i> - The specified connection cannot be found.</li><li><i>DF-015</i> - The provided filename must be in canonical form.</li><li><i>DF-016</i> - The datafile size quota for the given personal space has been exceeded.</li><li><i>DF-017</i> - The specified source file or folder could not be found.</li><li><i>DF-018</i> - The source and target of a datafile operation must either both be folders or both be files, but they are             not.</li><li><i>DF-019</i> - The specified target folder is a child of the specified source folder, which is not allowed.</li><li><i>DF-020</i> - The specified folder does not exist in the specified space.</li><li><i>DF-021</i> - The specified source file or folder is already locked.</li><li><i>DF-022</i> - The automatic creation of a missing parent folder failed.</li><li><i>DF-023</i> - An attempt to lock a parent folder of a given data file item failed.</li><li><i>DF-024</i> - The attempt to copy a source file or folder to a target failed.</li><li><i>DF-025</i> - The specified target file or folder is already locked.</li><li><i>DF-026</i> - The request results in the creation of a folder hierarchy which is beyond the max allowed folder             hierarchy depth.</li></ul> Enum: "HTTP-200", "HTTP-201", "HTTP-204", "HTTP-400", "HTTP-403", "HTTP-404", "HTTP-409", "HTTP-413", "HTTP-423", "HTTP-500", "HTTP-501", "HTTP-503", "DF-001", "DF-002", "DF-003", "DF-004", "DF-005", "DF-006", "DF-007", "DF-008", "DF-009", "DF-010", "DF-011", "DF-012", "DF-013", "DF-014", "DF-015", "DF-016", "DF-017", "DF-018", "DF-019", "DF-020", "DF-021", "DF-022", "DF-023", "DF-024", "DF-025", "DF-026" |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 409

A file or folder with the same name already exists in the specified user or app scope.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Fine-grained error codes for data-files REST operations.  For operations which do not have a more fine-grained error code, the error code is set to the HTTP status code.<p>Members:</p><ul><li><i>DF-001</i> - The page cursor passed as a parameter to the GET operation is invalid.</li><li><i>DF-002</i> - The sort specification passed as a parameter to the GET operation is invalid.</li><li><i>DF-003</i> - FolderPath and FolderId are mutually exclusive, they cannot both be passed as parameters.</li><li><i>DF-004</i> - The provided FolderPath must be in canonical form.</li><li><i>DF-005</i> - The specified parent folder cannot be found.</li><li><i>DF-006</i> - The specified owner cannot be found.</li><li><i>DF-007</i> - A connection corresponding to the specified space cannot be found.</li><li><i>DF-008</i> - THe specified ID must correspond to a folder, not a file.</li><li><i>DF-009</i> - The specified space cannot be found.</li><li><i>DF-010</i> - The specified file name contains an invalid file extension.</li><li><i>DF-011</i> - The specified file name is missing a file extension.</li><li><i>DF-012</i> - The specified temporary content file could not be found.</li><li><i>DF-013</i> - Access to the specified space is forbidden.</li><li><i>DF-014</i> - The specified connection cannot be found.</li><li><i>DF-015</i> - The provided filename must be in canonical form.</li><li><i>DF-016</i> - The datafile size quota for the given personal space has been exceeded.</li><li><i>DF-017</i> - The specified source file or folder could not be found.</li><li><i>DF-018</i> - The source and target of a datafile operation must either both be folders or both be files, but they are             not.</li><li><i>DF-019</i> - The specified target folder is a child of the specified source folder, which is not allowed.</li><li><i>DF-020</i> - The specified folder does not exist in the specified space.</li><li><i>DF-021</i> - The specified source file or folder is already locked.</li><li><i>DF-022</i> - The automatic creation of a missing parent folder failed.</li><li><i>DF-023</i> - An attempt to lock a parent folder of a given data file item failed.</li><li><i>DF-024</i> - The attempt to copy a source file or folder to a target failed.</li><li><i>DF-025</i> - The specified target file or folder is already locked.</li><li><i>DF-026</i> - The request results in the creation of a folder hierarchy which is beyond the max allowed folder             hierarchy depth.</li></ul> Enum: "HTTP-200", "HTTP-201", "HTTP-204", "HTTP-400", "HTTP-403", "HTTP-404", "HTTP-409", "HTTP-413", "HTTP-423", "HTTP-500", "HTTP-501", "HTTP-503", "DF-001", "DF-002", "DF-003", "DF-004", "DF-005", "DF-006", "DF-007", "DF-008", "DF-009", "DF-010", "DF-011", "DF-012", "DF-013", "DF-014", "DF-015", "DF-016", "DF-017", "DF-018", "DF-019", "DF-020", "DF-021", "DF-022", "DF-023", "DF-024", "DF-025", "DF-026" |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 413

The file exceeds the user's quota for maximum file size to upload.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Fine-grained error codes for data-files REST operations.  For operations which do not have a more fine-grained error code, the error code is set to the HTTP status code.<p>Members:</p><ul><li><i>DF-001</i> - The page cursor passed as a parameter to the GET operation is invalid.</li><li><i>DF-002</i> - The sort specification passed as a parameter to the GET operation is invalid.</li><li><i>DF-003</i> - FolderPath and FolderId are mutually exclusive, they cannot both be passed as parameters.</li><li><i>DF-004</i> - The provided FolderPath must be in canonical form.</li><li><i>DF-005</i> - The specified parent folder cannot be found.</li><li><i>DF-006</i> - The specified owner cannot be found.</li><li><i>DF-007</i> - A connection corresponding to the specified space cannot be found.</li><li><i>DF-008</i> - THe specified ID must correspond to a folder, not a file.</li><li><i>DF-009</i> - The specified space cannot be found.</li><li><i>DF-010</i> - The specified file name contains an invalid file extension.</li><li><i>DF-011</i> - The specified file name is missing a file extension.</li><li><i>DF-012</i> - The specified temporary content file could not be found.</li><li><i>DF-013</i> - Access to the specified space is forbidden.</li><li><i>DF-014</i> - The specified connection cannot be found.</li><li><i>DF-015</i> - The provided filename must be in canonical form.</li><li><i>DF-016</i> - The datafile size quota for the given personal space has been exceeded.</li><li><i>DF-017</i> - The specified source file or folder could not be found.</li><li><i>DF-018</i> - The source and target of a datafile operation must either both be folders or both be files, but they are             not.</li><li><i>DF-019</i> - The specified target folder is a child of the specified source folder, which is not allowed.</li><li><i>DF-020</i> - The specified folder does not exist in the specified space.</li><li><i>DF-021</i> - The specified source file or folder is already locked.</li><li><i>DF-022</i> - The automatic creation of a missing parent folder failed.</li><li><i>DF-023</i> - An attempt to lock a parent folder of a given data file item failed.</li><li><i>DF-024</i> - The attempt to copy a source file or folder to a target failed.</li><li><i>DF-025</i> - The specified target file or folder is already locked.</li><li><i>DF-026</i> - The request results in the creation of a folder hierarchy which is beyond the max allowed folder             hierarchy depth.</li></ul> Enum: "HTTP-200", "HTTP-201", "HTTP-204", "HTTP-400", "HTTP-403", "HTTP-404", "HTTP-409", "HTTP-413", "HTTP-423", "HTTP-500", "HTTP-501", "HTTP-503", "DF-001", "DF-002", "DF-003", "DF-004", "DF-005", "DF-006", "DF-007", "DF-008", "DF-009", "DF-010", "DF-011", "DF-012", "DF-013", "DF-014", "DF-015", "DF-016", "DF-017", "DF-018", "DF-019", "DF-020", "DF-021", "DF-022", "DF-023", "DF-024", "DF-025", "DF-026" |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 423

The file is already locked for read or write by another client.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Fine-grained error codes for data-files REST operations.  For operations which do not have a more fine-grained error code, the error code is set to the HTTP status code.<p>Members:</p><ul><li><i>DF-001</i> - The page cursor passed as a parameter to the GET operation is invalid.</li><li><i>DF-002</i> - The sort specification passed as a parameter to the GET operation is invalid.</li><li><i>DF-003</i> - FolderPath and FolderId are mutually exclusive, they cannot both be passed as parameters.</li><li><i>DF-004</i> - The provided FolderPath must be in canonical form.</li><li><i>DF-005</i> - The specified parent folder cannot be found.</li><li><i>DF-006</i> - The specified owner cannot be found.</li><li><i>DF-007</i> - A connection corresponding to the specified space cannot be found.</li><li><i>DF-008</i> - THe specified ID must correspond to a folder, not a file.</li><li><i>DF-009</i> - The specified space cannot be found.</li><li><i>DF-010</i> - The specified file name contains an invalid file extension.</li><li><i>DF-011</i> - The specified file name is missing a file extension.</li><li><i>DF-012</i> - The specified temporary content file could not be found.</li><li><i>DF-013</i> - Access to the specified space is forbidden.</li><li><i>DF-014</i> - The specified connection cannot be found.</li><li><i>DF-015</i> - The provided filename must be in canonical form.</li><li><i>DF-016</i> - The datafile size quota for the given personal space has been exceeded.</li><li><i>DF-017</i> - The specified source file or folder could not be found.</li><li><i>DF-018</i> - The source and target of a datafile operation must either both be folders or both be files, but they are             not.</li><li><i>DF-019</i> - The specified target folder is a child of the specified source folder, which is not allowed.</li><li><i>DF-020</i> - The specified folder does not exist in the specified space.</li><li><i>DF-021</i> - The specified source file or folder is already locked.</li><li><i>DF-022</i> - The automatic creation of a missing parent folder failed.</li><li><i>DF-023</i> - An attempt to lock a parent folder of a given data file item failed.</li><li><i>DF-024</i> - The attempt to copy a source file or folder to a target failed.</li><li><i>DF-025</i> - The specified target file or folder is already locked.</li><li><i>DF-026</i> - The request results in the creation of a folder hierarchy which is beyond the max allowed folder             hierarchy depth.</li></ul> Enum: "HTTP-200", "HTTP-201", "HTTP-204", "HTTP-400", "HTTP-403", "HTTP-404", "HTTP-409", "HTTP-413", "HTTP-423", "HTTP-500", "HTTP-501", "HTTP-503", "DF-001", "DF-002", "DF-003", "DF-004", "DF-005", "DF-006", "DF-007", "DF-008", "DF-009", "DF-010", "DF-011", "DF-012", "DF-013", "DF-014", "DF-015", "DF-016", "DF-017", "DF-018", "DF-019", "DF-020", "DF-021", "DF-022", "DF-023", "DF-024", "DF-025", "DF-026" |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 501

Not Implemented

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Fine-grained error codes for data-files REST operations.  For operations which do not have a more fine-grained error code, the error code is set to the HTTP status code.<p>Members:</p><ul><li><i>DF-001</i> - The page cursor passed as a parameter to the GET operation is invalid.</li><li><i>DF-002</i> - The sort specification passed as a parameter to the GET operation is invalid.</li><li><i>DF-003</i> - FolderPath and FolderId are mutually exclusive, they cannot both be passed as parameters.</li><li><i>DF-004</i> - The provided FolderPath must be in canonical form.</li><li><i>DF-005</i> - The specified parent folder cannot be found.</li><li><i>DF-006</i> - The specified owner cannot be found.</li><li><i>DF-007</i> - A connection corresponding to the specified space cannot be found.</li><li><i>DF-008</i> - THe specified ID must correspond to a folder, not a file.</li><li><i>DF-009</i> - The specified space cannot be found.</li><li><i>DF-010</i> - The specified file name contains an invalid file extension.</li><li><i>DF-011</i> - The specified file name is missing a file extension.</li><li><i>DF-012</i> - The specified temporary content file could not be found.</li><li><i>DF-013</i> - Access to the specified space is forbidden.</li><li><i>DF-014</i> - The specified connection cannot be found.</li><li><i>DF-015</i> - The provided filename must be in canonical form.</li><li><i>DF-016</i> - The datafile size quota for the given personal space has been exceeded.</li><li><i>DF-017</i> - The specified source file or folder could not be found.</li><li><i>DF-018</i> - The source and target of a datafile operation must either both be folders or both be files, but they are             not.</li><li><i>DF-019</i> - The specified target folder is a child of the specified source folder, which is not allowed.</li><li><i>DF-020</i> - The specified folder does not exist in the specified space.</li><li><i>DF-021</i> - The specified source file or folder is already locked.</li><li><i>DF-022</i> - The automatic creation of a missing parent folder failed.</li><li><i>DF-023</i> - An attempt to lock a parent folder of a given data file item failed.</li><li><i>DF-024</i> - The attempt to copy a source file or folder to a target failed.</li><li><i>DF-025</i> - The specified target file or folder is already locked.</li><li><i>DF-026</i> - The request results in the creation of a folder hierarchy which is beyond the max allowed folder             hierarchy depth.</li></ul> Enum: "HTTP-200", "HTTP-201", "HTTP-204", "HTTP-400", "HTTP-403", "HTTP-404", "HTTP-409", "HTTP-413", "HTTP-423", "HTTP-500", "HTTP-501", "HTTP-503", "DF-001", "DF-002", "DF-003", "DF-004", "DF-005", "DF-006", "DF-007", "DF-008", "DF-009", "DF-010", "DF-011", "DF-012", "DF-013", "DF-014", "DF-015", "DF-016", "DF-017", "DF-018", "DF-019", "DF-020", "DF-021", "DF-022", "DF-023", "DF-024", "DF-025", "DF-026" |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/data-files` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-files',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/data-files yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-files" \
-X POST \
-H "Content-type: multipart/form-data" \
-H "Authorization: Bearer <access_token>" \
-F "File=@/path/to/file" \
-F "Json={\"name\":\"some/folder/MyFile.csv\",\"appId\":\"f34b91a1-0dc3-44ac-a847-51cb84122c84\",\"folder\":false,\"folderId\":\"ee6a390c-5d33-11e8-9c2d-fa7ae01bbebc\",\"sourceId\":\"f34b91a1-0dc3-44ac-a847-51cb84122c84\",\"connectionId\":\"ee6a390c-5d33-11e8-9c2d-fa7ae01bbebc\",\"tempContentFileId\":\"624b0f54459f1c00018dade4\"}"
```

**Example Response:**

```json
{
  "id": "ee6a390c-5d33-11e8-9c2d-fa7ae01bbebc",
  "qri": "qri:qdf:space://ooSOGoLLaq7EMaSdSsCiGvLwcd_VAf1oU0mzwSfp_Qs#wME89c8gKu_Tpz8W_a0JKSbKC4hzbNu0NLVgqi2UFS0",
  "name": "some/folder/MyFile.csv",
  "size": 1024,
  "appId": "f34b91a1-0dc3-44ac-a847-51cb84122c84",
  "folder": true,
  "actions": [
    "Read"
  ],
  "ownerId": "lDL4DIINndhL_iJkcbqWyJenuwizP-2D",
  "spaceId": "617979737a9f56e49dea2e6e",
  "baseName": "MyFile.csv",
  "folderId": "ee6a390c-5d33-11e8-9c2d-fa7ae01bbebc",
  "folderPath": "some/folder",
  "createdDate": "2020-07-07T20:52:40.8534780Z",
  "folderStats": {
    "totalFileCount": 50,
    "directFileCount": 50,
    "totalFolderCount": 50,
    "aggregateFileSize": 10000,
    "directFolderCount": 50,
    "totalInternalFileCount": 50,
    "directInternalFileCount": 50,
    "totalAppScopedFileCount": 50,
    "directAppScopedFileCount": 50,
    "aggregateInternalFileSize": 10000,
    "aggregateAppScopedFileSize": 10000
  },
  "modifiedDate": "2020-07-07T20:52:40.8534780Z",
  "contentUpdatedDate": "2020-07-07T20:52:40.8534780Z"
}
```

---

### GET /api/v1/data-files/{id}

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the data file. |

#### Responses

##### 200

The file was located.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID for the file or folder. |
| `qri` | string | No | The QRI generated from the datafile or folder's metadata. |
| `name` | string | Yes | The full name of the file or folder, including any folder path prefix. |
| `size` | integer | Yes | The size of the uploaded file, in bytes.  0 if this item represents a folder |
| `appId` | string | No | If this file or folder is bound to the lifecycle of a specific app, this is the ID of this app. |
| `folder` | boolean | No | Whether or not this given item represents a folder or a file. |
| `actions` | string[] | Yes | The CRUD actions that are allowed on the given data file. Enum: "read", "update", "delete", "list", "change_owner", "change_space" |
| `ownerId` | string | Yes | The 'owner' of a file or folder is the user who last uploaded the item's content. |
| `spaceId` | string | No | If the file or folder was created in a team space, this is the ID of that space. |
| `baseName` | string | No | The name of the file or folder, not including any folder path prefix. |
| `folderId` | string | No | If the file or folder resides in a parent folder, this is the parent folder ID.  If the file or folder does not reside in a parent folder, this value is null. |
| `folderPath` | string | No | If the file or folder resides in a parent folder, this is the parent folder path.  If the file or folder does not reside in a parent folder, this value is null. |
| `createdDate` | string | Yes | The date that the file or folder was created. |
| `folderStats` | object | Yes |  |
| `modifiedDate` | string | No | The date that the updated file or folder was last modified. |
| `contentUpdatedDate` | string | No | If the data file's content was updated, this is the DateTime of the last content update. |

<details>
<summary>Properties of `folderStats`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `totalFileCount` | integer | Yes | The number of data files that reside as direct and indirect children of the given folder and it's sub-folder hierarchy. |
| `directFileCount` | integer | Yes | The number of data files that reside as direct children of the given folder. |
| `totalFolderCount` | integer | Yes | The number of folders that reside as direct and indirect children of the given folder and it's sub-folder hierarchy. |
| `aggregateFileSize` | integer | Yes | The sum of the file sizes, in bytes, of all data files that reside as direct and indirect children of the given folder and it's sub-folder hierarchy. |
| `directFolderCount` | integer | Yes | The number of sub-folders that reside as direct children of the given folder. |
| `totalInternalFileCount` | integer | Yes | The number of 'internal' data files (IE, those that are not visible to end users by default) that reside as direct and indirect children of the given folder and it's sub-folder hierarchy. |
| `directInternalFileCount` | integer | Yes | The number of 'internal' data files (IE, those that are not visible to end users by default) that reside as direct children of the given folder. |
| `totalAppScopedFileCount` | integer | Yes | The number of app-scoped data files that reside as direct and indirect children of the given folder and it's sub-folder hierarchy. |
| `directAppScopedFileCount` | integer | Yes | The number of app-scoped data files that reside as direct children of the given folder. |
| `aggregateInternalFileSize` | integer | Yes | The sum of the file sizes, in bytes, of all internal data files that reside as direct and indirect children of the given folder and it's sub-folder hierarchy. |
| `aggregateAppScopedFileSize` | integer | Yes | The sum of the file sizes, in bytes, of all app-scoped data files that reside as direct and indirect children of the given folder and it's sub-folder hierarchy. |

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Fine-grained error codes for data-files REST operations.  For operations which do not have a more fine-grained error code, the error code is set to the HTTP status code.<p>Members:</p><ul><li><i>DF-001</i> - The page cursor passed as a parameter to the GET operation is invalid.</li><li><i>DF-002</i> - The sort specification passed as a parameter to the GET operation is invalid.</li><li><i>DF-003</i> - FolderPath and FolderId are mutually exclusive, they cannot both be passed as parameters.</li><li><i>DF-004</i> - The provided FolderPath must be in canonical form.</li><li><i>DF-005</i> - The specified parent folder cannot be found.</li><li><i>DF-006</i> - The specified owner cannot be found.</li><li><i>DF-007</i> - A connection corresponding to the specified space cannot be found.</li><li><i>DF-008</i> - THe specified ID must correspond to a folder, not a file.</li><li><i>DF-009</i> - The specified space cannot be found.</li><li><i>DF-010</i> - The specified file name contains an invalid file extension.</li><li><i>DF-011</i> - The specified file name is missing a file extension.</li><li><i>DF-012</i> - The specified temporary content file could not be found.</li><li><i>DF-013</i> - Access to the specified space is forbidden.</li><li><i>DF-014</i> - The specified connection cannot be found.</li><li><i>DF-015</i> - The provided filename must be in canonical form.</li><li><i>DF-016</i> - The datafile size quota for the given personal space has been exceeded.</li><li><i>DF-017</i> - The specified source file or folder could not be found.</li><li><i>DF-018</i> - The source and target of a datafile operation must either both be folders or both be files, but they are             not.</li><li><i>DF-019</i> - The specified target folder is a child of the specified source folder, which is not allowed.</li><li><i>DF-020</i> - The specified folder does not exist in the specified space.</li><li><i>DF-021</i> - The specified source file or folder is already locked.</li><li><i>DF-022</i> - The automatic creation of a missing parent folder failed.</li><li><i>DF-023</i> - An attempt to lock a parent folder of a given data file item failed.</li><li><i>DF-024</i> - The attempt to copy a source file or folder to a target failed.</li><li><i>DF-025</i> - The specified target file or folder is already locked.</li><li><i>DF-026</i> - The request results in the creation of a folder hierarchy which is beyond the max allowed folder             hierarchy depth.</li></ul> Enum: "HTTP-200", "HTTP-201", "HTTP-204", "HTTP-400", "HTTP-403", "HTTP-404", "HTTP-409", "HTTP-413", "HTTP-423", "HTTP-500", "HTTP-501", "HTTP-503", "DF-001", "DF-002", "DF-003", "DF-004", "DF-005", "DF-006", "DF-007", "DF-008", "DF-009", "DF-010", "DF-011", "DF-012", "DF-013", "DF-014", "DF-015", "DF-016", "DF-017", "DF-018", "DF-019", "DF-020", "DF-021", "DF-022", "DF-023", "DF-024", "DF-025", "DF-026" |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Fine-grained error codes for data-files REST operations.  For operations which do not have a more fine-grained error code, the error code is set to the HTTP status code.<p>Members:</p><ul><li><i>DF-001</i> - The page cursor passed as a parameter to the GET operation is invalid.</li><li><i>DF-002</i> - The sort specification passed as a parameter to the GET operation is invalid.</li><li><i>DF-003</i> - FolderPath and FolderId are mutually exclusive, they cannot both be passed as parameters.</li><li><i>DF-004</i> - The provided FolderPath must be in canonical form.</li><li><i>DF-005</i> - The specified parent folder cannot be found.</li><li><i>DF-006</i> - The specified owner cannot be found.</li><li><i>DF-007</i> - A connection corresponding to the specified space cannot be found.</li><li><i>DF-008</i> - THe specified ID must correspond to a folder, not a file.</li><li><i>DF-009</i> - The specified space cannot be found.</li><li><i>DF-010</i> - The specified file name contains an invalid file extension.</li><li><i>DF-011</i> - The specified file name is missing a file extension.</li><li><i>DF-012</i> - The specified temporary content file could not be found.</li><li><i>DF-013</i> - Access to the specified space is forbidden.</li><li><i>DF-014</i> - The specified connection cannot be found.</li><li><i>DF-015</i> - The provided filename must be in canonical form.</li><li><i>DF-016</i> - The datafile size quota for the given personal space has been exceeded.</li><li><i>DF-017</i> - The specified source file or folder could not be found.</li><li><i>DF-018</i> - The source and target of a datafile operation must either both be folders or both be files, but they are             not.</li><li><i>DF-019</i> - The specified target folder is a child of the specified source folder, which is not allowed.</li><li><i>DF-020</i> - The specified folder does not exist in the specified space.</li><li><i>DF-021</i> - The specified source file or folder is already locked.</li><li><i>DF-022</i> - The automatic creation of a missing parent folder failed.</li><li><i>DF-023</i> - An attempt to lock a parent folder of a given data file item failed.</li><li><i>DF-024</i> - The attempt to copy a source file or folder to a target failed.</li><li><i>DF-025</i> - The specified target file or folder is already locked.</li><li><i>DF-026</i> - The request results in the creation of a folder hierarchy which is beyond the max allowed folder             hierarchy depth.</li></ul> Enum: "HTTP-200", "HTTP-201", "HTTP-204", "HTTP-400", "HTTP-403", "HTTP-404", "HTTP-409", "HTTP-413", "HTTP-423", "HTTP-500", "HTTP-501", "HTTP-503", "DF-001", "DF-002", "DF-003", "DF-004", "DF-005", "DF-006", "DF-007", "DF-008", "DF-009", "DF-010", "DF-011", "DF-012", "DF-013", "DF-014", "DF-015", "DF-016", "DF-017", "DF-018", "DF-019", "DF-020", "DF-021", "DF-022", "DF-023", "DF-024", "DF-025", "DF-026" |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 404

A data file with the specified ID was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Fine-grained error codes for data-files REST operations.  For operations which do not have a more fine-grained error code, the error code is set to the HTTP status code.<p>Members:</p><ul><li><i>DF-001</i> - The page cursor passed as a parameter to the GET operation is invalid.</li><li><i>DF-002</i> - The sort specification passed as a parameter to the GET operation is invalid.</li><li><i>DF-003</i> - FolderPath and FolderId are mutually exclusive, they cannot both be passed as parameters.</li><li><i>DF-004</i> - The provided FolderPath must be in canonical form.</li><li><i>DF-005</i> - The specified parent folder cannot be found.</li><li><i>DF-006</i> - The specified owner cannot be found.</li><li><i>DF-007</i> - A connection corresponding to the specified space cannot be found.</li><li><i>DF-008</i> - THe specified ID must correspond to a folder, not a file.</li><li><i>DF-009</i> - The specified space cannot be found.</li><li><i>DF-010</i> - The specified file name contains an invalid file extension.</li><li><i>DF-011</i> - The specified file name is missing a file extension.</li><li><i>DF-012</i> - The specified temporary content file could not be found.</li><li><i>DF-013</i> - Access to the specified space is forbidden.</li><li><i>DF-014</i> - The specified connection cannot be found.</li><li><i>DF-015</i> - The provided filename must be in canonical form.</li><li><i>DF-016</i> - The datafile size quota for the given personal space has been exceeded.</li><li><i>DF-017</i> - The specified source file or folder could not be found.</li><li><i>DF-018</i> - The source and target of a datafile operation must either both be folders or both be files, but they are             not.</li><li><i>DF-019</i> - The specified target folder is a child of the specified source folder, which is not allowed.</li><li><i>DF-020</i> - The specified folder does not exist in the specified space.</li><li><i>DF-021</i> - The specified source file or folder is already locked.</li><li><i>DF-022</i> - The automatic creation of a missing parent folder failed.</li><li><i>DF-023</i> - An attempt to lock a parent folder of a given data file item failed.</li><li><i>DF-024</i> - The attempt to copy a source file or folder to a target failed.</li><li><i>DF-025</i> - The specified target file or folder is already locked.</li><li><i>DF-026</i> - The request results in the creation of a folder hierarchy which is beyond the max allowed folder             hierarchy depth.</li></ul> Enum: "HTTP-200", "HTTP-201", "HTTP-204", "HTTP-400", "HTTP-403", "HTTP-404", "HTTP-409", "HTTP-413", "HTTP-423", "HTTP-500", "HTTP-501", "HTTP-503", "DF-001", "DF-002", "DF-003", "DF-004", "DF-005", "DF-006", "DF-007", "DF-008", "DF-009", "DF-010", "DF-011", "DF-012", "DF-013", "DF-014", "DF-015", "DF-016", "DF-017", "DF-018", "DF-019", "DF-020", "DF-021", "DF-022", "DF-023", "DF-024", "DF-025", "DF-026" |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/data-files/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-files/{id}',
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
# qlik-cli has not implemented support for GET /api/v1/data-files/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-files/{id}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "ee6a390c-5d33-11e8-9c2d-fa7ae01bbebc",
  "qri": "qri:qdf:space://ooSOGoLLaq7EMaSdSsCiGvLwcd_VAf1oU0mzwSfp_Qs#wME89c8gKu_Tpz8W_a0JKSbKC4hzbNu0NLVgqi2UFS0",
  "name": "some/folder/MyFile.csv",
  "size": 1024,
  "appId": "f34b91a1-0dc3-44ac-a847-51cb84122c84",
  "folder": true,
  "actions": [
    "Read"
  ],
  "ownerId": "lDL4DIINndhL_iJkcbqWyJenuwizP-2D",
  "spaceId": "617979737a9f56e49dea2e6e",
  "baseName": "MyFile.csv",
  "folderId": "ee6a390c-5d33-11e8-9c2d-fa7ae01bbebc",
  "folderPath": "some/folder",
  "createdDate": "2020-07-07T20:52:40.8534780Z",
  "folderStats": {
    "totalFileCount": 50,
    "directFileCount": 50,
    "totalFolderCount": 50,
    "aggregateFileSize": 10000,
    "directFolderCount": 50,
    "totalInternalFileCount": 50,
    "directInternalFileCount": 50,
    "totalAppScopedFileCount": 50,
    "directAppScopedFileCount": 50,
    "aggregateInternalFileSize": 10000,
    "aggregateAppScopedFileSize": 10000
  },
  "modifiedDate": "2020-07-07T20:52:40.8534780Z",
  "contentUpdatedDate": "2020-07-07T20:52:40.8534780Z"
}
```

---

### PUT /api/v1/data-files/{id}

- **Rate Limit:** Special (800 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the data file to update. |

#### Request Body

**Content-Type:** `multipart/form-data`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `File` | string | No | IFormFile form multipart/form-data |
| `Json` | object | No | See PutDataFileRequest schema which defines request structure.  See PutDataFileRequest model. |

<details>
<summary>Properties of `Json`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | string | No | Name that will be given to the file or folder.  If this name is different than the name used when the file or folder was last POSTed or PUT, this will result in a rename of the file or folder.  It should be noted that the '/' character in a data file name indicates a 'path' separator in a logical folder hierarchy for the name.  Names that contain '/'s should be used with the assumption that a logical 'folder hierarchy' is being defined for the full pathname of that file or folder..  '/' is a significant character in the data file or folder name. |
| `appId` | string | No | If this file should be bound to the lifecycle of a specific app, this is the ID of this app.  If this request is creating a folder, the specification of an app ID is not allowed. |
| `folderId` | string | No | If the specified file or folder should be created as a sub-item of an existing folder, this is the ID of this parent folder.  Any additional folder path that is present on the Name property will be created as a subfolder hierarchy of this folder.  If the FolderID is null, the file or folder specified in the Name property (including any folder prefix on that name), will be created in the root of the space. |
| `sourceId` | string | No | If a SourceId is specified, this is the ID of the existing data file or folder whose content should be copied into the specified data file or folder.  That is, for a file instead of the file content being specified in the Data element, it is effectively copied from an existing, previously uploaded file.  For a folder, it's contents are copied from an existing, previously created folder.  If there it existing content in the target folder, then how the source and target folder contents are merged together is specified in the FolderMergeBehavior option. |
| `connectionId` | string | No | If present, this is the DataFiles connection points to the space that the file or folder should reside in. If absent, the default is that the file or folder will reside in the Personal SPce.  If the DataFiles connection is different from the one specified when the file or folder was last POSTed or PUT, this will result in a logical move of this file or folder into the new space. |
| `tempContentFileId` | string | No | If a TempContentFileId is specified, this is the ID of a previously uploaded temporary content file whose content should be copied into the specified data file.  That is, instead of the file content being specified in the Data element, it is effectively copied from an existing, previously uploaded file.  The expectation is that this file was previously uploaded to the temporary content service, and the ID specified here is the one returned from the temp content upload request. |
| `folderMergeBehavior` | string | No | If a SourceId is specified, and a folder is being updated by this PUT operation, this specifies how the source folder contents should be applied to the target folder, if the target folder is not empty.  'merge' implies the contents of the source folder should be merged with the existing target contents.  That is, all existing direct or indirect child items in the target folder are replaced by the same items in the source folder. All existing items in the target folder that are not present in the source folder are left, as is, in the target. 'replace' implies the contents of the source folder should replace the contents of the target folder.  That is, all direct or indirect items in the target folder are removed before the items from the source folder are copied over.  The resulting target folder only contains the items from the source folder.  If not specified, the default behavior is 'merge'.<p>Members:</p><ul></ul> Enum: "merge", "replace" |

</details>

#### Responses

##### 201

The file or folder was updated.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID for the file or folder. |
| `qri` | string | No | The QRI generated from the datafile or folder's metadata. |
| `name` | string | Yes | The full name of the file or folder, including any folder path prefix. |
| `size` | integer | Yes | The size of the uploaded file, in bytes.  0 if this item represents a folder |
| `appId` | string | No | If this file or folder is bound to the lifecycle of a specific app, this is the ID of this app. |
| `folder` | boolean | No | Whether or not this given item represents a folder or a file. |
| `actions` | string[] | Yes | The CRUD actions that are allowed on the given data file. Enum: "read", "update", "delete", "list", "change_owner", "change_space" |
| `ownerId` | string | Yes | The 'owner' of a file or folder is the user who last uploaded the item's content. |
| `spaceId` | string | No | If the file or folder was created in a team space, this is the ID of that space. |
| `baseName` | string | No | The name of the file or folder, not including any folder path prefix. |
| `folderId` | string | No | If the file or folder resides in a parent folder, this is the parent folder ID.  If the file or folder does not reside in a parent folder, this value is null. |
| `folderPath` | string | No | If the file or folder resides in a parent folder, this is the parent folder path.  If the file or folder does not reside in a parent folder, this value is null. |
| `createdDate` | string | Yes | The date that the file or folder was created. |
| `folderStats` | object | Yes |  |
| `modifiedDate` | string | No | The date that the updated file or folder was last modified. |
| `contentUpdatedDate` | string | No | If the data file's content was updated, this is the DateTime of the last content update. |

<details>
<summary>Properties of `folderStats`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `totalFileCount` | integer | Yes | The number of data files that reside as direct and indirect children of the given folder and it's sub-folder hierarchy. |
| `directFileCount` | integer | Yes | The number of data files that reside as direct children of the given folder. |
| `totalFolderCount` | integer | Yes | The number of folders that reside as direct and indirect children of the given folder and it's sub-folder hierarchy. |
| `aggregateFileSize` | integer | Yes | The sum of the file sizes, in bytes, of all data files that reside as direct and indirect children of the given folder and it's sub-folder hierarchy. |
| `directFolderCount` | integer | Yes | The number of sub-folders that reside as direct children of the given folder. |
| `totalInternalFileCount` | integer | Yes | The number of 'internal' data files (IE, those that are not visible to end users by default) that reside as direct and indirect children of the given folder and it's sub-folder hierarchy. |
| `directInternalFileCount` | integer | Yes | The number of 'internal' data files (IE, those that are not visible to end users by default) that reside as direct children of the given folder. |
| `totalAppScopedFileCount` | integer | Yes | The number of app-scoped data files that reside as direct and indirect children of the given folder and it's sub-folder hierarchy. |
| `directAppScopedFileCount` | integer | Yes | The number of app-scoped data files that reside as direct children of the given folder. |
| `aggregateInternalFileSize` | integer | Yes | The sum of the file sizes, in bytes, of all internal data files that reside as direct and indirect children of the given folder and it's sub-folder hierarchy. |
| `aggregateAppScopedFileSize` | integer | Yes | The sum of the file sizes, in bytes, of all app-scoped data files that reside as direct and indirect children of the given folder and it's sub-folder hierarchy. |

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Fine-grained error codes for data-files REST operations.  For operations which do not have a more fine-grained error code, the error code is set to the HTTP status code.<p>Members:</p><ul><li><i>DF-001</i> - The page cursor passed as a parameter to the GET operation is invalid.</li><li><i>DF-002</i> - The sort specification passed as a parameter to the GET operation is invalid.</li><li><i>DF-003</i> - FolderPath and FolderId are mutually exclusive, they cannot both be passed as parameters.</li><li><i>DF-004</i> - The provided FolderPath must be in canonical form.</li><li><i>DF-005</i> - The specified parent folder cannot be found.</li><li><i>DF-006</i> - The specified owner cannot be found.</li><li><i>DF-007</i> - A connection corresponding to the specified space cannot be found.</li><li><i>DF-008</i> - THe specified ID must correspond to a folder, not a file.</li><li><i>DF-009</i> - The specified space cannot be found.</li><li><i>DF-010</i> - The specified file name contains an invalid file extension.</li><li><i>DF-011</i> - The specified file name is missing a file extension.</li><li><i>DF-012</i> - The specified temporary content file could not be found.</li><li><i>DF-013</i> - Access to the specified space is forbidden.</li><li><i>DF-014</i> - The specified connection cannot be found.</li><li><i>DF-015</i> - The provided filename must be in canonical form.</li><li><i>DF-016</i> - The datafile size quota for the given personal space has been exceeded.</li><li><i>DF-017</i> - The specified source file or folder could not be found.</li><li><i>DF-018</i> - The source and target of a datafile operation must either both be folders or both be files, but they are             not.</li><li><i>DF-019</i> - The specified target folder is a child of the specified source folder, which is not allowed.</li><li><i>DF-020</i> - The specified folder does not exist in the specified space.</li><li><i>DF-021</i> - The specified source file or folder is already locked.</li><li><i>DF-022</i> - The automatic creation of a missing parent folder failed.</li><li><i>DF-023</i> - An attempt to lock a parent folder of a given data file item failed.</li><li><i>DF-024</i> - The attempt to copy a source file or folder to a target failed.</li><li><i>DF-025</i> - The specified target file or folder is already locked.</li><li><i>DF-026</i> - The request results in the creation of a folder hierarchy which is beyond the max allowed folder             hierarchy depth.</li></ul> Enum: "HTTP-200", "HTTP-201", "HTTP-204", "HTTP-400", "HTTP-403", "HTTP-404", "HTTP-409", "HTTP-413", "HTTP-423", "HTTP-500", "HTTP-501", "HTTP-503", "DF-001", "DF-002", "DF-003", "DF-004", "DF-005", "DF-006", "DF-007", "DF-008", "DF-009", "DF-010", "DF-011", "DF-012", "DF-013", "DF-014", "DF-015", "DF-016", "DF-017", "DF-018", "DF-019", "DF-020", "DF-021", "DF-022", "DF-023", "DF-024", "DF-025", "DF-026" |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Fine-grained error codes for data-files REST operations.  For operations which do not have a more fine-grained error code, the error code is set to the HTTP status code.<p>Members:</p><ul><li><i>DF-001</i> - The page cursor passed as a parameter to the GET operation is invalid.</li><li><i>DF-002</i> - The sort specification passed as a parameter to the GET operation is invalid.</li><li><i>DF-003</i> - FolderPath and FolderId are mutually exclusive, they cannot both be passed as parameters.</li><li><i>DF-004</i> - The provided FolderPath must be in canonical form.</li><li><i>DF-005</i> - The specified parent folder cannot be found.</li><li><i>DF-006</i> - The specified owner cannot be found.</li><li><i>DF-007</i> - A connection corresponding to the specified space cannot be found.</li><li><i>DF-008</i> - THe specified ID must correspond to a folder, not a file.</li><li><i>DF-009</i> - The specified space cannot be found.</li><li><i>DF-010</i> - The specified file name contains an invalid file extension.</li><li><i>DF-011</i> - The specified file name is missing a file extension.</li><li><i>DF-012</i> - The specified temporary content file could not be found.</li><li><i>DF-013</i> - Access to the specified space is forbidden.</li><li><i>DF-014</i> - The specified connection cannot be found.</li><li><i>DF-015</i> - The provided filename must be in canonical form.</li><li><i>DF-016</i> - The datafile size quota for the given personal space has been exceeded.</li><li><i>DF-017</i> - The specified source file or folder could not be found.</li><li><i>DF-018</i> - The source and target of a datafile operation must either both be folders or both be files, but they are             not.</li><li><i>DF-019</i> - The specified target folder is a child of the specified source folder, which is not allowed.</li><li><i>DF-020</i> - The specified folder does not exist in the specified space.</li><li><i>DF-021</i> - The specified source file or folder is already locked.</li><li><i>DF-022</i> - The automatic creation of a missing parent folder failed.</li><li><i>DF-023</i> - An attempt to lock a parent folder of a given data file item failed.</li><li><i>DF-024</i> - The attempt to copy a source file or folder to a target failed.</li><li><i>DF-025</i> - The specified target file or folder is already locked.</li><li><i>DF-026</i> - The request results in the creation of a folder hierarchy which is beyond the max allowed folder             hierarchy depth.</li></ul> Enum: "HTTP-200", "HTTP-201", "HTTP-204", "HTTP-400", "HTTP-403", "HTTP-404", "HTTP-409", "HTTP-413", "HTTP-423", "HTTP-500", "HTTP-501", "HTTP-503", "DF-001", "DF-002", "DF-003", "DF-004", "DF-005", "DF-006", "DF-007", "DF-008", "DF-009", "DF-010", "DF-011", "DF-012", "DF-013", "DF-014", "DF-015", "DF-016", "DF-017", "DF-018", "DF-019", "DF-020", "DF-021", "DF-022", "DF-023", "DF-024", "DF-025", "DF-026" |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 404

A data file or folder with the specified ID was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Fine-grained error codes for data-files REST operations.  For operations which do not have a more fine-grained error code, the error code is set to the HTTP status code.<p>Members:</p><ul><li><i>DF-001</i> - The page cursor passed as a parameter to the GET operation is invalid.</li><li><i>DF-002</i> - The sort specification passed as a parameter to the GET operation is invalid.</li><li><i>DF-003</i> - FolderPath and FolderId are mutually exclusive, they cannot both be passed as parameters.</li><li><i>DF-004</i> - The provided FolderPath must be in canonical form.</li><li><i>DF-005</i> - The specified parent folder cannot be found.</li><li><i>DF-006</i> - The specified owner cannot be found.</li><li><i>DF-007</i> - A connection corresponding to the specified space cannot be found.</li><li><i>DF-008</i> - THe specified ID must correspond to a folder, not a file.</li><li><i>DF-009</i> - The specified space cannot be found.</li><li><i>DF-010</i> - The specified file name contains an invalid file extension.</li><li><i>DF-011</i> - The specified file name is missing a file extension.</li><li><i>DF-012</i> - The specified temporary content file could not be found.</li><li><i>DF-013</i> - Access to the specified space is forbidden.</li><li><i>DF-014</i> - The specified connection cannot be found.</li><li><i>DF-015</i> - The provided filename must be in canonical form.</li><li><i>DF-016</i> - The datafile size quota for the given personal space has been exceeded.</li><li><i>DF-017</i> - The specified source file or folder could not be found.</li><li><i>DF-018</i> - The source and target of a datafile operation must either both be folders or both be files, but they are             not.</li><li><i>DF-019</i> - The specified target folder is a child of the specified source folder, which is not allowed.</li><li><i>DF-020</i> - The specified folder does not exist in the specified space.</li><li><i>DF-021</i> - The specified source file or folder is already locked.</li><li><i>DF-022</i> - The automatic creation of a missing parent folder failed.</li><li><i>DF-023</i> - An attempt to lock a parent folder of a given data file item failed.</li><li><i>DF-024</i> - The attempt to copy a source file or folder to a target failed.</li><li><i>DF-025</i> - The specified target file or folder is already locked.</li><li><i>DF-026</i> - The request results in the creation of a folder hierarchy which is beyond the max allowed folder             hierarchy depth.</li></ul> Enum: "HTTP-200", "HTTP-201", "HTTP-204", "HTTP-400", "HTTP-403", "HTTP-404", "HTTP-409", "HTTP-413", "HTTP-423", "HTTP-500", "HTTP-501", "HTTP-503", "DF-001", "DF-002", "DF-003", "DF-004", "DF-005", "DF-006", "DF-007", "DF-008", "DF-009", "DF-010", "DF-011", "DF-012", "DF-013", "DF-014", "DF-015", "DF-016", "DF-017", "DF-018", "DF-019", "DF-020", "DF-021", "DF-022", "DF-023", "DF-024", "DF-025", "DF-026" |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 409

If the file or folder was renamed during the update, a file or folder with the new name
            already exists.  Also, if the space that the file or folder resides in was changed as part of the update,
            a file or folder with the same name already resides in the new space.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Fine-grained error codes for data-files REST operations.  For operations which do not have a more fine-grained error code, the error code is set to the HTTP status code.<p>Members:</p><ul><li><i>DF-001</i> - The page cursor passed as a parameter to the GET operation is invalid.</li><li><i>DF-002</i> - The sort specification passed as a parameter to the GET operation is invalid.</li><li><i>DF-003</i> - FolderPath and FolderId are mutually exclusive, they cannot both be passed as parameters.</li><li><i>DF-004</i> - The provided FolderPath must be in canonical form.</li><li><i>DF-005</i> - The specified parent folder cannot be found.</li><li><i>DF-006</i> - The specified owner cannot be found.</li><li><i>DF-007</i> - A connection corresponding to the specified space cannot be found.</li><li><i>DF-008</i> - THe specified ID must correspond to a folder, not a file.</li><li><i>DF-009</i> - The specified space cannot be found.</li><li><i>DF-010</i> - The specified file name contains an invalid file extension.</li><li><i>DF-011</i> - The specified file name is missing a file extension.</li><li><i>DF-012</i> - The specified temporary content file could not be found.</li><li><i>DF-013</i> - Access to the specified space is forbidden.</li><li><i>DF-014</i> - The specified connection cannot be found.</li><li><i>DF-015</i> - The provided filename must be in canonical form.</li><li><i>DF-016</i> - The datafile size quota for the given personal space has been exceeded.</li><li><i>DF-017</i> - The specified source file or folder could not be found.</li><li><i>DF-018</i> - The source and target of a datafile operation must either both be folders or both be files, but they are             not.</li><li><i>DF-019</i> - The specified target folder is a child of the specified source folder, which is not allowed.</li><li><i>DF-020</i> - The specified folder does not exist in the specified space.</li><li><i>DF-021</i> - The specified source file or folder is already locked.</li><li><i>DF-022</i> - The automatic creation of a missing parent folder failed.</li><li><i>DF-023</i> - An attempt to lock a parent folder of a given data file item failed.</li><li><i>DF-024</i> - The attempt to copy a source file or folder to a target failed.</li><li><i>DF-025</i> - The specified target file or folder is already locked.</li><li><i>DF-026</i> - The request results in the creation of a folder hierarchy which is beyond the max allowed folder             hierarchy depth.</li></ul> Enum: "HTTP-200", "HTTP-201", "HTTP-204", "HTTP-400", "HTTP-403", "HTTP-404", "HTTP-409", "HTTP-413", "HTTP-423", "HTTP-500", "HTTP-501", "HTTP-503", "DF-001", "DF-002", "DF-003", "DF-004", "DF-005", "DF-006", "DF-007", "DF-008", "DF-009", "DF-010", "DF-011", "DF-012", "DF-013", "DF-014", "DF-015", "DF-016", "DF-017", "DF-018", "DF-019", "DF-020", "DF-021", "DF-022", "DF-023", "DF-024", "DF-025", "DF-026" |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 413

The file exceeds the user's quota for maximum file size to upload.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Fine-grained error codes for data-files REST operations.  For operations which do not have a more fine-grained error code, the error code is set to the HTTP status code.<p>Members:</p><ul><li><i>DF-001</i> - The page cursor passed as a parameter to the GET operation is invalid.</li><li><i>DF-002</i> - The sort specification passed as a parameter to the GET operation is invalid.</li><li><i>DF-003</i> - FolderPath and FolderId are mutually exclusive, they cannot both be passed as parameters.</li><li><i>DF-004</i> - The provided FolderPath must be in canonical form.</li><li><i>DF-005</i> - The specified parent folder cannot be found.</li><li><i>DF-006</i> - The specified owner cannot be found.</li><li><i>DF-007</i> - A connection corresponding to the specified space cannot be found.</li><li><i>DF-008</i> - THe specified ID must correspond to a folder, not a file.</li><li><i>DF-009</i> - The specified space cannot be found.</li><li><i>DF-010</i> - The specified file name contains an invalid file extension.</li><li><i>DF-011</i> - The specified file name is missing a file extension.</li><li><i>DF-012</i> - The specified temporary content file could not be found.</li><li><i>DF-013</i> - Access to the specified space is forbidden.</li><li><i>DF-014</i> - The specified connection cannot be found.</li><li><i>DF-015</i> - The provided filename must be in canonical form.</li><li><i>DF-016</i> - The datafile size quota for the given personal space has been exceeded.</li><li><i>DF-017</i> - The specified source file or folder could not be found.</li><li><i>DF-018</i> - The source and target of a datafile operation must either both be folders or both be files, but they are             not.</li><li><i>DF-019</i> - The specified target folder is a child of the specified source folder, which is not allowed.</li><li><i>DF-020</i> - The specified folder does not exist in the specified space.</li><li><i>DF-021</i> - The specified source file or folder is already locked.</li><li><i>DF-022</i> - The automatic creation of a missing parent folder failed.</li><li><i>DF-023</i> - An attempt to lock a parent folder of a given data file item failed.</li><li><i>DF-024</i> - The attempt to copy a source file or folder to a target failed.</li><li><i>DF-025</i> - The specified target file or folder is already locked.</li><li><i>DF-026</i> - The request results in the creation of a folder hierarchy which is beyond the max allowed folder             hierarchy depth.</li></ul> Enum: "HTTP-200", "HTTP-201", "HTTP-204", "HTTP-400", "HTTP-403", "HTTP-404", "HTTP-409", "HTTP-413", "HTTP-423", "HTTP-500", "HTTP-501", "HTTP-503", "DF-001", "DF-002", "DF-003", "DF-004", "DF-005", "DF-006", "DF-007", "DF-008", "DF-009", "DF-010", "DF-011", "DF-012", "DF-013", "DF-014", "DF-015", "DF-016", "DF-017", "DF-018", "DF-019", "DF-020", "DF-021", "DF-022", "DF-023", "DF-024", "DF-025", "DF-026" |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 423

The file is already locked for read or write by another client.  If a folder is being
            updated, then if any file or folder in the subfolder hierarchy of this folder is already locked for write.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Fine-grained error codes for data-files REST operations.  For operations which do not have a more fine-grained error code, the error code is set to the HTTP status code.<p>Members:</p><ul><li><i>DF-001</i> - The page cursor passed as a parameter to the GET operation is invalid.</li><li><i>DF-002</i> - The sort specification passed as a parameter to the GET operation is invalid.</li><li><i>DF-003</i> - FolderPath and FolderId are mutually exclusive, they cannot both be passed as parameters.</li><li><i>DF-004</i> - The provided FolderPath must be in canonical form.</li><li><i>DF-005</i> - The specified parent folder cannot be found.</li><li><i>DF-006</i> - The specified owner cannot be found.</li><li><i>DF-007</i> - A connection corresponding to the specified space cannot be found.</li><li><i>DF-008</i> - THe specified ID must correspond to a folder, not a file.</li><li><i>DF-009</i> - The specified space cannot be found.</li><li><i>DF-010</i> - The specified file name contains an invalid file extension.</li><li><i>DF-011</i> - The specified file name is missing a file extension.</li><li><i>DF-012</i> - The specified temporary content file could not be found.</li><li><i>DF-013</i> - Access to the specified space is forbidden.</li><li><i>DF-014</i> - The specified connection cannot be found.</li><li><i>DF-015</i> - The provided filename must be in canonical form.</li><li><i>DF-016</i> - The datafile size quota for the given personal space has been exceeded.</li><li><i>DF-017</i> - The specified source file or folder could not be found.</li><li><i>DF-018</i> - The source and target of a datafile operation must either both be folders or both be files, but they are             not.</li><li><i>DF-019</i> - The specified target folder is a child of the specified source folder, which is not allowed.</li><li><i>DF-020</i> - The specified folder does not exist in the specified space.</li><li><i>DF-021</i> - The specified source file or folder is already locked.</li><li><i>DF-022</i> - The automatic creation of a missing parent folder failed.</li><li><i>DF-023</i> - An attempt to lock a parent folder of a given data file item failed.</li><li><i>DF-024</i> - The attempt to copy a source file or folder to a target failed.</li><li><i>DF-025</i> - The specified target file or folder is already locked.</li><li><i>DF-026</i> - The request results in the creation of a folder hierarchy which is beyond the max allowed folder             hierarchy depth.</li></ul> Enum: "HTTP-200", "HTTP-201", "HTTP-204", "HTTP-400", "HTTP-403", "HTTP-404", "HTTP-409", "HTTP-413", "HTTP-423", "HTTP-500", "HTTP-501", "HTTP-503", "DF-001", "DF-002", "DF-003", "DF-004", "DF-005", "DF-006", "DF-007", "DF-008", "DF-009", "DF-010", "DF-011", "DF-012", "DF-013", "DF-014", "DF-015", "DF-016", "DF-017", "DF-018", "DF-019", "DF-020", "DF-021", "DF-022", "DF-023", "DF-024", "DF-025", "DF-026" |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `PUT /api/v1/data-files/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-files/{id}',
  {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for PUT /api/v1/data-files/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-files/{id}" \
-X PUT \
-H "Content-type: multipart/form-data" \
-H "Authorization: Bearer <access_token>" \
-F "File=@/path/to/file" \
-F "Json={\"name\":\"some/folder/MyFile.csv\",\"appId\":\"f34b91a1-0dc3-44ac-a847-51cb84122c84\",\"folderId\":\"ee6a390c-5d33-11e8-9c2d-fa7ae01bbebc\",\"sourceId\":\"f34b91a1-0dc3-44ac-a847-51cb84122c84\",\"connectionId\":\"ee6a390c-5d33-11e8-9c2d-fa7ae01bbebc\",\"tempContentFileId\":\"624b0f54459f1c00018dade4\",\"folderMergeBehavior\":\"merge\"}"
```

**Example Response:**

```json
{
  "id": "ee6a390c-5d33-11e8-9c2d-fa7ae01bbebc",
  "qri": "qri:qdf:space://ooSOGoLLaq7EMaSdSsCiGvLwcd_VAf1oU0mzwSfp_Qs#wME89c8gKu_Tpz8W_a0JKSbKC4hzbNu0NLVgqi2UFS0",
  "name": "some/folder/MyFile.csv",
  "size": 1024,
  "appId": "f34b91a1-0dc3-44ac-a847-51cb84122c84",
  "folder": true,
  "actions": [
    "Read"
  ],
  "ownerId": "lDL4DIINndhL_iJkcbqWyJenuwizP-2D",
  "spaceId": "617979737a9f56e49dea2e6e",
  "baseName": "MyFile.csv",
  "folderId": "ee6a390c-5d33-11e8-9c2d-fa7ae01bbebc",
  "folderPath": "some/folder",
  "createdDate": "2020-07-07T20:52:40.8534780Z",
  "folderStats": {
    "totalFileCount": 50,
    "directFileCount": 50,
    "totalFolderCount": 50,
    "aggregateFileSize": 10000,
    "directFolderCount": 50,
    "totalInternalFileCount": 50,
    "directInternalFileCount": 50,
    "totalAppScopedFileCount": 50,
    "directAppScopedFileCount": 50,
    "aggregateInternalFileSize": 10000,
    "aggregateAppScopedFileSize": 10000
  },
  "modifiedDate": "2020-07-07T20:52:40.8534780Z",
  "contentUpdatedDate": "2020-07-07T20:52:40.8534780Z"
}
```

---

### DELETE /api/v1/data-files/{id}

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the data file or folder to delete. |

#### Responses

##### 204

The file or folder was deleted.

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Fine-grained error codes for data-files REST operations.  For operations which do not have a more fine-grained error code, the error code is set to the HTTP status code.<p>Members:</p><ul><li><i>DF-001</i> - The page cursor passed as a parameter to the GET operation is invalid.</li><li><i>DF-002</i> - The sort specification passed as a parameter to the GET operation is invalid.</li><li><i>DF-003</i> - FolderPath and FolderId are mutually exclusive, they cannot both be passed as parameters.</li><li><i>DF-004</i> - The provided FolderPath must be in canonical form.</li><li><i>DF-005</i> - The specified parent folder cannot be found.</li><li><i>DF-006</i> - The specified owner cannot be found.</li><li><i>DF-007</i> - A connection corresponding to the specified space cannot be found.</li><li><i>DF-008</i> - THe specified ID must correspond to a folder, not a file.</li><li><i>DF-009</i> - The specified space cannot be found.</li><li><i>DF-010</i> - The specified file name contains an invalid file extension.</li><li><i>DF-011</i> - The specified file name is missing a file extension.</li><li><i>DF-012</i> - The specified temporary content file could not be found.</li><li><i>DF-013</i> - Access to the specified space is forbidden.</li><li><i>DF-014</i> - The specified connection cannot be found.</li><li><i>DF-015</i> - The provided filename must be in canonical form.</li><li><i>DF-016</i> - The datafile size quota for the given personal space has been exceeded.</li><li><i>DF-017</i> - The specified source file or folder could not be found.</li><li><i>DF-018</i> - The source and target of a datafile operation must either both be folders or both be files, but they are             not.</li><li><i>DF-019</i> - The specified target folder is a child of the specified source folder, which is not allowed.</li><li><i>DF-020</i> - The specified folder does not exist in the specified space.</li><li><i>DF-021</i> - The specified source file or folder is already locked.</li><li><i>DF-022</i> - The automatic creation of a missing parent folder failed.</li><li><i>DF-023</i> - An attempt to lock a parent folder of a given data file item failed.</li><li><i>DF-024</i> - The attempt to copy a source file or folder to a target failed.</li><li><i>DF-025</i> - The specified target file or folder is already locked.</li><li><i>DF-026</i> - The request results in the creation of a folder hierarchy which is beyond the max allowed folder             hierarchy depth.</li></ul> Enum: "HTTP-200", "HTTP-201", "HTTP-204", "HTTP-400", "HTTP-403", "HTTP-404", "HTTP-409", "HTTP-413", "HTTP-423", "HTTP-500", "HTTP-501", "HTTP-503", "DF-001", "DF-002", "DF-003", "DF-004", "DF-005", "DF-006", "DF-007", "DF-008", "DF-009", "DF-010", "DF-011", "DF-012", "DF-013", "DF-014", "DF-015", "DF-016", "DF-017", "DF-018", "DF-019", "DF-020", "DF-021", "DF-022", "DF-023", "DF-024", "DF-025", "DF-026" |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Fine-grained error codes for data-files REST operations.  For operations which do not have a more fine-grained error code, the error code is set to the HTTP status code.<p>Members:</p><ul><li><i>DF-001</i> - The page cursor passed as a parameter to the GET operation is invalid.</li><li><i>DF-002</i> - The sort specification passed as a parameter to the GET operation is invalid.</li><li><i>DF-003</i> - FolderPath and FolderId are mutually exclusive, they cannot both be passed as parameters.</li><li><i>DF-004</i> - The provided FolderPath must be in canonical form.</li><li><i>DF-005</i> - The specified parent folder cannot be found.</li><li><i>DF-006</i> - The specified owner cannot be found.</li><li><i>DF-007</i> - A connection corresponding to the specified space cannot be found.</li><li><i>DF-008</i> - THe specified ID must correspond to a folder, not a file.</li><li><i>DF-009</i> - The specified space cannot be found.</li><li><i>DF-010</i> - The specified file name contains an invalid file extension.</li><li><i>DF-011</i> - The specified file name is missing a file extension.</li><li><i>DF-012</i> - The specified temporary content file could not be found.</li><li><i>DF-013</i> - Access to the specified space is forbidden.</li><li><i>DF-014</i> - The specified connection cannot be found.</li><li><i>DF-015</i> - The provided filename must be in canonical form.</li><li><i>DF-016</i> - The datafile size quota for the given personal space has been exceeded.</li><li><i>DF-017</i> - The specified source file or folder could not be found.</li><li><i>DF-018</i> - The source and target of a datafile operation must either both be folders or both be files, but they are             not.</li><li><i>DF-019</i> - The specified target folder is a child of the specified source folder, which is not allowed.</li><li><i>DF-020</i> - The specified folder does not exist in the specified space.</li><li><i>DF-021</i> - The specified source file or folder is already locked.</li><li><i>DF-022</i> - The automatic creation of a missing parent folder failed.</li><li><i>DF-023</i> - An attempt to lock a parent folder of a given data file item failed.</li><li><i>DF-024</i> - The attempt to copy a source file or folder to a target failed.</li><li><i>DF-025</i> - The specified target file or folder is already locked.</li><li><i>DF-026</i> - The request results in the creation of a folder hierarchy which is beyond the max allowed folder             hierarchy depth.</li></ul> Enum: "HTTP-200", "HTTP-201", "HTTP-204", "HTTP-400", "HTTP-403", "HTTP-404", "HTTP-409", "HTTP-413", "HTTP-423", "HTTP-500", "HTTP-501", "HTTP-503", "DF-001", "DF-002", "DF-003", "DF-004", "DF-005", "DF-006", "DF-007", "DF-008", "DF-009", "DF-010", "DF-011", "DF-012", "DF-013", "DF-014", "DF-015", "DF-016", "DF-017", "DF-018", "DF-019", "DF-020", "DF-021", "DF-022", "DF-023", "DF-024", "DF-025", "DF-026" |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 404

A data file or folder with the specified ID was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Fine-grained error codes for data-files REST operations.  For operations which do not have a more fine-grained error code, the error code is set to the HTTP status code.<p>Members:</p><ul><li><i>DF-001</i> - The page cursor passed as a parameter to the GET operation is invalid.</li><li><i>DF-002</i> - The sort specification passed as a parameter to the GET operation is invalid.</li><li><i>DF-003</i> - FolderPath and FolderId are mutually exclusive, they cannot both be passed as parameters.</li><li><i>DF-004</i> - The provided FolderPath must be in canonical form.</li><li><i>DF-005</i> - The specified parent folder cannot be found.</li><li><i>DF-006</i> - The specified owner cannot be found.</li><li><i>DF-007</i> - A connection corresponding to the specified space cannot be found.</li><li><i>DF-008</i> - THe specified ID must correspond to a folder, not a file.</li><li><i>DF-009</i> - The specified space cannot be found.</li><li><i>DF-010</i> - The specified file name contains an invalid file extension.</li><li><i>DF-011</i> - The specified file name is missing a file extension.</li><li><i>DF-012</i> - The specified temporary content file could not be found.</li><li><i>DF-013</i> - Access to the specified space is forbidden.</li><li><i>DF-014</i> - The specified connection cannot be found.</li><li><i>DF-015</i> - The provided filename must be in canonical form.</li><li><i>DF-016</i> - The datafile size quota for the given personal space has been exceeded.</li><li><i>DF-017</i> - The specified source file or folder could not be found.</li><li><i>DF-018</i> - The source and target of a datafile operation must either both be folders or both be files, but they are             not.</li><li><i>DF-019</i> - The specified target folder is a child of the specified source folder, which is not allowed.</li><li><i>DF-020</i> - The specified folder does not exist in the specified space.</li><li><i>DF-021</i> - The specified source file or folder is already locked.</li><li><i>DF-022</i> - The automatic creation of a missing parent folder failed.</li><li><i>DF-023</i> - An attempt to lock a parent folder of a given data file item failed.</li><li><i>DF-024</i> - The attempt to copy a source file or folder to a target failed.</li><li><i>DF-025</i> - The specified target file or folder is already locked.</li><li><i>DF-026</i> - The request results in the creation of a folder hierarchy which is beyond the max allowed folder             hierarchy depth.</li></ul> Enum: "HTTP-200", "HTTP-201", "HTTP-204", "HTTP-400", "HTTP-403", "HTTP-404", "HTTP-409", "HTTP-413", "HTTP-423", "HTTP-500", "HTTP-501", "HTTP-503", "DF-001", "DF-002", "DF-003", "DF-004", "DF-005", "DF-006", "DF-007", "DF-008", "DF-009", "DF-010", "DF-011", "DF-012", "DF-013", "DF-014", "DF-015", "DF-016", "DF-017", "DF-018", "DF-019", "DF-020", "DF-021", "DF-022", "DF-023", "DF-024", "DF-025", "DF-026" |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `DELETE /api/v1/data-files/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-files/{id}',
  {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
    },
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for DELETE /api/v1/data-files/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-files/{id}" \
-X DELETE \
-H "Authorization: Bearer <access_token>"
```

---

### POST /api/v1/data-files/{id}/actions/change-owner

This is primarily an admin type of operation.  In general, the owner of a data file or folder is implicitly
set as part of a create or update operation.  For data files or folders that reside in a personal space,
changing the owner has the effect of moving the data file to the new owner's personal space.  Note that,
If a given file or folder is not in the root of a personal space, this operation will not succeed, since
the parent folder does not reside in the target owner's personal space.  If the owner of a folder in the
root of a personal space is changed, the owner of all subfolders and files within those subfolders will
also recursively change.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the data file or folder whose owner will be updated. |

#### Request Body

The request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `ownerId` | string | Yes | The ID of the new owner. |

#### Responses

##### 204

The file or folder's owner was changed.

##### 400

An owner with the specified ID does not exist.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Fine-grained error codes for data-files REST operations.  For operations which do not have a more fine-grained error code, the error code is set to the HTTP status code.<p>Members:</p><ul><li><i>DF-001</i> - The page cursor passed as a parameter to the GET operation is invalid.</li><li><i>DF-002</i> - The sort specification passed as a parameter to the GET operation is invalid.</li><li><i>DF-003</i> - FolderPath and FolderId are mutually exclusive, they cannot both be passed as parameters.</li><li><i>DF-004</i> - The provided FolderPath must be in canonical form.</li><li><i>DF-005</i> - The specified parent folder cannot be found.</li><li><i>DF-006</i> - The specified owner cannot be found.</li><li><i>DF-007</i> - A connection corresponding to the specified space cannot be found.</li><li><i>DF-008</i> - THe specified ID must correspond to a folder, not a file.</li><li><i>DF-009</i> - The specified space cannot be found.</li><li><i>DF-010</i> - The specified file name contains an invalid file extension.</li><li><i>DF-011</i> - The specified file name is missing a file extension.</li><li><i>DF-012</i> - The specified temporary content file could not be found.</li><li><i>DF-013</i> - Access to the specified space is forbidden.</li><li><i>DF-014</i> - The specified connection cannot be found.</li><li><i>DF-015</i> - The provided filename must be in canonical form.</li><li><i>DF-016</i> - The datafile size quota for the given personal space has been exceeded.</li><li><i>DF-017</i> - The specified source file or folder could not be found.</li><li><i>DF-018</i> - The source and target of a datafile operation must either both be folders or both be files, but they are             not.</li><li><i>DF-019</i> - The specified target folder is a child of the specified source folder, which is not allowed.</li><li><i>DF-020</i> - The specified folder does not exist in the specified space.</li><li><i>DF-021</i> - The specified source file or folder is already locked.</li><li><i>DF-022</i> - The automatic creation of a missing parent folder failed.</li><li><i>DF-023</i> - An attempt to lock a parent folder of a given data file item failed.</li><li><i>DF-024</i> - The attempt to copy a source file or folder to a target failed.</li><li><i>DF-025</i> - The specified target file or folder is already locked.</li><li><i>DF-026</i> - The request results in the creation of a folder hierarchy which is beyond the max allowed folder             hierarchy depth.</li></ul> Enum: "HTTP-200", "HTTP-201", "HTTP-204", "HTTP-400", "HTTP-403", "HTTP-404", "HTTP-409", "HTTP-413", "HTTP-423", "HTTP-500", "HTTP-501", "HTTP-503", "DF-001", "DF-002", "DF-003", "DF-004", "DF-005", "DF-006", "DF-007", "DF-008", "DF-009", "DF-010", "DF-011", "DF-012", "DF-013", "DF-014", "DF-015", "DF-016", "DF-017", "DF-018", "DF-019", "DF-020", "DF-021", "DF-022", "DF-023", "DF-024", "DF-025", "DF-026" |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 403

The user does not have permission to modify the specified data file or folder, or if the
            item does not reside in the root of the space.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Fine-grained error codes for data-files REST operations.  For operations which do not have a more fine-grained error code, the error code is set to the HTTP status code.<p>Members:</p><ul><li><i>DF-001</i> - The page cursor passed as a parameter to the GET operation is invalid.</li><li><i>DF-002</i> - The sort specification passed as a parameter to the GET operation is invalid.</li><li><i>DF-003</i> - FolderPath and FolderId are mutually exclusive, they cannot both be passed as parameters.</li><li><i>DF-004</i> - The provided FolderPath must be in canonical form.</li><li><i>DF-005</i> - The specified parent folder cannot be found.</li><li><i>DF-006</i> - The specified owner cannot be found.</li><li><i>DF-007</i> - A connection corresponding to the specified space cannot be found.</li><li><i>DF-008</i> - THe specified ID must correspond to a folder, not a file.</li><li><i>DF-009</i> - The specified space cannot be found.</li><li><i>DF-010</i> - The specified file name contains an invalid file extension.</li><li><i>DF-011</i> - The specified file name is missing a file extension.</li><li><i>DF-012</i> - The specified temporary content file could not be found.</li><li><i>DF-013</i> - Access to the specified space is forbidden.</li><li><i>DF-014</i> - The specified connection cannot be found.</li><li><i>DF-015</i> - The provided filename must be in canonical form.</li><li><i>DF-016</i> - The datafile size quota for the given personal space has been exceeded.</li><li><i>DF-017</i> - The specified source file or folder could not be found.</li><li><i>DF-018</i> - The source and target of a datafile operation must either both be folders or both be files, but they are             not.</li><li><i>DF-019</i> - The specified target folder is a child of the specified source folder, which is not allowed.</li><li><i>DF-020</i> - The specified folder does not exist in the specified space.</li><li><i>DF-021</i> - The specified source file or folder is already locked.</li><li><i>DF-022</i> - The automatic creation of a missing parent folder failed.</li><li><i>DF-023</i> - An attempt to lock a parent folder of a given data file item failed.</li><li><i>DF-024</i> - The attempt to copy a source file or folder to a target failed.</li><li><i>DF-025</i> - The specified target file or folder is already locked.</li><li><i>DF-026</i> - The request results in the creation of a folder hierarchy which is beyond the max allowed folder             hierarchy depth.</li></ul> Enum: "HTTP-200", "HTTP-201", "HTTP-204", "HTTP-400", "HTTP-403", "HTTP-404", "HTTP-409", "HTTP-413", "HTTP-423", "HTTP-500", "HTTP-501", "HTTP-503", "DF-001", "DF-002", "DF-003", "DF-004", "DF-005", "DF-006", "DF-007", "DF-008", "DF-009", "DF-010", "DF-011", "DF-012", "DF-013", "DF-014", "DF-015", "DF-016", "DF-017", "DF-018", "DF-019", "DF-020", "DF-021", "DF-022", "DF-023", "DF-024", "DF-025", "DF-026" |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 404

A data file or folder with the specified ID was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Fine-grained error codes for data-files REST operations.  For operations which do not have a more fine-grained error code, the error code is set to the HTTP status code.<p>Members:</p><ul><li><i>DF-001</i> - The page cursor passed as a parameter to the GET operation is invalid.</li><li><i>DF-002</i> - The sort specification passed as a parameter to the GET operation is invalid.</li><li><i>DF-003</i> - FolderPath and FolderId are mutually exclusive, they cannot both be passed as parameters.</li><li><i>DF-004</i> - The provided FolderPath must be in canonical form.</li><li><i>DF-005</i> - The specified parent folder cannot be found.</li><li><i>DF-006</i> - The specified owner cannot be found.</li><li><i>DF-007</i> - A connection corresponding to the specified space cannot be found.</li><li><i>DF-008</i> - THe specified ID must correspond to a folder, not a file.</li><li><i>DF-009</i> - The specified space cannot be found.</li><li><i>DF-010</i> - The specified file name contains an invalid file extension.</li><li><i>DF-011</i> - The specified file name is missing a file extension.</li><li><i>DF-012</i> - The specified temporary content file could not be found.</li><li><i>DF-013</i> - Access to the specified space is forbidden.</li><li><i>DF-014</i> - The specified connection cannot be found.</li><li><i>DF-015</i> - The provided filename must be in canonical form.</li><li><i>DF-016</i> - The datafile size quota for the given personal space has been exceeded.</li><li><i>DF-017</i> - The specified source file or folder could not be found.</li><li><i>DF-018</i> - The source and target of a datafile operation must either both be folders or both be files, but they are             not.</li><li><i>DF-019</i> - The specified target folder is a child of the specified source folder, which is not allowed.</li><li><i>DF-020</i> - The specified folder does not exist in the specified space.</li><li><i>DF-021</i> - The specified source file or folder is already locked.</li><li><i>DF-022</i> - The automatic creation of a missing parent folder failed.</li><li><i>DF-023</i> - An attempt to lock a parent folder of a given data file item failed.</li><li><i>DF-024</i> - The attempt to copy a source file or folder to a target failed.</li><li><i>DF-025</i> - The specified target file or folder is already locked.</li><li><i>DF-026</i> - The request results in the creation of a folder hierarchy which is beyond the max allowed folder             hierarchy depth.</li></ul> Enum: "HTTP-200", "HTTP-201", "HTTP-204", "HTTP-400", "HTTP-403", "HTTP-404", "HTTP-409", "HTTP-413", "HTTP-423", "HTTP-500", "HTTP-501", "HTTP-503", "DF-001", "DF-002", "DF-003", "DF-004", "DF-005", "DF-006", "DF-007", "DF-008", "DF-009", "DF-010", "DF-011", "DF-012", "DF-013", "DF-014", "DF-015", "DF-016", "DF-017", "DF-018", "DF-019", "DF-020", "DF-021", "DF-022", "DF-023", "DF-024", "DF-025", "DF-026" |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 409

If the file or folder is in a personal space, and the personal space of the new owner
            already has an item in the space with the same name as the item being moved.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Fine-grained error codes for data-files REST operations.  For operations which do not have a more fine-grained error code, the error code is set to the HTTP status code.<p>Members:</p><ul><li><i>DF-001</i> - The page cursor passed as a parameter to the GET operation is invalid.</li><li><i>DF-002</i> - The sort specification passed as a parameter to the GET operation is invalid.</li><li><i>DF-003</i> - FolderPath and FolderId are mutually exclusive, they cannot both be passed as parameters.</li><li><i>DF-004</i> - The provided FolderPath must be in canonical form.</li><li><i>DF-005</i> - The specified parent folder cannot be found.</li><li><i>DF-006</i> - The specified owner cannot be found.</li><li><i>DF-007</i> - A connection corresponding to the specified space cannot be found.</li><li><i>DF-008</i> - THe specified ID must correspond to a folder, not a file.</li><li><i>DF-009</i> - The specified space cannot be found.</li><li><i>DF-010</i> - The specified file name contains an invalid file extension.</li><li><i>DF-011</i> - The specified file name is missing a file extension.</li><li><i>DF-012</i> - The specified temporary content file could not be found.</li><li><i>DF-013</i> - Access to the specified space is forbidden.</li><li><i>DF-014</i> - The specified connection cannot be found.</li><li><i>DF-015</i> - The provided filename must be in canonical form.</li><li><i>DF-016</i> - The datafile size quota for the given personal space has been exceeded.</li><li><i>DF-017</i> - The specified source file or folder could not be found.</li><li><i>DF-018</i> - The source and target of a datafile operation must either both be folders or both be files, but they are             not.</li><li><i>DF-019</i> - The specified target folder is a child of the specified source folder, which is not allowed.</li><li><i>DF-020</i> - The specified folder does not exist in the specified space.</li><li><i>DF-021</i> - The specified source file or folder is already locked.</li><li><i>DF-022</i> - The automatic creation of a missing parent folder failed.</li><li><i>DF-023</i> - An attempt to lock a parent folder of a given data file item failed.</li><li><i>DF-024</i> - The attempt to copy a source file or folder to a target failed.</li><li><i>DF-025</i> - The specified target file or folder is already locked.</li><li><i>DF-026</i> - The request results in the creation of a folder hierarchy which is beyond the max allowed folder             hierarchy depth.</li></ul> Enum: "HTTP-200", "HTTP-201", "HTTP-204", "HTTP-400", "HTTP-403", "HTTP-404", "HTTP-409", "HTTP-413", "HTTP-423", "HTTP-500", "HTTP-501", "HTTP-503", "DF-001", "DF-002", "DF-003", "DF-004", "DF-005", "DF-006", "DF-007", "DF-008", "DF-009", "DF-010", "DF-011", "DF-012", "DF-013", "DF-014", "DF-015", "DF-016", "DF-017", "DF-018", "DF-019", "DF-020", "DF-021", "DF-022", "DF-023", "DF-024", "DF-025", "DF-026" |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 423

The file or folder is already locked for write by another client.  For folders, any
            write lock on a subfolder or file underneath this folder implies a lock on the folder.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Fine-grained error codes for data-files REST operations.  For operations which do not have a more fine-grained error code, the error code is set to the HTTP status code.<p>Members:</p><ul><li><i>DF-001</i> - The page cursor passed as a parameter to the GET operation is invalid.</li><li><i>DF-002</i> - The sort specification passed as a parameter to the GET operation is invalid.</li><li><i>DF-003</i> - FolderPath and FolderId are mutually exclusive, they cannot both be passed as parameters.</li><li><i>DF-004</i> - The provided FolderPath must be in canonical form.</li><li><i>DF-005</i> - The specified parent folder cannot be found.</li><li><i>DF-006</i> - The specified owner cannot be found.</li><li><i>DF-007</i> - A connection corresponding to the specified space cannot be found.</li><li><i>DF-008</i> - THe specified ID must correspond to a folder, not a file.</li><li><i>DF-009</i> - The specified space cannot be found.</li><li><i>DF-010</i> - The specified file name contains an invalid file extension.</li><li><i>DF-011</i> - The specified file name is missing a file extension.</li><li><i>DF-012</i> - The specified temporary content file could not be found.</li><li><i>DF-013</i> - Access to the specified space is forbidden.</li><li><i>DF-014</i> - The specified connection cannot be found.</li><li><i>DF-015</i> - The provided filename must be in canonical form.</li><li><i>DF-016</i> - The datafile size quota for the given personal space has been exceeded.</li><li><i>DF-017</i> - The specified source file or folder could not be found.</li><li><i>DF-018</i> - The source and target of a datafile operation must either both be folders or both be files, but they are             not.</li><li><i>DF-019</i> - The specified target folder is a child of the specified source folder, which is not allowed.</li><li><i>DF-020</i> - The specified folder does not exist in the specified space.</li><li><i>DF-021</i> - The specified source file or folder is already locked.</li><li><i>DF-022</i> - The automatic creation of a missing parent folder failed.</li><li><i>DF-023</i> - An attempt to lock a parent folder of a given data file item failed.</li><li><i>DF-024</i> - The attempt to copy a source file or folder to a target failed.</li><li><i>DF-025</i> - The specified target file or folder is already locked.</li><li><i>DF-026</i> - The request results in the creation of a folder hierarchy which is beyond the max allowed folder             hierarchy depth.</li></ul> Enum: "HTTP-200", "HTTP-201", "HTTP-204", "HTTP-400", "HTTP-403", "HTTP-404", "HTTP-409", "HTTP-413", "HTTP-423", "HTTP-500", "HTTP-501", "HTTP-503", "DF-001", "DF-002", "DF-003", "DF-004", "DF-005", "DF-006", "DF-007", "DF-008", "DF-009", "DF-010", "DF-011", "DF-012", "DF-013", "DF-014", "DF-015", "DF-016", "DF-017", "DF-018", "DF-019", "DF-020", "DF-021", "DF-022", "DF-023", "DF-024", "DF-025", "DF-026" |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/data-files/{id}/actions/change-owner` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-files/{id}/actions/change-owner',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      ownerId: 'lDL4DIINndhL_iJkcbqWyJenuwizP-2D',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/data-files/{id}/actions/change-owner yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-files/{id}/actions/change-owner" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"ownerId":"lDL4DIINndhL_iJkcbqWyJenuwizP-2D"}'
```

---

### POST /api/v1/data-files/{id}/actions/change-space

This is to allow for a separate admin type of operation that is more global in terms of access in cases
where admin users may not explicitly have been granted full access to a given space within the declared
space-level permissions.  If the space ID is set to null, then the datafile or folder will end up residing
in the personal space of the user who is the owner of the item.  Note that, if a given file or folder is not
in the root of a given space, this operation will not succeed, since the parent folder does not reside in
the target space.  If the space of a folder in the root of the source space is changed, all subfolders and
files within those subfolders will also recursively be moved to the new space.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the data file or folder whose             space will be updated. |

#### Request Body

The request.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `spaceId` | string | No | The ID of the space.  If null, this data file will be moved to the user's personal space. |

#### Responses

##### 204

The file or folder's space was changed.

##### 400

A space with the specified ID does not exist.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Fine-grained error codes for data-files REST operations.  For operations which do not have a more fine-grained error code, the error code is set to the HTTP status code.<p>Members:</p><ul><li><i>DF-001</i> - The page cursor passed as a parameter to the GET operation is invalid.</li><li><i>DF-002</i> - The sort specification passed as a parameter to the GET operation is invalid.</li><li><i>DF-003</i> - FolderPath and FolderId are mutually exclusive, they cannot both be passed as parameters.</li><li><i>DF-004</i> - The provided FolderPath must be in canonical form.</li><li><i>DF-005</i> - The specified parent folder cannot be found.</li><li><i>DF-006</i> - The specified owner cannot be found.</li><li><i>DF-007</i> - A connection corresponding to the specified space cannot be found.</li><li><i>DF-008</i> - THe specified ID must correspond to a folder, not a file.</li><li><i>DF-009</i> - The specified space cannot be found.</li><li><i>DF-010</i> - The specified file name contains an invalid file extension.</li><li><i>DF-011</i> - The specified file name is missing a file extension.</li><li><i>DF-012</i> - The specified temporary content file could not be found.</li><li><i>DF-013</i> - Access to the specified space is forbidden.</li><li><i>DF-014</i> - The specified connection cannot be found.</li><li><i>DF-015</i> - The provided filename must be in canonical form.</li><li><i>DF-016</i> - The datafile size quota for the given personal space has been exceeded.</li><li><i>DF-017</i> - The specified source file or folder could not be found.</li><li><i>DF-018</i> - The source and target of a datafile operation must either both be folders or both be files, but they are             not.</li><li><i>DF-019</i> - The specified target folder is a child of the specified source folder, which is not allowed.</li><li><i>DF-020</i> - The specified folder does not exist in the specified space.</li><li><i>DF-021</i> - The specified source file or folder is already locked.</li><li><i>DF-022</i> - The automatic creation of a missing parent folder failed.</li><li><i>DF-023</i> - An attempt to lock a parent folder of a given data file item failed.</li><li><i>DF-024</i> - The attempt to copy a source file or folder to a target failed.</li><li><i>DF-025</i> - The specified target file or folder is already locked.</li><li><i>DF-026</i> - The request results in the creation of a folder hierarchy which is beyond the max allowed folder             hierarchy depth.</li></ul> Enum: "HTTP-200", "HTTP-201", "HTTP-204", "HTTP-400", "HTTP-403", "HTTP-404", "HTTP-409", "HTTP-413", "HTTP-423", "HTTP-500", "HTTP-501", "HTTP-503", "DF-001", "DF-002", "DF-003", "DF-004", "DF-005", "DF-006", "DF-007", "DF-008", "DF-009", "DF-010", "DF-011", "DF-012", "DF-013", "DF-014", "DF-015", "DF-016", "DF-017", "DF-018", "DF-019", "DF-020", "DF-021", "DF-022", "DF-023", "DF-024", "DF-025", "DF-026" |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 403

The user does not have permission to modify the specified data file or folder, or if the
            item does not reside in the root of the space.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Fine-grained error codes for data-files REST operations.  For operations which do not have a more fine-grained error code, the error code is set to the HTTP status code.<p>Members:</p><ul><li><i>DF-001</i> - The page cursor passed as a parameter to the GET operation is invalid.</li><li><i>DF-002</i> - The sort specification passed as a parameter to the GET operation is invalid.</li><li><i>DF-003</i> - FolderPath and FolderId are mutually exclusive, they cannot both be passed as parameters.</li><li><i>DF-004</i> - The provided FolderPath must be in canonical form.</li><li><i>DF-005</i> - The specified parent folder cannot be found.</li><li><i>DF-006</i> - The specified owner cannot be found.</li><li><i>DF-007</i> - A connection corresponding to the specified space cannot be found.</li><li><i>DF-008</i> - THe specified ID must correspond to a folder, not a file.</li><li><i>DF-009</i> - The specified space cannot be found.</li><li><i>DF-010</i> - The specified file name contains an invalid file extension.</li><li><i>DF-011</i> - The specified file name is missing a file extension.</li><li><i>DF-012</i> - The specified temporary content file could not be found.</li><li><i>DF-013</i> - Access to the specified space is forbidden.</li><li><i>DF-014</i> - The specified connection cannot be found.</li><li><i>DF-015</i> - The provided filename must be in canonical form.</li><li><i>DF-016</i> - The datafile size quota for the given personal space has been exceeded.</li><li><i>DF-017</i> - The specified source file or folder could not be found.</li><li><i>DF-018</i> - The source and target of a datafile operation must either both be folders or both be files, but they are             not.</li><li><i>DF-019</i> - The specified target folder is a child of the specified source folder, which is not allowed.</li><li><i>DF-020</i> - The specified folder does not exist in the specified space.</li><li><i>DF-021</i> - The specified source file or folder is already locked.</li><li><i>DF-022</i> - The automatic creation of a missing parent folder failed.</li><li><i>DF-023</i> - An attempt to lock a parent folder of a given data file item failed.</li><li><i>DF-024</i> - The attempt to copy a source file or folder to a target failed.</li><li><i>DF-025</i> - The specified target file or folder is already locked.</li><li><i>DF-026</i> - The request results in the creation of a folder hierarchy which is beyond the max allowed folder             hierarchy depth.</li></ul> Enum: "HTTP-200", "HTTP-201", "HTTP-204", "HTTP-400", "HTTP-403", "HTTP-404", "HTTP-409", "HTTP-413", "HTTP-423", "HTTP-500", "HTTP-501", "HTTP-503", "DF-001", "DF-002", "DF-003", "DF-004", "DF-005", "DF-006", "DF-007", "DF-008", "DF-009", "DF-010", "DF-011", "DF-012", "DF-013", "DF-014", "DF-015", "DF-016", "DF-017", "DF-018", "DF-019", "DF-020", "DF-021", "DF-022", "DF-023", "DF-024", "DF-025", "DF-026" |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 404

A data file or folder with the specified ID was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Fine-grained error codes for data-files REST operations.  For operations which do not have a more fine-grained error code, the error code is set to the HTTP status code.<p>Members:</p><ul><li><i>DF-001</i> - The page cursor passed as a parameter to the GET operation is invalid.</li><li><i>DF-002</i> - The sort specification passed as a parameter to the GET operation is invalid.</li><li><i>DF-003</i> - FolderPath and FolderId are mutually exclusive, they cannot both be passed as parameters.</li><li><i>DF-004</i> - The provided FolderPath must be in canonical form.</li><li><i>DF-005</i> - The specified parent folder cannot be found.</li><li><i>DF-006</i> - The specified owner cannot be found.</li><li><i>DF-007</i> - A connection corresponding to the specified space cannot be found.</li><li><i>DF-008</i> - THe specified ID must correspond to a folder, not a file.</li><li><i>DF-009</i> - The specified space cannot be found.</li><li><i>DF-010</i> - The specified file name contains an invalid file extension.</li><li><i>DF-011</i> - The specified file name is missing a file extension.</li><li><i>DF-012</i> - The specified temporary content file could not be found.</li><li><i>DF-013</i> - Access to the specified space is forbidden.</li><li><i>DF-014</i> - The specified connection cannot be found.</li><li><i>DF-015</i> - The provided filename must be in canonical form.</li><li><i>DF-016</i> - The datafile size quota for the given personal space has been exceeded.</li><li><i>DF-017</i> - The specified source file or folder could not be found.</li><li><i>DF-018</i> - The source and target of a datafile operation must either both be folders or both be files, but they are             not.</li><li><i>DF-019</i> - The specified target folder is a child of the specified source folder, which is not allowed.</li><li><i>DF-020</i> - The specified folder does not exist in the specified space.</li><li><i>DF-021</i> - The specified source file or folder is already locked.</li><li><i>DF-022</i> - The automatic creation of a missing parent folder failed.</li><li><i>DF-023</i> - An attempt to lock a parent folder of a given data file item failed.</li><li><i>DF-024</i> - The attempt to copy a source file or folder to a target failed.</li><li><i>DF-025</i> - The specified target file or folder is already locked.</li><li><i>DF-026</i> - The request results in the creation of a folder hierarchy which is beyond the max allowed folder             hierarchy depth.</li></ul> Enum: "HTTP-200", "HTTP-201", "HTTP-204", "HTTP-400", "HTTP-403", "HTTP-404", "HTTP-409", "HTTP-413", "HTTP-423", "HTTP-500", "HTTP-501", "HTTP-503", "DF-001", "DF-002", "DF-003", "DF-004", "DF-005", "DF-006", "DF-007", "DF-008", "DF-009", "DF-010", "DF-011", "DF-012", "DF-013", "DF-014", "DF-015", "DF-016", "DF-017", "DF-018", "DF-019", "DF-020", "DF-021", "DF-022", "DF-023", "DF-024", "DF-025", "DF-026" |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 409

If there is a file or folder in the target space with the same name as the item being
            moved.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Fine-grained error codes for data-files REST operations.  For operations which do not have a more fine-grained error code, the error code is set to the HTTP status code.<p>Members:</p><ul><li><i>DF-001</i> - The page cursor passed as a parameter to the GET operation is invalid.</li><li><i>DF-002</i> - The sort specification passed as a parameter to the GET operation is invalid.</li><li><i>DF-003</i> - FolderPath and FolderId are mutually exclusive, they cannot both be passed as parameters.</li><li><i>DF-004</i> - The provided FolderPath must be in canonical form.</li><li><i>DF-005</i> - The specified parent folder cannot be found.</li><li><i>DF-006</i> - The specified owner cannot be found.</li><li><i>DF-007</i> - A connection corresponding to the specified space cannot be found.</li><li><i>DF-008</i> - THe specified ID must correspond to a folder, not a file.</li><li><i>DF-009</i> - The specified space cannot be found.</li><li><i>DF-010</i> - The specified file name contains an invalid file extension.</li><li><i>DF-011</i> - The specified file name is missing a file extension.</li><li><i>DF-012</i> - The specified temporary content file could not be found.</li><li><i>DF-013</i> - Access to the specified space is forbidden.</li><li><i>DF-014</i> - The specified connection cannot be found.</li><li><i>DF-015</i> - The provided filename must be in canonical form.</li><li><i>DF-016</i> - The datafile size quota for the given personal space has been exceeded.</li><li><i>DF-017</i> - The specified source file or folder could not be found.</li><li><i>DF-018</i> - The source and target of a datafile operation must either both be folders or both be files, but they are             not.</li><li><i>DF-019</i> - The specified target folder is a child of the specified source folder, which is not allowed.</li><li><i>DF-020</i> - The specified folder does not exist in the specified space.</li><li><i>DF-021</i> - The specified source file or folder is already locked.</li><li><i>DF-022</i> - The automatic creation of a missing parent folder failed.</li><li><i>DF-023</i> - An attempt to lock a parent folder of a given data file item failed.</li><li><i>DF-024</i> - The attempt to copy a source file or folder to a target failed.</li><li><i>DF-025</i> - The specified target file or folder is already locked.</li><li><i>DF-026</i> - The request results in the creation of a folder hierarchy which is beyond the max allowed folder             hierarchy depth.</li></ul> Enum: "HTTP-200", "HTTP-201", "HTTP-204", "HTTP-400", "HTTP-403", "HTTP-404", "HTTP-409", "HTTP-413", "HTTP-423", "HTTP-500", "HTTP-501", "HTTP-503", "DF-001", "DF-002", "DF-003", "DF-004", "DF-005", "DF-006", "DF-007", "DF-008", "DF-009", "DF-010", "DF-011", "DF-012", "DF-013", "DF-014", "DF-015", "DF-016", "DF-017", "DF-018", "DF-019", "DF-020", "DF-021", "DF-022", "DF-023", "DF-024", "DF-025", "DF-026" |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 423

The file is already locked for write by another client.  For folders, any write lock on
            a subfolder or file underneath this folder implies a lock on the folder.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Fine-grained error codes for data-files REST operations.  For operations which do not have a more fine-grained error code, the error code is set to the HTTP status code.<p>Members:</p><ul><li><i>DF-001</i> - The page cursor passed as a parameter to the GET operation is invalid.</li><li><i>DF-002</i> - The sort specification passed as a parameter to the GET operation is invalid.</li><li><i>DF-003</i> - FolderPath and FolderId are mutually exclusive, they cannot both be passed as parameters.</li><li><i>DF-004</i> - The provided FolderPath must be in canonical form.</li><li><i>DF-005</i> - The specified parent folder cannot be found.</li><li><i>DF-006</i> - The specified owner cannot be found.</li><li><i>DF-007</i> - A connection corresponding to the specified space cannot be found.</li><li><i>DF-008</i> - THe specified ID must correspond to a folder, not a file.</li><li><i>DF-009</i> - The specified space cannot be found.</li><li><i>DF-010</i> - The specified file name contains an invalid file extension.</li><li><i>DF-011</i> - The specified file name is missing a file extension.</li><li><i>DF-012</i> - The specified temporary content file could not be found.</li><li><i>DF-013</i> - Access to the specified space is forbidden.</li><li><i>DF-014</i> - The specified connection cannot be found.</li><li><i>DF-015</i> - The provided filename must be in canonical form.</li><li><i>DF-016</i> - The datafile size quota for the given personal space has been exceeded.</li><li><i>DF-017</i> - The specified source file or folder could not be found.</li><li><i>DF-018</i> - The source and target of a datafile operation must either both be folders or both be files, but they are             not.</li><li><i>DF-019</i> - The specified target folder is a child of the specified source folder, which is not allowed.</li><li><i>DF-020</i> - The specified folder does not exist in the specified space.</li><li><i>DF-021</i> - The specified source file or folder is already locked.</li><li><i>DF-022</i> - The automatic creation of a missing parent folder failed.</li><li><i>DF-023</i> - An attempt to lock a parent folder of a given data file item failed.</li><li><i>DF-024</i> - The attempt to copy a source file or folder to a target failed.</li><li><i>DF-025</i> - The specified target file or folder is already locked.</li><li><i>DF-026</i> - The request results in the creation of a folder hierarchy which is beyond the max allowed folder             hierarchy depth.</li></ul> Enum: "HTTP-200", "HTTP-201", "HTTP-204", "HTTP-400", "HTTP-403", "HTTP-404", "HTTP-409", "HTTP-413", "HTTP-423", "HTTP-500", "HTTP-501", "HTTP-503", "DF-001", "DF-002", "DF-003", "DF-004", "DF-005", "DF-006", "DF-007", "DF-008", "DF-009", "DF-010", "DF-011", "DF-012", "DF-013", "DF-014", "DF-015", "DF-016", "DF-017", "DF-018", "DF-019", "DF-020", "DF-021", "DF-022", "DF-023", "DF-024", "DF-025", "DF-026" |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/data-files/{id}/actions/change-space` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-files/{id}/actions/change-space',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      spaceId: '617979737a9f56e49dea2e6e',
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/data-files/{id}/actions/change-space yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-files/{id}/actions/change-space" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"spaceId":"617979737a9f56e49dea2e6e"}'
```

---

### POST /api/v1/data-files/actions/change-space

This is to allow for a separate admin type of operation that is more global in terms of access in cases
where admin users may not explicitly have been granted full access to a given space within the declared
space-level permissions.  If the space ID is set to null, then the data file or folder will end up residing
in the personal space of the user who is the owner of the item.

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

The batch of IDs for each data file in the batch whose space will be changed along with
            the space IDs for each change.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `change-space` | object[] | Yes | The list of data files to delete. |

<details>
<summary>Properties of `change-space`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the data file whose space will be changed. |
| `spaceId` | string | No | The ID of the new space.  Passing in a null will result in the data file being moved to the user's personal space. |

</details>

#### Responses

##### 207

The result status of the change space operations on each specified data file.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes | List of individual results for the items in the specified batch. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the file. |
| `code` | string | Yes | Fine-grained error codes for data-files REST operations.  For operations which do not have a more fine-grained error code, the error code is set to the HTTP status code.<p>Members:</p><ul><li><i>DF-001</i> - The page cursor passed as a parameter to the GET operation is invalid.</li><li><i>DF-002</i> - The sort specification passed as a parameter to the GET operation is invalid.</li><li><i>DF-003</i> - FolderPath and FolderId are mutually exclusive, they cannot both be passed as parameters.</li><li><i>DF-004</i> - The provided FolderPath must be in canonical form.</li><li><i>DF-005</i> - The specified parent folder cannot be found.</li><li><i>DF-006</i> - The specified owner cannot be found.</li><li><i>DF-007</i> - A connection corresponding to the specified space cannot be found.</li><li><i>DF-008</i> - THe specified ID must correspond to a folder, not a file.</li><li><i>DF-009</i> - The specified space cannot be found.</li><li><i>DF-010</i> - The specified file name contains an invalid file extension.</li><li><i>DF-011</i> - The specified file name is missing a file extension.</li><li><i>DF-012</i> - The specified temporary content file could not be found.</li><li><i>DF-013</i> - Access to the specified space is forbidden.</li><li><i>DF-014</i> - The specified connection cannot be found.</li><li><i>DF-015</i> - The provided filename must be in canonical form.</li><li><i>DF-016</i> - The datafile size quota for the given personal space has been exceeded.</li><li><i>DF-017</i> - The specified source file or folder could not be found.</li><li><i>DF-018</i> - The source and target of a datafile operation must either both be folders or both be files, but they are             not.</li><li><i>DF-019</i> - The specified target folder is a child of the specified source folder, which is not allowed.</li><li><i>DF-020</i> - The specified folder does not exist in the specified space.</li><li><i>DF-021</i> - The specified source file or folder is already locked.</li><li><i>DF-022</i> - The automatic creation of a missing parent folder failed.</li><li><i>DF-023</i> - An attempt to lock a parent folder of a given data file item failed.</li><li><i>DF-024</i> - The attempt to copy a source file or folder to a target failed.</li><li><i>DF-025</i> - The specified target file or folder is already locked.</li><li><i>DF-026</i> - The request results in the creation of a folder hierarchy which is beyond the max allowed folder             hierarchy depth.</li></ul> Enum: "HTTP-200", "HTTP-201", "HTTP-204", "HTTP-400", "HTTP-403", "HTTP-404", "HTTP-409", "HTTP-413", "HTTP-423", "HTTP-500", "HTTP-501", "HTTP-503", "DF-001", "DF-002", "DF-003", "DF-004", "DF-005", "DF-006", "DF-007", "DF-008", "DF-009", "DF-010", "DF-011", "DF-012", "DF-013", "DF-014", "DF-015", "DF-016", "DF-017", "DF-018", "DF-019", "DF-020", "DF-021", "DF-022", "DF-023", "DF-024", "DF-025", "DF-026" |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `status` | integer | Yes | The HTTP status code. |

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Fine-grained error codes for data-files REST operations.  For operations which do not have a more fine-grained error code, the error code is set to the HTTP status code.<p>Members:</p><ul><li><i>DF-001</i> - The page cursor passed as a parameter to the GET operation is invalid.</li><li><i>DF-002</i> - The sort specification passed as a parameter to the GET operation is invalid.</li><li><i>DF-003</i> - FolderPath and FolderId are mutually exclusive, they cannot both be passed as parameters.</li><li><i>DF-004</i> - The provided FolderPath must be in canonical form.</li><li><i>DF-005</i> - The specified parent folder cannot be found.</li><li><i>DF-006</i> - The specified owner cannot be found.</li><li><i>DF-007</i> - A connection corresponding to the specified space cannot be found.</li><li><i>DF-008</i> - THe specified ID must correspond to a folder, not a file.</li><li><i>DF-009</i> - The specified space cannot be found.</li><li><i>DF-010</i> - The specified file name contains an invalid file extension.</li><li><i>DF-011</i> - The specified file name is missing a file extension.</li><li><i>DF-012</i> - The specified temporary content file could not be found.</li><li><i>DF-013</i> - Access to the specified space is forbidden.</li><li><i>DF-014</i> - The specified connection cannot be found.</li><li><i>DF-015</i> - The provided filename must be in canonical form.</li><li><i>DF-016</i> - The datafile size quota for the given personal space has been exceeded.</li><li><i>DF-017</i> - The specified source file or folder could not be found.</li><li><i>DF-018</i> - The source and target of a datafile operation must either both be folders or both be files, but they are             not.</li><li><i>DF-019</i> - The specified target folder is a child of the specified source folder, which is not allowed.</li><li><i>DF-020</i> - The specified folder does not exist in the specified space.</li><li><i>DF-021</i> - The specified source file or folder is already locked.</li><li><i>DF-022</i> - The automatic creation of a missing parent folder failed.</li><li><i>DF-023</i> - An attempt to lock a parent folder of a given data file item failed.</li><li><i>DF-024</i> - The attempt to copy a source file or folder to a target failed.</li><li><i>DF-025</i> - The specified target file or folder is already locked.</li><li><i>DF-026</i> - The request results in the creation of a folder hierarchy which is beyond the max allowed folder             hierarchy depth.</li></ul> Enum: "HTTP-200", "HTTP-201", "HTTP-204", "HTTP-400", "HTTP-403", "HTTP-404", "HTTP-409", "HTTP-413", "HTTP-423", "HTTP-500", "HTTP-501", "HTTP-503", "DF-001", "DF-002", "DF-003", "DF-004", "DF-005", "DF-006", "DF-007", "DF-008", "DF-009", "DF-010", "DF-011", "DF-012", "DF-013", "DF-014", "DF-015", "DF-016", "DF-017", "DF-018", "DF-019", "DF-020", "DF-021", "DF-022", "DF-023", "DF-024", "DF-025", "DF-026" |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/data-files/actions/change-space` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-files/actions/change-space',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      'change-space': [
        {
          id: 'ee6a390c-5d33-11e8-9c2d-fa7ae01bbebc',
          spaceId: '617979737a9f56e49dea2e6e',
        },
      ],
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/data-files/actions/change-space yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-files/actions/change-space" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"change-space":[{"id":"ee6a390c-5d33-11e8-9c2d-fa7ae01bbebc","spaceId":"617979737a9f56e49dea2e6e"}]}'
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "ee6a390c-5d33-11e8-9c2d-fa7ae01bbebc",
      "code": "HTTP-200",
      "title": "Cursor not formatted correctly.",
      "detail": "Invalid encoding of cursor.",
      "status": 400
    }
  ]
}
```

---

### POST /api/v1/data-files/actions/delete

- **Rate Limit:** Tier 2 (100 requests per minute)

#### Request Body

The specification of the batch of data files and folders to delete.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `delete` | object[] | Yes | If specified, the explicit list of data files to delete. |
| `deleteAllBySpace` | object[] | No | If specified, attempt to delete all of the data files from the specified shared spaces. |
| `deleteAllFromPersonalSpace` | boolean | No | If specified, attempt to delete all of the datafiles from ther user's personal space. |

<details>
<summary>Properties of `delete`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the data file to delete. |

</details>

<details>
<summary>Properties of `deleteAllBySpace`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the space whose data files will be deleted. |

</details>

#### Responses

##### 207

The result status of the delete operations on each specified data file or folder.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes | List of individual results for the items in the specified batch. |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the file. |
| `code` | string | Yes | Fine-grained error codes for data-files REST operations.  For operations which do not have a more fine-grained error code, the error code is set to the HTTP status code.<p>Members:</p><ul><li><i>DF-001</i> - The page cursor passed as a parameter to the GET operation is invalid.</li><li><i>DF-002</i> - The sort specification passed as a parameter to the GET operation is invalid.</li><li><i>DF-003</i> - FolderPath and FolderId are mutually exclusive, they cannot both be passed as parameters.</li><li><i>DF-004</i> - The provided FolderPath must be in canonical form.</li><li><i>DF-005</i> - The specified parent folder cannot be found.</li><li><i>DF-006</i> - The specified owner cannot be found.</li><li><i>DF-007</i> - A connection corresponding to the specified space cannot be found.</li><li><i>DF-008</i> - THe specified ID must correspond to a folder, not a file.</li><li><i>DF-009</i> - The specified space cannot be found.</li><li><i>DF-010</i> - The specified file name contains an invalid file extension.</li><li><i>DF-011</i> - The specified file name is missing a file extension.</li><li><i>DF-012</i> - The specified temporary content file could not be found.</li><li><i>DF-013</i> - Access to the specified space is forbidden.</li><li><i>DF-014</i> - The specified connection cannot be found.</li><li><i>DF-015</i> - The provided filename must be in canonical form.</li><li><i>DF-016</i> - The datafile size quota for the given personal space has been exceeded.</li><li><i>DF-017</i> - The specified source file or folder could not be found.</li><li><i>DF-018</i> - The source and target of a datafile operation must either both be folders or both be files, but they are             not.</li><li><i>DF-019</i> - The specified target folder is a child of the specified source folder, which is not allowed.</li><li><i>DF-020</i> - The specified folder does not exist in the specified space.</li><li><i>DF-021</i> - The specified source file or folder is already locked.</li><li><i>DF-022</i> - The automatic creation of a missing parent folder failed.</li><li><i>DF-023</i> - An attempt to lock a parent folder of a given data file item failed.</li><li><i>DF-024</i> - The attempt to copy a source file or folder to a target failed.</li><li><i>DF-025</i> - The specified target file or folder is already locked.</li><li><i>DF-026</i> - The request results in the creation of a folder hierarchy which is beyond the max allowed folder             hierarchy depth.</li></ul> Enum: "HTTP-200", "HTTP-201", "HTTP-204", "HTTP-400", "HTTP-403", "HTTP-404", "HTTP-409", "HTTP-413", "HTTP-423", "HTTP-500", "HTTP-501", "HTTP-503", "DF-001", "DF-002", "DF-003", "DF-004", "DF-005", "DF-006", "DF-007", "DF-008", "DF-009", "DF-010", "DF-011", "DF-012", "DF-013", "DF-014", "DF-015", "DF-016", "DF-017", "DF-018", "DF-019", "DF-020", "DF-021", "DF-022", "DF-023", "DF-024", "DF-025", "DF-026" |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |
| `status` | integer | Yes | The HTTP status code. |

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Fine-grained error codes for data-files REST operations.  For operations which do not have a more fine-grained error code, the error code is set to the HTTP status code.<p>Members:</p><ul><li><i>DF-001</i> - The page cursor passed as a parameter to the GET operation is invalid.</li><li><i>DF-002</i> - The sort specification passed as a parameter to the GET operation is invalid.</li><li><i>DF-003</i> - FolderPath and FolderId are mutually exclusive, they cannot both be passed as parameters.</li><li><i>DF-004</i> - The provided FolderPath must be in canonical form.</li><li><i>DF-005</i> - The specified parent folder cannot be found.</li><li><i>DF-006</i> - The specified owner cannot be found.</li><li><i>DF-007</i> - A connection corresponding to the specified space cannot be found.</li><li><i>DF-008</i> - THe specified ID must correspond to a folder, not a file.</li><li><i>DF-009</i> - The specified space cannot be found.</li><li><i>DF-010</i> - The specified file name contains an invalid file extension.</li><li><i>DF-011</i> - The specified file name is missing a file extension.</li><li><i>DF-012</i> - The specified temporary content file could not be found.</li><li><i>DF-013</i> - Access to the specified space is forbidden.</li><li><i>DF-014</i> - The specified connection cannot be found.</li><li><i>DF-015</i> - The provided filename must be in canonical form.</li><li><i>DF-016</i> - The datafile size quota for the given personal space has been exceeded.</li><li><i>DF-017</i> - The specified source file or folder could not be found.</li><li><i>DF-018</i> - The source and target of a datafile operation must either both be folders or both be files, but they are             not.</li><li><i>DF-019</i> - The specified target folder is a child of the specified source folder, which is not allowed.</li><li><i>DF-020</i> - The specified folder does not exist in the specified space.</li><li><i>DF-021</i> - The specified source file or folder is already locked.</li><li><i>DF-022</i> - The automatic creation of a missing parent folder failed.</li><li><i>DF-023</i> - An attempt to lock a parent folder of a given data file item failed.</li><li><i>DF-024</i> - The attempt to copy a source file or folder to a target failed.</li><li><i>DF-025</i> - The specified target file or folder is already locked.</li><li><i>DF-026</i> - The request results in the creation of a folder hierarchy which is beyond the max allowed folder             hierarchy depth.</li></ul> Enum: "HTTP-200", "HTTP-201", "HTTP-204", "HTTP-400", "HTTP-403", "HTTP-404", "HTTP-409", "HTTP-413", "HTTP-423", "HTTP-500", "HTTP-501", "HTTP-503", "DF-001", "DF-002", "DF-003", "DF-004", "DF-005", "DF-006", "DF-007", "DF-008", "DF-009", "DF-010", "DF-011", "DF-012", "DF-013", "DF-014", "DF-015", "DF-016", "DF-017", "DF-018", "DF-019", "DF-020", "DF-021", "DF-022", "DF-023", "DF-024", "DF-025", "DF-026" |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/data-files/actions/delete` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-files/actions/delete',
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      delete: [
        {
          id: 'ee6a390c-5d33-11e8-9c2d-fa7ae01bbebc',
        },
      ],
      deleteAllBySpace: [
        { id: '617979737a9f56e49dea2e6e' },
      ],
      deleteAllFromPersonalSpace: true,
    }),
  },
)

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/data-files/actions/delete yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-files/actions/delete" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"delete":[{"id":"ee6a390c-5d33-11e8-9c2d-fa7ae01bbebc"}],"deleteAllBySpace":[{"id":"617979737a9f56e49dea2e6e"}],"deleteAllFromPersonalSpace":true}'
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "ee6a390c-5d33-11e8-9c2d-fa7ae01bbebc",
      "code": "HTTP-200",
      "title": "Cursor not formatted correctly.",
      "detail": "Invalid encoding of cursor.",
      "status": 400
    }
  ]
}
```

---

### GET /api/v1/data-files/connections

The non-filtered list contains a set of hardcoded connections, along with one connection per team space that
the given user has access to.

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | No | If present, get connections with connection strings that are scoped to the given app ID. |
| `includeSpaceStats` | boolean | No | If set to true, include computed space-level statistics for the spaces represented by the connections in the returned list.  If false, this information is not returned. |
| `limit` | integer | No | If present, the maximum number of data file connection records to return. |
| `name` | string | No | If present, only return connections with the given name. |
| `page` | string | No | If present, the cursor that starts the page of data that is returned. |
| `personal` | boolean | No | If true, only return the connections that access data in a personal space.  Default is false. |
| `sort` | string | No | The name of the field used to sort the result.  By default, the sort is ascending.  Putting a '+' prefix on the sort field name explicitly indicates ascending sort order.  A '-' prefix indicates a descending sort order. Enum: "spaceId", "+spaceId", "-spaceId" |
| `spaceId` | string | No | If present, only return the connection that accesses data files in the specified space. |

#### Responses

##### 200

Connection list was returned.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes | Properties of the connections to the tenant spaces. |
| `links` | object | Yes |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the connection. |
| `name` | string | Yes | The name of the connection. |
| `type` | string | Yes | The type of the connection. |
| `spaceId` | string | No | The team space that the given connection is associated with.  If null, the connection is not associated with any specific team space. |
| `spaceStats` | object | No |  |
| `connectStatement` | string | Yes | The connect statement that will be passed to the connector when invoked. |

<details>
<summary>Properties of `spaceStats`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `totalFileCount` | integer | Yes | The number of data files that reside as direct and indirect children of the given folder and it's sub-folder hierarchy. |
| `directFileCount` | integer | Yes | The number of data files that reside as direct children of the given folder. |
| `totalFolderCount` | integer | Yes | The number of folders that reside as direct and indirect children of the given folder and it's sub-folder hierarchy. |
| `aggregateFileSize` | integer | Yes | The sum of the file sizes, in bytes, of all data files that reside as direct and indirect children of the given folder and it's sub-folder hierarchy. |
| `directFolderCount` | integer | Yes | The number of sub-folders that reside as direct children of the given folder. |
| `totalInternalFileCount` | integer | Yes | The number of 'internal' data files (IE, those that are not visible to end users by default) that reside as direct and indirect children of the given folder and it's sub-folder hierarchy. |
| `directInternalFileCount` | integer | Yes | The number of 'internal' data files (IE, those that are not visible to end users by default) that reside as direct children of the given folder. |
| `totalAppScopedFileCount` | integer | Yes | The number of app-scoped data files that reside as direct and indirect children of the given folder and it's sub-folder hierarchy. |
| `directAppScopedFileCount` | integer | Yes | The number of app-scoped data files that reside as direct children of the given folder. |
| `aggregateInternalFileSize` | integer | Yes | The sum of the file sizes, in bytes, of all internal data files that reside as direct and indirect children of the given folder and it's sub-folder hierarchy. |
| `aggregateAppScopedFileSize` | integer | Yes | The sum of the file sizes, in bytes, of all app-scoped data files that reside as direct and indirect children of the given folder and it's sub-folder hierarchy. |

</details>

</details>

<details>
<summary>Properties of `links`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `next` | object | Yes |  |
| `prev` | object | Yes |  |
| `self` | object | Yes |  |

<details>
<summary>Properties of `next`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | The URL for the link. |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | The URL for the link. |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No | The URL for the link. |

</details>

</details>

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Fine-grained error codes for data-files REST operations.  For operations which do not have a more fine-grained error code, the error code is set to the HTTP status code.<p>Members:</p><ul><li><i>DF-001</i> - The page cursor passed as a parameter to the GET operation is invalid.</li><li><i>DF-002</i> - The sort specification passed as a parameter to the GET operation is invalid.</li><li><i>DF-003</i> - FolderPath and FolderId are mutually exclusive, they cannot both be passed as parameters.</li><li><i>DF-004</i> - The provided FolderPath must be in canonical form.</li><li><i>DF-005</i> - The specified parent folder cannot be found.</li><li><i>DF-006</i> - The specified owner cannot be found.</li><li><i>DF-007</i> - A connection corresponding to the specified space cannot be found.</li><li><i>DF-008</i> - THe specified ID must correspond to a folder, not a file.</li><li><i>DF-009</i> - The specified space cannot be found.</li><li><i>DF-010</i> - The specified file name contains an invalid file extension.</li><li><i>DF-011</i> - The specified file name is missing a file extension.</li><li><i>DF-012</i> - The specified temporary content file could not be found.</li><li><i>DF-013</i> - Access to the specified space is forbidden.</li><li><i>DF-014</i> - The specified connection cannot be found.</li><li><i>DF-015</i> - The provided filename must be in canonical form.</li><li><i>DF-016</i> - The datafile size quota for the given personal space has been exceeded.</li><li><i>DF-017</i> - The specified source file or folder could not be found.</li><li><i>DF-018</i> - The source and target of a datafile operation must either both be folders or both be files, but they are             not.</li><li><i>DF-019</i> - The specified target folder is a child of the specified source folder, which is not allowed.</li><li><i>DF-020</i> - The specified folder does not exist in the specified space.</li><li><i>DF-021</i> - The specified source file or folder is already locked.</li><li><i>DF-022</i> - The automatic creation of a missing parent folder failed.</li><li><i>DF-023</i> - An attempt to lock a parent folder of a given data file item failed.</li><li><i>DF-024</i> - The attempt to copy a source file or folder to a target failed.</li><li><i>DF-025</i> - The specified target file or folder is already locked.</li><li><i>DF-026</i> - The request results in the creation of a folder hierarchy which is beyond the max allowed folder             hierarchy depth.</li></ul> Enum: "HTTP-200", "HTTP-201", "HTTP-204", "HTTP-400", "HTTP-403", "HTTP-404", "HTTP-409", "HTTP-413", "HTTP-423", "HTTP-500", "HTTP-501", "HTTP-503", "DF-001", "DF-002", "DF-003", "DF-004", "DF-005", "DF-006", "DF-007", "DF-008", "DF-009", "DF-010", "DF-011", "DF-012", "DF-013", "DF-014", "DF-015", "DF-016", "DF-017", "DF-018", "DF-019", "DF-020", "DF-021", "DF-022", "DF-023", "DF-024", "DF-025", "DF-026" |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Fine-grained error codes for data-files REST operations.  For operations which do not have a more fine-grained error code, the error code is set to the HTTP status code.<p>Members:</p><ul><li><i>DF-001</i> - The page cursor passed as a parameter to the GET operation is invalid.</li><li><i>DF-002</i> - The sort specification passed as a parameter to the GET operation is invalid.</li><li><i>DF-003</i> - FolderPath and FolderId are mutually exclusive, they cannot both be passed as parameters.</li><li><i>DF-004</i> - The provided FolderPath must be in canonical form.</li><li><i>DF-005</i> - The specified parent folder cannot be found.</li><li><i>DF-006</i> - The specified owner cannot be found.</li><li><i>DF-007</i> - A connection corresponding to the specified space cannot be found.</li><li><i>DF-008</i> - THe specified ID must correspond to a folder, not a file.</li><li><i>DF-009</i> - The specified space cannot be found.</li><li><i>DF-010</i> - The specified file name contains an invalid file extension.</li><li><i>DF-011</i> - The specified file name is missing a file extension.</li><li><i>DF-012</i> - The specified temporary content file could not be found.</li><li><i>DF-013</i> - Access to the specified space is forbidden.</li><li><i>DF-014</i> - The specified connection cannot be found.</li><li><i>DF-015</i> - The provided filename must be in canonical form.</li><li><i>DF-016</i> - The datafile size quota for the given personal space has been exceeded.</li><li><i>DF-017</i> - The specified source file or folder could not be found.</li><li><i>DF-018</i> - The source and target of a datafile operation must either both be folders or both be files, but they are             not.</li><li><i>DF-019</i> - The specified target folder is a child of the specified source folder, which is not allowed.</li><li><i>DF-020</i> - The specified folder does not exist in the specified space.</li><li><i>DF-021</i> - The specified source file or folder is already locked.</li><li><i>DF-022</i> - The automatic creation of a missing parent folder failed.</li><li><i>DF-023</i> - An attempt to lock a parent folder of a given data file item failed.</li><li><i>DF-024</i> - The attempt to copy a source file or folder to a target failed.</li><li><i>DF-025</i> - The specified target file or folder is already locked.</li><li><i>DF-026</i> - The request results in the creation of a folder hierarchy which is beyond the max allowed folder             hierarchy depth.</li></ul> Enum: "HTTP-200", "HTTP-201", "HTTP-204", "HTTP-400", "HTTP-403", "HTTP-404", "HTTP-409", "HTTP-413", "HTTP-423", "HTTP-500", "HTTP-501", "HTTP-503", "DF-001", "DF-002", "DF-003", "DF-004", "DF-005", "DF-006", "DF-007", "DF-008", "DF-009", "DF-010", "DF-011", "DF-012", "DF-013", "DF-014", "DF-015", "DF-016", "DF-017", "DF-018", "DF-019", "DF-020", "DF-021", "DF-022", "DF-023", "DF-024", "DF-025", "DF-026" |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/data-files/connections` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-files/connections',
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
# qlik-cli has not implemented support for GET /api/v1/data-files/connections yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-files/connections" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "id": "ee6a390c-5d33-11e8-9c2d-fa7ae01bbebc",
      "name": "DataFiles",
      "type": "qix-datafiles.exe",
      "spaceId": "617979737a9f56e49dea2e6e",
      "spaceStats": {
        "totalFileCount": 50,
        "directFileCount": 50,
        "totalFolderCount": 50,
        "aggregateFileSize": 10000,
        "directFolderCount": 50,
        "totalInternalFileCount": 50,
        "directInternalFileCount": 50,
        "totalAppScopedFileCount": 50,
        "directAppScopedFileCount": 50,
        "aggregateInternalFileSize": 10000,
        "aggregateAppScopedFileSize": 10000
      },
      "connectStatement": "CUSTOM CONNECT TO \\\"provider=qix-datafiles.exe;path=mydatafiles;\\\""
    }
  ],
  "links": {
    "next": {
      "href": "string"
    },
    "prev": {
      "href": "string"
    },
    "self": {
      "href": "string"
    }
  }
}
```

---

### GET /api/v1/data-files/connections/{id}

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The ID of the connection. |

#### Responses

##### 200

The connection was returned.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The unique identifier of the connection. |
| `name` | string | Yes | The name of the connection. |
| `type` | string | Yes | The type of the connection. |
| `spaceId` | string | No | The team space that the given connection is associated with.  If null, the connection is not associated with any specific team space. |
| `spaceStats` | object | No |  |
| `connectStatement` | string | Yes | The connect statement that will be passed to the connector when invoked. |

<details>
<summary>Properties of `spaceStats`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `totalFileCount` | integer | Yes | The number of data files that reside as direct and indirect children of the given folder and it's sub-folder hierarchy. |
| `directFileCount` | integer | Yes | The number of data files that reside as direct children of the given folder. |
| `totalFolderCount` | integer | Yes | The number of folders that reside as direct and indirect children of the given folder and it's sub-folder hierarchy. |
| `aggregateFileSize` | integer | Yes | The sum of the file sizes, in bytes, of all data files that reside as direct and indirect children of the given folder and it's sub-folder hierarchy. |
| `directFolderCount` | integer | Yes | The number of sub-folders that reside as direct children of the given folder. |
| `totalInternalFileCount` | integer | Yes | The number of 'internal' data files (IE, those that are not visible to end users by default) that reside as direct and indirect children of the given folder and it's sub-folder hierarchy. |
| `directInternalFileCount` | integer | Yes | The number of 'internal' data files (IE, those that are not visible to end users by default) that reside as direct children of the given folder. |
| `totalAppScopedFileCount` | integer | Yes | The number of app-scoped data files that reside as direct and indirect children of the given folder and it's sub-folder hierarchy. |
| `directAppScopedFileCount` | integer | Yes | The number of app-scoped data files that reside as direct children of the given folder. |
| `aggregateInternalFileSize` | integer | Yes | The sum of the file sizes, in bytes, of all internal data files that reside as direct and indirect children of the given folder and it's sub-folder hierarchy. |
| `aggregateAppScopedFileSize` | integer | Yes | The sum of the file sizes, in bytes, of all app-scoped data files that reside as direct and indirect children of the given folder and it's sub-folder hierarchy. |

</details>

##### 403

The space referenced by the specified connection was not found, or is not accessible to the current user.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Fine-grained error codes for data-files REST operations.  For operations which do not have a more fine-grained error code, the error code is set to the HTTP status code.<p>Members:</p><ul><li><i>DF-001</i> - The page cursor passed as a parameter to the GET operation is invalid.</li><li><i>DF-002</i> - The sort specification passed as a parameter to the GET operation is invalid.</li><li><i>DF-003</i> - FolderPath and FolderId are mutually exclusive, they cannot both be passed as parameters.</li><li><i>DF-004</i> - The provided FolderPath must be in canonical form.</li><li><i>DF-005</i> - The specified parent folder cannot be found.</li><li><i>DF-006</i> - The specified owner cannot be found.</li><li><i>DF-007</i> - A connection corresponding to the specified space cannot be found.</li><li><i>DF-008</i> - THe specified ID must correspond to a folder, not a file.</li><li><i>DF-009</i> - The specified space cannot be found.</li><li><i>DF-010</i> - The specified file name contains an invalid file extension.</li><li><i>DF-011</i> - The specified file name is missing a file extension.</li><li><i>DF-012</i> - The specified temporary content file could not be found.</li><li><i>DF-013</i> - Access to the specified space is forbidden.</li><li><i>DF-014</i> - The specified connection cannot be found.</li><li><i>DF-015</i> - The provided filename must be in canonical form.</li><li><i>DF-016</i> - The datafile size quota for the given personal space has been exceeded.</li><li><i>DF-017</i> - The specified source file or folder could not be found.</li><li><i>DF-018</i> - The source and target of a datafile operation must either both be folders or both be files, but they are             not.</li><li><i>DF-019</i> - The specified target folder is a child of the specified source folder, which is not allowed.</li><li><i>DF-020</i> - The specified folder does not exist in the specified space.</li><li><i>DF-021</i> - The specified source file or folder is already locked.</li><li><i>DF-022</i> - The automatic creation of a missing parent folder failed.</li><li><i>DF-023</i> - An attempt to lock a parent folder of a given data file item failed.</li><li><i>DF-024</i> - The attempt to copy a source file or folder to a target failed.</li><li><i>DF-025</i> - The specified target file or folder is already locked.</li><li><i>DF-026</i> - The request results in the creation of a folder hierarchy which is beyond the max allowed folder             hierarchy depth.</li></ul> Enum: "HTTP-200", "HTTP-201", "HTTP-204", "HTTP-400", "HTTP-403", "HTTP-404", "HTTP-409", "HTTP-413", "HTTP-423", "HTTP-500", "HTTP-501", "HTTP-503", "DF-001", "DF-002", "DF-003", "DF-004", "DF-005", "DF-006", "DF-007", "DF-008", "DF-009", "DF-010", "DF-011", "DF-012", "DF-013", "DF-014", "DF-015", "DF-016", "DF-017", "DF-018", "DF-019", "DF-020", "DF-021", "DF-022", "DF-023", "DF-024", "DF-025", "DF-026" |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 404

A connection with the specified ID was not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Fine-grained error codes for data-files REST operations.  For operations which do not have a more fine-grained error code, the error code is set to the HTTP status code.<p>Members:</p><ul><li><i>DF-001</i> - The page cursor passed as a parameter to the GET operation is invalid.</li><li><i>DF-002</i> - The sort specification passed as a parameter to the GET operation is invalid.</li><li><i>DF-003</i> - FolderPath and FolderId are mutually exclusive, they cannot both be passed as parameters.</li><li><i>DF-004</i> - The provided FolderPath must be in canonical form.</li><li><i>DF-005</i> - The specified parent folder cannot be found.</li><li><i>DF-006</i> - The specified owner cannot be found.</li><li><i>DF-007</i> - A connection corresponding to the specified space cannot be found.</li><li><i>DF-008</i> - THe specified ID must correspond to a folder, not a file.</li><li><i>DF-009</i> - The specified space cannot be found.</li><li><i>DF-010</i> - The specified file name contains an invalid file extension.</li><li><i>DF-011</i> - The specified file name is missing a file extension.</li><li><i>DF-012</i> - The specified temporary content file could not be found.</li><li><i>DF-013</i> - Access to the specified space is forbidden.</li><li><i>DF-014</i> - The specified connection cannot be found.</li><li><i>DF-015</i> - The provided filename must be in canonical form.</li><li><i>DF-016</i> - The datafile size quota for the given personal space has been exceeded.</li><li><i>DF-017</i> - The specified source file or folder could not be found.</li><li><i>DF-018</i> - The source and target of a datafile operation must either both be folders or both be files, but they are             not.</li><li><i>DF-019</i> - The specified target folder is a child of the specified source folder, which is not allowed.</li><li><i>DF-020</i> - The specified folder does not exist in the specified space.</li><li><i>DF-021</i> - The specified source file or folder is already locked.</li><li><i>DF-022</i> - The automatic creation of a missing parent folder failed.</li><li><i>DF-023</i> - An attempt to lock a parent folder of a given data file item failed.</li><li><i>DF-024</i> - The attempt to copy a source file or folder to a target failed.</li><li><i>DF-025</i> - The specified target file or folder is already locked.</li><li><i>DF-026</i> - The request results in the creation of a folder hierarchy which is beyond the max allowed folder             hierarchy depth.</li></ul> Enum: "HTTP-200", "HTTP-201", "HTTP-204", "HTTP-400", "HTTP-403", "HTTP-404", "HTTP-409", "HTTP-413", "HTTP-423", "HTTP-500", "HTTP-501", "HTTP-503", "DF-001", "DF-002", "DF-003", "DF-004", "DF-005", "DF-006", "DF-007", "DF-008", "DF-009", "DF-010", "DF-011", "DF-012", "DF-013", "DF-014", "DF-015", "DF-016", "DF-017", "DF-018", "DF-019", "DF-020", "DF-021", "DF-022", "DF-023", "DF-024", "DF-025", "DF-026" |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/data-files/connections/{id}` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-files/connections/{id}',
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
# qlik-cli has not implemented support for GET /api/v1/data-files/connections/{id} yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-files/connections/{id}" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "id": "ee6a390c-5d33-11e8-9c2d-fa7ae01bbebc",
  "name": "DataFiles",
  "type": "qix-datafiles.exe",
  "spaceId": "617979737a9f56e49dea2e6e",
  "spaceStats": {
    "totalFileCount": 50,
    "directFileCount": 50,
    "totalFolderCount": 50,
    "aggregateFileSize": 10000,
    "directFolderCount": 50,
    "totalInternalFileCount": 50,
    "directInternalFileCount": 50,
    "totalAppScopedFileCount": 50,
    "directAppScopedFileCount": 50,
    "aggregateInternalFileSize": 10000,
    "aggregateAppScopedFileSize": 10000
  },
  "connectStatement": "CUSTOM CONNECT TO \\\"provider=qix-datafiles.exe;path=mydatafiles;\\\""
}
```

---

### GET /api/v1/data-files/quotas

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Responses

##### 200

The quota information was retrieved.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `size` | integer | Yes | The current aggregate size of all files uploaded by a given user.  If the current aggregate size is greater than the maximum aggregate size, this is a quota violation. |
| `maxSize` | integer | Yes | The maximum aggregate size of all files uploaded by a given user. |
| `maxFileSize` | integer | Yes | Maximum allowable size of an uploaded file. |
| `maxLargeFileSize` | integer | Yes | Maximum allowable size for a single uploaded large data file (in bytes).  This is a file that was indirectly uploaded using the temp content service chunked upload capability. |
| `allowedExtensions` | string[] | Yes | The allowed file extensions on files that are uploaded. |
| `allowedInternalExtensions` | string[] | Yes | The allowed file extensions for files that are only used internally by the system (and thus not typically shown to end users). |

##### 400

Bad Request

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Fine-grained error codes for data-files REST operations.  For operations which do not have a more fine-grained error code, the error code is set to the HTTP status code.<p>Members:</p><ul><li><i>DF-001</i> - The page cursor passed as a parameter to the GET operation is invalid.</li><li><i>DF-002</i> - The sort specification passed as a parameter to the GET operation is invalid.</li><li><i>DF-003</i> - FolderPath and FolderId are mutually exclusive, they cannot both be passed as parameters.</li><li><i>DF-004</i> - The provided FolderPath must be in canonical form.</li><li><i>DF-005</i> - The specified parent folder cannot be found.</li><li><i>DF-006</i> - The specified owner cannot be found.</li><li><i>DF-007</i> - A connection corresponding to the specified space cannot be found.</li><li><i>DF-008</i> - THe specified ID must correspond to a folder, not a file.</li><li><i>DF-009</i> - The specified space cannot be found.</li><li><i>DF-010</i> - The specified file name contains an invalid file extension.</li><li><i>DF-011</i> - The specified file name is missing a file extension.</li><li><i>DF-012</i> - The specified temporary content file could not be found.</li><li><i>DF-013</i> - Access to the specified space is forbidden.</li><li><i>DF-014</i> - The specified connection cannot be found.</li><li><i>DF-015</i> - The provided filename must be in canonical form.</li><li><i>DF-016</i> - The datafile size quota for the given personal space has been exceeded.</li><li><i>DF-017</i> - The specified source file or folder could not be found.</li><li><i>DF-018</i> - The source and target of a datafile operation must either both be folders or both be files, but they are             not.</li><li><i>DF-019</i> - The specified target folder is a child of the specified source folder, which is not allowed.</li><li><i>DF-020</i> - The specified folder does not exist in the specified space.</li><li><i>DF-021</i> - The specified source file or folder is already locked.</li><li><i>DF-022</i> - The automatic creation of a missing parent folder failed.</li><li><i>DF-023</i> - An attempt to lock a parent folder of a given data file item failed.</li><li><i>DF-024</i> - The attempt to copy a source file or folder to a target failed.</li><li><i>DF-025</i> - The specified target file or folder is already locked.</li><li><i>DF-026</i> - The request results in the creation of a folder hierarchy which is beyond the max allowed folder             hierarchy depth.</li></ul> Enum: "HTTP-200", "HTTP-201", "HTTP-204", "HTTP-400", "HTTP-403", "HTTP-404", "HTTP-409", "HTTP-413", "HTTP-423", "HTTP-500", "HTTP-501", "HTTP-503", "DF-001", "DF-002", "DF-003", "DF-004", "DF-005", "DF-006", "DF-007", "DF-008", "DF-009", "DF-010", "DF-011", "DF-012", "DF-013", "DF-014", "DF-015", "DF-016", "DF-017", "DF-018", "DF-019", "DF-020", "DF-021", "DF-022", "DF-023", "DF-024", "DF-025", "DF-026" |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

##### 403

Forbidden

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | Yes | List of errors and their properties. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | Fine-grained error codes for data-files REST operations.  For operations which do not have a more fine-grained error code, the error code is set to the HTTP status code.<p>Members:</p><ul><li><i>DF-001</i> - The page cursor passed as a parameter to the GET operation is invalid.</li><li><i>DF-002</i> - The sort specification passed as a parameter to the GET operation is invalid.</li><li><i>DF-003</i> - FolderPath and FolderId are mutually exclusive, they cannot both be passed as parameters.</li><li><i>DF-004</i> - The provided FolderPath must be in canonical form.</li><li><i>DF-005</i> - The specified parent folder cannot be found.</li><li><i>DF-006</i> - The specified owner cannot be found.</li><li><i>DF-007</i> - A connection corresponding to the specified space cannot be found.</li><li><i>DF-008</i> - THe specified ID must correspond to a folder, not a file.</li><li><i>DF-009</i> - The specified space cannot be found.</li><li><i>DF-010</i> - The specified file name contains an invalid file extension.</li><li><i>DF-011</i> - The specified file name is missing a file extension.</li><li><i>DF-012</i> - The specified temporary content file could not be found.</li><li><i>DF-013</i> - Access to the specified space is forbidden.</li><li><i>DF-014</i> - The specified connection cannot be found.</li><li><i>DF-015</i> - The provided filename must be in canonical form.</li><li><i>DF-016</i> - The datafile size quota for the given personal space has been exceeded.</li><li><i>DF-017</i> - The specified source file or folder could not be found.</li><li><i>DF-018</i> - The source and target of a datafile operation must either both be folders or both be files, but they are             not.</li><li><i>DF-019</i> - The specified target folder is a child of the specified source folder, which is not allowed.</li><li><i>DF-020</i> - The specified folder does not exist in the specified space.</li><li><i>DF-021</i> - The specified source file or folder is already locked.</li><li><i>DF-022</i> - The automatic creation of a missing parent folder failed.</li><li><i>DF-023</i> - An attempt to lock a parent folder of a given data file item failed.</li><li><i>DF-024</i> - The attempt to copy a source file or folder to a target failed.</li><li><i>DF-025</i> - The specified target file or folder is already locked.</li><li><i>DF-026</i> - The request results in the creation of a folder hierarchy which is beyond the max allowed folder             hierarchy depth.</li></ul> Enum: "HTTP-200", "HTTP-201", "HTTP-204", "HTTP-400", "HTTP-403", "HTTP-404", "HTTP-409", "HTTP-413", "HTTP-423", "HTTP-500", "HTTP-501", "HTTP-503", "DF-001", "DF-002", "DF-003", "DF-004", "DF-005", "DF-006", "DF-007", "DF-008", "DF-009", "DF-010", "DF-011", "DF-012", "DF-013", "DF-014", "DF-015", "DF-016", "DF-017", "DF-018", "DF-019", "DF-020", "DF-021", "DF-022", "DF-023", "DF-024", "DF-025", "DF-026" |
| `title` | string | No | Summary of the problem. |
| `detail` | string | No | A human-readable explanation specific to this occurrence of the problem. |

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/data-files/quotas` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/data-files/quotas',
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
# qlik-cli has not implemented support for GET /api/v1/data-files/quotas yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/data-files/quotas" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "size": 5000,
  "maxSize": 9223372036854776000,
  "maxFileSize": 524288000,
  "maxLargeFileSize": 6442450944,
  "allowedExtensions": "csv, xlsx, txt, qvd",
  "allowedInternalExtensions": "dxf, gml, qrep"
}
```

---
