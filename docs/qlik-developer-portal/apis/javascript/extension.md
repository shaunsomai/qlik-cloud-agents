---
source: https://qlik.dev/apis/javascript/extension/
last_updated: 2026-01-19T15:48:02Z
---

# Extensions

`Version: 1.1.1` | _stable_

The Extension API consists of methods and properties used to create custom legacy visualization extensions. Consider leveraging nebula.js for new extension authoring.

## Table of Contents

### Entries

- [define](#definedependencies-cb-function)
- [qext](#qext-interface)

### Definitions

- [BackendAPI](#backendapi-class)
- [Extension](#extension-interface)
- [ExtensionContext](#extensioncontext-interface)
- [ExtensionFn](#extensionfn-interface)
- [PP](#pp-namespace)
- [eachRow](#eachrow-interface)
- [empty](#empty-object)
- [successful](#successful-object)
- [supportFn](#supportfn-interface)
- [actionFn](#actionfn-interface)
- [option](#option-interface)
- [optionFn](#optionfn-interface)
- [option](#option-interface)
- [optionFn](#optionfn-interface)
- [option](#option-interface)
- [optionFn](#optionfn-interface)
- [showFn](#showfn-interface)
- [option](#option-interface)
- [showFn](#showfn-interface)

## Entries

### define(dependencies, cb) `function`

The extension as an AMD module.

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `dependencies` | string[] | Yes | - |  |
| `cb` | [ExtensionFn](#extensionfn-interface) | Yes | - |  |

---

### qext `interface`

The extension metadata file (QEXT) is a JSON file, and is used by Qlik Sense to identify the visualization extension.
It contains the metadata used for the library or assets panel. When deployed to Qlik Sense, the visualization extension is displayed in the Charts section of the assets panel or library panel.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `name` | string | Yes | - | This is the name of the visualization extension and is displayed in the library as well as in the preview.   It is recommended to use a unique name for the visualization to avoid interference with other visualizations that may have the same name. |
| `type` | 'visualization' | Yes | - | This defines the type of extension. It should always be `'visualization'` for visualization extensions. |
| `description` | string | No | - | This defines the description visible in the preview of the visualization extension. |
| `icon` | 'bar-chart-vertical' \| 'extension' \| 'filterpane' \| 'gauge-chart' \| 'line-chart' \| 'list' \| 'map' \| 'pie-chart' \| 'scatter-chart' \| 'table' \| 'text-image' \| 'treemap' | No | "extension" | This defines the icon displayed in the library. |
| `preview` | string | No | - | This defines which preview image is to be used. The preview image is displayed in a pop-up when you select the visualization extension in the library. |
| `version` | string | No | - | This defines your individual version handling of the visualization extension. This setting is manually defined. Semantic versioning is recommended. |
| `author` | string | No | - | This defines the author of the visualization extension. This setting is manually defined. |

<details>
<summary>Examples</summary>

```json
{
  "name": "Hello World",
  "description": "Hello world example",
  "preview": "helloworld.png",
  "type": "visualization",
  "version": 1,
  "author": "Qlik International"
}
```

</details>

---

## Definitions

### BackendAPI() `class`

Helper functions for Engine calls and access to Engine data. Available for extensions as
`this.backendApi`.

---

#### abortSearch() `function`

Aborts the result of a search in a list object.
Clears the existing search and returns the object to the state it was prior to the start of the search.

##### Returns

Promise<[empty](#empty-object)> - A promise of a Qlik engine response.

<details>
<summary>Examples</summary>

```javascript
this.backendApi.abortSearch();
```

</details>

---

#### acceptSearch(toggleMode) `function`

Accepts the result of a search in a list object and the search result is selected in the field.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `toggleMode` | boolean | Yes | - | If `true`, toggle state for selected values. |

##### Returns

Promise<[empty](#empty-object)> - A promise of a Qlik engine response.

<details>
<summary>Examples</summary>

```javascript
this.backendApi.acceptSearch(false);
```

</details>

---

#### applyPatches(qPatches, qSoftPatch) `function`

Updates the properties for this object.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qPatches` | QAE.NxPatch[] | Yes | - | Array of patches to apply. |
| `qSoftPatch` | boolean | Yes | - | Set to `true` if properties should be soft, that is not persisted. |

##### Returns

Promise<[empty](#empty-object)> - A promise of a Qlik engine reply.

<details>
<summary>Examples</summary>

```javascript
this.backendApi.applyPatches([
  {
    "qPath": "/qListObjectDef/qDef/qSortCriterias/0/qSortByLoadOrder",
    "qOp": "replace",
    "qValue": "-1"
  },
  {
    "qPath": "/meta",
    "qOp": "add",
    "qValue": "{ \"data\": \"this is the data\"}"
  }
], true);
```

</details>

---

#### clearSelections() `function`

Clears unconfirmed selections for this object.

##### Returns

Promise<[empty](#empty-object)> - A promise of a Qlik engine reply.

<details>
<summary>Examples</summary>

```javascript
this.backendApi.clearSelections();
```

</details>

---

#### clearSoftPatches() `function`

Clears all soft patches that have previously been applied to this object using the `applyPatches`
method.

##### Returns

Promise<[empty](#empty-object)> - A promise of a Qlik engine reply.

<details>
<summary>Examples</summary>

```javascript
this.backendApi.clearSoftPatches();
```

</details>

---

#### collapseLeft(qRow, qCol, qAll?) `function`

Collapses the left dimensions of a pivot table. Only works for HyperCubes with `qMode = 'P'` which are
not always fully expanded.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qRow` | number | Yes | - | Row index. |
| `qCol` | number | Yes | - | Column index. |
| `qAll` | boolean | No | - | If set to `true`, `qRow` and `qCol` are ignored and all cells are collapsed. |

##### Returns

Promise<[empty](#empty-object)> - A promise of a Qlik engine reply.

<details>
<summary>Examples</summary>

```javascript
this.backendApi.collapseLeft(0, 0, true);
```

</details>

---

#### collapseTop(qRow, qCol, qAll?) `function`

Collapses the top dimensions of a pivot table. Only works for hypercubes with `qMode = 'P'` which are
not always fully expanded.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qRow` | number | Yes | - | Row index. |
| `qCol` | number | Yes | - | Column index. |
| `qAll` | boolean | No | - | If set to true, `qRow` and `qCol` are ignored and all cells are collapsed. |

##### Returns

Promise<[empty](#empty-object)> - A promise of a Qlik engine reply.

<details>
<summary>Examples</summary>

```javascript
this.backendApi.collapseTop(0, 1);
```

</details>

---

#### eachDataRow(callback) `function`

Loops through data rows for this object. Only rows that are available client side will be used.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `callback` | [eachRow](#eachrow-interface) | Yes | - | Function to call for each row. Parameters are row number and row data as an array of `QAE.NxCell` objects. The loop is terminated if the function returns `false`. |

<details>
<summary>Examples</summary>

```javascript
this.backendApi.eachDataRow(function(rownum, row) {
  html += '<li class="state-' + row[0].qState + '" data-value="'
  + row[0].qElemNumber + '">' + row[0].qText;
    if(row[0].qFrequency) {
      html += '<span>' + row[0].qFrequency + '</span>';
    }
  html += '</li>';
});
```

</details>

---

#### expandLeft(qRow, qCol, qAll?) `function`

Expands the left dimensions of a pivot table. Only works for hypercubes with `qMode = 'P'` which are
not always fully expanded.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qRow` | number | Yes | - | Row index. |
| `qCol` | number | Yes | - | Column index. |
| `qAll` | boolean | No | - | If set to `true`, ignore `qRow` and `qCol` and expands all cells. |

##### Returns

Promise<[empty](#empty-object)> - A promise of a Qlik engine reply.

<details>
<summary>Examples</summary>

```javascript
this.backendApi.expandLeft(0, 0, true);
```

</details>

---

#### expandTop(qRow, qCol, qAll?) `function`

Expands the top dimensions of a pivot table. Only works for hypercubes with `qMode = 'P'` which are
not always fully expanded.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qRow` | number | Yes | - | Row index. |
| `qCol` | number | Yes | - | Column index. |
| `qAll` | boolean | No | - | If set to `true`, `qRow` and `qCol` are ignored and all cells are expanded. |

##### Returns

Promise<[empty](#empty-object)> - A promise of a Qlik engine reply.

<details>
<summary>Examples</summary>

```javascript
this.backendApi.expandTop(0, 1);
```

</details>

---

#### getData(qPages) `function`

Gets data from Qlik engine for this object.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qPages` | QAE.NxPage[] | Yes | - | An array of `QAE.NxPage` objects. |

##### Returns

`Promise<QAE.NxDataPage[]>` - A promise of `Array<QAE.NxDataPage>`.

<details>
<summary>Examples</summary>

```javascript
var self = this;
var requestPage = [{
  qTop: i + this.currpos,
  qLeft: 0,
  qWidth: 10,
  qHeight: this.displayrows
}];

this.backendApi.getData(requestPage).then(function(dataPages) {
  self.paint($element);
});
```

</details>

---

#### getDataRow(rownum) `function`

Gets a data row for this object.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `rownum` | number | Yes | - | The row number. |

##### Returns

`QAE.NxCell[]` - An array of `QAE.NxCell` or `null` if the row is not available
client side and need to be fetched with `getData`.

<details>
<summary>Examples</summary>

```javascript
var cells = this.backendApi.getDataRow(row);
if(cells) {
  cells.each(function(cell) {
    console.log('cell text: ', cell.qText);
  });
}
```

</details>

---

#### getDimensionInfos() `function`

Gets `qDimensionInfo` for this object.

##### Returns

`QAE.NxDimensionInfo[]` - An array of `QAE.NxDimensionInfo` objects.

<details>
<summary>Examples</summary>

```javascript
this.backendApi.getDimensionInfos().forEach(function(dimInfo){
  console.log('title: ', dimInfo.qFallbackTitle);
});
```

</details>

---

#### getMeasureInfos() `function`

Get `qMeasureInfo` for this object.

##### Returns

`QAE.NxMeasureInfo[]` - Array of `QAE.NxMeasureInfo` objects.

<details>
<summary>Examples</summary>

```javascript
this.backendApi.getMeasureInfos().forEach(function(measureInfo){
  console.log('title: ', measureInfo.qFallbackTitle);
});
```

</details>

---

#### getPivotData(qPages) `function`

Gets pivot data from the Qlik engine for this object. Only works for hypercubes with `qMode = 'P'`.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qPages` | QAE.NxPage[] | Yes | - | An array of request page objects. |

##### Returns

`Promise<QAE.NxPivotPage[]>` - A promise of pivot data pages.

<details>
<summary>Examples</summary>

```javascript
var requestPage = {
  qTop : 0,
  qLeft : 0,
  qWidth : 10,
  qHeight : count
};

this.backendApi.getPivotData([requestPage]).then(function(dataPages) {
  ...
});
```

</details>

---

#### getProperties() `function`

Get Properties for this object.

##### Returns

`Promise<QAE.GenericObjectProperties>` - A promise of object properties.

<details>
<summary>Examples</summary>

```javascript
var me = this;
this.backendApi.getProperties().then(function(reply){
  reply.title = 'New title';
  me.backendApi.setProperties(reply);
});
```

</details>

---

#### getReducedData(qPages, qZoomFactor, qReductionMode) `function`

Get reduced data from Qlik engine for this object. This method is intended for preserving
the shape of the data, not for viewing the actual data points.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qPages` | QAE.NxPage[] | Yes | - | An array of `QAE.NxPage` objects. |
| `qZoomFactor` | number | Yes | - | If set to -1, the Qlik engine decides the zoom factor. If `qReductionMode` is `'D1'` or `'S'`, the zoom factor is 2ⁿ. If the zoom factor is `5`, the data is reduced by a factor 32. If `qReductionMode` is `'C'`, the zoom factor defines the number of centroids. |
| `qReductionMode` | string | Yes | - | Reduction mode. One of:  - `'N'` for no data reduction. - `'D1'` to reduce a bar chart or line chart.     The profile of the chart is reduced whatever the number of dimensions in the chart. - `'S'` to reduce the resolution of a scatter plot. - `'C'` to reduce the data of a scatter plot chart. - `'ST'` to reduce the data of a stacked pivot table. |

##### Returns

`Promise<QAE.NxDataPage[]>` - A promise of reduced data pages.

<details>
<summary>Examples</summary>

```javascript
var requestPage = [{
  qTop : 0,
  qLeft : 0,
  qWidth : 10,
  qHeight : count
}];

this.backendApi.getReducedData(requestPage, -1, "D1").then(function(dataPages) {
  ...
});
```

</details>

---

#### getRowCount() `function`

Gets the total number of data rows for this object.

##### Returns

`number` - The total number of data rows.

<details>
<summary>Examples</summary>

```javascript
if (this.backendApi.getRowCount() > lastrow + 1) {
  morebutton = true;
}
```

</details>

---

#### getStackData(qPages, qMaxNbrCells?) `function`

Gets stacked data from the Qlik engine for this object. Only works for hypercubes with `qMode = 'S'`.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qPages` | QAE.NxPage[] | Yes | - | An array of request page objects. |
| `qMaxNbrCells` | number | No | 1000 | Maximum number of cells at outer level. |

##### Returns

`Promise<QAE.NxStackPage[]>` - A promise of stacked data pages.

<details>
<summary>Examples</summary>

```javascript
var requestPage = {
  qTop : 0,
  qLeft : 0,
  qWidth : 10,
  qHeight : count
};

this.backendApi.getStackData([requestPage], 1000).then(function(dataPages) {
  ...
});
```

</details>

---

#### hasSelections() `function`

Returns `true` if there are unconfirmed selections for this object.

##### Returns

`boolean` - `true` if there are unconfirmed selections.

<details>
<summary>Examples</summary>

```javascript
this.backendApi.hasSelections();
```

</details>

---

#### save() `function`  _(deprecated)_

Save this object.

##### Returns

Promise<[empty](#empty-object)> - A promise of a Qlik engine reply.

---

#### search(term) `function`

Search for a term in a list object. Results in an updated layout, containing only matching records.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `term` | string | Yes | - | Term to search for. |

##### Returns

Promise<[successful](#successful-object)> - A promise of a Qlik engine response. Note that the response will show if the search
operation was successful or not. It will not contain the matching results.

<details>
<summary>Examples</summary>

```javascript
this.backendApi.search("A");
```

</details>

---

#### selectRange(qRanges, qOrMode) `function`

Select values in this object using ranges. Only applicable to hypercubes.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qRanges` | QAE.NxRangeSelectionInfo[] | Yes | - | Array of ranges to select. |
| `qOrMode` | boolean | Yes | - | If true, only one of the measures needs to be in range. |

##### Returns

Promise<[successful](#successful-object)> - A promise of a Qlik engine response with the status of the operation, i.e. if it was
successful or not, and details on which objects were updated following the selections.

<details>
<summary>Examples</summary>

```javascript
var range = {
  qMeasureIx: 1,
  qRange: {
  qMin: 10,
  qMax: 100,
  qMinInclEq: true,
  qMaxInclEq: true
};
this.backendApi.selectRange([range], false);
```

</details>

---

#### selectValues(qDimNo, qValues, qToggleMode) `function`

Selects values in this object with a Qlik engine call that triggers a repaint of the object.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qDimNo` | number | Yes | - | Dimension number. `0` is the first dimension. |
| `qValues` | number[] | Yes | - | Array of values (`qElemNumber` in the matrix from engine) to select or deselect. |
| `qToggleMode` | boolean | Yes | - | If `true`, values in the field are selected in addition to any previously selected items. If `false`, values in the field are selected while previously selected items are deselected. |

<details>
<summary>Examples</summary>

```javascript
$element.find('li').on('qv-activate', function() {
  if(this.hasAttribute("data-value")) {
    var value = parseInt(this.getAttribute("data-value"), 10), dim = 0;
    self.backendApi.selectValues(dim, [value], true);
  }
});
```

</details>

---

#### setCacheOptions(opts) `function`

Sets caching of page requests.

When enabled, calls to `getData` are throttled and new requests are created based on internal cache settings.
If you want full control of requests to `getData`, set `enabled = false`.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `opts` | object | Yes | - |  |

<details>
<summary>Examples</summary>

```javascript
this.backendApi.setCacheOptions({
  enabled: false // disable cache
})
```

</details>

---

#### setProperties(props) `function`

Set properties for this object.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `props` | QAE.GenericObjectProperties | Yes | - | The properties to set. |

##### Returns

Promise<[empty](#empty-object)> - A promise of a Qlik engine reply.

<details>
<summary>Examples</summary>

```javascript
var me = this;
this.backendApi.getProperties().then(function(reply){
  reply.title = 'New title';
  me.backendApi.setProperties(reply);
});
```

</details>

---

### Extension `interface`

Interface for a Qlik Sense Extension

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `initialProperties` | QAE.GenericObjectProperties | No | - |  |
| `definition` | [Component](#component-union) | No | - |  |
| `support` | object | No | - |  |

<details>
<summary>Properties of `support`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `export` | boolean \| [supportFn](#supportfn-interface) | No | false | Enables or disables the ability to export the visualization extension as an image and as a PDF. Also handles the ability to allow the visualization extension to be included in a export from Storytelling (PowerPoint or PDF). When set to `true`, the Export as an image and the Export to PDF context menu options for the visualization extension. This also allow visualization extensions to be part of stories exported to PowerPoint or PDF on the Export story to PowerPoint and Export story to PDF context menu options |
| `exportData` | boolean \| [supportFn](#supportfn-interface) | No | true | Enables or disables the ability to export data from the visualization extension and save it in an XLSX file. When set to `true`, the Export data context menu option is enabled for the visualization extension. |
| `snapshot` | boolean \| [supportFn](#supportfn-interface) | No | false | Enables or disables the ability to take snapshots of the visualization extension for use in Data Storytelling. |
| `viewData` | boolean \| [supportFn](#supportfn-interface) | No | false | Enables or disables the ability to show the visualization extension as a table. |

</details>

---

#### mounted($element) `function`

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `$element` | jqLiteElement | Yes | - |  |

---

#### paint($element, layout) `function`

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `$element` | jqLiteElement | Yes | - |  |
| `layout` | QAE.GenericObjectLayout | Yes | - |  |

##### Returns

`Promise<void>`

---

#### updateData(layout) `function`

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `layout` | QAE.GenericObjectLayout | Yes | - |  |

##### Returns

`Promise<void>`

---

#### resize($element, layout) `function`

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `$element` | jqLiteElement | Yes | - |  |
| `layout` | QAE.GenericObjectLayout | Yes | - |  |

##### Returns

`Promise<void>`

---

#### beforeDestroy() `function`

---

### ExtensionContext `interface`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `backendApi` | [BackendAPI](#backendapi-class) | Yes | - |  |

---

#### selectValues(qDimNo, qValues, qToggleMode) `function`

Selects or deselects a value. If not in selection mode, it is initialized and
the selection toolbar is displayed.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qDimNo` | number | Yes | - | Dimension number 0 = first dimension. |
| `qValues` | number[] | Yes | - | Array of values (qElemNumber in the matrix from engine) to select or deselect. |
| `qToggleMode` | boolean | Yes | - | Toggle mode. |

<details>
<summary>Examples</summary>

```javascript
$element.find('.selectable').on('qv-activate', function() {
	if(this.hasAttribute("data-value")) {
		var value = parseInt(this.getAttribute("data-value"), 10), dim = 0;
			self.selectValues(dim, [value], true);
			$(this).toggleClass("selected");
		}
	});
```

</details>

---

#### paint($element, layout) `function`

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `$element` | jqLiteElement | Yes | - |  |
| `layout` | QAE.GenericObjectLayout | Yes | - |  |

##### Returns

`Promise<void>`

---

#### updateData(layout) `function`

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `layout` | QAE.GenericObjectLayout | Yes | - |  |

##### Returns

`Promise<void>`

---

### ExtensionFn `interface`

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `libs` | any[] | Yes | - |  |

#### Returns

[Extension](#extension-interface)

---

### PP `namespace`

Property panel definitions

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `Component` | [Items](#items-interface) \| [Accordion](#accordion-interface) \| [Button](#button-interface) \| [Buttongroup](#buttongroup-interface) \| [Checkbox](#checkbox-interface) \| [ColorPicker](#colorpicker-interface-experimental) \| [Dropdown](#dropdown-interface) \| [Integer](#integer-interface) \| [Link](#link-interface) \| [List](#list-interface-experimental) \| [Media](#media-interface-experimental) \| [Number](#number-interface) \| [Radiobuttons](#radiobuttons-interface) \| [RangeSlider](#rangeslider-interface) \| [Slider](#slider-interface) \| [String](#string-interface) \| [Switch](#switch-interface) \| [Text](#text-interface) \| [Textarea](#textarea-interface) \| [DefaultDimensions](#defaultdimensions-interface) \| [DefaultMeasures](#defaultmeasures-interface) \| [DefaultSettings](#defaultsettings-interface) \| [DefaultSorting](#defaultsorting-interface) \| [DefaultAddons](#defaultaddons-interface) | Yes | - |  |

---

#### Accordion `interface`

The accordion definition property template can be used to add a custom accordion.

##### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | 'items' | Yes | - |  |
| `component` | 'accordion' | Yes | - |  |
| `items` | object<string, [Component](#component-union)> | Yes | - |  |
| `label` | string | No | "" | Defines the label that is displayed in the property panel. |

---

#### Button `interface`

The button definition property template can be used to add a custom property of button type.

##### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `label` | string | No | "" | The label that is displayed on the button. |
| `component` | 'button' | Yes | - | Defines how the property is visualized in the property panel. Used to override the default component that comes with the `type` setting. |
| `ref` | string | No | - | Name or ID used to reference a property. |
| `type` | 'string' \| 'integer' \| 'number' \| 'array' \| 'boolean' | No | - | Used for all custom property type definitions. Can be `'string'`, `'integer'`, `'number'`, `'array'` or `'boolean'`. |
| `action` | [actionFn](#actionfn-interface) | No | - | Defines the action when clicking the button. |

---

#### Buttongroup `interface`

The button group definition property template can be used to add a custom property of radio button type.

##### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | 'string' | Yes | - |  |
| `component` | 'buttongroup' | Yes | - | Defines how the property is visualized in the property panel. Used to override the default component that comes with the `type` setting. |
| `ref` | string | No | - | Name or ID used to reference a property. |
| `options` | [option](#option-interface)[] \| [optionFn](#optionfn-interface) | Yes | - |  |
| `defaultValue` | any | Yes | - | Defines the default value of your custom property. |
| `label` | string | No | "" | Defines the label that is displayed in the property panel. |

---

#### Checkbox `interface`

The check box definition property template can be used to add a custom property of check box type.

##### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | 'boolean' | Yes | - |  |
| `component` | 'checkbox' | Yes | - |  |
| `ref` | string | No | - | Name or ID used to reference a property. |
| `defaultValue` | boolean | No | true | Used for defining the default value of your custom property. |
| `label` | string | No | "" | Defines the label that is displayed in the property panel. |

---

#### ColorPicker `interface`  **[experimental]**

The color-picker definition property template can be used to add a custom color-picker property.

##### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | 'integer' | Yes | - |  |
| `component` | 'color-picker' | Yes | - |  |
| `ref` | string | No | - | Name or ID used to reference a property. |
| `defaultValue` | integer | Yes | 3 | Used for defining the default value of your custom property. |
| `label` | string | No | "" | Defines the label that is displayed in the property panel. |

---

#### DefaultAddons `interface`

##### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `uses` | 'addons' | Yes | - |  |

<details>
<summary>Examples</summary>

```js
{
  uses: 'addons',
}

</details>

---

#### DefaultDimensions `interface`

##### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `uses` | 'dimensions' | Yes | - |  |
| `min` | number | No | 1 | Defines the minimum number of dimensions. |
| `max` | number | No | - | Defines the maximum number of dimensions. |

<details>
<summary>Examples</summary>

```js
{
  uses: 'dimensions',
  min: 1,
  max: 2
}

</details>

---

#### DefaultMeasures `interface`

##### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `uses` | 'measures' | Yes | - |  |
| `min` | number | No | 1 | Defines the minimum number of measures. |
| `max` | number | No | - | Defines the maximum number of measures. |

<details>
<summary>Examples</summary>

```js
{
  uses: 'measures',
  min: 1,
  max: 2
}

</details>

---

#### DefaultSettings `interface`

##### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `uses` | 'settings' | Yes | - |  |

<details>
<summary>Examples</summary>

```js
{
  uses: 'settings',
}

</details>

---

#### DefaultSorting `interface`

##### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `uses` | 'sorting' | Yes | - |  |

<details>
<summary>Examples</summary>

```js
{
  uses: 'sorting',
}

</details>

---

#### Dropdown `interface`

The drop down list definition property template can be used to add a custom property of drop down list type.

##### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | 'string' | Yes | - |  |
| `component` | 'dropwdown' | Yes | - | Defines how the property is visualized in the property panel. Used to override the default component that comes with the `type` setting. |
| `ref` | string | No | - | Name or ID used to reference a property. |
| `defaultValue` | any | No | - | Defines the default value of your custom property. |
| `options` | [option](#option-interface)[] \| [optionFn](#optionfn-interface) | Yes | - |  |
| `label` | string | No | "" | Defines the label that is displayed in the property panel. |

---

#### Integer `interface`

The integer definition property template can be used to add a custom property of integer type.

##### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | 'integer' | Yes | - |  |
| `component` | 'integer' | Yes | - | Defines how the property is visualized in the property panel. Used to override the default component that comes with the `type` setting. |
| `min` | number | No | - | Used for defining the minimum value of the property. |
| `max` | number | No | - | Used for defining the maximum value of the property. |
| `defaultValue` | any | Yes | - | Defines the default value of your custom property. |
| `label` | string | No | "" | Defines the label that is displayed in the property panel. |
| `ref` | string | No | - | Name or ID used to reference a property. |

<details>
<summary>Examples</summary>

```js
{
  type: 'integer',
  label: 'Minimum',
  ref: 'myProperties.min',
  defaultValue: '15',
  min: '10',
  max: '20'
}
```

</details>

---

#### Items `interface`

##### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `component` | 'items' | No | "items" |  |
| `items` | object<string, [Component](#component-union)> | Yes | - |  |

---

#### Link `interface`

The link definition property template can be used to add a custom property of link type.

##### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `component` | 'link' | Yes | - |  |
| `label` | string | No | "" | Defines the label that is displayed in the property panel. |
| `url` | string | Yes | - | Defines the web address used in the link. |
| `type` | 'string' \| 'integer' \| 'number' \| 'array' \| 'boolean' | Yes | - | Used for all custom property type definitions. Can be `'string'`, `'integer'`, `'number'`, `'array'` or `'boolean'`. |

---

#### List `interface`  **[experimental]**

The list definition property template can be used to add a custom property of list type.

##### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | 'array' | Yes | - |  |
| `component` | 'list' | Yes | - |  |
| `ref` | string | No | - | Name or ID used to reference a property. |
| `items` | object<string, [Component](#component-union)> | Yes | - |  |
| `itemTitleRef` | string | No | - | Defines the title of the section items. |
| `addTranslation` | string | No | - | Defines a label of the button used to add new items. |
| `allowAdd` | boolean | No | - | `true` adds a button for adding new items. |
| `allowMove` | boolean | No | - | `true` enables the ability to move the item in the properties panel. |
| `label` | string | No | "" | Defines the label that is displayed in the property panel. |

---

#### Media `interface`  **[experimental]**

The media definition property template can be used to add a custom property of media type.

##### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `component` | 'media' | Yes | - |  |
| `type` | 'string' | Yes | - |  |
| `label` | string | No | "" | Defines the label that is displayed in the property panel. |
| `layoutRef` | string | Yes | - | Name or Id used to reference the layout. |

<details>
<summary>Examples</summary>

```js
{
  label:"My media",
  component: "media",
  ref: "myMedia",
  layoutRef: "myMedia",
  type: "string"
}
```

</details>

---

#### Number `interface`

The number definition property template can be used to add a custom property of number type.

##### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | 'number' | Yes | - |  |
| `component` | 'number' | Yes | - | Defines how the property is visualized in the property panel. Used to override the default component that comes with the `type` setting. |
| `min` | number | No | - | Used for defining the minimum value of the property. |
| `max` | number | No | - | Used for defining the maximum value of the property. |
| `defaultValue` | any | Yes | - | Defines the default value of your custom property. |
| `label` | string | No | "" | Defines the label that is displayed in the property panel. |
| `ref` | string | No | - | Name or ID used to reference a property. |

---

#### Radiobuttons `interface`

The radio button definition property template can be used to add a custom property of radio button type.

##### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | 'string' | Yes | - |  |
| `component` | 'radiobuttons' | Yes | - | Defines how the property is visualized in the property panel. Used to override the default component that comes with the `type` setting. |
| `ref` | string | No | - | Name or ID used to reference a property. |
| `options` | [option](#option-interface)[] \| [optionFn](#optionfn-interface) | Yes | - |  |
| `defaultValue` | any | Yes | - | Defines the default value of your custom property. |
| `label` | string | No | "" | Defines the label that is displayed in the property panel. |

---

#### RangeSlider `interface`

The range-slider definition property template can be used to add a custom property of range-slider type.

##### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | 'array' | Yes | - |  |
| `component` | 'slider' | Yes | - | Defines how the property is visualized in the property panel. Used to override the default component that comes with the `type` setting. |
| `defaultValue` | (number, number)[] | Yes | - | Defines the default value of your custom property. |
| `min` | number | No | - | Defines the minimum value of the property. |
| `max` | number | No | - | Defines the maximum value of the property. |
| `step` | number | No | - | Defines the step value of the property. |
| `label` | string | No | "" | Defines the label that is displayed in the property panel. |
| `ref` | string | No | - | Name or ID used to reference a property. |

---

#### Slider `interface`

The slider definition property template can be used to add a custom property of range-slider type.

##### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | 'number' | Yes | - | This field is mandatory and should always be `"number"` for a slider property type definition. > The slider effect is achieved by defining the `component` field to `'slider'`. |
| `component` | 'slider' | Yes | - | Defines how the property is visualized in the property panel. Used to override the default component that comes with the `type` setting. |
| `min` | number | No | - | Defines the minimum value of the property. |
| `max` | number | No | - | Defines the maximum value of the property. |
| `step` | number | No | - | Defines the step value of the property. |
| `defaultValue` | any | Yes | - | Defines the default value of your custom property. |
| `label` | string | No | "" | Defines the label that is displayed in the property panel. |
| `ref` | string | No | - | Name or ID used to reference a property. |

---

#### String `interface`

The string definition property template can be used to add a custom property of string type.

##### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | 'string' | Yes | - |  |
| `component` | 'string' | Yes | - |  |
| `expression` | '' \| 'always' \| 'optional' | No | "" | Defines if values starting with `=` will be treated as expressions that are evaluated by the Qlik Sense Engine. - `"always"`: the property will always be evaluated as an expression meaning that the property will be the value of for example `"Avg(Sales)"`. - `"optional"`: the property will only be evaluated as an expression if a `=` sign is leading the expression. For example `"Avg(Sales)"` will be presented as the string `"Avg(Sales)"` while `"=Avg(Sales)"` will be evaluated as an expression and presented as either `5` or `"5"` depending on if it is used in a Number/Integer component or in a String component. - `""`: If the setting is left empty or not defined at all, the property will not be evaluated as an expression meaning that the property will be the string `"Avg(Sales)"`. |
| `show` | boolean \| [showFn](#showfn-interface) | No | true |  |
| `maxLength` | number | No | - | The maximum number of characters the string can consist of. |
| `defaultValue` | any | Yes | - | Defines the default value of your custom property. |
| `label` | string | No | "" | Defines the label that is displayed in the property panel. |
| `ref` | string | No | - | Name or ID used to reference a property. |

---

#### Switch `interface`

The switch definition property template can be used to add a custom property of switch type.

##### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | 'boolean' | Yes | - |  |
| `component` | 'switch' | Yes | - |  |
| `defaultValue` | boolean | Yes | true | Used for defining the default value of your custom property. |
| `options` | ([option](#option-interface), [option](#option-interface))[] | Yes | - |  |
| `label` | string | No | "" | Defines the label that is displayed in the property panel. |
| `ref` | string | No | - | Name or ID used to reference a property. |

---

#### Text `interface`

The text definition property template can be used to add a custom property of text type.

##### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | 'string' \| 'integer' \| 'number' \| 'array' \| 'boolean' | No | - | Used for all custom property type definitions. Can be `'string'`, `'integer'`, `'number'`, `'array'` or `'boolean'`. |
| `component` | 'text' | Yes | - |  |
| `label` | string | No | "" | Defines the label that is displayed in the property panel. |

---

#### Textarea `interface`

The text area definition property template can be used to add a custom property of text area type.

##### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | 'textarea' | Yes | - |  |
| `component` | 'textarea' | Yes | - |  |
| `rows` | number | No | 3 | The amount of rows in the text area component. |
| `maxLength` | number | No | 512 | Defines the maximum number of characters in the text. |
| `show` | boolean \| [showFn](#showfn-interface) | No | true |  |
| `defaultValue` | any | Yes | - | Defines the default value of your custom property. |
| `label` | string | No | "" | Defines the label that is displayed in the property panel. |
| `ref` | string | No | - | Name or ID used to reference a property. |

---

### eachRow `interface`

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `rowIdx` | number | Yes | - |  |
| `row` | QAE.NxCell[] | Yes | - |  |

---

### empty `object`

---

### successful `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qSuccess` | boolean | Yes | - |  |

---

### supportFn `interface`

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `data` | QAE.GenericObjectLayout | Yes | - |  |

#### Returns

`boolean`

---

### actionFn `interface`

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `data` | QAE.GenericObjectProperties | Yes | - |  |

---

### option `interface`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `value` | any | Yes | - |  |
| `label` | string | No | "" |  |
| `tooltip` | string | No | - |  |

---

### optionFn `interface`

#### Returns

Promise<[option](#option-interface)[]>

---

### option `interface`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `value` | any | Yes | - |  |
| `label` | string | Yes | - |  |

---

### optionFn `interface`

#### Returns

[option](#option-interface)[] | Promise<[option](#option-interface)[]>

---

### option `interface`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `value` | string | Yes | - |  |
| `label` | string | Yes | - |  |

---

### optionFn `interface`

#### Returns

[option](#option-interface)[] | Promise<[option](#option-interface)[]>

---

### showFn `interface`

#### Returns

`boolean`

---

### option `interface`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `value` | boolean | Yes | - |  |
| `label` | string | Yes | - |  |

---

### showFn `interface`

#### Returns

`boolean`

---
