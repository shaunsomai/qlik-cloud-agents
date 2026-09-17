---
source: https://qlik.dev/apis/javascript/sense-client-objects/
last_updated: 2026-01-19T15:48:02Z
---

# Sense Client Objects

`Version: 1.4.0` | _stable_

Sense Client Objects consists of a collection of properties for defining different types of objects compatible with Qlik Sense Client

## Table of Contents

### Definitions

- [appProperties](#appproperties-object)
- [appPropertiesList](#apppropertieslist-object)
- [bookmark](#bookmark-object)
- [bookmarkList](#bookmarklist-object)
- [currentSelections](#currentselections-object)
- [dimension](#dimension-object)
- [dimensionList](#dimensionlist-object)
- [fieldList](#fieldlist-object)
- [masterobject](#masterobject-object)
- [masterobjectList](#masterobjectlist-object)
- [measure](#measure-object)
- [measureList](#measurelist-object)
- [sheet](#sheet-object)
- [sheetList](#sheetlist-object)
- [variable](#variable-object)
- [variableList](#variablelist-object)

## Definitions

### appProperties `object`

appProperties

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `chartAnimations` | boolean | No | true | Enable chart animations for all sheet objects Default:true |
| `disableCellNavMenu` | boolean | No | false | Disables the hover menu for all sheet objects Default:false |
| `qExtendsId` | string | Yes | - | Should be set to create an object that is linked to another object. Enter the identifier of the linking object (i.e the object you want to link to). If you do not want to link your object, set this parameter to an empty string. |
| `qInfo` | object | Yes | - |  |
| `qMetaDef` | object | Yes | - | Used to collect meta data.  Properties Semantic type with an empty structure. |
| `qStateName` | string | No | "$" | Name of the alternate state. Default is current selections _$_ . Default:$ |
| `rtl` | boolean | No | false | Right to left layout for right-to-left languages Default:false |
| `sheetLogoPosition` | string | Yes | - | Position of the sheet logo. right\|left\|center |
| `sheetLogoThumbnail` | object | Yes | - |  |
| `sheetTitleBgColor` | string | Yes | - | Color of the sheet background. Left side color when using gradient |
| `sheetTitleColor` | string | Yes | - | Color of the sheet title text |
| `sheetTitleGradientColor` | string | Yes | - | Right side background color when using gradient |
| `theme` | string | No | "horizon" | The theme used across the app Default:horizon |

<details>
<summary>Properties of `qInfo`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qId` | string | Yes | - | Identifier of the object. If the chosen identifier is already in use, the engine automatically sets another one. If an identifier is not set, the engine automatically sets one. This parameter is optional. |
| `qType` | string | No | "appprops" | Type of the object. This parameter is mandatory. Default:appprops |

</details>

<details>
<summary>Properties of `sheetLogoThumbnail`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qStaticContentUrlDef` | object | Yes | - | In addition, this structure can contain dynamic properties. |

<details>
<summary>Properties of `qStaticContentUrlDef`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qUrl` | string | Yes | - | Relative path of the thumbnail. |

</details>

</details>

---

### appPropertiesList `object`

appPropertiesList

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qAppObjectListDef` | object | Yes | - | Defines the list of objects in an app. An app object is a generic object created at app level. |
| `qExtendsId` | string | Yes | - | Should be set to create an object that is linked to another object. Enter the identifier of the linking object (i.e the object you want to link to). If you do not want to link your object, set this parameter to an empty string. |
| `qInfo` | object | Yes | - |  |
| `qMetaDef` | object | Yes | - | Used to collect meta data.  Properties Semantic type with an empty structure. |
| `qStateName` | string | No | "$" | Name of the alternate state. Default is current selections _$_ . Default:$ |

<details>
<summary>Properties of `qAppObjectListDef`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qData` | object | Yes | - | Contains dynamic JSON data specified by the client. |
| `qType` | string | No | "appprops" | Object type. Default:appprops |

<details>
<summary>Properties of `qData`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `chartAnimations` | string | No | "/chartAnimations" | Path to chartAnimations in AppGenericProperties Default:/chartAnimations |
| `disableCellNavMenu` | string | No | "/disableCellNavMenu" | Path to disableCellNavMenu in AppGenericProperties Default:/disableCellNavMenu |
| `rtl` | string | No | "/rtl" | Path to rtl in AppGenericProperties Default:/rtl |
| `sheetLogoPosition` | string | No | "/sheetLogoPosition" | Path to sheetLogoPosition in AppGenericProperties Default:/sheetLogoPosition |
| `sheetLogoThumbnail` | string | No | "/sheetLogoThumbnail" | Path to sheetLogoThumbnail in AppGenericProperties Default:/sheetLogoThumbnail |
| `sheetTitleBgColor` | string | No | "/sheetTitleBgColor" | Path to sheetTitleBgColor in AppGenericProperties Default:/sheetTitleBgColor |
| `sheetTitleColor` | string | No | "/sheetTitleColor" | Path to sheetTitleColor in AppGenericProperties Default:/sheetTitleColor |
| `sheetTitleGradientColor` | string | No | "/sheetTitleGradientColor" | Path to sheetTitleGradientColor in AppGenericProperties Default:/sheetTitleGradientColor |
| `theme` | string | No | "/theme" | Path to theme in AppGenericProperties Default:/theme |

</details>

</details>

<details>
<summary>Properties of `qInfo`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qId` | string | Yes | - | Identifier of the object. If the chosen identifier is already in use, the engine automatically sets another one. If an identifier is not set, the engine automatically sets one. This parameter is optional. |
| `qType` | string | No | "AppPropsList" | List object type. Default:AppPropsList |

</details>

---

### bookmark `object`

bookmark

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `creationDate` | string | Yes | - | Creation date of the bookmark. |
| `qDistinctValues` | boolean | No | false | If true all selected values will be stored distinct, i.e. searchstrings will not be kept. Default:false |
| `qIncludeVariables` | boolean | No | false | If true all variables will be stored in the bookmark. Default:false |
| `qInfo` | object | Yes | - |  |
| `qMetaDef` | object | Yes | - | The metadata object used by all app objects |
| `selectionFields` | string | Yes | - | Fields that have selections made to them. |
| `sheetId` | string | Yes | - | Sheet ID of the sheet that the bookmark applies to. |

<details>
<summary>Properties of `qInfo`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qId` | string | Yes | - | Identifier of the object. If the chosen identifier is already in use, the engine automatically sets another one. If an identifier is not set, the engine automatically sets one. This parameter is optional. |
| `qType` | string | No | "bookmark" | Object type. Default:bookmark |

</details>

<details>
<summary>Properties of `qMetaDef`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `description` | string | Yes | - | Short description for the app object |
| `tags` | string[] | Yes | - | Tags for the app object |
| `title` | string | Yes | - | Title for the app object |

</details>

---

### bookmarkList `object`

Properties for defining list of Bookmarks.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qBookmarkListDef` | object | Yes | - | Defines the list of bookmarks. |
| `qExtendsId` | string | Yes | - | Should be set to create an object that is linked to another object. Enter the identifier of the linking object (i.e the object you want to link to). If you do not want to link your object, set this parameter to an empty string. |
| `qInfo` | object | Yes | - |  |
| `qMetaDef` | object | Yes | - | Used to collect meta data.  Properties Semantic type with an empty structure. |
| `qStateName` | string | No | "$" | Name of the alternate state. Default is current selections _$_ . Default:$ |

<details>
<summary>Properties of `qBookmarkListDef`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qData` | object | Yes | - | Contains dynamic JSON data specified by the client. |
| `qIncludePatches` | boolean | Yes | - | Include the bookmark patches. Patches can be very large and may make the list result unmanageable. |
| `qType` | string | No | "bookmark" | Object type. Default:bookmark |

<details>
<summary>Properties of `qData`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `creationDate` | string | No | "/creationDate" | Path to creationDate in BookmarkProperties Default:/creationDate |
| `description` | string | No | "/qMetaDef/description" | Path to description in BookmarkProperties Default:/qMetaDef/description |
| `selectionFields` | string | No | "/selectionFields" | Path to selectionFields in BookmarkProperties Default:/selectionFields |
| `sheetId` | string | No | "/sheetId" | Path to sheetId in BookmarkProperties Default:/sheetId |
| `title` | string | No | "/qMetaDef/title" | Path to title in BookmarkProperties Default:/qMetaDef/title |

</details>

</details>

<details>
<summary>Properties of `qInfo`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qId` | string | Yes | - | Identifier of the object. If the chosen identifier is already in use, the engine automatically sets another one. If an identifier is not set, the engine automatically sets one. This parameter is optional. |
| `qType` | string | No | "BookmarkList" | List object type. Default:BookmarkList |

</details>

<details>
<summary>Examples</summary>

```javascript
const bookmarkListProps = {
  "qInfo": {
    "qType": "BookmarkList",
    "qId": ""
  },
  "qBookmarkListDef": {
    "qData": {
      "title": "/qMetaDef/title",
      "description": "/qMetaDef/description",
      "sheetId": "/sheetId",
      "selectionFields": "/selectionFields",
      "creationDate": "/creationDate"
    },
    "qType": "bookmark",
    "qIncludePatches": true
  }
};
const bookmarkList = await doc.createSessionObject(bookmarkListProps).then(list => list.getLayout());
```

</details>

---

### currentSelections `object`

currentSelections

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qExtendsId` | string | Yes | - | Should be set to create an object that is linked to another object. Enter the identifier of the linking object (i.e the object you want to link to). If you do not want to link your object, set this parameter to an empty string. |
| `qInfo` | object | Yes | - |  |
| `qMetaDef` | object | Yes | - | Used to collect meta data.  Properties Semantic type with an empty structure. |
| `qSelectionObjectDef` | object | Yes | - |  |
| `qStateName` | string | No | "$" | Name of the alternate state. Default is current selections _$_ . Default:$ |
| `qType` | string | No | "CurrentSelection" | CurrentSelections Object Default:CurrentSelection |

<details>
<summary>Properties of `qInfo`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qId` | string | No | "CurrentSelections" | Object id. Default:CurrentSelections |
| `qType` | string | No | "CurrentSelections" | Object type. Default:CurrentSelections |

</details>

<details>
<summary>Properties of `qSelectionObjectDef`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qStateName` | string | No | "$" | Name of the alternate state. Default is current selections _$_ . Default:$ |

</details>

<details>
<summary>Examples</summary>

```javascript
const currentSelectionsProps = {
  "qInfo": {
    "qType": "CurrentSelections",
    "qId": "CurrentSelections"
  },
  "qSelectionObjectDef": {
    "qStateName": "$"
  }
};
const currentSelections = await doc.createSessionObject(currentSelectionsProps).then(list => list.getLayout());
```

</details>

---

### dimension `object`

dimension

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qDim` | object | Yes | - |  |
| `qInfo` | object | Yes | - |  |
| `qMetaDef` | object | Yes | - | The metadata object used by all app objects |

<details>
<summary>Properties of `qDim`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `coloring` | object | Yes | - | Settings coloring by master dimension. |
| `descriptionExpression` | object | Yes | - | Properties Abbreviated syntax: "qStringExpression":"=&lt;expression&gt;" Extended object syntax: "qStringExpression":{"qExpr":"=&lt;expression&gt;"} Where: &lt; **expression** &gt; is a string  The "=" sign in the string expression is not mandatory. Even if the "=" sign is not given, the expression is evaluated. A string expression is not evaluated, if the expression is surrounded by simple quotes. The result of the evaluation of the expression can be of any type, as it is returned as a JSON (quoted) string. |
| `qFieldDefs` | string[] | Yes | - | Array of dimension names. |
| `qFieldLabels` | string[] | Yes | - | Array of dimension labels. |
| `qGrouping` | string | Yes | - | One of: N, H, C. |
| `qLabelExpression` | string | Yes | - | Name of the dimension as an expression. Only when qGrouping is N. |
| `title` | string | Yes | - | Name of the dimension. Used unless label expression is set. |

<details>
<summary>Properties of `coloring`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `baseColor` | object | Yes | - | Color information structure. Holds actual color and index in palette. |

<details>
<summary>Properties of `baseColor`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `color` | string | Yes | - | Color as hex string |
| `index` | integer | No | 6 | Index in palette Default:6 |

</details>

</details>

<details>
<summary>Properties of `descriptionExpression`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qExpr` | string | Yes | - |  |

</details>

</details>

<details>
<summary>Properties of `qInfo`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qId` | string | Yes | - | Identifier of the object. If the chosen identifier is already in use, the engine automatically sets another one. If an identifier is not set, the engine automatically sets one. This parameter is optional. |
| `qType` | string | No | "dimension" | Object type. Default:dimension |

</details>

<details>
<summary>Properties of `qMetaDef`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `description` | string | Yes | - | Short description for the app object |
| `tags` | string[] | Yes | - | Tags for the app object |
| `title` | string | Yes | - | Title for the app object |

</details>

---

### dimensionList `object`

Properties for defining list of Dimensions.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qDimensionListDef` | object | Yes | - | Defines the lists of dimensions. |
| `qExtendsId` | string | Yes | - | Should be set to create an object that is linked to another object. Enter the identifier of the linking object (i.e the object you want to link to). If you do not want to link your object, set this parameter to an empty string. |
| `qInfo` | object | Yes | - |  |
| `qMetaDef` | object | Yes | - | Used to collect meta data.  Properties Semantic type with an empty structure. |
| `qStateName` | string | No | "$" | Name of the alternate state. Default is current selections _$_ . Default:$ |

<details>
<summary>Properties of `qDimensionListDef`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qData` | object | Yes | - | Contains dynamic JSON data specified by the client. |
| `qType` | string | No | "dimension" | Object type Default:dimension |

<details>
<summary>Properties of `qData`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `grouping` | string | No | "/qDim/grouping" | Path to grouping in DimensionProperties Default:/qDim/grouping |
| `info` | string | No | "/qDimInfos" | Path to qDimInfos in DimensionProperties Default:/qDimInfos |
| `labelExpression` | string | No | "/qDim/labelExpression" | Path to labelExpression in DimensionProperties Default:/qDim/labelExpression |
| `tags` | string | No | "/qMetaDef/tags" | Path to tags in DimensionProperties Default:/qMetaDef/tags |
| `title` | string | No | "/qMetaDef/title" | Path to title in DimensionProperties Default:/qMetaDef/title |

</details>

</details>

<details>
<summary>Properties of `qInfo`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qId` | string | Yes | - | Identifier of the object. If the chosen identifier is already in use, the engine automatically sets another one. If an identifier is not set, the engine automatically sets one. This parameter is optional. |
| `qType` | string | No | "DimensionList" | List object type. Default:DimensionList |

</details>

<details>
<summary>Examples</summary>

```javascript
const dimensionListProps = {
  "qInfo": {
    "qType": "DimensionList",
    "qId": ""
  },
  "qDimensionListDef": {
    "qData": {
      "title": "/qMetaDef/title",
      "tags": "/qMetaDef/tags",
      "grouping": "/qDim/grouping",
      "info": "/qDimInfos",
      "labelExpression": "/qDim/labelExpression"
    },
    "qType": "dimension"
  }
};
const dimensionList = await doc.createSessionObject(dimensionListProps).then(list => list.getLayout());
```

</details>

---

### fieldList `object`

fieldList

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qExtendsId` | string | Yes | - | Should be set to create an object that is linked to another object. Enter the identifier of the linking object (i.e the object you want to link to). If you do not want to link your object, set this parameter to an empty string. |
| `qFieldListDef` | object | Yes | - |  |
| `qInfo` | object | Yes | - |  |
| `qMetaDef` | object | Yes | - | Used to collect meta data.  Properties Semantic type with an empty structure. |
| `qStateName` | string | No | "$" | Name of the alternate state. Default is current selections _$_ . Default:$ |
| `qType` | string | No | "FieldList" | FieldList Object Default:FieldList |

<details>
<summary>Properties of `qFieldListDef`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qShowDefinitionOnly` | boolean | No | false | Shows the fields defined on the fly if set to true. Default is false. Default:false |
| `qShowDerivedFields` | boolean | No | true | Shows the fields and derived fields if set to true. Default is true. Default:true |
| `qShowHidden` | boolean | No | false | Shows the hidden fields if set to true. Default is false. Default:false |
| `qShowImplicit` | boolean | No | false | Shows the Direct Discovery measure fields if set to true. Default is false. Default:false |
| `qShowSemantic` | boolean | No | true | Show the semantic fields if set to true. Default is true. Default:true |
| `qShowSrcTables` | boolean | No | true | Shows the tables and fields present in the data model viewer if set to true. Default is true. Default:true |
| `qShowSystem` | boolean | No | false | Shows the system tables if set to true. Default is false. Default:false |

</details>

<details>
<summary>Properties of `qInfo`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qId` | string | No | "FieldList" | Object id. Default:FieldList |
| `qType` | string | No | "FieldList" | Object type. Default:FieldList |

</details>

<details>
<summary>Examples</summary>

```javascript
const fieldListProps = {
  "qInfo": {
    "qType": "FieldList",
    "qId": "FieldList"
  },
  "qFieldListDef": {
    "qShowDefinitionOnly": "false",
    "qShowDerivedFields": "true",
    "qShowHidden": "false",
    "qShowImplicit": "false",
    "qShowSemantic": "true",
    "qShowSrcTables": "true",
    "qShowSystem": "false"
  }
};
const fieldList = await doc.createSessionObject(fieldListProps).then(list => list.getLayout());
```

</details>

---

### masterobject `object`

Base visualizations class with common settings.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `masterVersion` | number | No | 0.95 | Version number. Will default to latest Qlik Sense version if not manually set. Default:0.95 |
| `qExtendsId` | string | Yes | - | Should be set to create an object that is linked to another object. Enter the identifier of the linking object (i.e the object you want to link to). If you do not want to link your object, set this parameter to an empty string. |
| `qInfo` | object | Yes | - |  |
| `qLayoutExclude` | object | Yes | - |  |
| `qMetaDef` | object | Yes | - | The metadata object used by all app objects |
| `qStateName` | string | No | "$" | Name of the alternate state. Default is current selections _$_ . Default:$ |
| `showDetails` | boolean | No | false | Show visualization details toggle Default:false |
| `showTitles` | boolean | No | true | Visualization subtitle Default:true |
| `visualization` | string | Yes | - | Visualization type. Must always be set. |

<details>
<summary>Properties of `qInfo`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qId` | string | Yes | - | Identifier of the object. If the chosen identifier is already in use, the engine automatically sets another one. If an identifier is not set, the engine automatically sets one. This parameter is optional. |
| `qType` | string | No | "masterobject" | Object type. Default:masterobject |

</details>

<details>
<summary>Properties of `qMetaDef`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `description` | string | Yes | - | Short description for the app object |
| `tags` | string[] | Yes | - | Tags for the app object |
| `title` | string | Yes | - | Title for the app object |

</details>

---

### masterobjectList `object`

Properties for defining list of MasterObjects.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qAppObjectListDef` | object | Yes | - | Defines the list of objects in an app. An app object is a generic object created at app level. |
| `qExtendsId` | string | Yes | - | Should be set to create an object that is linked to another object. Enter the identifier of the linking object (i.e the object you want to link to). If you do not want to link your object, set this parameter to an empty string. |
| `qInfo` | object | Yes | - |  |
| `qMetaDef` | object | Yes | - | Used to collect meta data.  Properties Semantic type with an empty structure. |
| `qStateName` | string | No | "$" | Name of the alternate state. Default is current selections _$_ . Default:$ |

<details>
<summary>Properties of `qAppObjectListDef`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qData` | object | Yes | - | Contains dynamic JSON data specified by the client. |
| `qType` | string | No | "masterobject" | Object type Default:masterobject |

<details>
<summary>Properties of `qData`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `labelExpression` | string | No | "/labelExpression" | Path to labelExpression in MasterObjectProperties Default:/labelExpression |
| `name` | string | No | "/qMetaDef/title" | Path to title in MasterObjectProperties Default:/qMetaDef/title |
| `tags` | string | No | "/qMetaDef/tags" | Path to tags in MasterObjectProperties Default:/qMetaDef/tags |
| `visualization` | string | No | "/visualization" | Path to visualization in MasterObjectProperties Default:/visualization |

</details>

</details>

<details>
<summary>Properties of `qInfo`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qId` | string | Yes | - | Identifier of the object. If the chosen identifier is already in use, the engine automatically sets another one. If an identifier is not set, the engine automatically sets one. This parameter is optional. |
| `qType` | string | No | "MasterObjectList" | List object type. Default:MasterObjectList |

</details>

<details>
<summary>Examples</summary>

```javascript
const masterobjectListProps = {
  "qInfo": {
    "qType": "MasterObjectList",
    "qId": ""
  },
  "qAppObjectListDef": {
    "qData": {
      "name": "/qMetaDef/title",
      "labelExpression": "/labelExpression",
      "visualization": "/visualization",
      "tags": "/qMetaDef/tags"
    },
    "qType": "masterobject"
  }
};
const masterobjectList = await doc.createSessionObject(masterobjectListProps).then(list => list.getLayout());
```

</details>

---

### measure `object`

measure

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qInfo` | object | Yes | - |  |
| `qMeasure` | object | Yes | - |  |
| `qMetaDef` | object | Yes | - | The metadata object used by all app objects |

<details>
<summary>Properties of `qInfo`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qId` | string | Yes | - | Identifier of the object. If the chosen identifier is already in use, the engine automatically sets another one. If an identifier is not set, the engine automatically sets one. This parameter is optional. |
| `qType` | string | No | "measure" | Object type. Default:measure |

</details>

<details>
<summary>Properties of `qMeasure`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `coloring` | object | Yes | - | Settings coloring by master measure. |
| `descriptionExpression` | object | Yes | - | Properties Abbreviated syntax: "qStringExpression":"=&lt;expression&gt;" Extended object syntax: "qStringExpression":{"qExpr":"=&lt;expression&gt;"} Where: &lt; **expression** &gt; is a string  The "=" sign in the string expression is not mandatory. Even if the "=" sign is not given, the expression is evaluated. A string expression is not evaluated, if the expression is surrounded by simple quotes. The result of the evaluation of the expression can be of any type, as it is returned as a JSON (quoted) string. |
| `isCustomFormatted` | boolean | No | false | Denotes whether the measure has custom formatting applied Default:false |
| `numFormatFromTemplate` | boolean | No | false | Denotes whether the number formatting comes from a template Default:false |
| `qActiveExpression` | integer | Yes | - | Index to the active expression in a measure. |
| `qDef` | string | Yes | - | Definition of the measure. |
| `qExpressions` | string[] | Yes | - | Array of expressions. |
| `qGrouping` | string | Yes | - | One of: N, H, C. |
| `qLabel` | string | Yes | - | Name of the Measure |
| `qLabelExpression` | string | Yes | - | Optional expression used for dynamic label. |
| `qNumFormat` | object | Yes | - | Sets the formatting of a field. The properties of _qFieldAttributes_ and the formatting mechanism are described below.  Formatting mechanism The formatting mechanism depends on the type set in _qType,_ as shown below: In case of inconsistencies between the type and the format pattern, the format pattern takes precedence over the type.  Type is DATE, TIME, TIMESTAMP or INTERVAL The following applies: If a format pattern is defined in _qFmt_ , the formatting is as defined in _qFmt_ . If _qFmt_ is empty, the formatting is defined by the number interpretation variables included at the top of the script ( _TimeFormat_ , _DateFormat_ , _TimeStampFormat_ ). The properties _qDec_ , _qThou_ , _qnDec_ , _qUseThou_ are not used.  Type is INTEGER The following applies: If a format pattern is defined in _qFmt_ , the engine looks at the values set in _qDec_ and _qThou_ . If these properties are not defined, the formatting mechanism uses the number interpretation variables included at the top of the script ( _DecimalSep_ and _ThousandSep_ ). If no format pattern is defined in _qFmt_ , no formatting is applied. The properties _qDec_ , _qThou_ , _qnDec_ , _qUseThou_ and the number interpretation variables defined in the script are not used .  Type is REAL The following applies: If a format pattern is defined in _qFmt_ , the engine looks at the values set in _qDec_ and _qThou_ . If these properties are not defined, the engine uses the number interpretation variables included at the top of the script ( _DecimalSep_ and _ThousandSep_ ). If no format pattern is defined in _qFmt_ , and if the value is almost an integer value (for example, 14,000012), the value is formatted as an integer. The properties _qDec_ , _qThou_ , _qnDec_ , _qUseThou_ are not used. If no format pattern is defined in _qFmt_ , and if _qnDec_ is defined and not 0, the property _qDec_ is used. If _qDec_ is not defined, the variable _DecimalSep_ defined at the top of the script is used. If no format pattern is defined in _qFmt_ , and if _qnDec_ is 0, the number of decimals is 14 and the property _qDec_ is used. If _qDec_ is not defined, the variable _DecimalSep_ defined at the top of the script is used.  Type is FIX The following applies: If a format pattern is defined in _qFmt_ , the engine looks at the values set in _qDec_ and _qThou_ . If these properties are not defined, the engine uses the number interpretation variables included at the top of the script ( _DecimalSep_ and _ThousandSep_ ). If no format pattern is defined in _qFmt_ , the properties _qDec_ and _qnDec_ are used. If _qDec_ is not defined, the variable _DecimalSep_ defined at the top of the script is used.  Type is MONEY The following applies: If a format pattern is defined in _qFmt_ , the engine looks at the values set in _qDec_ and _qThou_ . If these properties are not defined, the engine uses the number interpretation variables included at the top of any script ( _MoneyDecimalSep_ and _MoneyThousandSep_ ). If no format pattern is defined in _qFmt_ , the engine uses the number interpretation variables included at the top of the script ( _MoneyDecimalSep_ and _MoneyThousandSep_ ).  Type is ASCII No formatting, _qFmt_ is ignored. |

<details>
<summary>Properties of `coloring`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `baseColor` | object | Yes | - | Color information structure. Holds actual color and index in palette. |
| `gradient` | object | Yes | - | Color map used in by dimension color modes. |

<details>
<summary>Properties of `baseColor`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `color` | string | Yes | - | Color as hex string |
| `index` | integer | No | 6 | Index in palette Default:6 |

</details>

<details>
<summary>Properties of `gradient`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `breakTypes` | boolean[] | Yes | - | Specifies how to blend in color intersections. Should be of length one less than the number of colors. |
| `colors` | object[] | Yes | - | Colors to map against measure values |
| `limitType` | string | No | "percent" | percent\|absolute Default:percent |
| `limits` | integer[] | Yes | - | Specifies where to place the color breakpoints. Should be of length one less than the number of colors. |

</details>

</details>

<details>
<summary>Properties of `descriptionExpression`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qExpr` | string | Yes | - |  |

</details>

<details>
<summary>Properties of `qNumFormat`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qDec` | string | Yes | - | Defines the decimal separator. Example: **.** |
| `qFmt` | string | Yes | - | Defines the format pattern that applies to _qText_ . Is used in connection to the type of the field (parameter **qType** ). For more information, see _Formatting mechanism_. Example: _YYYY-MM-DD_ for a date. |
| `qThou` | string | Yes | - | Defines the thousand separator (if any). Is used if **qUseThou** is set to 1. Example: **,** |
| `qType` | string | Yes | - | One of: U, A, I, R, F, M, D, T, TS, IV. |
| `qUseThou` | integer | No | 0 | Defines whether or not a thousands separator must be used. Default is 0. Default:0 |
| `qnDec` | integer | No | 10 | Number of decimals. Default is 10. Default:10 |

</details>

</details>

<details>
<summary>Properties of `qMetaDef`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `description` | string | Yes | - | Short description for the app object |
| `tags` | string[] | Yes | - | Tags for the app object |
| `title` | string | Yes | - | Title for the app object |

</details>

---

### measureList `object`

Properties for defining list of Measures.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qExtendsId` | string | Yes | - | Should be set to create an object that is linked to another object. Enter the identifier of the linking object (i.e the object you want to link to). If you do not want to link your object, set this parameter to an empty string. |
| `qInfo` | object | Yes | - |  |
| `qMeasureListDef` | object | Yes | - | Defines the list of measures. |
| `qMetaDef` | object | Yes | - | Used to collect meta data.  Properties Semantic type with an empty structure. |
| `qStateName` | string | No | "$" | Name of the alternate state. Default is current selections _$_ . Default:$ |

<details>
<summary>Properties of `qInfo`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qId` | string | Yes | - | Identifier of the object. If the chosen identifier is already in use, the engine automatically sets another one. If an identifier is not set, the engine automatically sets one. This parameter is optional. |
| `qType` | string | No | "MeasureList" | List object type. Default:MeasureList |

</details>

<details>
<summary>Properties of `qMeasureListDef`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qData` | object | Yes | - | Contains dynamic JSON data specified by the client. |
| `qType` | string | No | "measure" | Object type Default:measure |

<details>
<summary>Properties of `qData`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `labelExpression` | string | No | "/qMeasure/qLabelExpression" | Path to labelExpression in MeasureProperties Default:/qMeasure/qLabelExpression |
| `tags` | string | No | "/qMetaDef/tags" | Path to tags in MeasureProperties Default:/qMetaDef/tags |
| `title` | string | No | "/qMetaDef/title" | Path to title in MeasureProperties Default:/qMetaDef/title |

</details>

</details>

<details>
<summary>Examples</summary>

```javascript
const measureListProps = {
  "qInfo": {
    "qType": "MeasureList",
    "qId": ""
  },
  "qMeasureListDef": {
    "qData": {
      "title": "/qMetaDef/title",
      "tags": "/qMetaDef/tags",
      "labelExpression": "/qMeasure/qLabelExpression"
    },
    "qType": "measure"
  }
};
const measureList = await doc.createSessionObject(measureListProps).then(list => list.getLayout());
```

</details>

---

### sheet `object`

sheet

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `cells` | object[] | Yes | - | Sheet cells. |
| `columns` | integer | No | 24 | Number of grid columns the sheet consists of. Using anything else than the default setting may cause the Qlik Sense client to malfunction. Default:24 |
| `gridResolution` | string | No | "small" | Sets the number of grid cells: small\|medium\|large Default:small |
| `height` | integer | Yes | - | Height in percentage. Used in tandem with layoutOptions.sheetMode RESPONSIVE and extended sheets. Can be larger than 100 |
| `layoutOptions` | object | Yes | - |  |
| `pxHeight` | integer | Yes | - | Height in pixels. Used in tandem with layoutOptions.sheetMode |
| `pxWidth` | integer | Yes | - | Width in pixels. Used in tandem with layoutOptions.sheetMode CUSTOM |
| `qChildListDef` | object | Yes | - |  |
| `qExtendsId` | string | Yes | - | Should be set to create an object that is linked to another object. Enter the identifier of the linking object (i.e the object you want to link to). If you do not want to link your object, set this parameter to an empty string. |
| `qInfo` | object | Yes | - |  |
| `qMetaDef` | object | Yes | - | The metadata object used by all app objects |
| `qStateName` | string | No | "$" | Name of the alternate state. Default is current selections _$_ . Default:$ |
| `rank` | number | No | 1 | Sheet rank. The sheet with the lowest rank will be displayed first, so the rank is inverted. Default:1 |
| `rows` | integer | No | 12 | Number of grid rows the sheet consists of. Using anything else than the default setting may cause the Qlik Sense client to malfunction. Default:12 |
| `thumbnail` | object | Yes | - |  |

<details>
<summary>Properties of `layoutOptions`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `extendable` | boolean | No | false | Flag to show extend sheet button in the grid Default:false |
| `mobileLayout` | string | No | "LIST" | Sets the mobile display of the sheet in sense client: LIST\|GRID Default:LIST |
| `sheetMode` | string | Yes | - | Sets scaling used by the sheet: RESPONSIVE\|CUSTOM |

</details>

<details>
<summary>Properties of `qChildListDef`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qData` | object | Yes | - |  |

<details>
<summary>Properties of `qData`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `title` | string | No | "/title" | Default:/title |

</details>

</details>

<details>
<summary>Properties of `qInfo`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qId` | string | Yes | - | Identifier of the object. If the chosen identifier is already in use, the engine automatically sets another one. If an identifier is not set, the engine automatically sets one. This parameter is optional. |
| `qType` | string | No | "sheet" | Object type. Default:sheet |

</details>

<details>
<summary>Properties of `qMetaDef`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `description` | string | Yes | - | Short description for the app object |
| `tags` | string[] | Yes | - | Tags for the app object |
| `title` | string | Yes | - | Title for the app object |

</details>

<details>
<summary>Properties of `thumbnail`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qStaticContentUrlDef` | object | Yes | - | In addition, this structure can contain dynamic properties. |

<details>
<summary>Properties of `qStaticContentUrlDef`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qUrl` | string | Yes | - | Relative path of the thumbnail. |

</details>

</details>

---

### sheetList `object`

sheetList

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qAppObjectListDef` | object | Yes | - | Defines the list of objects in an app. An app object is a generic object created at app level. |
| `qExtendsId` | string | Yes | - | Should be set to create an object that is linked to another object. Enter the identifier of the linking object (i.e the object you want to link to). If you do not want to link your object, set this parameter to an empty string. |
| `qInfo` | object | Yes | - |  |
| `qMetaDef` | object | Yes | - | Used to collect meta data.  Properties Semantic type with an empty structure. |
| `qStateName` | string | No | "$" | Name of the alternate state. Default is current selections _$_ . Default:$ |

<details>
<summary>Properties of `qAppObjectListDef`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qData` | object | Yes | - | Contains dynamic JSON data specified by the client. |
| `qType` | string | No | "sheet" | Object type. Default:sheet |

<details>
<summary>Properties of `qData`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `cells` | string | No | "/cells" | Path to cells in SheetProperties Default:/cells |
| `columns` | string | No | "/columns" | Path to columns in SheetProperties Default:/columns |
| `description` | string | No | "/qMetaDef/description" | Path to description in SheetProperties Default:/qMetaDef/description |
| `descriptionExpression` | string | No | "/qMetaDef/descriptionExpression" | Path to descriptionExpression in SheetProperties Default:/qMetaDef/descriptionExpression |
| `labelExpression` | string | No | "/labelExpression" | Path to labelExpression in SheetProperties Default:/labelExpression |
| `rank` | string | No | "/rank" | Path to rank in SheetProperties Default:/rank |
| `rows` | string | No | "/rows" | Path to rows in SheetProperties Default:/rows |
| `showCondition` | string | No | "/showCondition" | Path to showCondition in SheetProperties Default:/showCondition |
| `thumbnail` | string | No | "/qMetaDef/thumbnail" | Path to thumbnail in SheetProperties Default:/qMetaDef/thumbnail |
| `title` | string | No | "/qMetaDef/title" | Path to title in SheetProperties Default:/qMetaDef/title |

</details>

</details>

<details>
<summary>Properties of `qInfo`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qId` | string | Yes | - | Identifier of the object. If the chosen identifier is already in use, the engine automatically sets another one. If an identifier is not set, the engine automatically sets one. This parameter is optional. |
| `qType` | string | No | "SheetList" | List object type. Default:SheetList |

</details>

<details>
<summary>Examples</summary>

```javascript
const sheetListProps = {
  "qInfo": {
    "qType": "SheetList",
    "qId": ""
  },
  "qAppObjectListDef": {
    "qData": {
      "title": "/qMetaDef/title",
      "labelExpression": "/labelExpression",
      "showCondition": "/showCondition",
      "description": "/qMetaDef/description",
      "descriptionExpression": "/qMetaDef/descriptionExpression",
      "thumbnail": "/qMetaDef/thumbnail",
      "cells": "/cells",
      "rank": "/rank",
      "columns": "/columns",
      "rows": "/rows"
    },
    "qType": "sheet"
  }
};
const sheetList = await doc.createSessionObject(sheetListProps).then(list => list.getLayout());
```

</details>

---

### variable `object`

variable

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qComment` | string | Yes | - | Comment related to the variable. This parameter is optional. |
| `qDefinition` | string | Yes | - | Definition of the variable. |
| `qIncludeInBookmark` | boolean | No | false | Set this property to true to update the variable when applying a bookmark. The variable value will be persisted in the bookmark. The value of a variable can affect the state of the selections. Script variables cannot be persisted in the bookmark. The default value is false. Default:false |
| `qInfo` | object | Yes | - |  |
| `qMetaDef` | object | Yes | - | Used to collect meta data.  Properties Semantic type with an empty structure. |
| `qName` | string | Yes | - | Name of the variable. The name must be unique. This parameter is mandatory. |
| `qNumberPresentation` | object | Yes | - | Sets the formatting of a field. The properties of _qFieldAttributes_ and the formatting mechanism are described below.  Formatting mechanism The formatting mechanism depends on the type set in _qType,_ as shown below: In case of inconsistencies between the type and the format pattern, the format pattern takes precedence over the type.  Type is DATE, TIME, TIMESTAMP or INTERVAL The following applies: If a format pattern is defined in _qFmt_ , the formatting is as defined in _qFmt_ . If _qFmt_ is empty, the formatting is defined by the number interpretation variables included at the top of the script ( _TimeFormat_ , _DateFormat_ , _TimeStampFormat_ ). The properties _qDec_ , _qThou_ , _qnDec_ , _qUseThou_ are not used.  Type is INTEGER The following applies: If a format pattern is defined in _qFmt_ , the engine looks at the values set in _qDec_ and _qThou_ . If these properties are not defined, the formatting mechanism uses the number interpretation variables included at the top of the script ( _DecimalSep_ and _ThousandSep_ ). If no format pattern is defined in _qFmt_ , no formatting is applied. The properties _qDec_ , _qThou_ , _qnDec_ , _qUseThou_ and the number interpretation variables defined in the script are not used .  Type is REAL The following applies: If a format pattern is defined in _qFmt_ , the engine looks at the values set in _qDec_ and _qThou_ . If these properties are not defined, the engine uses the number interpretation variables included at the top of the script ( _DecimalSep_ and _ThousandSep_ ). If no format pattern is defined in _qFmt_ , and if the value is almost an integer value (for example, 14,000012), the value is formatted as an integer. The properties _qDec_ , _qThou_ , _qnDec_ , _qUseThou_ are not used. If no format pattern is defined in _qFmt_ , and if _qnDec_ is defined and not 0, the property _qDec_ is used. If _qDec_ is not defined, the variable _DecimalSep_ defined at the top of the script is used. If no format pattern is defined in _qFmt_ , and if _qnDec_ is 0, the number of decimals is 14 and the property _qDec_ is used. If _qDec_ is not defined, the variable _DecimalSep_ defined at the top of the script is used.  Type is FIX The following applies: If a format pattern is defined in _qFmt_ , the engine looks at the values set in _qDec_ and _qThou_ . If these properties are not defined, the engine uses the number interpretation variables included at the top of the script ( _DecimalSep_ and _ThousandSep_ ). If no format pattern is defined in _qFmt_ , the properties _qDec_ and _qnDec_ are used. If _qDec_ is not defined, the variable _DecimalSep_ defined at the top of the script is used.  Type is MONEY The following applies: If a format pattern is defined in _qFmt_ , the engine looks at the values set in _qDec_ and _qThou_ . If these properties are not defined, the engine uses the number interpretation variables included at the top of any script ( _MoneyDecimalSep_ and _MoneyThousandSep_ ). If no format pattern is defined in _qFmt_ , the engine uses the number interpretation variables included at the top of the script ( _MoneyDecimalSep_ and _MoneyThousandSep_ ).  Type is ASCII No formatting, _qFmt_ is ignored. |
| `tags` | string[] | Yes | - | Tags added to the variable. Optional. |

<details>
<summary>Properties of `qInfo`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qId` | string | Yes | - | Identifier of the object. If the chosen identifier is already in use, the engine automatically sets another one. If an identifier is not set, the engine automatically sets one. This parameter is optional. |
| `qType` | string | No | "variable" | Object type. Default:variable |

</details>

<details>
<summary>Properties of `qNumberPresentation`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qDec` | string | Yes | - | Defines the decimal separator. Example: **.** |
| `qFmt` | string | Yes | - | Defines the format pattern that applies to _qText_ . Is used in connection to the type of the field (parameter **qType** ). For more information, see _Formatting mechanism_. Example: _YYYY-MM-DD_ for a date. |
| `qThou` | string | Yes | - | Defines the thousand separator (if any). Is used if **qUseThou** is set to 1. Example: **,** |
| `qType` | string | Yes | - | One of: U, A, I, R, F, M, D, T, TS, IV. |
| `qUseThou` | integer | No | 0 | Defines whether or not a thousands separator must be used. Default is 0. Default:0 |
| `qnDec` | integer | No | 10 | Number of decimals. Default is 10. Default:10 |

</details>

---

### variableList `object`

Properties for defining list of Variables.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qExtendsId` | string | Yes | - | Should be set to create an object that is linked to another object. Enter the identifier of the linking object (i.e the object you want to link to). If you do not want to link your object, set this parameter to an empty string. |
| `qInfo` | object | Yes | - |  |
| `qMetaDef` | object | Yes | - | Used to collect meta data.  Properties Semantic type with an empty structure. |
| `qStateName` | string | No | "$" | Name of the alternate state. Default is current selections _$_ . Default:$ |
| `qVariableListDef` | object | Yes | - | Defines the list of variables in an app. |

<details>
<summary>Properties of `qInfo`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qId` | string | Yes | - | Identifier of the object. If the chosen identifier is already in use, the engine automatically sets another one. If an identifier is not set, the engine automatically sets one. This parameter is optional. |
| `qType` | string | No | "VariableList" | List object type. Default:VariableList |

</details>

<details>
<summary>Properties of `qVariableListDef`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qData` | object | Yes | - | Contains dynamic JSON data specified by the client. |
| `qShowConfig` | boolean | No | true | Shows the system variables if set to true. Default:true |
| `qShowReserved` | boolean | No | true | Shows the reserved variables if set to true. Default:true |
| `qShowSession` | boolean | Yes | - | Shows the session variables if set to true. |
| `qType` | string | No | "variable" | Object type. Default:variable |

<details>
<summary>Properties of `qData`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `tags` | string | No | "/tags" | Path to tags in VariableProperties Default:/tags |

</details>

</details>

<details>
<summary>Examples</summary>

```javascript
const variableListProps = {
  "qInfo": {
    "qType": "VariableList",
    "qId": ""
  },
  "qVariableListDef": {
    "qData": {
      "tags": "/tags"
    },
    "qType": "variable",
    "qShowReserved": "true",
    "qShowConfig": "true",
    "qShowSession": true
  }
};
const variableList = await doc.createSessionObject(variableListProps).then(list => list.getLayout());
```

</details>

---
