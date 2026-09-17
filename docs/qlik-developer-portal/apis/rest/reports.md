# Reports

**Base URL:** `https://{tenant}.{region}.qlikcloud.com`

Reports are downloadable assets generated from data in analytics applications.

## Table of Contents

| Method | Path | Description |
|--------|------|-------------|
| `POST` | [`/api/v1/reports`](#post-apiv1reports) |  |
| `GET` | [`/api/v1/reports/{id}/outputs`](#get-apiv1reportsidoutputs) | Get the list of the outputs produced so far for the given report request. The outputs are generated asynchronously  |
| `GET` | [`/api/v1/reports/{id}/status`](#get-apiv1reportsidstatus) |  |

## API Reference

### POST /api/v1/reports

- **Rate Limit:** Special (10 requests per minute)

#### Request Body

**Required**

Definition of the report request.
Please note that sense-powerpoint-template-1.0, sense-word-template-1.0, sense-story-x.0 and qv-data-x.0 types are only for internal use.

Each report request type requires a specific template to be provided:
 - composition-1.0 requires compositionTemplates to be set
 - sense-excel-template-1.0 requires senseExcelTemplate to be set
 - sense-image-1.0 requires senseImageTemplate to be set
 - sense-sheet-1.0 requires senseSheetTemplate to be set
 - sense-data-1.0 requires senseDataTemplate to be set
 - sense-pixel-perfect-template-1.0 requires sensePixelPerfectTemplate to be set
 - sense-html-template-1.0 requires senseHtmlTemplate to be set
 - sense-powerpoint-template-1.0 requires sensePowerPointTemplate to be set
 - sense-word-template-1.0 requires senseWordTemplate to be set

Each template type supports specific output types:
 - composition-1.0 supports only pdfcomposition and pptxcomposition output types
 - sense-excel-template-1.0 supports excel and pdf output type
 - sense-image-1.0 supports pdf, pptx and image output types
 - sense-sheet-1.0 supports pdf and pptx output type
 - sense-data-1.0 supports xlsx output type
 - sense-pixel-perfect-template-1.0 supports pdf output types
 - sense-html-template-1.0 supports html output types
 - sense-powerpoint-template-1.0 supports powerpoint and pdf output types
 - sense-word-template-1.0 supports word and pdf output types

Each output type requires a specific output to be provided:
 - pdfcomposition requires pdfCompositionOutput to be set
 - pptxcomposition requires pptxCompositionOutput to be set
 - pdf requires pdfOutput to be set
 - pptx requires pptxOutput to be set
 - image requires imageOutput to be set
 - xlsx requires xlsxOutput to be set


**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `meta` | object | No | Define the request metadata. It includes priority, deadline and future settings on execution policy of the request. |
| `type` | string | Yes | Template type and version using semantic versioning. It must have the following name convention: dashed-separated-template-name-MAJOR.MINOR. Please note that sense-powerpoint-template-1.0, sense-word-template-1.0, sense-story-x.0 and qv-data-x.0 are only for internal use.  Each type requires a specific template to be provided:   - composition-1.0 requires compositionTemplates to be set   - sense-excel-template-1.0 requires senseExcelTemplate to be set   - sense-image-1.0 requires senseImageTemplate to be set   - sense-sheet-1.0 requires senseSheetTemplate to be set   - sense-data-1.0 requires senseDataTemplate to be set   - sense-pixel-perfect-template-1.0 requires sensePixelPerfectTemplate to be set   - sense-html-template-1.0 requires senseHtmlTemplate to be set   - sense-powerpoint-template-1.0 requires sensePowerPointTemplate to be set   - sense-word-template-1.0 requires senseWordTemplate to be set  Each template type supports specific output types:   - composition-1.0 supports pdfcomposition and pptxcomposition output type   - sense-excel-template-1.0 supports excel and pdf output type   - sense-image-1.0 supports pdf, pptx and png output types   - sense-sheet-1.0 supports pdf, pptx output type   - sense-data-1.0 supports xlsx output type   - sense-pixel-perfect-template-1.0 supports pdf output types   - sense-html-template-1.0 supports html output types   - sense-powerpoint-template-1.0 supports powerpoint and pdf output types   - sense-word-template-1.0 supports word and pdf output types  Each output type requires a specific output to be provided:   - pdfcomposition requires pdfCompositionOutput to be set   - pptxcomposition requires pptxCompositionOutput to be set   - pdf requires pdfOutput to be set   - pptx requires pptxOutput to be set   - image requires imageOutput to be set   - xlsx requires xlsxOutput to be set  Enum: "composition-1.0", "sense-image-1.0", "sense-data-1.0", "sense-sheet-1.0", "sense-story-1.0", "qv-data-1.0", "qv-data-2.0", "sense-excel-template-1.0", "sense-pixel-perfect-template-1.0", "sense-html-template-1.0", "sense-powerpoint-template-1.0", "sense-word-template-1.0" |
| `output` | object | Yes |  |
| `definitions` | object | No | Definitions of common properties that are shared between templates, e.g. selectionsByState can be the same for all templates within a composition of templates. |
| `senseDataTemplate` | object | No |  |
| `senseHtmlTemplate` | object | No | Used to produce reports from a template file. |
| `senseWordTemplate` | object | No | Used to produce reports from a template file. |
| `senseExcelTemplate` | object | No | Used to produce reports from a template file. |
| `senseImageTemplate` | object | No | Used to export a single visualization as pdf, pptx or png. |
| `senseSheetTemplate` | object | No | Used to export a sheet as pdf or pptx. |
| `compositionTemplates` | object[] | No | Composition of senseSheetTemplate and/or senseImageTemplate templates. |
| `requestCallBackAction` | object | No | The callback to be performed once the report is done. |
| `sensePowerPointTemplate` | object | No | Used to produce reports from a template file. |
| `sensePixelPerfectTemplate` | object | No | Used to produce reports from a template file. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `outputTtl` | string | No | Time to live of the final result artifacts in ISO8601 duration format. After that duration the request and underlying output files will not be guaranteed to be available. Default is 1 hour. |
| `exportDeadline` | string | No | The maximum interval, starting from the time the API request is received, within which a report must be produced, past this interval the report generation fails. The default value is 10 minutes, the maximum allowed value is 4 hours. The recommended value for standard apps and exports (image, data, sheet) is 10 minutes, for larger apps or reports using composition or file based templates (Excel, PixelPerfect, HTML...) it should be set to 1 hour. |

</details>

<details>
<summary>Properties of `output`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | Yes | The generated report type.  Each template type supports specific output types:    - composition-1.0 supports only pdfcomposition and pptxcomposition output types    - sense-excel-template-1.0 supports only excel and pdf output type    - sense-pixel-perfect-template-1.0 supports only pdf output type    - sense-html-template-1.0 supports only html output type    - sense-powerpoint-template-1.0 supports powerpoint and pdf output types    - sense-word-template-1.0 supports word and pdf output types    - sense-image-1.0 supports pdf, pptx and image output types    - sense-sheet-1.0 supports pdf and pptx output type    - sense-data-1.0 supports xlsx output type  Each output type requires a specific output to be provided:    - excel requires excelOutput to be set    - pdfcomposition requires pdfCompositionOutput to be set    - pptxcomposition requires pptxCompositionOutput to be set    - pdf requires pdfOutput to be set    - pptx requires pptxOutput to be set    - image requires imageOutput to be set    - csv doesn't have csv output    - xlsx requires xlsxOutput to be set  Enum: "image", "pdf", "xlsx", "jsondata", "pdfcomposition", "excel", "pptx", "pptxcomposition", "csv", "cycle", "html", "powerpoint", "word" |
| `outputId` | string | Yes | The output identifier which uniquely identifies an output (PDF, image etc.) within the same request. It does not need to be a GUID. No spaces and colons are allowed in the outputId string. |
| `pdfOutput` | object | No | Output to be used to export a single visualization, a sheet, Sense Excel template as pdf. For Sense Excel template (sense-excel-template-1.0) no properties are needed, any property specified has no effect. |
| `pptxOutput` | object | No | Output to be used to export a single visualization or a sheet as PowerPoint presentation. |
| `cycleOutput` | object | No |  |
| `excelOutput` | object | No | Output to be used to export an excel template. |
| `imageOutput` | object | No | Output to be used to export a single visualization as image. |
| `callBackAction` | object | No | The callback to be performed once the report is done. |
| `pdfCompositionOutput` | object | No | Output to be used to export a composition of templates as pdf. |
| `pptxCompositionOutput` | object | No | Output to be used to export a composition of templates as pptx. |

<details>
<summary>Properties of `pdfOutput`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `size` | string | No | Size of the pdf page. Enum: "A1", "A2", "A3", "A4", "A5", "A6", "Letter", "Legal", "Tabloid" |
| `align` | object | No | Content alignment. |
| `properties` | object | No | Properties of the document. In case of multiple composition, only properties specified in the composition output are taken and the ones specified in each output item are ignored. |
| `resizeData` | object | No | The area where the object (eg. sheet, chart) is printed. Required in case of "fit" resizeType. |
| `resizeType` | string | No | The type of resize to be performed:   - none is used to export a visualization, sheet or story as is (e.g. normal size), regardless of its size. This may result in cropping.   - autofit automatically fits the visualization, sheet or story into the output size (i.e. A4, A3 etc.). Any provided resizeData parameter will be ignored for this configuration.   - fit fits the visualization, sheet or story into the area specified in resizeData. The content will be rescaled to fit in that area.  Enum: "none", "autofit", "fit" |
| `orientation` | string | No | P for portrait, L for landscape and A for auto-detect. Auto-detect sets the orientation depending on the content width and height proportions: if content width > height the orientation is automatically set to landscape, portrait otherwise. Enum: "P", "L", "A" |
| `imageRenderingDpi` | number | No | This value is used for rendered images only, set to a default of 300 dpi. |

<details>
<summary>Properties of `align`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `properties`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `resizeData`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `pptxOutput`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `size` | string | No | Size of the PowerPoint slide:   - Widescreen: 960x540   - OnScreen: 720x540   - OnScreen16x9: 720x405   - OnScreen16x10: 720x450  Enum: "Widescreen", "OnScreen", "OnScreen16x9", "OnScreen16x10" |
| `properties` | object | No | Properties of the document. In case of multiple composition, only properties specified in the composition output are taken and the ones specified in each output item are ignored. |
| `resizeType` | string | No | The type of resize to be performed. Autofit automatically fits the visualization, sheet or story into the output size (i.e. Widescreen, OnScreen etc.).  Enum: "autofit" |
| `orientation` | string | No | L for landscape, P for portrait and A for auto-detect. Auto-detect sets landscape, the default PowerPoint orientation. Enum: "L", "P", "A" |
| `imageRenderingDpi` | number | No | This value is used for rendered images only, set to a default of 300 dpi. |

<details>
<summary>Properties of `properties`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `cycleOutput`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | Yes | Enum: "excel", "pdf", "html", "powerpoint", "word" |
| `pdfOutput` | object | No | Output to be used to export a single visualization, a sheet, Sense Excel template as pdf. For Sense Excel template (sense-excel-template-1.0) no properties are needed, any property specified has no effect. |
| `excelOutput` | object | No | Output to be used to export an excel template. |
| `namingPattern` | string | No | not needed at initial phase Enum: "fieldValueWithUnderscore" |

<details>
<summary>Properties of `pdfOutput`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `excelOutput`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `excelOutput`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `outFormat` | string | No | The output format of the report to be produced. Enum: "xlsx" |

</details>

<details>
<summary>Properties of `imageOutput`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `outDpi` | integer | No | Image resolution in DPI (default 96 DPI). |
| `outZoom` | number | No | The scale factor to be applied in image scaling. A zoom greater than 5 will not be applied to the device pixel ratio which will remain fixed at 5. |
| `outFormat` | string | No | The image format of the report to be produced. Enum: "png", "jsondata" |

</details>

<details>
<summary>Properties of `callBackAction`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpRequest` | object | No | Http callback. The provided uri will be called once the report is done. |

<details>
<summary>Properties of `httpRequest`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `pdfCompositionOutput`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pdfOutputs` | object[] | No | The ordered list of PDF outputs, the number must match the composable templates. |
| `properties` | object | No | Properties of the document. In case of multiple composition, only properties specified in the composition output are taken and the ones specified in each output item are ignored. |

<details>
<summary>Properties of `pdfOutputs`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `properties`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `pptxCompositionOutput`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `pptxOutput` | object | No | Output to be used to export a single visualization or a sheet as PowerPoint presentation. |

<details>
<summary>Properties of `pptxOutput`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `definitions`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `selectionsByState` | object | No | It maps an ID to a selectionsByState object. |

</details>

<details>
<summary>Properties of `senseDataTemplate`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Sense visualization id. Visualizations created "on the fly" are not supported. |
| `appId` | string | Yes |  |
| `patches` | object[] | No | Patches to apply to sense charts. Patches are soft properties meaning that are not persistent and they live within a session. |
| `variables` | array | No |  |
| `exportOptions` | object | No |  |
| `selectionType` | string | No | Enum: "selectionsByState", "temporaryBookmark", "persistentBookmark", "temporaryBookmarkV2" |
| `selectionStrategy` | string | No | Enum: "failOnErrors", "ignoreErrorsReturnDetails", "ignoreErrorsNoDetails" |
| `selectionsByState` | object | No | Map of selections to apply by state. Maximum number of states allowed is 125. Maximum number of fields allowed is 125 and maximum number of overall field values allowed is 150000. |
| `persistentBookmark` | object | No |  |
| `temporaryBookmarkV2` | object | No | The temporary bookmark to apply. Patches and Variables are ignored if passed to the API, because they already are applied in the backend. |
| `reloadTimestampMatchType` | string | No | Choose the reloadTimestamp constraint to apply. An empty value leads to the default noCheck. Enum: "noCheck", "requestTimeExact" |

<details>
<summary>Properties of `patches`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `qOp` | string | Yes | Enum: "add", "remove", "replace" |
| `qPath` | string | Yes | Path to the property to add, remove or replace. |
| `qValue` | string | No | Corresponds to the value of the property to add or to the new value of the property to update. |

</details>

<details>
<summary>Properties of `exportOptions`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `showTitles` | boolean | No | Show Visualization Title, SubTitle, Footnote in the artifact produced |
| `showTotals` | boolean | No | Show Visualization Totals in the artifact produced |
| `showSelections` | boolean | No | Show the Selections Applied to the Visualization in the artifact produced |

</details>

<details>
<summary>Properties of `persistentBookmark`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Sense Persistence Bookmark id. |

</details>

<details>
<summary>Properties of `temporaryBookmarkV2`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Sense Temporary Bookmark id. |

</details>

</details>

<details>
<summary>Properties of `senseHtmlTemplate`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `jsOpts` | object | No | A JSON object that is passed as-is to the mashup page while rendering, this will be applied to all charts within the sheet. It includes properties of the whole sheet such as theme, gradient etc. Currently only the "theme" and "language" properties are supported. |
| `cycleFields` | string[] | No | The values of the field to be selected. |
| `selectionChain` | object[] | No | Array of ChainableSelection |
| `templateLocation` | object | Yes | The location of the report template. Currently it can be an absolute or relative URL to a persisted report template, or to a template file saved as temporary content, as in the following examples: - https://qlikcloud.com:443/api/v1/report-templates/223940f7-3170-46b7-91ea-e0c81230adf7 - https://qlikcloud.com:443/api/v1/temp-contents/653bb4acae966r0730da15fc |
| `reloadTimestampMatchType` | string | No | Choose the reloadTimestamp constraint to apply. An empty value leads to the default noCheck. Enum: "noCheck", "requestTimeExact" |

<details>
<summary>Properties of `selectionChain`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `selectionType` | string | Yes | Enum: "selectionFilter", "persistentBookmark", "temporaryBookmarkV2" |
| `selectionFilter` | object | No |  |
| `persistentBookmark` | object | No |  |
| `temporaryBookmarkV2` | object | No | The temporary bookmark to apply. Patches and Variables are ignored if passed to the API, because they already are applied in the backend. |

<details>
<summary>Properties of `selectionFilter`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `persistentBookmark`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `temporaryBookmarkV2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `templateLocation`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | string | Yes | The report template location path. |
| `format` | string | No | Enum: "url" |

</details>

</details>

<details>
<summary>Properties of `senseWordTemplate`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `jsOpts` | object | No | A JSON object that is passed as-is to the mashup page while rendering, this will be applied to all charts within the sheet. It includes properties of the whole sheet such as theme, gradient etc. Currently only the "theme" and "language" properties are supported. |
| `cycleFields` | string[] | No | The values of the field to be selected. |
| `selectionChain` | object[] | No | Array of ChainableSelection |
| `templateLocation` | object | Yes | The location of the report template. Currently it can be an absolute or relative URL to a persisted report template, or to a template file saved as temporary content, as in the following examples: - https://qlikcloud.com:443/api/v1/report-templates/223940f7-3170-46b7-91ea-e0c81230adf7 - https://qlikcloud.com:443/api/v1/temp-contents/653bb4acae966r0730da15fc |
| `reloadTimestampMatchType` | string | No | Choose the reloadTimestamp constraint to apply. An empty value leads to the default noCheck. Enum: "noCheck", "requestTimeExact" |

<details>
<summary>Properties of `selectionChain`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `selectionType` | string | Yes | Enum: "selectionFilter", "persistentBookmark", "temporaryBookmarkV2" |
| `selectionFilter` | object | No |  |
| `persistentBookmark` | object | No |  |
| `temporaryBookmarkV2` | object | No | The temporary bookmark to apply. Patches and Variables are ignored if passed to the API, because they already are applied in the backend. |

<details>
<summary>Properties of `selectionFilter`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `persistentBookmark`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `temporaryBookmarkV2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `templateLocation`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | string | Yes | The report template location path. |
| `format` | string | No | Enum: "url" |

</details>

</details>

<details>
<summary>Properties of `senseExcelTemplate`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `jsOpts` | object | No | A JSON object that is passed as-is to the mashup page while rendering, this will be applied to all charts within the sheet. It includes properties of the whole sheet such as theme, gradient etc. Currently only the "theme" and "language" properties are supported. |
| `cycleFields` | string[] | No | The values of the field to be selected. |
| `selectionChain` | object[] | No | Array of ChainableSelection |
| `templateLocation` | object | Yes | The location of the report template. Currently it can be an absolute or relative URL to a persisted report template, or to a template file saved as temporary content, as in the following examples: - https://qlikcloud.com:443/api/v1/report-templates/223940f7-3170-46b7-91ea-e0c81230adf7 - https://qlikcloud.com:443/api/v1/temp-contents/653bb4acae966r0730da15fc |
| `reloadTimestampMatchType` | string | No | Choose the reloadTimestamp constraint to apply. An empty value leads to the default noCheck. Enum: "noCheck", "requestTimeExact" |

<details>
<summary>Properties of `selectionChain`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `selectionType` | string | Yes | Enum: "selectionFilter", "persistentBookmark", "temporaryBookmarkV2" |
| `selectionFilter` | object | No |  |
| `persistentBookmark` | object | No |  |
| `temporaryBookmarkV2` | object | No | The temporary bookmark to apply. Patches and Variables are ignored if passed to the API, because they already are applied in the backend. |

<details>
<summary>Properties of `selectionFilter`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `persistentBookmark`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `temporaryBookmarkV2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `templateLocation`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | string | Yes | The report template location path. |
| `format` | string | No | Enum: "url" |

</details>

</details>

<details>
<summary>Properties of `senseImageTemplate`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes |  |
| `selectionType` | string | No | Enum: "selectionsByState", "temporaryBookmark", "persistentBookmark", "temporaryBookmarkV2" |
| `visualization` | object | Yes |  |
| `selectionChain` | object[] | No | Array of ChainableSelection |
| `selectionStrategy` | string | No | Enum: "failOnErrors", "ignoreErrorsReturnDetails", "ignoreErrorsNoDetails" |
| `selectionsByState` | object | No | Map of selections to apply by state. Maximum number of states allowed is 125. Maximum number of fields allowed is 125 and maximum number of overall field values allowed is 150000. |
| `persistentBookmark` | object | No |  |
| `temporaryBookmarkV2` | object | No | The temporary bookmark to apply. Patches and Variables are ignored if passed to the API, because they already are applied in the backend. |
| `selectionsByStateDef` | string | No | The definition ID referring to a selectionsByState definition declared in definitions. |
| `reloadTimestampMatchType` | string | No | Choose the reloadTimestamp constraint to apply. An empty value leads to the default noCheck. Enum: "noCheck", "requestTimeExact" |

<details>
<summary>Properties of `visualization`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The sense visualization id or json definition. |
| `type` | string | No | Choose visualization to export an image of a sense chart, sessionobject for a visualization to be created on-the-fly, sheet to export a sheet as a whole image. An empty value leads to the type being inferred by its id. Enum: "visualization", "sessionobject", "sheet" |
| `jsOpts` | object | No | A JSON object that is passed as-is to the mashup page while rendering. |
| `patches` | object[] | No | Soft properties, aka patches, to be applied to the visualization. |
| `widthPx` | number | Yes | Width in pixels. |
| `heightPx` | number | Yes | Height in pixels. |

<details>
<summary>Properties of `patches`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `selectionChain`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `selectionType` | string | Yes | Enum: "selectionFilter", "persistentBookmark", "temporaryBookmarkV2" |
| `selectionFilter` | object | No |  |
| `persistentBookmark` | object | No |  |
| `temporaryBookmarkV2` | object | No | The temporary bookmark to apply. Patches and Variables are ignored if passed to the API, because they already are applied in the backend. |

<details>
<summary>Properties of `selectionFilter`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `persistentBookmark`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `temporaryBookmarkV2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `persistentBookmark`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Sense Persistence Bookmark id. |

</details>

<details>
<summary>Properties of `temporaryBookmarkV2`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Sense Temporary Bookmark id. |

</details>

</details>

<details>
<summary>Properties of `senseSheetTemplate`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes |  |
| `sheet` | object | Yes | It refers to the Sense Sheet to be exported. Note that if widthPx and heightPx are not specified, default values will be applied depending on the actual size and layout properties of the Sense Sheet object. |
| `selectionType` | string | No | Enum: "selectionsByState", "temporaryBookmark", "persistentBookmark", "temporaryBookmarkV2" |
| `selectionStrategy` | string | No | Enum: "failOnErrors", "ignoreErrorsReturnDetails", "ignoreErrorsNoDetails" |
| `selectionsByState` | object | No | Map of selections to apply by state. Maximum number of states allowed is 125. Maximum number of fields allowed is 125 and maximum number of overall field values allowed is 150000. |
| `persistentBookmark` | object | No |  |
| `temporaryBookmarkV2` | object | No | The temporary bookmark to apply. Patches and Variables are ignored if passed to the API, because they already are applied in the backend. |
| `selectionsByStateDef` | string | No | The definition ID referring to a selectionsByState definition declared in definitions. |
| `reloadTimestampMatchType` | string | No | Choose the reloadTimestamp constraint to apply. An empty value leads to the default noCheck. Enum: "noCheck", "requestTimeExact" |

<details>
<summary>Properties of `sheet`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | The id of the sheet. |
| `jsOpts` | object | No | A JSON object that is passed as-is to the mashup page while rendering, this will be applied to all charts within the sheet. It includes properties of the whole sheet such as theme, gradient etc. |
| `widthPx` | number | No | The width of the sheet in pixels. Default value is: - 1680 pixels for responsive sheet - 1120 pixels for extended sheet - same width set in sheet properties for custom sheet |
| `heightPx` | number | No | The height of the sheet in pixels. Default value is: - 1120 pixels for responsive sheet - 1680 pixels for extended sheet - same height set in sheet properties for custom sheet |
| `jsOptsById` | object | No | A map for applying jsOpts to specific visualization IDs within the sheet. |
| `patchesById` | object | No | A map for applying soft properties, aka patches, to specific visualization IDs within the sheet. |

</details>

<details>
<summary>Properties of `persistentBookmark`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Sense Persistence Bookmark id. |

</details>

<details>
<summary>Properties of `temporaryBookmarkV2`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Sense Temporary Bookmark id. |

</details>

</details>

<details>
<summary>Properties of `compositionTemplates`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | string | Yes | Template type and version using semantic versioning. It must have the following name convention, dashed-separated-template-name-MAJOR.MINOR Enum: "sense-image-1.0", "sense-sheet-1.0" |
| `senseImageTemplate` | object | No | Used to export a single visualization as pdf, pptx or png. |
| `senseSheetTemplate` | object | No | Used to export a sheet as pdf or pptx. |

<details>
<summary>Properties of `senseImageTemplate`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes |  |
| `selectionType` | string | No | Enum: "selectionsByState", "temporaryBookmark", "persistentBookmark", "temporaryBookmarkV2" |
| `visualization` | object | Yes |  |
| `selectionChain` | object[] | No | Array of ChainableSelection |
| `selectionStrategy` | string | No | Enum: "failOnErrors", "ignoreErrorsReturnDetails", "ignoreErrorsNoDetails" |
| `selectionsByState` | object | No | Map of selections to apply by state. Maximum number of states allowed is 125. Maximum number of fields allowed is 125 and maximum number of overall field values allowed is 150000. |
| `persistentBookmark` | object | No |  |
| `temporaryBookmarkV2` | object | No | The temporary bookmark to apply. Patches and Variables are ignored if passed to the API, because they already are applied in the backend. |
| `selectionsByStateDef` | string | No | The definition ID referring to a selectionsByState definition declared in definitions. |
| `reloadTimestampMatchType` | string | No | Choose the reloadTimestamp constraint to apply. An empty value leads to the default noCheck. Enum: "noCheck", "requestTimeExact" |

<details>
<summary>Properties of `visualization`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `selectionChain`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `persistentBookmark`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `temporaryBookmarkV2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `senseSheetTemplate`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | string | Yes |  |
| `sheet` | object | Yes | It refers to the Sense Sheet to be exported. Note that if widthPx and heightPx are not specified, default values will be applied depending on the actual size and layout properties of the Sense Sheet object. |
| `selectionType` | string | No | Enum: "selectionsByState", "temporaryBookmark", "persistentBookmark", "temporaryBookmarkV2" |
| `selectionStrategy` | string | No | Enum: "failOnErrors", "ignoreErrorsReturnDetails", "ignoreErrorsNoDetails" |
| `selectionsByState` | object | No | Map of selections to apply by state. Maximum number of states allowed is 125. Maximum number of fields allowed is 125 and maximum number of overall field values allowed is 150000. |
| `persistentBookmark` | object | No |  |
| `temporaryBookmarkV2` | object | No | The temporary bookmark to apply. Patches and Variables are ignored if passed to the API, because they already are applied in the backend. |
| `selectionsByStateDef` | string | No | The definition ID referring to a selectionsByState definition declared in definitions. |
| `reloadTimestampMatchType` | string | No | Choose the reloadTimestamp constraint to apply. An empty value leads to the default noCheck. Enum: "noCheck", "requestTimeExact" |

<details>
<summary>Properties of `sheet`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `persistentBookmark`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `temporaryBookmarkV2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `requestCallBackAction`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `httpRequest` | object | No | Http callback. The provided uri will be called once the report is done. |

<details>
<summary>Properties of `httpRequest`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `uri` | string | No | URI of the request. |

</details>

</details>

<details>
<summary>Properties of `sensePowerPointTemplate`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `jsOpts` | object | No | A JSON object that is passed as-is to the mashup page while rendering, this will be applied to all charts within the sheet. It includes properties of the whole sheet such as theme, gradient etc. Currently only the "theme" and "language" properties are supported. |
| `cycleFields` | string[] | No | The values of the field to be selected. |
| `selectionChain` | object[] | No | Array of ChainableSelection |
| `templateLocation` | object | Yes | The location of the report template. Currently it can be an absolute or relative URL to a persisted report template, or to a template file saved as temporary content, as in the following examples: - https://qlikcloud.com:443/api/v1/report-templates/223940f7-3170-46b7-91ea-e0c81230adf7 - https://qlikcloud.com:443/api/v1/temp-contents/653bb4acae966r0730da15fc |
| `reloadTimestampMatchType` | string | No | Choose the reloadTimestamp constraint to apply. An empty value leads to the default noCheck. Enum: "noCheck", "requestTimeExact" |

<details>
<summary>Properties of `selectionChain`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `selectionType` | string | Yes | Enum: "selectionFilter", "persistentBookmark", "temporaryBookmarkV2" |
| `selectionFilter` | object | No |  |
| `persistentBookmark` | object | No |  |
| `temporaryBookmarkV2` | object | No | The temporary bookmark to apply. Patches and Variables are ignored if passed to the API, because they already are applied in the backend. |

<details>
<summary>Properties of `selectionFilter`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `persistentBookmark`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `temporaryBookmarkV2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `templateLocation`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | string | Yes | The report template location path. |
| `format` | string | No | Enum: "url" |

</details>

</details>

<details>
<summary>Properties of `sensePixelPerfectTemplate`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `jsOpts` | object | No | A JSON object that is passed as-is to the mashup page while rendering, this will be applied to all charts within the sheet. It includes properties of the whole sheet such as theme, gradient etc. Currently only the "theme" and "language" properties are supported. |
| `cycleFields` | string[] | No | The values of the field to be selected. |
| `selectionChain` | object[] | No | Array of ChainableSelection |
| `templateLocation` | object | Yes | The location of the report template. Currently it can be an absolute or relative URL to a persisted report template, or to a template file saved as temporary content, as in the following examples: - https://qlikcloud.com:443/api/v1/report-templates/223940f7-3170-46b7-91ea-e0c81230adf7 - https://qlikcloud.com:443/api/v1/temp-contents/653bb4acae966r0730da15fc |
| `reloadTimestampMatchType` | string | No | Choose the reloadTimestamp constraint to apply. An empty value leads to the default noCheck. Enum: "noCheck", "requestTimeExact" |

<details>
<summary>Properties of `selectionChain`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `selectionType` | string | Yes | Enum: "selectionFilter", "persistentBookmark", "temporaryBookmarkV2" |
| `selectionFilter` | object | No |  |
| `persistentBookmark` | object | No |  |
| `temporaryBookmarkV2` | object | No | The temporary bookmark to apply. Patches and Variables are ignored if passed to the API, because they already are applied in the backend. |

<details>
<summary>Properties of `selectionFilter`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `persistentBookmark`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `temporaryBookmarkV2`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `templateLocation`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `path` | string | Yes | The report template location path. |
| `format` | string | No | Enum: "url" |

</details>

</details>

#### Responses

##### 202

Report request accepted.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `message` | string | No | A message indicating the status of the request. |
| `requestId` | string | No | The report request ID |
| `outputsUrl` | string | No | The absolute URL to get the outputs of the report request. |

##### 400

Bad request, malformed syntax, errors in params or the report request is not valid.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Errors occured during report generation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400009" Maximum 16384 columns limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of columns you can download. - "REP-400010" Maximum 1048566 rows limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of rows you can download. - "REP-400011" The size of the downloaded Excel file exceed 100 MB limit. Download data in a visualization can't generate an .xlsx file due to limitations to the amount of data you can download. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-400017" Static App size exceeded. - "REP-400018" Excel string length exceeded. - "REP-400020" Invalid Issuer. - "REP-400024" Cannot extract claims from JWT. - "REP-400028" Invalid Tags. - "REP-400029" Reload Entitlement Limit Reached. - "REP-400035" Multiple selections detected in a field having OneAndOnlyone attribute. - "REP-400036" No selection detected in a field having OneAndOnlyone attribute. - "REP-400037" Max number of images exceeded in a report. - "REP-400038" Max number of nested levels exceeded in report. - "REP-400039" Max number of objects exceeded in a report. - "REP-400040" Max number of templates exceeded in a report. - "REP-400041" Unsupported dimension type for level tag. - "REP-400050" Error retrieving outputs. - "REP-400052" Report Request Aborted from internal error. - "REP-400054" The number of generated cycle reports exceeds the maximum allowed. - "REP-400055" Export options not allowed for this object. - "REP-400057" The sense object has an empty GenericType. - "REP-400102" Image rendering invalid strategy error on Sense client. - "REP-400240" Engine Client Global generic closure error - "REP-400260" Engine Client generic closure error. - "REP-400280" Engine Client proxy generic closure error. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-403019" Export is not available for app with enabled directQuery feature. - "REP-403025" No entitlement to perform the operation. - "REP-403026" No entitlement to perform the operation. Export capability is off. - "REP-403027" Object without Hypercube or unsupported object type. - "REP-403048" Forbidden. User does not have permission to export the report (access control usePermission) - "REP-404000" Not found. The server can not find the requested resource. - "REP-404001" App not found, the app does not exist or it has been deleted. - "REP-404002" Chart not found, the chart does not exist or it has been deleted. - "REP-404003" Sheet not found, the sheet does not exist or it has been deleted or it is unavailable. - "REP-404004" Story not found, the story does not exist or it has been deleted or it is unavailable. - "REP-409001" App conflict. - "REP-409021" Reload timestamp constraint not met. - "REP-409046" Report aborted due to app reload. - "REP-422030" Apply variables error. - "REP-422051" There is no report to produce due to empty dataset or missing fields (the measure/dimension was removed or omitted in Section Access) - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429014" The export could not be completed within the requested deadline. - "REP-429016" Exceeded max session tenant quota per day. - "REP-429022" Enigma generic abort. - "REP-400064" Missing Bookmark  - "REP-500000" Fail to resolve resource. - "REP-500006" Fail to get report session parameters. - "REP-500014" The app did not open within 10 minutes. - "REP-500023" Validate Report Request Tags failure. - "REP-500045" Failure setting Bookmark timestamp. - "REP-500047" Error setting GroupState. - "REP-500053" Unexpected number of generated cycle reports. - "REP-500059" The App is corrupt. - "REP-500061" Engine Memory limit reached. - "REP-500062" Too many resolution attempts for a task. - "REP-500063" Engine terminated - "REP-500100" Image rendering generic error on Sense client. - "REP-500101" Image rendering could not set cookies error on Sense client. - "REP-500103" Image rendering JS timeout error on Sense client. - "REP-500104" Image rendering load URL timeout error on Sense client. - "REP-500105" Image rendering max paint attempts exceeded error on Sense client. - "REP-500106" Image rendering max JS attempts exceeded error on Sense client. - "REP-500107" Image rendering render timeout error on Sense client. - "REP-500108" Image rendering JS failure due to timeout error on Sense client. - "REP-500109" Image rendering generic JS failure error on Sense client. - "REP-500200" Report Generator error. - "REP-500240" Engine Global generic closure error. - "REP-500260" Engine Websocket generic closure error. - "REP-500280" Engine proxy generic closure error. - "REP-503001" Rest Engine Error. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-503060" Engine Service unavailable. |
| `meta` | object | No | Define the export error metadata. Each property is filled if it is related to the export error type. |
| `title` | string | Yes | A summary in english explaining what went wrong. |
| `detail` | string | No | Optional. MAY be used to provide more concrete details. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appErrors` | object[] | No | Errors occurring when dealing with the app. |
| `selectionErrors` | object[] | No | Errors occurring in selections. |

<details>
<summary>Properties of `appErrors`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `selectionErrors`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 401

Unauthorized, JWT invalid or not provided.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Errors occured during report generation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400009" Maximum 16384 columns limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of columns you can download. - "REP-400010" Maximum 1048566 rows limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of rows you can download. - "REP-400011" The size of the downloaded Excel file exceed 100 MB limit. Download data in a visualization can't generate an .xlsx file due to limitations to the amount of data you can download. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-400017" Static App size exceeded. - "REP-400018" Excel string length exceeded. - "REP-400020" Invalid Issuer. - "REP-400024" Cannot extract claims from JWT. - "REP-400028" Invalid Tags. - "REP-400029" Reload Entitlement Limit Reached. - "REP-400035" Multiple selections detected in a field having OneAndOnlyone attribute. - "REP-400036" No selection detected in a field having OneAndOnlyone attribute. - "REP-400037" Max number of images exceeded in a report. - "REP-400038" Max number of nested levels exceeded in report. - "REP-400039" Max number of objects exceeded in a report. - "REP-400040" Max number of templates exceeded in a report. - "REP-400041" Unsupported dimension type for level tag. - "REP-400050" Error retrieving outputs. - "REP-400052" Report Request Aborted from internal error. - "REP-400054" The number of generated cycle reports exceeds the maximum allowed. - "REP-400055" Export options not allowed for this object. - "REP-400057" The sense object has an empty GenericType. - "REP-400102" Image rendering invalid strategy error on Sense client. - "REP-400240" Engine Client Global generic closure error - "REP-400260" Engine Client generic closure error. - "REP-400280" Engine Client proxy generic closure error. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-403019" Export is not available for app with enabled directQuery feature. - "REP-403025" No entitlement to perform the operation. - "REP-403026" No entitlement to perform the operation. Export capability is off. - "REP-403027" Object without Hypercube or unsupported object type. - "REP-403048" Forbidden. User does not have permission to export the report (access control usePermission) - "REP-404000" Not found. The server can not find the requested resource. - "REP-404001" App not found, the app does not exist or it has been deleted. - "REP-404002" Chart not found, the chart does not exist or it has been deleted. - "REP-404003" Sheet not found, the sheet does not exist or it has been deleted or it is unavailable. - "REP-404004" Story not found, the story does not exist or it has been deleted or it is unavailable. - "REP-409001" App conflict. - "REP-409021" Reload timestamp constraint not met. - "REP-409046" Report aborted due to app reload. - "REP-422030" Apply variables error. - "REP-422051" There is no report to produce due to empty dataset or missing fields (the measure/dimension was removed or omitted in Section Access) - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429014" The export could not be completed within the requested deadline. - "REP-429016" Exceeded max session tenant quota per day. - "REP-429022" Enigma generic abort. - "REP-400064" Missing Bookmark  - "REP-500000" Fail to resolve resource. - "REP-500006" Fail to get report session parameters. - "REP-500014" The app did not open within 10 minutes. - "REP-500023" Validate Report Request Tags failure. - "REP-500045" Failure setting Bookmark timestamp. - "REP-500047" Error setting GroupState. - "REP-500053" Unexpected number of generated cycle reports. - "REP-500059" The App is corrupt. - "REP-500061" Engine Memory limit reached. - "REP-500062" Too many resolution attempts for a task. - "REP-500063" Engine terminated - "REP-500100" Image rendering generic error on Sense client. - "REP-500101" Image rendering could not set cookies error on Sense client. - "REP-500103" Image rendering JS timeout error on Sense client. - "REP-500104" Image rendering load URL timeout error on Sense client. - "REP-500105" Image rendering max paint attempts exceeded error on Sense client. - "REP-500106" Image rendering max JS attempts exceeded error on Sense client. - "REP-500107" Image rendering render timeout error on Sense client. - "REP-500108" Image rendering JS failure due to timeout error on Sense client. - "REP-500109" Image rendering generic JS failure error on Sense client. - "REP-500200" Report Generator error. - "REP-500240" Engine Global generic closure error. - "REP-500260" Engine Websocket generic closure error. - "REP-500280" Engine proxy generic closure error. - "REP-503001" Rest Engine Error. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-503060" Engine Service unavailable. |
| `meta` | object | No | Define the export error metadata. Each property is filled if it is related to the export error type. |
| `title` | string | Yes | A summary in english explaining what went wrong. |
| `detail` | string | No | Optional. MAY be used to provide more concrete details. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appErrors` | object[] | No | Errors occurring when dealing with the app. |
| `selectionErrors` | object[] | No | Errors occurring in selections. |

<details>
<summary>Properties of `appErrors`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `selectionErrors`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 403

Forbidden, the user does not have access rights.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Errors occured during report generation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400009" Maximum 16384 columns limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of columns you can download. - "REP-400010" Maximum 1048566 rows limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of rows you can download. - "REP-400011" The size of the downloaded Excel file exceed 100 MB limit. Download data in a visualization can't generate an .xlsx file due to limitations to the amount of data you can download. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-400017" Static App size exceeded. - "REP-400018" Excel string length exceeded. - "REP-400020" Invalid Issuer. - "REP-400024" Cannot extract claims from JWT. - "REP-400028" Invalid Tags. - "REP-400029" Reload Entitlement Limit Reached. - "REP-400035" Multiple selections detected in a field having OneAndOnlyone attribute. - "REP-400036" No selection detected in a field having OneAndOnlyone attribute. - "REP-400037" Max number of images exceeded in a report. - "REP-400038" Max number of nested levels exceeded in report. - "REP-400039" Max number of objects exceeded in a report. - "REP-400040" Max number of templates exceeded in a report. - "REP-400041" Unsupported dimension type for level tag. - "REP-400050" Error retrieving outputs. - "REP-400052" Report Request Aborted from internal error. - "REP-400054" The number of generated cycle reports exceeds the maximum allowed. - "REP-400055" Export options not allowed for this object. - "REP-400057" The sense object has an empty GenericType. - "REP-400102" Image rendering invalid strategy error on Sense client. - "REP-400240" Engine Client Global generic closure error - "REP-400260" Engine Client generic closure error. - "REP-400280" Engine Client proxy generic closure error. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-403019" Export is not available for app with enabled directQuery feature. - "REP-403025" No entitlement to perform the operation. - "REP-403026" No entitlement to perform the operation. Export capability is off. - "REP-403027" Object without Hypercube or unsupported object type. - "REP-403048" Forbidden. User does not have permission to export the report (access control usePermission) - "REP-404000" Not found. The server can not find the requested resource. - "REP-404001" App not found, the app does not exist or it has been deleted. - "REP-404002" Chart not found, the chart does not exist or it has been deleted. - "REP-404003" Sheet not found, the sheet does not exist or it has been deleted or it is unavailable. - "REP-404004" Story not found, the story does not exist or it has been deleted or it is unavailable. - "REP-409001" App conflict. - "REP-409021" Reload timestamp constraint not met. - "REP-409046" Report aborted due to app reload. - "REP-422030" Apply variables error. - "REP-422051" There is no report to produce due to empty dataset or missing fields (the measure/dimension was removed or omitted in Section Access) - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429014" The export could not be completed within the requested deadline. - "REP-429016" Exceeded max session tenant quota per day. - "REP-429022" Enigma generic abort. - "REP-400064" Missing Bookmark  - "REP-500000" Fail to resolve resource. - "REP-500006" Fail to get report session parameters. - "REP-500014" The app did not open within 10 minutes. - "REP-500023" Validate Report Request Tags failure. - "REP-500045" Failure setting Bookmark timestamp. - "REP-500047" Error setting GroupState. - "REP-500053" Unexpected number of generated cycle reports. - "REP-500059" The App is corrupt. - "REP-500061" Engine Memory limit reached. - "REP-500062" Too many resolution attempts for a task. - "REP-500063" Engine terminated - "REP-500100" Image rendering generic error on Sense client. - "REP-500101" Image rendering could not set cookies error on Sense client. - "REP-500103" Image rendering JS timeout error on Sense client. - "REP-500104" Image rendering load URL timeout error on Sense client. - "REP-500105" Image rendering max paint attempts exceeded error on Sense client. - "REP-500106" Image rendering max JS attempts exceeded error on Sense client. - "REP-500107" Image rendering render timeout error on Sense client. - "REP-500108" Image rendering JS failure due to timeout error on Sense client. - "REP-500109" Image rendering generic JS failure error on Sense client. - "REP-500200" Report Generator error. - "REP-500240" Engine Global generic closure error. - "REP-500260" Engine Websocket generic closure error. - "REP-500280" Engine proxy generic closure error. - "REP-503001" Rest Engine Error. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-503060" Engine Service unavailable. |
| `meta` | object | No | Define the export error metadata. Each property is filled if it is related to the export error type. |
| `title` | string | Yes | A summary in english explaining what went wrong. |
| `detail` | string | No | Optional. MAY be used to provide more concrete details. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appErrors` | object[] | No | Errors occurring when dealing with the app. |
| `selectionErrors` | object[] | No | Errors occurring in selections. |

<details>
<summary>Properties of `appErrors`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `selectionErrors`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 404

Not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Errors occured during report generation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400009" Maximum 16384 columns limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of columns you can download. - "REP-400010" Maximum 1048566 rows limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of rows you can download. - "REP-400011" The size of the downloaded Excel file exceed 100 MB limit. Download data in a visualization can't generate an .xlsx file due to limitations to the amount of data you can download. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-400017" Static App size exceeded. - "REP-400018" Excel string length exceeded. - "REP-400020" Invalid Issuer. - "REP-400024" Cannot extract claims from JWT. - "REP-400028" Invalid Tags. - "REP-400029" Reload Entitlement Limit Reached. - "REP-400035" Multiple selections detected in a field having OneAndOnlyone attribute. - "REP-400036" No selection detected in a field having OneAndOnlyone attribute. - "REP-400037" Max number of images exceeded in a report. - "REP-400038" Max number of nested levels exceeded in report. - "REP-400039" Max number of objects exceeded in a report. - "REP-400040" Max number of templates exceeded in a report. - "REP-400041" Unsupported dimension type for level tag. - "REP-400050" Error retrieving outputs. - "REP-400052" Report Request Aborted from internal error. - "REP-400054" The number of generated cycle reports exceeds the maximum allowed. - "REP-400055" Export options not allowed for this object. - "REP-400057" The sense object has an empty GenericType. - "REP-400102" Image rendering invalid strategy error on Sense client. - "REP-400240" Engine Client Global generic closure error - "REP-400260" Engine Client generic closure error. - "REP-400280" Engine Client proxy generic closure error. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-403019" Export is not available for app with enabled directQuery feature. - "REP-403025" No entitlement to perform the operation. - "REP-403026" No entitlement to perform the operation. Export capability is off. - "REP-403027" Object without Hypercube or unsupported object type. - "REP-403048" Forbidden. User does not have permission to export the report (access control usePermission) - "REP-404000" Not found. The server can not find the requested resource. - "REP-404001" App not found, the app does not exist or it has been deleted. - "REP-404002" Chart not found, the chart does not exist or it has been deleted. - "REP-404003" Sheet not found, the sheet does not exist or it has been deleted or it is unavailable. - "REP-404004" Story not found, the story does not exist or it has been deleted or it is unavailable. - "REP-409001" App conflict. - "REP-409021" Reload timestamp constraint not met. - "REP-409046" Report aborted due to app reload. - "REP-422030" Apply variables error. - "REP-422051" There is no report to produce due to empty dataset or missing fields (the measure/dimension was removed or omitted in Section Access) - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429014" The export could not be completed within the requested deadline. - "REP-429016" Exceeded max session tenant quota per day. - "REP-429022" Enigma generic abort. - "REP-400064" Missing Bookmark  - "REP-500000" Fail to resolve resource. - "REP-500006" Fail to get report session parameters. - "REP-500014" The app did not open within 10 minutes. - "REP-500023" Validate Report Request Tags failure. - "REP-500045" Failure setting Bookmark timestamp. - "REP-500047" Error setting GroupState. - "REP-500053" Unexpected number of generated cycle reports. - "REP-500059" The App is corrupt. - "REP-500061" Engine Memory limit reached. - "REP-500062" Too many resolution attempts for a task. - "REP-500063" Engine terminated - "REP-500100" Image rendering generic error on Sense client. - "REP-500101" Image rendering could not set cookies error on Sense client. - "REP-500103" Image rendering JS timeout error on Sense client. - "REP-500104" Image rendering load URL timeout error on Sense client. - "REP-500105" Image rendering max paint attempts exceeded error on Sense client. - "REP-500106" Image rendering max JS attempts exceeded error on Sense client. - "REP-500107" Image rendering render timeout error on Sense client. - "REP-500108" Image rendering JS failure due to timeout error on Sense client. - "REP-500109" Image rendering generic JS failure error on Sense client. - "REP-500200" Report Generator error. - "REP-500240" Engine Global generic closure error. - "REP-500260" Engine Websocket generic closure error. - "REP-500280" Engine proxy generic closure error. - "REP-503001" Rest Engine Error. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-503060" Engine Service unavailable. |
| `meta` | object | No | Define the export error metadata. Each property is filled if it is related to the export error type. |
| `title` | string | Yes | A summary in english explaining what went wrong. |
| `detail` | string | No | Optional. MAY be used to provide more concrete details. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appErrors` | object[] | No | Errors occurring when dealing with the app. |
| `selectionErrors` | object[] | No | Errors occurring in selections. |

<details>
<summary>Properties of `appErrors`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `selectionErrors`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 409

Conflicted request. Report aborted.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Errors occured during report generation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400009" Maximum 16384 columns limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of columns you can download. - "REP-400010" Maximum 1048566 rows limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of rows you can download. - "REP-400011" The size of the downloaded Excel file exceed 100 MB limit. Download data in a visualization can't generate an .xlsx file due to limitations to the amount of data you can download. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-400017" Static App size exceeded. - "REP-400018" Excel string length exceeded. - "REP-400020" Invalid Issuer. - "REP-400024" Cannot extract claims from JWT. - "REP-400028" Invalid Tags. - "REP-400029" Reload Entitlement Limit Reached. - "REP-400035" Multiple selections detected in a field having OneAndOnlyone attribute. - "REP-400036" No selection detected in a field having OneAndOnlyone attribute. - "REP-400037" Max number of images exceeded in a report. - "REP-400038" Max number of nested levels exceeded in report. - "REP-400039" Max number of objects exceeded in a report. - "REP-400040" Max number of templates exceeded in a report. - "REP-400041" Unsupported dimension type for level tag. - "REP-400050" Error retrieving outputs. - "REP-400052" Report Request Aborted from internal error. - "REP-400054" The number of generated cycle reports exceeds the maximum allowed. - "REP-400055" Export options not allowed for this object. - "REP-400057" The sense object has an empty GenericType. - "REP-400102" Image rendering invalid strategy error on Sense client. - "REP-400240" Engine Client Global generic closure error - "REP-400260" Engine Client generic closure error. - "REP-400280" Engine Client proxy generic closure error. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-403019" Export is not available for app with enabled directQuery feature. - "REP-403025" No entitlement to perform the operation. - "REP-403026" No entitlement to perform the operation. Export capability is off. - "REP-403027" Object without Hypercube or unsupported object type. - "REP-403048" Forbidden. User does not have permission to export the report (access control usePermission) - "REP-404000" Not found. The server can not find the requested resource. - "REP-404001" App not found, the app does not exist or it has been deleted. - "REP-404002" Chart not found, the chart does not exist or it has been deleted. - "REP-404003" Sheet not found, the sheet does not exist or it has been deleted or it is unavailable. - "REP-404004" Story not found, the story does not exist or it has been deleted or it is unavailable. - "REP-409001" App conflict. - "REP-409021" Reload timestamp constraint not met. - "REP-409046" Report aborted due to app reload. - "REP-422030" Apply variables error. - "REP-422051" There is no report to produce due to empty dataset or missing fields (the measure/dimension was removed or omitted in Section Access) - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429014" The export could not be completed within the requested deadline. - "REP-429016" Exceeded max session tenant quota per day. - "REP-429022" Enigma generic abort. - "REP-400064" Missing Bookmark  - "REP-500000" Fail to resolve resource. - "REP-500006" Fail to get report session parameters. - "REP-500014" The app did not open within 10 minutes. - "REP-500023" Validate Report Request Tags failure. - "REP-500045" Failure setting Bookmark timestamp. - "REP-500047" Error setting GroupState. - "REP-500053" Unexpected number of generated cycle reports. - "REP-500059" The App is corrupt. - "REP-500061" Engine Memory limit reached. - "REP-500062" Too many resolution attempts for a task. - "REP-500063" Engine terminated - "REP-500100" Image rendering generic error on Sense client. - "REP-500101" Image rendering could not set cookies error on Sense client. - "REP-500103" Image rendering JS timeout error on Sense client. - "REP-500104" Image rendering load URL timeout error on Sense client. - "REP-500105" Image rendering max paint attempts exceeded error on Sense client. - "REP-500106" Image rendering max JS attempts exceeded error on Sense client. - "REP-500107" Image rendering render timeout error on Sense client. - "REP-500108" Image rendering JS failure due to timeout error on Sense client. - "REP-500109" Image rendering generic JS failure error on Sense client. - "REP-500200" Report Generator error. - "REP-500240" Engine Global generic closure error. - "REP-500260" Engine Websocket generic closure error. - "REP-500280" Engine proxy generic closure error. - "REP-503001" Rest Engine Error. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-503060" Engine Service unavailable. |
| `meta` | object | No | Define the export error metadata. Each property is filled if it is related to the export error type. |
| `title` | string | Yes | A summary in english explaining what went wrong. |
| `detail` | string | No | Optional. MAY be used to provide more concrete details. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appErrors` | object[] | No | Errors occurring when dealing with the app. |
| `selectionErrors` | object[] | No | Errors occurring in selections. |

<details>
<summary>Properties of `appErrors`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `selectionErrors`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 429

Too many request. Indicates the user has sent too many requests in a given amount of time, aka "rate limiting".

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Errors occured during report generation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400009" Maximum 16384 columns limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of columns you can download. - "REP-400010" Maximum 1048566 rows limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of rows you can download. - "REP-400011" The size of the downloaded Excel file exceed 100 MB limit. Download data in a visualization can't generate an .xlsx file due to limitations to the amount of data you can download. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-400017" Static App size exceeded. - "REP-400018" Excel string length exceeded. - "REP-400020" Invalid Issuer. - "REP-400024" Cannot extract claims from JWT. - "REP-400028" Invalid Tags. - "REP-400029" Reload Entitlement Limit Reached. - "REP-400035" Multiple selections detected in a field having OneAndOnlyone attribute. - "REP-400036" No selection detected in a field having OneAndOnlyone attribute. - "REP-400037" Max number of images exceeded in a report. - "REP-400038" Max number of nested levels exceeded in report. - "REP-400039" Max number of objects exceeded in a report. - "REP-400040" Max number of templates exceeded in a report. - "REP-400041" Unsupported dimension type for level tag. - "REP-400050" Error retrieving outputs. - "REP-400052" Report Request Aborted from internal error. - "REP-400054" The number of generated cycle reports exceeds the maximum allowed. - "REP-400055" Export options not allowed for this object. - "REP-400057" The sense object has an empty GenericType. - "REP-400102" Image rendering invalid strategy error on Sense client. - "REP-400240" Engine Client Global generic closure error - "REP-400260" Engine Client generic closure error. - "REP-400280" Engine Client proxy generic closure error. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-403019" Export is not available for app with enabled directQuery feature. - "REP-403025" No entitlement to perform the operation. - "REP-403026" No entitlement to perform the operation. Export capability is off. - "REP-403027" Object without Hypercube or unsupported object type. - "REP-403048" Forbidden. User does not have permission to export the report (access control usePermission) - "REP-404000" Not found. The server can not find the requested resource. - "REP-404001" App not found, the app does not exist or it has been deleted. - "REP-404002" Chart not found, the chart does not exist or it has been deleted. - "REP-404003" Sheet not found, the sheet does not exist or it has been deleted or it is unavailable. - "REP-404004" Story not found, the story does not exist or it has been deleted or it is unavailable. - "REP-409001" App conflict. - "REP-409021" Reload timestamp constraint not met. - "REP-409046" Report aborted due to app reload. - "REP-422030" Apply variables error. - "REP-422051" There is no report to produce due to empty dataset or missing fields (the measure/dimension was removed or omitted in Section Access) - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429014" The export could not be completed within the requested deadline. - "REP-429016" Exceeded max session tenant quota per day. - "REP-429022" Enigma generic abort. - "REP-400064" Missing Bookmark  - "REP-500000" Fail to resolve resource. - "REP-500006" Fail to get report session parameters. - "REP-500014" The app did not open within 10 minutes. - "REP-500023" Validate Report Request Tags failure. - "REP-500045" Failure setting Bookmark timestamp. - "REP-500047" Error setting GroupState. - "REP-500053" Unexpected number of generated cycle reports. - "REP-500059" The App is corrupt. - "REP-500061" Engine Memory limit reached. - "REP-500062" Too many resolution attempts for a task. - "REP-500063" Engine terminated - "REP-500100" Image rendering generic error on Sense client. - "REP-500101" Image rendering could not set cookies error on Sense client. - "REP-500103" Image rendering JS timeout error on Sense client. - "REP-500104" Image rendering load URL timeout error on Sense client. - "REP-500105" Image rendering max paint attempts exceeded error on Sense client. - "REP-500106" Image rendering max JS attempts exceeded error on Sense client. - "REP-500107" Image rendering render timeout error on Sense client. - "REP-500108" Image rendering JS failure due to timeout error on Sense client. - "REP-500109" Image rendering generic JS failure error on Sense client. - "REP-500200" Report Generator error. - "REP-500240" Engine Global generic closure error. - "REP-500260" Engine Websocket generic closure error. - "REP-500280" Engine proxy generic closure error. - "REP-503001" Rest Engine Error. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-503060" Engine Service unavailable. |
| `meta` | object | No | Define the export error metadata. Each property is filled if it is related to the export error type. |
| `title` | string | Yes | A summary in english explaining what went wrong. |
| `detail` | string | No | Optional. MAY be used to provide more concrete details. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appErrors` | object[] | No | Errors occurring when dealing with the app. |
| `selectionErrors` | object[] | No | Errors occurring in selections. |

<details>
<summary>Properties of `appErrors`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `selectionErrors`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Errors occured during report generation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400009" Maximum 16384 columns limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of columns you can download. - "REP-400010" Maximum 1048566 rows limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of rows you can download. - "REP-400011" The size of the downloaded Excel file exceed 100 MB limit. Download data in a visualization can't generate an .xlsx file due to limitations to the amount of data you can download. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-400017" Static App size exceeded. - "REP-400018" Excel string length exceeded. - "REP-400020" Invalid Issuer. - "REP-400024" Cannot extract claims from JWT. - "REP-400028" Invalid Tags. - "REP-400029" Reload Entitlement Limit Reached. - "REP-400035" Multiple selections detected in a field having OneAndOnlyone attribute. - "REP-400036" No selection detected in a field having OneAndOnlyone attribute. - "REP-400037" Max number of images exceeded in a report. - "REP-400038" Max number of nested levels exceeded in report. - "REP-400039" Max number of objects exceeded in a report. - "REP-400040" Max number of templates exceeded in a report. - "REP-400041" Unsupported dimension type for level tag. - "REP-400050" Error retrieving outputs. - "REP-400052" Report Request Aborted from internal error. - "REP-400054" The number of generated cycle reports exceeds the maximum allowed. - "REP-400055" Export options not allowed for this object. - "REP-400057" The sense object has an empty GenericType. - "REP-400102" Image rendering invalid strategy error on Sense client. - "REP-400240" Engine Client Global generic closure error - "REP-400260" Engine Client generic closure error. - "REP-400280" Engine Client proxy generic closure error. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-403019" Export is not available for app with enabled directQuery feature. - "REP-403025" No entitlement to perform the operation. - "REP-403026" No entitlement to perform the operation. Export capability is off. - "REP-403027" Object without Hypercube or unsupported object type. - "REP-403048" Forbidden. User does not have permission to export the report (access control usePermission) - "REP-404000" Not found. The server can not find the requested resource. - "REP-404001" App not found, the app does not exist or it has been deleted. - "REP-404002" Chart not found, the chart does not exist or it has been deleted. - "REP-404003" Sheet not found, the sheet does not exist or it has been deleted or it is unavailable. - "REP-404004" Story not found, the story does not exist or it has been deleted or it is unavailable. - "REP-409001" App conflict. - "REP-409021" Reload timestamp constraint not met. - "REP-409046" Report aborted due to app reload. - "REP-422030" Apply variables error. - "REP-422051" There is no report to produce due to empty dataset or missing fields (the measure/dimension was removed or omitted in Section Access) - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429014" The export could not be completed within the requested deadline. - "REP-429016" Exceeded max session tenant quota per day. - "REP-429022" Enigma generic abort. - "REP-400064" Missing Bookmark  - "REP-500000" Fail to resolve resource. - "REP-500006" Fail to get report session parameters. - "REP-500014" The app did not open within 10 minutes. - "REP-500023" Validate Report Request Tags failure. - "REP-500045" Failure setting Bookmark timestamp. - "REP-500047" Error setting GroupState. - "REP-500053" Unexpected number of generated cycle reports. - "REP-500059" The App is corrupt. - "REP-500061" Engine Memory limit reached. - "REP-500062" Too many resolution attempts for a task. - "REP-500063" Engine terminated - "REP-500100" Image rendering generic error on Sense client. - "REP-500101" Image rendering could not set cookies error on Sense client. - "REP-500103" Image rendering JS timeout error on Sense client. - "REP-500104" Image rendering load URL timeout error on Sense client. - "REP-500105" Image rendering max paint attempts exceeded error on Sense client. - "REP-500106" Image rendering max JS attempts exceeded error on Sense client. - "REP-500107" Image rendering render timeout error on Sense client. - "REP-500108" Image rendering JS failure due to timeout error on Sense client. - "REP-500109" Image rendering generic JS failure error on Sense client. - "REP-500200" Report Generator error. - "REP-500240" Engine Global generic closure error. - "REP-500260" Engine Websocket generic closure error. - "REP-500280" Engine proxy generic closure error. - "REP-503001" Rest Engine Error. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-503060" Engine Service unavailable. |
| `meta` | object | No | Define the export error metadata. Each property is filled if it is related to the export error type. |
| `title` | string | Yes | A summary in english explaining what went wrong. |
| `detail` | string | No | Optional. MAY be used to provide more concrete details. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appErrors` | object[] | No | Errors occurring when dealing with the app. |
| `selectionErrors` | object[] | No | Errors occurring in selections. |

<details>
<summary>Properties of `appErrors`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `selectionErrors`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `POST /api/v1/reports` yet.
// In the meantime, you can use fetch like this:

const response = await fetch('/api/v1/reports', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    type: 'composition-1.0',
    output: {
      type: 'pdfcomposition',
      outputId: 'composition1',
      pdfCompositionOutput: {
        pdfOutputs: [
          {
            size: 'A4',
            align: {
              vertical: 'middle',
              horizontal: 'center',
            },
            resizeType: 'autofit',
            orientation: 'A',
          },
          {
            size: 'A4',
            align: {
              vertical: 'middle',
              horizontal: 'center',
            },
            resizeType: 'autofit',
            orientation: 'A',
          },
        ],
      },
    },
    definitions: {
      selectionsByState: {
        sel1: {
          $: [
            {
              values: [
                {
                  text: 'Arizona',
                  isNumeric: false,
                },
              ],
              fieldName: 'Region',
              defaultIsNumeric: false,
            },
          ],
        },
      },
    },
    compositionTemplates: [
      {
        type: 'sense-sheet-1.0',
        senseSheetTemplate: {
          appId:
            '2451e58e-a1b9-4047-abf6-315e91d8a610',
          sheet: {
            id: '5ffe3801-1b6d-439d-a849-84d0748358f1',
          },
          selectionsByStateDef: 'sel1',
        },
      },
      {
        type: 'sense-sheet-1.0',
        senseSheetTemplate: {
          appId:
            '2451e58e-a1b9-4047-abf6-315e91d8a610',
          sheet: { id: 'ffrxJyA' },
          selectionsByStateDef: 'sel1',
        },
      },
    ],
  }),
})

```

**Qlik CLI:**

```bash
# qlik-cli has not implemented support for POST /api/v1/reports yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/reports" \
-X POST \
-H "Content-type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"type":"composition-1.0","output":{"type":"pdfcomposition","outputId":"composition1","pdfCompositionOutput":{"pdfOutputs":[{"size":"A4","align":{"vertical":"middle","horizontal":"center"},"resizeType":"autofit","orientation":"A"},{"size":"A4","align":{"vertical":"middle","horizontal":"center"},"resizeType":"autofit","orientation":"A"}]}},"definitions":{"selectionsByState":{"sel1":{"$":[{"values":[{"text":"Arizona","isNumeric":false}],"fieldName":"Region","defaultIsNumeric":false}]}}},"compositionTemplates":[{"type":"sense-sheet-1.0","senseSheetTemplate":{"appId":"2451e58e-a1b9-4047-abf6-315e91d8a610","sheet":{"id":"5ffe3801-1b6d-439d-a849-84d0748358f1"},"selectionsByStateDef":"sel1"}},{"type":"sense-sheet-1.0","senseSheetTemplate":{"appId":"2451e58e-a1b9-4047-abf6-315e91d8a610","sheet":{"id":"ffrxJyA"},"selectionsByStateDef":"sel1"}}]}'
```

**Example Response:**

```json
{
  "message": "Report request has been accepted and is being processed.",
  "requestId": "c61841ac-7b35-4434-aa74-4421f10fc68e",
  "outputsUrl": "https://t.eu.qlikcloud.com:443/api/v1/reports/c61841ac-7b35-4434-aa74-4421f10fc68e/outputs"
}
```

---

### GET /api/v1/reports/{id}/outputs

Get the list of the outputs produced so far for the given report request. The outputs are generated asynchronously 
and are complete only when the status of the report request is 'done' or 'failed' or 'aborted'.


- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Identifier of the request. |

#### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `filter` | string | No | The advanced filtering to use for the query. Refer to [RFC 7644](https://datatracker.ietf.org/doc/rfc7644/) for the syntax. Cannot be combined with any of the fields marked as deprecated. All conditional statements within this query parameter are case insensitive. The following fields support the `eq` (equals) operator: `outputId` Example: outputId eq "123" or outputId eq "321" |
| `limit` | integer | No | Limit the returned result set |
| `page` | string | No | If present, the cursor that starts the page of data that is returned. |
| `sort` | string[] | No | Sorting parameters Enum: "+outputId", "-outputId", "+sizeBytes", "-sizeBytes" |

#### Responses

##### 200

The outputs have been successfully returned.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | object[] | Yes | a list of outputs containing all the report outputs |
| `links` | object | Yes |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | No | Status of the requested report. Enum: "queued", "processing", "done", "failed", "aborted", "aborting" |
| `traceId` | string | No |  |
| `location` | string | No | Location to download the generated report file. |
| `outputId` | string | No | The output ID |
| `sizeBytes` | integer | No | output size in bytes |
| `exportErrors` | object[] | No | Errors occured during report generation. |
| `cycleSelections` | object[] | No |  |

<details>
<summary>Properties of `exportErrors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400009" Maximum 16384 columns limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of columns you can download. - "REP-400010" Maximum 1048566 rows limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of rows you can download. - "REP-400011" The size of the downloaded Excel file exceed 100 MB limit. Download data in a visualization can't generate an .xlsx file due to limitations to the amount of data you can download. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-400017" Static App size exceeded. - "REP-400018" Excel string length exceeded. - "REP-400020" Invalid Issuer. - "REP-400024" Cannot extract claims from JWT. - "REP-400028" Invalid Tags. - "REP-400029" Reload Entitlement Limit Reached. - "REP-400035" Multiple selections detected in a field having OneAndOnlyone attribute. - "REP-400036" No selection detected in a field having OneAndOnlyone attribute. - "REP-400037" Max number of images exceeded in a report. - "REP-400038" Max number of nested levels exceeded in report. - "REP-400039" Max number of objects exceeded in a report. - "REP-400040" Max number of templates exceeded in a report. - "REP-400041" Unsupported dimension type for level tag. - "REP-400050" Error retrieving outputs. - "REP-400052" Report Request Aborted from internal error. - "REP-400054" The number of generated cycle reports exceeds the maximum allowed. - "REP-400055" Export options not allowed for this object. - "REP-400057" The sense object has an empty GenericType. - "REP-400102" Image rendering invalid strategy error on Sense client. - "REP-400240" Engine Client Global generic closure error - "REP-400260" Engine Client generic closure error. - "REP-400280" Engine Client proxy generic closure error. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-403019" Export is not available for app with enabled directQuery feature. - "REP-403025" No entitlement to perform the operation. - "REP-403026" No entitlement to perform the operation. Export capability is off. - "REP-403027" Object without Hypercube or unsupported object type. - "REP-403048" Forbidden. User does not have permission to export the report (access control usePermission) - "REP-404000" Not found. The server can not find the requested resource. - "REP-404001" App not found, the app does not exist or it has been deleted. - "REP-404002" Chart not found, the chart does not exist or it has been deleted. - "REP-404003" Sheet not found, the sheet does not exist or it has been deleted or it is unavailable. - "REP-404004" Story not found, the story does not exist or it has been deleted or it is unavailable. - "REP-409001" App conflict. - "REP-409021" Reload timestamp constraint not met. - "REP-409046" Report aborted due to app reload. - "REP-422030" Apply variables error. - "REP-422051" There is no report to produce due to empty dataset or missing fields (the measure/dimension was removed or omitted in Section Access) - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429014" The export could not be completed within the requested deadline. - "REP-429016" Exceeded max session tenant quota per day. - "REP-429022" Enigma generic abort. - "REP-400064" Missing Bookmark  - "REP-500000" Fail to resolve resource. - "REP-500006" Fail to get report session parameters. - "REP-500014" The app did not open within 10 minutes. - "REP-500023" Validate Report Request Tags failure. - "REP-500045" Failure setting Bookmark timestamp. - "REP-500047" Error setting GroupState. - "REP-500053" Unexpected number of generated cycle reports. - "REP-500059" The App is corrupt. - "REP-500061" Engine Memory limit reached. - "REP-500062" Too many resolution attempts for a task. - "REP-500063" Engine terminated - "REP-500100" Image rendering generic error on Sense client. - "REP-500101" Image rendering could not set cookies error on Sense client. - "REP-500103" Image rendering JS timeout error on Sense client. - "REP-500104" Image rendering load URL timeout error on Sense client. - "REP-500105" Image rendering max paint attempts exceeded error on Sense client. - "REP-500106" Image rendering max JS attempts exceeded error on Sense client. - "REP-500107" Image rendering render timeout error on Sense client. - "REP-500108" Image rendering JS failure due to timeout error on Sense client. - "REP-500109" Image rendering generic JS failure error on Sense client. - "REP-500200" Report Generator error. - "REP-500240" Engine Global generic closure error. - "REP-500260" Engine Websocket generic closure error. - "REP-500280" Engine proxy generic closure error. - "REP-503001" Rest Engine Error. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-503060" Engine Service unavailable. |
| `meta` | object | No | Define the export error metadata. Each property is filled if it is related to the export error type. |
| `title` | string | Yes | A summary in english explaining what went wrong. |
| `detail` | string | No | Optional. MAY be used to provide more concrete details. |

<details>
<summary>Properties of `meta`</summary>

_Properties truncated due to depth limit._

</details>

</details>

<details>
<summary>Properties of `cycleSelections`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `values` | object[] | Yes | The values of the field to be selected. |
| `fieldName` | string | Yes | The name of the field to be selected. |
| `defaultIsNumeric` | boolean | Yes | Default value that QFieldValue isNumeric property takes if missing. |

<details>
<summary>Properties of `values`</summary>

_Properties truncated due to depth limit._

</details>

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
| `href` | string | No |  |

</details>

<details>
<summary>Properties of `prev`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

<details>
<summary>Properties of `self`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `href` | string | No |  |

</details>

</details>

##### 400

Bad request. Malformed syntax, errors in params.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Errors occured during report generation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400009" Maximum 16384 columns limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of columns you can download. - "REP-400010" Maximum 1048566 rows limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of rows you can download. - "REP-400011" The size of the downloaded Excel file exceed 100 MB limit. Download data in a visualization can't generate an .xlsx file due to limitations to the amount of data you can download. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-400017" Static App size exceeded. - "REP-400018" Excel string length exceeded. - "REP-400020" Invalid Issuer. - "REP-400024" Cannot extract claims from JWT. - "REP-400028" Invalid Tags. - "REP-400029" Reload Entitlement Limit Reached. - "REP-400035" Multiple selections detected in a field having OneAndOnlyone attribute. - "REP-400036" No selection detected in a field having OneAndOnlyone attribute. - "REP-400037" Max number of images exceeded in a report. - "REP-400038" Max number of nested levels exceeded in report. - "REP-400039" Max number of objects exceeded in a report. - "REP-400040" Max number of templates exceeded in a report. - "REP-400041" Unsupported dimension type for level tag. - "REP-400050" Error retrieving outputs. - "REP-400052" Report Request Aborted from internal error. - "REP-400054" The number of generated cycle reports exceeds the maximum allowed. - "REP-400055" Export options not allowed for this object. - "REP-400057" The sense object has an empty GenericType. - "REP-400102" Image rendering invalid strategy error on Sense client. - "REP-400240" Engine Client Global generic closure error - "REP-400260" Engine Client generic closure error. - "REP-400280" Engine Client proxy generic closure error. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-403019" Export is not available for app with enabled directQuery feature. - "REP-403025" No entitlement to perform the operation. - "REP-403026" No entitlement to perform the operation. Export capability is off. - "REP-403027" Object without Hypercube or unsupported object type. - "REP-403048" Forbidden. User does not have permission to export the report (access control usePermission) - "REP-404000" Not found. The server can not find the requested resource. - "REP-404001" App not found, the app does not exist or it has been deleted. - "REP-404002" Chart not found, the chart does not exist or it has been deleted. - "REP-404003" Sheet not found, the sheet does not exist or it has been deleted or it is unavailable. - "REP-404004" Story not found, the story does not exist or it has been deleted or it is unavailable. - "REP-409001" App conflict. - "REP-409021" Reload timestamp constraint not met. - "REP-409046" Report aborted due to app reload. - "REP-422030" Apply variables error. - "REP-422051" There is no report to produce due to empty dataset or missing fields (the measure/dimension was removed or omitted in Section Access) - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429014" The export could not be completed within the requested deadline. - "REP-429016" Exceeded max session tenant quota per day. - "REP-429022" Enigma generic abort. - "REP-400064" Missing Bookmark  - "REP-500000" Fail to resolve resource. - "REP-500006" Fail to get report session parameters. - "REP-500014" The app did not open within 10 minutes. - "REP-500023" Validate Report Request Tags failure. - "REP-500045" Failure setting Bookmark timestamp. - "REP-500047" Error setting GroupState. - "REP-500053" Unexpected number of generated cycle reports. - "REP-500059" The App is corrupt. - "REP-500061" Engine Memory limit reached. - "REP-500062" Too many resolution attempts for a task. - "REP-500063" Engine terminated - "REP-500100" Image rendering generic error on Sense client. - "REP-500101" Image rendering could not set cookies error on Sense client. - "REP-500103" Image rendering JS timeout error on Sense client. - "REP-500104" Image rendering load URL timeout error on Sense client. - "REP-500105" Image rendering max paint attempts exceeded error on Sense client. - "REP-500106" Image rendering max JS attempts exceeded error on Sense client. - "REP-500107" Image rendering render timeout error on Sense client. - "REP-500108" Image rendering JS failure due to timeout error on Sense client. - "REP-500109" Image rendering generic JS failure error on Sense client. - "REP-500200" Report Generator error. - "REP-500240" Engine Global generic closure error. - "REP-500260" Engine Websocket generic closure error. - "REP-500280" Engine proxy generic closure error. - "REP-503001" Rest Engine Error. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-503060" Engine Service unavailable. |
| `meta` | object | No | Define the export error metadata. Each property is filled if it is related to the export error type. |
| `title` | string | Yes | A summary in english explaining what went wrong. |
| `detail` | string | No | Optional. MAY be used to provide more concrete details. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appErrors` | object[] | No | Errors occurring when dealing with the app. |
| `selectionErrors` | object[] | No | Errors occurring in selections. |

<details>
<summary>Properties of `appErrors`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `selectionErrors`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 401

Unauthorized, JWT invalid or not provided.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Errors occured during report generation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400009" Maximum 16384 columns limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of columns you can download. - "REP-400010" Maximum 1048566 rows limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of rows you can download. - "REP-400011" The size of the downloaded Excel file exceed 100 MB limit. Download data in a visualization can't generate an .xlsx file due to limitations to the amount of data you can download. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-400017" Static App size exceeded. - "REP-400018" Excel string length exceeded. - "REP-400020" Invalid Issuer. - "REP-400024" Cannot extract claims from JWT. - "REP-400028" Invalid Tags. - "REP-400029" Reload Entitlement Limit Reached. - "REP-400035" Multiple selections detected in a field having OneAndOnlyone attribute. - "REP-400036" No selection detected in a field having OneAndOnlyone attribute. - "REP-400037" Max number of images exceeded in a report. - "REP-400038" Max number of nested levels exceeded in report. - "REP-400039" Max number of objects exceeded in a report. - "REP-400040" Max number of templates exceeded in a report. - "REP-400041" Unsupported dimension type for level tag. - "REP-400050" Error retrieving outputs. - "REP-400052" Report Request Aborted from internal error. - "REP-400054" The number of generated cycle reports exceeds the maximum allowed. - "REP-400055" Export options not allowed for this object. - "REP-400057" The sense object has an empty GenericType. - "REP-400102" Image rendering invalid strategy error on Sense client. - "REP-400240" Engine Client Global generic closure error - "REP-400260" Engine Client generic closure error. - "REP-400280" Engine Client proxy generic closure error. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-403019" Export is not available for app with enabled directQuery feature. - "REP-403025" No entitlement to perform the operation. - "REP-403026" No entitlement to perform the operation. Export capability is off. - "REP-403027" Object without Hypercube or unsupported object type. - "REP-403048" Forbidden. User does not have permission to export the report (access control usePermission) - "REP-404000" Not found. The server can not find the requested resource. - "REP-404001" App not found, the app does not exist or it has been deleted. - "REP-404002" Chart not found, the chart does not exist or it has been deleted. - "REP-404003" Sheet not found, the sheet does not exist or it has been deleted or it is unavailable. - "REP-404004" Story not found, the story does not exist or it has been deleted or it is unavailable. - "REP-409001" App conflict. - "REP-409021" Reload timestamp constraint not met. - "REP-409046" Report aborted due to app reload. - "REP-422030" Apply variables error. - "REP-422051" There is no report to produce due to empty dataset or missing fields (the measure/dimension was removed or omitted in Section Access) - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429014" The export could not be completed within the requested deadline. - "REP-429016" Exceeded max session tenant quota per day. - "REP-429022" Enigma generic abort. - "REP-400064" Missing Bookmark  - "REP-500000" Fail to resolve resource. - "REP-500006" Fail to get report session parameters. - "REP-500014" The app did not open within 10 minutes. - "REP-500023" Validate Report Request Tags failure. - "REP-500045" Failure setting Bookmark timestamp. - "REP-500047" Error setting GroupState. - "REP-500053" Unexpected number of generated cycle reports. - "REP-500059" The App is corrupt. - "REP-500061" Engine Memory limit reached. - "REP-500062" Too many resolution attempts for a task. - "REP-500063" Engine terminated - "REP-500100" Image rendering generic error on Sense client. - "REP-500101" Image rendering could not set cookies error on Sense client. - "REP-500103" Image rendering JS timeout error on Sense client. - "REP-500104" Image rendering load URL timeout error on Sense client. - "REP-500105" Image rendering max paint attempts exceeded error on Sense client. - "REP-500106" Image rendering max JS attempts exceeded error on Sense client. - "REP-500107" Image rendering render timeout error on Sense client. - "REP-500108" Image rendering JS failure due to timeout error on Sense client. - "REP-500109" Image rendering generic JS failure error on Sense client. - "REP-500200" Report Generator error. - "REP-500240" Engine Global generic closure error. - "REP-500260" Engine Websocket generic closure error. - "REP-500280" Engine proxy generic closure error. - "REP-503001" Rest Engine Error. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-503060" Engine Service unavailable. |
| `meta` | object | No | Define the export error metadata. Each property is filled if it is related to the export error type. |
| `title` | string | Yes | A summary in english explaining what went wrong. |
| `detail` | string | No | Optional. MAY be used to provide more concrete details. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appErrors` | object[] | No | Errors occurring when dealing with the app. |
| `selectionErrors` | object[] | No | Errors occurring in selections. |

<details>
<summary>Properties of `appErrors`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `selectionErrors`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 403

Forbidden, user did not authenticate.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Errors occured during report generation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400009" Maximum 16384 columns limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of columns you can download. - "REP-400010" Maximum 1048566 rows limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of rows you can download. - "REP-400011" The size of the downloaded Excel file exceed 100 MB limit. Download data in a visualization can't generate an .xlsx file due to limitations to the amount of data you can download. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-400017" Static App size exceeded. - "REP-400018" Excel string length exceeded. - "REP-400020" Invalid Issuer. - "REP-400024" Cannot extract claims from JWT. - "REP-400028" Invalid Tags. - "REP-400029" Reload Entitlement Limit Reached. - "REP-400035" Multiple selections detected in a field having OneAndOnlyone attribute. - "REP-400036" No selection detected in a field having OneAndOnlyone attribute. - "REP-400037" Max number of images exceeded in a report. - "REP-400038" Max number of nested levels exceeded in report. - "REP-400039" Max number of objects exceeded in a report. - "REP-400040" Max number of templates exceeded in a report. - "REP-400041" Unsupported dimension type for level tag. - "REP-400050" Error retrieving outputs. - "REP-400052" Report Request Aborted from internal error. - "REP-400054" The number of generated cycle reports exceeds the maximum allowed. - "REP-400055" Export options not allowed for this object. - "REP-400057" The sense object has an empty GenericType. - "REP-400102" Image rendering invalid strategy error on Sense client. - "REP-400240" Engine Client Global generic closure error - "REP-400260" Engine Client generic closure error. - "REP-400280" Engine Client proxy generic closure error. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-403019" Export is not available for app with enabled directQuery feature. - "REP-403025" No entitlement to perform the operation. - "REP-403026" No entitlement to perform the operation. Export capability is off. - "REP-403027" Object without Hypercube or unsupported object type. - "REP-403048" Forbidden. User does not have permission to export the report (access control usePermission) - "REP-404000" Not found. The server can not find the requested resource. - "REP-404001" App not found, the app does not exist or it has been deleted. - "REP-404002" Chart not found, the chart does not exist or it has been deleted. - "REP-404003" Sheet not found, the sheet does not exist or it has been deleted or it is unavailable. - "REP-404004" Story not found, the story does not exist or it has been deleted or it is unavailable. - "REP-409001" App conflict. - "REP-409021" Reload timestamp constraint not met. - "REP-409046" Report aborted due to app reload. - "REP-422030" Apply variables error. - "REP-422051" There is no report to produce due to empty dataset or missing fields (the measure/dimension was removed or omitted in Section Access) - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429014" The export could not be completed within the requested deadline. - "REP-429016" Exceeded max session tenant quota per day. - "REP-429022" Enigma generic abort. - "REP-400064" Missing Bookmark  - "REP-500000" Fail to resolve resource. - "REP-500006" Fail to get report session parameters. - "REP-500014" The app did not open within 10 minutes. - "REP-500023" Validate Report Request Tags failure. - "REP-500045" Failure setting Bookmark timestamp. - "REP-500047" Error setting GroupState. - "REP-500053" Unexpected number of generated cycle reports. - "REP-500059" The App is corrupt. - "REP-500061" Engine Memory limit reached. - "REP-500062" Too many resolution attempts for a task. - "REP-500063" Engine terminated - "REP-500100" Image rendering generic error on Sense client. - "REP-500101" Image rendering could not set cookies error on Sense client. - "REP-500103" Image rendering JS timeout error on Sense client. - "REP-500104" Image rendering load URL timeout error on Sense client. - "REP-500105" Image rendering max paint attempts exceeded error on Sense client. - "REP-500106" Image rendering max JS attempts exceeded error on Sense client. - "REP-500107" Image rendering render timeout error on Sense client. - "REP-500108" Image rendering JS failure due to timeout error on Sense client. - "REP-500109" Image rendering generic JS failure error on Sense client. - "REP-500200" Report Generator error. - "REP-500240" Engine Global generic closure error. - "REP-500260" Engine Websocket generic closure error. - "REP-500280" Engine proxy generic closure error. - "REP-503001" Rest Engine Error. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-503060" Engine Service unavailable. |
| `meta` | object | No | Define the export error metadata. Each property is filled if it is related to the export error type. |
| `title` | string | Yes | A summary in english explaining what went wrong. |
| `detail` | string | No | Optional. MAY be used to provide more concrete details. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appErrors` | object[] | No | Errors occurring when dealing with the app. |
| `selectionErrors` | object[] | No | Errors occurring in selections. |

<details>
<summary>Properties of `appErrors`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `selectionErrors`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 404

Not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Errors occured during report generation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400009" Maximum 16384 columns limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of columns you can download. - "REP-400010" Maximum 1048566 rows limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of rows you can download. - "REP-400011" The size of the downloaded Excel file exceed 100 MB limit. Download data in a visualization can't generate an .xlsx file due to limitations to the amount of data you can download. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-400017" Static App size exceeded. - "REP-400018" Excel string length exceeded. - "REP-400020" Invalid Issuer. - "REP-400024" Cannot extract claims from JWT. - "REP-400028" Invalid Tags. - "REP-400029" Reload Entitlement Limit Reached. - "REP-400035" Multiple selections detected in a field having OneAndOnlyone attribute. - "REP-400036" No selection detected in a field having OneAndOnlyone attribute. - "REP-400037" Max number of images exceeded in a report. - "REP-400038" Max number of nested levels exceeded in report. - "REP-400039" Max number of objects exceeded in a report. - "REP-400040" Max number of templates exceeded in a report. - "REP-400041" Unsupported dimension type for level tag. - "REP-400050" Error retrieving outputs. - "REP-400052" Report Request Aborted from internal error. - "REP-400054" The number of generated cycle reports exceeds the maximum allowed. - "REP-400055" Export options not allowed for this object. - "REP-400057" The sense object has an empty GenericType. - "REP-400102" Image rendering invalid strategy error on Sense client. - "REP-400240" Engine Client Global generic closure error - "REP-400260" Engine Client generic closure error. - "REP-400280" Engine Client proxy generic closure error. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-403019" Export is not available for app with enabled directQuery feature. - "REP-403025" No entitlement to perform the operation. - "REP-403026" No entitlement to perform the operation. Export capability is off. - "REP-403027" Object without Hypercube or unsupported object type. - "REP-403048" Forbidden. User does not have permission to export the report (access control usePermission) - "REP-404000" Not found. The server can not find the requested resource. - "REP-404001" App not found, the app does not exist or it has been deleted. - "REP-404002" Chart not found, the chart does not exist or it has been deleted. - "REP-404003" Sheet not found, the sheet does not exist or it has been deleted or it is unavailable. - "REP-404004" Story not found, the story does not exist or it has been deleted or it is unavailable. - "REP-409001" App conflict. - "REP-409021" Reload timestamp constraint not met. - "REP-409046" Report aborted due to app reload. - "REP-422030" Apply variables error. - "REP-422051" There is no report to produce due to empty dataset or missing fields (the measure/dimension was removed or omitted in Section Access) - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429014" The export could not be completed within the requested deadline. - "REP-429016" Exceeded max session tenant quota per day. - "REP-429022" Enigma generic abort. - "REP-400064" Missing Bookmark  - "REP-500000" Fail to resolve resource. - "REP-500006" Fail to get report session parameters. - "REP-500014" The app did not open within 10 minutes. - "REP-500023" Validate Report Request Tags failure. - "REP-500045" Failure setting Bookmark timestamp. - "REP-500047" Error setting GroupState. - "REP-500053" Unexpected number of generated cycle reports. - "REP-500059" The App is corrupt. - "REP-500061" Engine Memory limit reached. - "REP-500062" Too many resolution attempts for a task. - "REP-500063" Engine terminated - "REP-500100" Image rendering generic error on Sense client. - "REP-500101" Image rendering could not set cookies error on Sense client. - "REP-500103" Image rendering JS timeout error on Sense client. - "REP-500104" Image rendering load URL timeout error on Sense client. - "REP-500105" Image rendering max paint attempts exceeded error on Sense client. - "REP-500106" Image rendering max JS attempts exceeded error on Sense client. - "REP-500107" Image rendering render timeout error on Sense client. - "REP-500108" Image rendering JS failure due to timeout error on Sense client. - "REP-500109" Image rendering generic JS failure error on Sense client. - "REP-500200" Report Generator error. - "REP-500240" Engine Global generic closure error. - "REP-500260" Engine Websocket generic closure error. - "REP-500280" Engine proxy generic closure error. - "REP-503001" Rest Engine Error. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-503060" Engine Service unavailable. |
| `meta` | object | No | Define the export error metadata. Each property is filled if it is related to the export error type. |
| `title` | string | Yes | A summary in english explaining what went wrong. |
| `detail` | string | No | Optional. MAY be used to provide more concrete details. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appErrors` | object[] | No | Errors occurring when dealing with the app. |
| `selectionErrors` | object[] | No | Errors occurring in selections. |

<details>
<summary>Properties of `appErrors`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `selectionErrors`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 409

Conflicted request. Report aborted.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Errors occured during report generation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400009" Maximum 16384 columns limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of columns you can download. - "REP-400010" Maximum 1048566 rows limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of rows you can download. - "REP-400011" The size of the downloaded Excel file exceed 100 MB limit. Download data in a visualization can't generate an .xlsx file due to limitations to the amount of data you can download. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-400017" Static App size exceeded. - "REP-400018" Excel string length exceeded. - "REP-400020" Invalid Issuer. - "REP-400024" Cannot extract claims from JWT. - "REP-400028" Invalid Tags. - "REP-400029" Reload Entitlement Limit Reached. - "REP-400035" Multiple selections detected in a field having OneAndOnlyone attribute. - "REP-400036" No selection detected in a field having OneAndOnlyone attribute. - "REP-400037" Max number of images exceeded in a report. - "REP-400038" Max number of nested levels exceeded in report. - "REP-400039" Max number of objects exceeded in a report. - "REP-400040" Max number of templates exceeded in a report. - "REP-400041" Unsupported dimension type for level tag. - "REP-400050" Error retrieving outputs. - "REP-400052" Report Request Aborted from internal error. - "REP-400054" The number of generated cycle reports exceeds the maximum allowed. - "REP-400055" Export options not allowed for this object. - "REP-400057" The sense object has an empty GenericType. - "REP-400102" Image rendering invalid strategy error on Sense client. - "REP-400240" Engine Client Global generic closure error - "REP-400260" Engine Client generic closure error. - "REP-400280" Engine Client proxy generic closure error. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-403019" Export is not available for app with enabled directQuery feature. - "REP-403025" No entitlement to perform the operation. - "REP-403026" No entitlement to perform the operation. Export capability is off. - "REP-403027" Object without Hypercube or unsupported object type. - "REP-403048" Forbidden. User does not have permission to export the report (access control usePermission) - "REP-404000" Not found. The server can not find the requested resource. - "REP-404001" App not found, the app does not exist or it has been deleted. - "REP-404002" Chart not found, the chart does not exist or it has been deleted. - "REP-404003" Sheet not found, the sheet does not exist or it has been deleted or it is unavailable. - "REP-404004" Story not found, the story does not exist or it has been deleted or it is unavailable. - "REP-409001" App conflict. - "REP-409021" Reload timestamp constraint not met. - "REP-409046" Report aborted due to app reload. - "REP-422030" Apply variables error. - "REP-422051" There is no report to produce due to empty dataset or missing fields (the measure/dimension was removed or omitted in Section Access) - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429014" The export could not be completed within the requested deadline. - "REP-429016" Exceeded max session tenant quota per day. - "REP-429022" Enigma generic abort. - "REP-400064" Missing Bookmark  - "REP-500000" Fail to resolve resource. - "REP-500006" Fail to get report session parameters. - "REP-500014" The app did not open within 10 minutes. - "REP-500023" Validate Report Request Tags failure. - "REP-500045" Failure setting Bookmark timestamp. - "REP-500047" Error setting GroupState. - "REP-500053" Unexpected number of generated cycle reports. - "REP-500059" The App is corrupt. - "REP-500061" Engine Memory limit reached. - "REP-500062" Too many resolution attempts for a task. - "REP-500063" Engine terminated - "REP-500100" Image rendering generic error on Sense client. - "REP-500101" Image rendering could not set cookies error on Sense client. - "REP-500103" Image rendering JS timeout error on Sense client. - "REP-500104" Image rendering load URL timeout error on Sense client. - "REP-500105" Image rendering max paint attempts exceeded error on Sense client. - "REP-500106" Image rendering max JS attempts exceeded error on Sense client. - "REP-500107" Image rendering render timeout error on Sense client. - "REP-500108" Image rendering JS failure due to timeout error on Sense client. - "REP-500109" Image rendering generic JS failure error on Sense client. - "REP-500200" Report Generator error. - "REP-500240" Engine Global generic closure error. - "REP-500260" Engine Websocket generic closure error. - "REP-500280" Engine proxy generic closure error. - "REP-503001" Rest Engine Error. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-503060" Engine Service unavailable. |
| `meta` | object | No | Define the export error metadata. Each property is filled if it is related to the export error type. |
| `title` | string | Yes | A summary in english explaining what went wrong. |
| `detail` | string | No | Optional. MAY be used to provide more concrete details. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appErrors` | object[] | No | Errors occurring when dealing with the app. |
| `selectionErrors` | object[] | No | Errors occurring in selections. |

<details>
<summary>Properties of `appErrors`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `selectionErrors`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 429

Too many request. Indicates the user has sent too many requests in a given amount of time, aka "rate limiting".

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Errors occured during report generation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400009" Maximum 16384 columns limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of columns you can download. - "REP-400010" Maximum 1048566 rows limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of rows you can download. - "REP-400011" The size of the downloaded Excel file exceed 100 MB limit. Download data in a visualization can't generate an .xlsx file due to limitations to the amount of data you can download. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-400017" Static App size exceeded. - "REP-400018" Excel string length exceeded. - "REP-400020" Invalid Issuer. - "REP-400024" Cannot extract claims from JWT. - "REP-400028" Invalid Tags. - "REP-400029" Reload Entitlement Limit Reached. - "REP-400035" Multiple selections detected in a field having OneAndOnlyone attribute. - "REP-400036" No selection detected in a field having OneAndOnlyone attribute. - "REP-400037" Max number of images exceeded in a report. - "REP-400038" Max number of nested levels exceeded in report. - "REP-400039" Max number of objects exceeded in a report. - "REP-400040" Max number of templates exceeded in a report. - "REP-400041" Unsupported dimension type for level tag. - "REP-400050" Error retrieving outputs. - "REP-400052" Report Request Aborted from internal error. - "REP-400054" The number of generated cycle reports exceeds the maximum allowed. - "REP-400055" Export options not allowed for this object. - "REP-400057" The sense object has an empty GenericType. - "REP-400102" Image rendering invalid strategy error on Sense client. - "REP-400240" Engine Client Global generic closure error - "REP-400260" Engine Client generic closure error. - "REP-400280" Engine Client proxy generic closure error. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-403019" Export is not available for app with enabled directQuery feature. - "REP-403025" No entitlement to perform the operation. - "REP-403026" No entitlement to perform the operation. Export capability is off. - "REP-403027" Object without Hypercube or unsupported object type. - "REP-403048" Forbidden. User does not have permission to export the report (access control usePermission) - "REP-404000" Not found. The server can not find the requested resource. - "REP-404001" App not found, the app does not exist or it has been deleted. - "REP-404002" Chart not found, the chart does not exist or it has been deleted. - "REP-404003" Sheet not found, the sheet does not exist or it has been deleted or it is unavailable. - "REP-404004" Story not found, the story does not exist or it has been deleted or it is unavailable. - "REP-409001" App conflict. - "REP-409021" Reload timestamp constraint not met. - "REP-409046" Report aborted due to app reload. - "REP-422030" Apply variables error. - "REP-422051" There is no report to produce due to empty dataset or missing fields (the measure/dimension was removed or omitted in Section Access) - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429014" The export could not be completed within the requested deadline. - "REP-429016" Exceeded max session tenant quota per day. - "REP-429022" Enigma generic abort. - "REP-400064" Missing Bookmark  - "REP-500000" Fail to resolve resource. - "REP-500006" Fail to get report session parameters. - "REP-500014" The app did not open within 10 minutes. - "REP-500023" Validate Report Request Tags failure. - "REP-500045" Failure setting Bookmark timestamp. - "REP-500047" Error setting GroupState. - "REP-500053" Unexpected number of generated cycle reports. - "REP-500059" The App is corrupt. - "REP-500061" Engine Memory limit reached. - "REP-500062" Too many resolution attempts for a task. - "REP-500063" Engine terminated - "REP-500100" Image rendering generic error on Sense client. - "REP-500101" Image rendering could not set cookies error on Sense client. - "REP-500103" Image rendering JS timeout error on Sense client. - "REP-500104" Image rendering load URL timeout error on Sense client. - "REP-500105" Image rendering max paint attempts exceeded error on Sense client. - "REP-500106" Image rendering max JS attempts exceeded error on Sense client. - "REP-500107" Image rendering render timeout error on Sense client. - "REP-500108" Image rendering JS failure due to timeout error on Sense client. - "REP-500109" Image rendering generic JS failure error on Sense client. - "REP-500200" Report Generator error. - "REP-500240" Engine Global generic closure error. - "REP-500260" Engine Websocket generic closure error. - "REP-500280" Engine proxy generic closure error. - "REP-503001" Rest Engine Error. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-503060" Engine Service unavailable. |
| `meta` | object | No | Define the export error metadata. Each property is filled if it is related to the export error type. |
| `title` | string | Yes | A summary in english explaining what went wrong. |
| `detail` | string | No | Optional. MAY be used to provide more concrete details. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appErrors` | object[] | No | Errors occurring when dealing with the app. |
| `selectionErrors` | object[] | No | Errors occurring in selections. |

<details>
<summary>Properties of `appErrors`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `selectionErrors`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Errors occured during report generation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400009" Maximum 16384 columns limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of columns you can download. - "REP-400010" Maximum 1048566 rows limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of rows you can download. - "REP-400011" The size of the downloaded Excel file exceed 100 MB limit. Download data in a visualization can't generate an .xlsx file due to limitations to the amount of data you can download. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-400017" Static App size exceeded. - "REP-400018" Excel string length exceeded. - "REP-400020" Invalid Issuer. - "REP-400024" Cannot extract claims from JWT. - "REP-400028" Invalid Tags. - "REP-400029" Reload Entitlement Limit Reached. - "REP-400035" Multiple selections detected in a field having OneAndOnlyone attribute. - "REP-400036" No selection detected in a field having OneAndOnlyone attribute. - "REP-400037" Max number of images exceeded in a report. - "REP-400038" Max number of nested levels exceeded in report. - "REP-400039" Max number of objects exceeded in a report. - "REP-400040" Max number of templates exceeded in a report. - "REP-400041" Unsupported dimension type for level tag. - "REP-400050" Error retrieving outputs. - "REP-400052" Report Request Aborted from internal error. - "REP-400054" The number of generated cycle reports exceeds the maximum allowed. - "REP-400055" Export options not allowed for this object. - "REP-400057" The sense object has an empty GenericType. - "REP-400102" Image rendering invalid strategy error on Sense client. - "REP-400240" Engine Client Global generic closure error - "REP-400260" Engine Client generic closure error. - "REP-400280" Engine Client proxy generic closure error. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-403019" Export is not available for app with enabled directQuery feature. - "REP-403025" No entitlement to perform the operation. - "REP-403026" No entitlement to perform the operation. Export capability is off. - "REP-403027" Object without Hypercube or unsupported object type. - "REP-403048" Forbidden. User does not have permission to export the report (access control usePermission) - "REP-404000" Not found. The server can not find the requested resource. - "REP-404001" App not found, the app does not exist or it has been deleted. - "REP-404002" Chart not found, the chart does not exist or it has been deleted. - "REP-404003" Sheet not found, the sheet does not exist or it has been deleted or it is unavailable. - "REP-404004" Story not found, the story does not exist or it has been deleted or it is unavailable. - "REP-409001" App conflict. - "REP-409021" Reload timestamp constraint not met. - "REP-409046" Report aborted due to app reload. - "REP-422030" Apply variables error. - "REP-422051" There is no report to produce due to empty dataset or missing fields (the measure/dimension was removed or omitted in Section Access) - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429014" The export could not be completed within the requested deadline. - "REP-429016" Exceeded max session tenant quota per day. - "REP-429022" Enigma generic abort. - "REP-400064" Missing Bookmark  - "REP-500000" Fail to resolve resource. - "REP-500006" Fail to get report session parameters. - "REP-500014" The app did not open within 10 minutes. - "REP-500023" Validate Report Request Tags failure. - "REP-500045" Failure setting Bookmark timestamp. - "REP-500047" Error setting GroupState. - "REP-500053" Unexpected number of generated cycle reports. - "REP-500059" The App is corrupt. - "REP-500061" Engine Memory limit reached. - "REP-500062" Too many resolution attempts for a task. - "REP-500063" Engine terminated - "REP-500100" Image rendering generic error on Sense client. - "REP-500101" Image rendering could not set cookies error on Sense client. - "REP-500103" Image rendering JS timeout error on Sense client. - "REP-500104" Image rendering load URL timeout error on Sense client. - "REP-500105" Image rendering max paint attempts exceeded error on Sense client. - "REP-500106" Image rendering max JS attempts exceeded error on Sense client. - "REP-500107" Image rendering render timeout error on Sense client. - "REP-500108" Image rendering JS failure due to timeout error on Sense client. - "REP-500109" Image rendering generic JS failure error on Sense client. - "REP-500200" Report Generator error. - "REP-500240" Engine Global generic closure error. - "REP-500260" Engine Websocket generic closure error. - "REP-500280" Engine proxy generic closure error. - "REP-503001" Rest Engine Error. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-503060" Engine Service unavailable. |
| `meta` | object | No | Define the export error metadata. Each property is filled if it is related to the export error type. |
| `title` | string | Yes | A summary in english explaining what went wrong. |
| `detail` | string | No | Optional. MAY be used to provide more concrete details. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appErrors` | object[] | No | Errors occurring when dealing with the app. |
| `selectionErrors` | object[] | No | Errors occurring in selections. |

<details>
<summary>Properties of `appErrors`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `selectionErrors`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/reports/{id}/outputs` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/reports/{id}/outputs',
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
# qlik-cli has not implemented support for GET /api/v1/reports/{id}/outputs yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/reports/{id}/outputs" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "data": [
    {
      "status": "processing",
      "traceId": "1234",
      "location": "https://t.eu.qlikcloud.com:443/api/v1/temp-contents/619b77be498fea00018de0e1?inline=1",
      "outputId": "c61841ac-7b35-4434-aa74-4421f10fc68e",
      "sizeBytes": 42,
      "exportErrors": [
        {
          "code": "string",
          "meta": {
            "appErrors": [
              {
                "appId": "11ecf638-0be4-4b94-a9e6-91218f34e175",
                "method": "GetObject",
                "parameters": {}
              }
            ],
            "selectionErrors": [
              {
                "detail": "string",
                "errorType": "fieldMissing",
                "fieldName": "Year",
                "stateName": "string",
                "missingValues": [
                  {
                    "text": "2021",
                    "number": 42,
                    "isNumeric": true
                  }
                ],
                "isFieldNameMissing": false
              }
            ]
          },
          "title": "string",
          "detail": "string"
        }
      ],
      "cycleSelections": [
        {
          "values": [
            {
              "text": "2021",
              "number": 42,
              "isNumeric": true
            }
          ],
          "fieldName": "Year",
          "defaultIsNumeric": true
        }
      ]
    }
  ],
  "links": {
    "next": {
      "href": "https://tenant.qlik-cloud.com:443/api/v1/apps/816e23e1-03d2-446b-8721-cdee6b5e59cf/report-filters?filter=&filterTypes=REP&filterTypes=REP&limit=20&page=0&sort=%2Bname"
    },
    "prev": {
      "href": "https://tenant.qlik-cloud.com:443/api/v1/apps/816e23e1-03d2-446b-8721-cdee6b5e59cf/report-filters?filter=&filterTypes=REP&filterTypes=REP&limit=20&page=0&sort=%2Bname"
    },
    "self": {
      "href": "https://tenant.qlik-cloud.com:443/api/v1/apps/816e23e1-03d2-446b-8721-cdee6b5e59cf/report-filters?filter=&filterTypes=REP&filterTypes=REP&limit=20&page=0&sort=%2Bname"
    }
  }
}
```

---

### GET /api/v1/reports/{id}/status

- **Rate Limit:** Tier 1 (1000 requests per minute)

#### Path Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | Yes | Identifier of the request. |

#### Responses

##### 200

Returns the request processing status.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | string | Yes | Status of the requested report. Enum: "queued", "processing", "done", "failed", "aborted", "visiting", "aborting" |
| `reasons` | object[] | No | _(deprecated)_ Present when status is failed. Deprecated. Use /reports/{id}/outputs instead. |
| `results` | object[] | No | _(deprecated)_ Present when the status is "done". Deprecated. Use /reports/{id}/outputs instead. |
| `requestErrors` | object[] | No | Errors occured during report generation. |
| `statusLocation` | string | No | Relative path to status location. |
| `resolutionAttempts` | integer | No | Count how many times the resolution of this report was attempted. |

<details>
<summary>Properties of `reasons`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `traceId` | string | No |  |
| `outputId` | string | No | The output identifier which uniquely identifies an output (PDF, image etc.) within the same request. |
| `exportErrors` | object[] | No | Errors occured during report generation. |

<details>
<summary>Properties of `exportErrors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400009" Maximum 16384 columns limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of columns you can download. - "REP-400010" Maximum 1048566 rows limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of rows you can download. - "REP-400011" The size of the downloaded Excel file exceed 100 MB limit. Download data in a visualization can't generate an .xlsx file due to limitations to the amount of data you can download. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-400017" Static App size exceeded. - "REP-400018" Excel string length exceeded. - "REP-400020" Invalid Issuer. - "REP-400024" Cannot extract claims from JWT. - "REP-400028" Invalid Tags. - "REP-400029" Reload Entitlement Limit Reached. - "REP-400035" Multiple selections detected in a field having OneAndOnlyone attribute. - "REP-400036" No selection detected in a field having OneAndOnlyone attribute. - "REP-400037" Max number of images exceeded in a report. - "REP-400038" Max number of nested levels exceeded in report. - "REP-400039" Max number of objects exceeded in a report. - "REP-400040" Max number of templates exceeded in a report. - "REP-400041" Unsupported dimension type for level tag. - "REP-400050" Error retrieving outputs. - "REP-400052" Report Request Aborted from internal error. - "REP-400054" The number of generated cycle reports exceeds the maximum allowed. - "REP-400055" Export options not allowed for this object. - "REP-400057" The sense object has an empty GenericType. - "REP-400102" Image rendering invalid strategy error on Sense client. - "REP-400240" Engine Client Global generic closure error - "REP-400260" Engine Client generic closure error. - "REP-400280" Engine Client proxy generic closure error. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-403019" Export is not available for app with enabled directQuery feature. - "REP-403025" No entitlement to perform the operation. - "REP-403026" No entitlement to perform the operation. Export capability is off. - "REP-403027" Object without Hypercube or unsupported object type. - "REP-403048" Forbidden. User does not have permission to export the report (access control usePermission) - "REP-404000" Not found. The server can not find the requested resource. - "REP-404001" App not found, the app does not exist or it has been deleted. - "REP-404002" Chart not found, the chart does not exist or it has been deleted. - "REP-404003" Sheet not found, the sheet does not exist or it has been deleted or it is unavailable. - "REP-404004" Story not found, the story does not exist or it has been deleted or it is unavailable. - "REP-409001" App conflict. - "REP-409021" Reload timestamp constraint not met. - "REP-409046" Report aborted due to app reload. - "REP-422030" Apply variables error. - "REP-422051" There is no report to produce due to empty dataset or missing fields (the measure/dimension was removed or omitted in Section Access) - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429014" The export could not be completed within the requested deadline. - "REP-429016" Exceeded max session tenant quota per day. - "REP-429022" Enigma generic abort. - "REP-400064" Missing Bookmark  - "REP-500000" Fail to resolve resource. - "REP-500006" Fail to get report session parameters. - "REP-500014" The app did not open within 10 minutes. - "REP-500023" Validate Report Request Tags failure. - "REP-500045" Failure setting Bookmark timestamp. - "REP-500047" Error setting GroupState. - "REP-500053" Unexpected number of generated cycle reports. - "REP-500059" The App is corrupt. - "REP-500061" Engine Memory limit reached. - "REP-500062" Too many resolution attempts for a task. - "REP-500063" Engine terminated - "REP-500100" Image rendering generic error on Sense client. - "REP-500101" Image rendering could not set cookies error on Sense client. - "REP-500103" Image rendering JS timeout error on Sense client. - "REP-500104" Image rendering load URL timeout error on Sense client. - "REP-500105" Image rendering max paint attempts exceeded error on Sense client. - "REP-500106" Image rendering max JS attempts exceeded error on Sense client. - "REP-500107" Image rendering render timeout error on Sense client. - "REP-500108" Image rendering JS failure due to timeout error on Sense client. - "REP-500109" Image rendering generic JS failure error on Sense client. - "REP-500200" Report Generator error. - "REP-500240" Engine Global generic closure error. - "REP-500260" Engine Websocket generic closure error. - "REP-500280" Engine proxy generic closure error. - "REP-503001" Rest Engine Error. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-503060" Engine Service unavailable. |
| `meta` | object | No | Define the export error metadata. Each property is filled if it is related to the export error type. |
| `title` | string | Yes | A summary in english explaining what went wrong. |
| `detail` | string | No | Optional. MAY be used to provide more concrete details. |

<details>
<summary>Properties of `meta`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `results`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `location` | string | Yes | Location to download the generated report. |
| `outputId` | string | Yes | The output identifier which uniquely identifies an output (PDF, image etc.) within the same request. |
| `exportErrors` | object[] | No | Errors occured during report generation. |

<details>
<summary>Properties of `exportErrors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400009" Maximum 16384 columns limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of columns you can download. - "REP-400010" Maximum 1048566 rows limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of rows you can download. - "REP-400011" The size of the downloaded Excel file exceed 100 MB limit. Download data in a visualization can't generate an .xlsx file due to limitations to the amount of data you can download. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-400017" Static App size exceeded. - "REP-400018" Excel string length exceeded. - "REP-400020" Invalid Issuer. - "REP-400024" Cannot extract claims from JWT. - "REP-400028" Invalid Tags. - "REP-400029" Reload Entitlement Limit Reached. - "REP-400035" Multiple selections detected in a field having OneAndOnlyone attribute. - "REP-400036" No selection detected in a field having OneAndOnlyone attribute. - "REP-400037" Max number of images exceeded in a report. - "REP-400038" Max number of nested levels exceeded in report. - "REP-400039" Max number of objects exceeded in a report. - "REP-400040" Max number of templates exceeded in a report. - "REP-400041" Unsupported dimension type for level tag. - "REP-400050" Error retrieving outputs. - "REP-400052" Report Request Aborted from internal error. - "REP-400054" The number of generated cycle reports exceeds the maximum allowed. - "REP-400055" Export options not allowed for this object. - "REP-400057" The sense object has an empty GenericType. - "REP-400102" Image rendering invalid strategy error on Sense client. - "REP-400240" Engine Client Global generic closure error - "REP-400260" Engine Client generic closure error. - "REP-400280" Engine Client proxy generic closure error. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-403019" Export is not available for app with enabled directQuery feature. - "REP-403025" No entitlement to perform the operation. - "REP-403026" No entitlement to perform the operation. Export capability is off. - "REP-403027" Object without Hypercube or unsupported object type. - "REP-403048" Forbidden. User does not have permission to export the report (access control usePermission) - "REP-404000" Not found. The server can not find the requested resource. - "REP-404001" App not found, the app does not exist or it has been deleted. - "REP-404002" Chart not found, the chart does not exist or it has been deleted. - "REP-404003" Sheet not found, the sheet does not exist or it has been deleted or it is unavailable. - "REP-404004" Story not found, the story does not exist or it has been deleted or it is unavailable. - "REP-409001" App conflict. - "REP-409021" Reload timestamp constraint not met. - "REP-409046" Report aborted due to app reload. - "REP-422030" Apply variables error. - "REP-422051" There is no report to produce due to empty dataset or missing fields (the measure/dimension was removed or omitted in Section Access) - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429014" The export could not be completed within the requested deadline. - "REP-429016" Exceeded max session tenant quota per day. - "REP-429022" Enigma generic abort. - "REP-400064" Missing Bookmark  - "REP-500000" Fail to resolve resource. - "REP-500006" Fail to get report session parameters. - "REP-500014" The app did not open within 10 minutes. - "REP-500023" Validate Report Request Tags failure. - "REP-500045" Failure setting Bookmark timestamp. - "REP-500047" Error setting GroupState. - "REP-500053" Unexpected number of generated cycle reports. - "REP-500059" The App is corrupt. - "REP-500061" Engine Memory limit reached. - "REP-500062" Too many resolution attempts for a task. - "REP-500063" Engine terminated - "REP-500100" Image rendering generic error on Sense client. - "REP-500101" Image rendering could not set cookies error on Sense client. - "REP-500103" Image rendering JS timeout error on Sense client. - "REP-500104" Image rendering load URL timeout error on Sense client. - "REP-500105" Image rendering max paint attempts exceeded error on Sense client. - "REP-500106" Image rendering max JS attempts exceeded error on Sense client. - "REP-500107" Image rendering render timeout error on Sense client. - "REP-500108" Image rendering JS failure due to timeout error on Sense client. - "REP-500109" Image rendering generic JS failure error on Sense client. - "REP-500200" Report Generator error. - "REP-500240" Engine Global generic closure error. - "REP-500260" Engine Websocket generic closure error. - "REP-500280" Engine proxy generic closure error. - "REP-503001" Rest Engine Error. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-503060" Engine Service unavailable. |
| `meta` | object | No | Define the export error metadata. Each property is filled if it is related to the export error type. |
| `title` | string | Yes | A summary in english explaining what went wrong. |
| `detail` | string | No | Optional. MAY be used to provide more concrete details. |

<details>
<summary>Properties of `meta`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

<details>
<summary>Properties of `requestErrors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400009" Maximum 16384 columns limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of columns you can download. - "REP-400010" Maximum 1048566 rows limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of rows you can download. - "REP-400011" The size of the downloaded Excel file exceed 100 MB limit. Download data in a visualization can't generate an .xlsx file due to limitations to the amount of data you can download. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-400017" Static App size exceeded. - "REP-400018" Excel string length exceeded. - "REP-400020" Invalid Issuer. - "REP-400024" Cannot extract claims from JWT. - "REP-400028" Invalid Tags. - "REP-400029" Reload Entitlement Limit Reached. - "REP-400035" Multiple selections detected in a field having OneAndOnlyone attribute. - "REP-400036" No selection detected in a field having OneAndOnlyone attribute. - "REP-400037" Max number of images exceeded in a report. - "REP-400038" Max number of nested levels exceeded in report. - "REP-400039" Max number of objects exceeded in a report. - "REP-400040" Max number of templates exceeded in a report. - "REP-400041" Unsupported dimension type for level tag. - "REP-400050" Error retrieving outputs. - "REP-400052" Report Request Aborted from internal error. - "REP-400054" The number of generated cycle reports exceeds the maximum allowed. - "REP-400055" Export options not allowed for this object. - "REP-400057" The sense object has an empty GenericType. - "REP-400102" Image rendering invalid strategy error on Sense client. - "REP-400240" Engine Client Global generic closure error - "REP-400260" Engine Client generic closure error. - "REP-400280" Engine Client proxy generic closure error. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-403019" Export is not available for app with enabled directQuery feature. - "REP-403025" No entitlement to perform the operation. - "REP-403026" No entitlement to perform the operation. Export capability is off. - "REP-403027" Object without Hypercube or unsupported object type. - "REP-403048" Forbidden. User does not have permission to export the report (access control usePermission) - "REP-404000" Not found. The server can not find the requested resource. - "REP-404001" App not found, the app does not exist or it has been deleted. - "REP-404002" Chart not found, the chart does not exist or it has been deleted. - "REP-404003" Sheet not found, the sheet does not exist or it has been deleted or it is unavailable. - "REP-404004" Story not found, the story does not exist or it has been deleted or it is unavailable. - "REP-409001" App conflict. - "REP-409021" Reload timestamp constraint not met. - "REP-409046" Report aborted due to app reload. - "REP-422030" Apply variables error. - "REP-422051" There is no report to produce due to empty dataset or missing fields (the measure/dimension was removed or omitted in Section Access) - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429014" The export could not be completed within the requested deadline. - "REP-429016" Exceeded max session tenant quota per day. - "REP-429022" Enigma generic abort. - "REP-400064" Missing Bookmark  - "REP-500000" Fail to resolve resource. - "REP-500006" Fail to get report session parameters. - "REP-500014" The app did not open within 10 minutes. - "REP-500023" Validate Report Request Tags failure. - "REP-500045" Failure setting Bookmark timestamp. - "REP-500047" Error setting GroupState. - "REP-500053" Unexpected number of generated cycle reports. - "REP-500059" The App is corrupt. - "REP-500061" Engine Memory limit reached. - "REP-500062" Too many resolution attempts for a task. - "REP-500063" Engine terminated - "REP-500100" Image rendering generic error on Sense client. - "REP-500101" Image rendering could not set cookies error on Sense client. - "REP-500103" Image rendering JS timeout error on Sense client. - "REP-500104" Image rendering load URL timeout error on Sense client. - "REP-500105" Image rendering max paint attempts exceeded error on Sense client. - "REP-500106" Image rendering max JS attempts exceeded error on Sense client. - "REP-500107" Image rendering render timeout error on Sense client. - "REP-500108" Image rendering JS failure due to timeout error on Sense client. - "REP-500109" Image rendering generic JS failure error on Sense client. - "REP-500200" Report Generator error. - "REP-500240" Engine Global generic closure error. - "REP-500260" Engine Websocket generic closure error. - "REP-500280" Engine proxy generic closure error. - "REP-503001" Rest Engine Error. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-503060" Engine Service unavailable. |
| `meta` | object | No | Define the export error metadata. Each property is filled if it is related to the export error type. |
| `title` | string | Yes | A summary in english explaining what went wrong. |
| `detail` | string | No | Optional. MAY be used to provide more concrete details. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appErrors` | object[] | No | Errors occurring when dealing with the app. |
| `selectionErrors` | object[] | No | Errors occurring in selections. |

<details>
<summary>Properties of `appErrors`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `selectionErrors`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 400

Bad request. Malformed syntax, errors in params.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Errors occured during report generation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400009" Maximum 16384 columns limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of columns you can download. - "REP-400010" Maximum 1048566 rows limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of rows you can download. - "REP-400011" The size of the downloaded Excel file exceed 100 MB limit. Download data in a visualization can't generate an .xlsx file due to limitations to the amount of data you can download. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-400017" Static App size exceeded. - "REP-400018" Excel string length exceeded. - "REP-400020" Invalid Issuer. - "REP-400024" Cannot extract claims from JWT. - "REP-400028" Invalid Tags. - "REP-400029" Reload Entitlement Limit Reached. - "REP-400035" Multiple selections detected in a field having OneAndOnlyone attribute. - "REP-400036" No selection detected in a field having OneAndOnlyone attribute. - "REP-400037" Max number of images exceeded in a report. - "REP-400038" Max number of nested levels exceeded in report. - "REP-400039" Max number of objects exceeded in a report. - "REP-400040" Max number of templates exceeded in a report. - "REP-400041" Unsupported dimension type for level tag. - "REP-400050" Error retrieving outputs. - "REP-400052" Report Request Aborted from internal error. - "REP-400054" The number of generated cycle reports exceeds the maximum allowed. - "REP-400055" Export options not allowed for this object. - "REP-400057" The sense object has an empty GenericType. - "REP-400102" Image rendering invalid strategy error on Sense client. - "REP-400240" Engine Client Global generic closure error - "REP-400260" Engine Client generic closure error. - "REP-400280" Engine Client proxy generic closure error. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-403019" Export is not available for app with enabled directQuery feature. - "REP-403025" No entitlement to perform the operation. - "REP-403026" No entitlement to perform the operation. Export capability is off. - "REP-403027" Object without Hypercube or unsupported object type. - "REP-403048" Forbidden. User does not have permission to export the report (access control usePermission) - "REP-404000" Not found. The server can not find the requested resource. - "REP-404001" App not found, the app does not exist or it has been deleted. - "REP-404002" Chart not found, the chart does not exist or it has been deleted. - "REP-404003" Sheet not found, the sheet does not exist or it has been deleted or it is unavailable. - "REP-404004" Story not found, the story does not exist or it has been deleted or it is unavailable. - "REP-409001" App conflict. - "REP-409021" Reload timestamp constraint not met. - "REP-409046" Report aborted due to app reload. - "REP-422030" Apply variables error. - "REP-422051" There is no report to produce due to empty dataset or missing fields (the measure/dimension was removed or omitted in Section Access) - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429014" The export could not be completed within the requested deadline. - "REP-429016" Exceeded max session tenant quota per day. - "REP-429022" Enigma generic abort. - "REP-400064" Missing Bookmark  - "REP-500000" Fail to resolve resource. - "REP-500006" Fail to get report session parameters. - "REP-500014" The app did not open within 10 minutes. - "REP-500023" Validate Report Request Tags failure. - "REP-500045" Failure setting Bookmark timestamp. - "REP-500047" Error setting GroupState. - "REP-500053" Unexpected number of generated cycle reports. - "REP-500059" The App is corrupt. - "REP-500061" Engine Memory limit reached. - "REP-500062" Too many resolution attempts for a task. - "REP-500063" Engine terminated - "REP-500100" Image rendering generic error on Sense client. - "REP-500101" Image rendering could not set cookies error on Sense client. - "REP-500103" Image rendering JS timeout error on Sense client. - "REP-500104" Image rendering load URL timeout error on Sense client. - "REP-500105" Image rendering max paint attempts exceeded error on Sense client. - "REP-500106" Image rendering max JS attempts exceeded error on Sense client. - "REP-500107" Image rendering render timeout error on Sense client. - "REP-500108" Image rendering JS failure due to timeout error on Sense client. - "REP-500109" Image rendering generic JS failure error on Sense client. - "REP-500200" Report Generator error. - "REP-500240" Engine Global generic closure error. - "REP-500260" Engine Websocket generic closure error. - "REP-500280" Engine proxy generic closure error. - "REP-503001" Rest Engine Error. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-503060" Engine Service unavailable. |
| `meta` | object | No | Define the export error metadata. Each property is filled if it is related to the export error type. |
| `title` | string | Yes | A summary in english explaining what went wrong. |
| `detail` | string | No | Optional. MAY be used to provide more concrete details. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appErrors` | object[] | No | Errors occurring when dealing with the app. |
| `selectionErrors` | object[] | No | Errors occurring in selections. |

<details>
<summary>Properties of `appErrors`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `selectionErrors`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 401

Unauthorized, JWT invalid or not provided.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Errors occured during report generation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400009" Maximum 16384 columns limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of columns you can download. - "REP-400010" Maximum 1048566 rows limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of rows you can download. - "REP-400011" The size of the downloaded Excel file exceed 100 MB limit. Download data in a visualization can't generate an .xlsx file due to limitations to the amount of data you can download. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-400017" Static App size exceeded. - "REP-400018" Excel string length exceeded. - "REP-400020" Invalid Issuer. - "REP-400024" Cannot extract claims from JWT. - "REP-400028" Invalid Tags. - "REP-400029" Reload Entitlement Limit Reached. - "REP-400035" Multiple selections detected in a field having OneAndOnlyone attribute. - "REP-400036" No selection detected in a field having OneAndOnlyone attribute. - "REP-400037" Max number of images exceeded in a report. - "REP-400038" Max number of nested levels exceeded in report. - "REP-400039" Max number of objects exceeded in a report. - "REP-400040" Max number of templates exceeded in a report. - "REP-400041" Unsupported dimension type for level tag. - "REP-400050" Error retrieving outputs. - "REP-400052" Report Request Aborted from internal error. - "REP-400054" The number of generated cycle reports exceeds the maximum allowed. - "REP-400055" Export options not allowed for this object. - "REP-400057" The sense object has an empty GenericType. - "REP-400102" Image rendering invalid strategy error on Sense client. - "REP-400240" Engine Client Global generic closure error - "REP-400260" Engine Client generic closure error. - "REP-400280" Engine Client proxy generic closure error. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-403019" Export is not available for app with enabled directQuery feature. - "REP-403025" No entitlement to perform the operation. - "REP-403026" No entitlement to perform the operation. Export capability is off. - "REP-403027" Object without Hypercube or unsupported object type. - "REP-403048" Forbidden. User does not have permission to export the report (access control usePermission) - "REP-404000" Not found. The server can not find the requested resource. - "REP-404001" App not found, the app does not exist or it has been deleted. - "REP-404002" Chart not found, the chart does not exist or it has been deleted. - "REP-404003" Sheet not found, the sheet does not exist or it has been deleted or it is unavailable. - "REP-404004" Story not found, the story does not exist or it has been deleted or it is unavailable. - "REP-409001" App conflict. - "REP-409021" Reload timestamp constraint not met. - "REP-409046" Report aborted due to app reload. - "REP-422030" Apply variables error. - "REP-422051" There is no report to produce due to empty dataset or missing fields (the measure/dimension was removed or omitted in Section Access) - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429014" The export could not be completed within the requested deadline. - "REP-429016" Exceeded max session tenant quota per day. - "REP-429022" Enigma generic abort. - "REP-400064" Missing Bookmark  - "REP-500000" Fail to resolve resource. - "REP-500006" Fail to get report session parameters. - "REP-500014" The app did not open within 10 minutes. - "REP-500023" Validate Report Request Tags failure. - "REP-500045" Failure setting Bookmark timestamp. - "REP-500047" Error setting GroupState. - "REP-500053" Unexpected number of generated cycle reports. - "REP-500059" The App is corrupt. - "REP-500061" Engine Memory limit reached. - "REP-500062" Too many resolution attempts for a task. - "REP-500063" Engine terminated - "REP-500100" Image rendering generic error on Sense client. - "REP-500101" Image rendering could not set cookies error on Sense client. - "REP-500103" Image rendering JS timeout error on Sense client. - "REP-500104" Image rendering load URL timeout error on Sense client. - "REP-500105" Image rendering max paint attempts exceeded error on Sense client. - "REP-500106" Image rendering max JS attempts exceeded error on Sense client. - "REP-500107" Image rendering render timeout error on Sense client. - "REP-500108" Image rendering JS failure due to timeout error on Sense client. - "REP-500109" Image rendering generic JS failure error on Sense client. - "REP-500200" Report Generator error. - "REP-500240" Engine Global generic closure error. - "REP-500260" Engine Websocket generic closure error. - "REP-500280" Engine proxy generic closure error. - "REP-503001" Rest Engine Error. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-503060" Engine Service unavailable. |
| `meta` | object | No | Define the export error metadata. Each property is filled if it is related to the export error type. |
| `title` | string | Yes | A summary in english explaining what went wrong. |
| `detail` | string | No | Optional. MAY be used to provide more concrete details. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appErrors` | object[] | No | Errors occurring when dealing with the app. |
| `selectionErrors` | object[] | No | Errors occurring in selections. |

<details>
<summary>Properties of `appErrors`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `selectionErrors`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 403

Forbidden, user did not authenticate.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Errors occured during report generation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400009" Maximum 16384 columns limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of columns you can download. - "REP-400010" Maximum 1048566 rows limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of rows you can download. - "REP-400011" The size of the downloaded Excel file exceed 100 MB limit. Download data in a visualization can't generate an .xlsx file due to limitations to the amount of data you can download. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-400017" Static App size exceeded. - "REP-400018" Excel string length exceeded. - "REP-400020" Invalid Issuer. - "REP-400024" Cannot extract claims from JWT. - "REP-400028" Invalid Tags. - "REP-400029" Reload Entitlement Limit Reached. - "REP-400035" Multiple selections detected in a field having OneAndOnlyone attribute. - "REP-400036" No selection detected in a field having OneAndOnlyone attribute. - "REP-400037" Max number of images exceeded in a report. - "REP-400038" Max number of nested levels exceeded in report. - "REP-400039" Max number of objects exceeded in a report. - "REP-400040" Max number of templates exceeded in a report. - "REP-400041" Unsupported dimension type for level tag. - "REP-400050" Error retrieving outputs. - "REP-400052" Report Request Aborted from internal error. - "REP-400054" The number of generated cycle reports exceeds the maximum allowed. - "REP-400055" Export options not allowed for this object. - "REP-400057" The sense object has an empty GenericType. - "REP-400102" Image rendering invalid strategy error on Sense client. - "REP-400240" Engine Client Global generic closure error - "REP-400260" Engine Client generic closure error. - "REP-400280" Engine Client proxy generic closure error. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-403019" Export is not available for app with enabled directQuery feature. - "REP-403025" No entitlement to perform the operation. - "REP-403026" No entitlement to perform the operation. Export capability is off. - "REP-403027" Object without Hypercube or unsupported object type. - "REP-403048" Forbidden. User does not have permission to export the report (access control usePermission) - "REP-404000" Not found. The server can not find the requested resource. - "REP-404001" App not found, the app does not exist or it has been deleted. - "REP-404002" Chart not found, the chart does not exist or it has been deleted. - "REP-404003" Sheet not found, the sheet does not exist or it has been deleted or it is unavailable. - "REP-404004" Story not found, the story does not exist or it has been deleted or it is unavailable. - "REP-409001" App conflict. - "REP-409021" Reload timestamp constraint not met. - "REP-409046" Report aborted due to app reload. - "REP-422030" Apply variables error. - "REP-422051" There is no report to produce due to empty dataset or missing fields (the measure/dimension was removed or omitted in Section Access) - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429014" The export could not be completed within the requested deadline. - "REP-429016" Exceeded max session tenant quota per day. - "REP-429022" Enigma generic abort. - "REP-400064" Missing Bookmark  - "REP-500000" Fail to resolve resource. - "REP-500006" Fail to get report session parameters. - "REP-500014" The app did not open within 10 minutes. - "REP-500023" Validate Report Request Tags failure. - "REP-500045" Failure setting Bookmark timestamp. - "REP-500047" Error setting GroupState. - "REP-500053" Unexpected number of generated cycle reports. - "REP-500059" The App is corrupt. - "REP-500061" Engine Memory limit reached. - "REP-500062" Too many resolution attempts for a task. - "REP-500063" Engine terminated - "REP-500100" Image rendering generic error on Sense client. - "REP-500101" Image rendering could not set cookies error on Sense client. - "REP-500103" Image rendering JS timeout error on Sense client. - "REP-500104" Image rendering load URL timeout error on Sense client. - "REP-500105" Image rendering max paint attempts exceeded error on Sense client. - "REP-500106" Image rendering max JS attempts exceeded error on Sense client. - "REP-500107" Image rendering render timeout error on Sense client. - "REP-500108" Image rendering JS failure due to timeout error on Sense client. - "REP-500109" Image rendering generic JS failure error on Sense client. - "REP-500200" Report Generator error. - "REP-500240" Engine Global generic closure error. - "REP-500260" Engine Websocket generic closure error. - "REP-500280" Engine proxy generic closure error. - "REP-503001" Rest Engine Error. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-503060" Engine Service unavailable. |
| `meta` | object | No | Define the export error metadata. Each property is filled if it is related to the export error type. |
| `title` | string | Yes | A summary in english explaining what went wrong. |
| `detail` | string | No | Optional. MAY be used to provide more concrete details. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appErrors` | object[] | No | Errors occurring when dealing with the app. |
| `selectionErrors` | object[] | No | Errors occurring in selections. |

<details>
<summary>Properties of `appErrors`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `selectionErrors`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 404

Not found.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Errors occured during report generation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400009" Maximum 16384 columns limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of columns you can download. - "REP-400010" Maximum 1048566 rows limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of rows you can download. - "REP-400011" The size of the downloaded Excel file exceed 100 MB limit. Download data in a visualization can't generate an .xlsx file due to limitations to the amount of data you can download. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-400017" Static App size exceeded. - "REP-400018" Excel string length exceeded. - "REP-400020" Invalid Issuer. - "REP-400024" Cannot extract claims from JWT. - "REP-400028" Invalid Tags. - "REP-400029" Reload Entitlement Limit Reached. - "REP-400035" Multiple selections detected in a field having OneAndOnlyone attribute. - "REP-400036" No selection detected in a field having OneAndOnlyone attribute. - "REP-400037" Max number of images exceeded in a report. - "REP-400038" Max number of nested levels exceeded in report. - "REP-400039" Max number of objects exceeded in a report. - "REP-400040" Max number of templates exceeded in a report. - "REP-400041" Unsupported dimension type for level tag. - "REP-400050" Error retrieving outputs. - "REP-400052" Report Request Aborted from internal error. - "REP-400054" The number of generated cycle reports exceeds the maximum allowed. - "REP-400055" Export options not allowed for this object. - "REP-400057" The sense object has an empty GenericType. - "REP-400102" Image rendering invalid strategy error on Sense client. - "REP-400240" Engine Client Global generic closure error - "REP-400260" Engine Client generic closure error. - "REP-400280" Engine Client proxy generic closure error. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-403019" Export is not available for app with enabled directQuery feature. - "REP-403025" No entitlement to perform the operation. - "REP-403026" No entitlement to perform the operation. Export capability is off. - "REP-403027" Object without Hypercube or unsupported object type. - "REP-403048" Forbidden. User does not have permission to export the report (access control usePermission) - "REP-404000" Not found. The server can not find the requested resource. - "REP-404001" App not found, the app does not exist or it has been deleted. - "REP-404002" Chart not found, the chart does not exist or it has been deleted. - "REP-404003" Sheet not found, the sheet does not exist or it has been deleted or it is unavailable. - "REP-404004" Story not found, the story does not exist or it has been deleted or it is unavailable. - "REP-409001" App conflict. - "REP-409021" Reload timestamp constraint not met. - "REP-409046" Report aborted due to app reload. - "REP-422030" Apply variables error. - "REP-422051" There is no report to produce due to empty dataset or missing fields (the measure/dimension was removed or omitted in Section Access) - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429014" The export could not be completed within the requested deadline. - "REP-429016" Exceeded max session tenant quota per day. - "REP-429022" Enigma generic abort. - "REP-400064" Missing Bookmark  - "REP-500000" Fail to resolve resource. - "REP-500006" Fail to get report session parameters. - "REP-500014" The app did not open within 10 minutes. - "REP-500023" Validate Report Request Tags failure. - "REP-500045" Failure setting Bookmark timestamp. - "REP-500047" Error setting GroupState. - "REP-500053" Unexpected number of generated cycle reports. - "REP-500059" The App is corrupt. - "REP-500061" Engine Memory limit reached. - "REP-500062" Too many resolution attempts for a task. - "REP-500063" Engine terminated - "REP-500100" Image rendering generic error on Sense client. - "REP-500101" Image rendering could not set cookies error on Sense client. - "REP-500103" Image rendering JS timeout error on Sense client. - "REP-500104" Image rendering load URL timeout error on Sense client. - "REP-500105" Image rendering max paint attempts exceeded error on Sense client. - "REP-500106" Image rendering max JS attempts exceeded error on Sense client. - "REP-500107" Image rendering render timeout error on Sense client. - "REP-500108" Image rendering JS failure due to timeout error on Sense client. - "REP-500109" Image rendering generic JS failure error on Sense client. - "REP-500200" Report Generator error. - "REP-500240" Engine Global generic closure error. - "REP-500260" Engine Websocket generic closure error. - "REP-500280" Engine proxy generic closure error. - "REP-503001" Rest Engine Error. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-503060" Engine Service unavailable. |
| `meta` | object | No | Define the export error metadata. Each property is filled if it is related to the export error type. |
| `title` | string | Yes | A summary in english explaining what went wrong. |
| `detail` | string | No | Optional. MAY be used to provide more concrete details. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appErrors` | object[] | No | Errors occurring when dealing with the app. |
| `selectionErrors` | object[] | No | Errors occurring in selections. |

<details>
<summary>Properties of `appErrors`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `selectionErrors`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 409

Conflicted request. Report aborted.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Errors occured during report generation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400009" Maximum 16384 columns limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of columns you can download. - "REP-400010" Maximum 1048566 rows limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of rows you can download. - "REP-400011" The size of the downloaded Excel file exceed 100 MB limit. Download data in a visualization can't generate an .xlsx file due to limitations to the amount of data you can download. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-400017" Static App size exceeded. - "REP-400018" Excel string length exceeded. - "REP-400020" Invalid Issuer. - "REP-400024" Cannot extract claims from JWT. - "REP-400028" Invalid Tags. - "REP-400029" Reload Entitlement Limit Reached. - "REP-400035" Multiple selections detected in a field having OneAndOnlyone attribute. - "REP-400036" No selection detected in a field having OneAndOnlyone attribute. - "REP-400037" Max number of images exceeded in a report. - "REP-400038" Max number of nested levels exceeded in report. - "REP-400039" Max number of objects exceeded in a report. - "REP-400040" Max number of templates exceeded in a report. - "REP-400041" Unsupported dimension type for level tag. - "REP-400050" Error retrieving outputs. - "REP-400052" Report Request Aborted from internal error. - "REP-400054" The number of generated cycle reports exceeds the maximum allowed. - "REP-400055" Export options not allowed for this object. - "REP-400057" The sense object has an empty GenericType. - "REP-400102" Image rendering invalid strategy error on Sense client. - "REP-400240" Engine Client Global generic closure error - "REP-400260" Engine Client generic closure error. - "REP-400280" Engine Client proxy generic closure error. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-403019" Export is not available for app with enabled directQuery feature. - "REP-403025" No entitlement to perform the operation. - "REP-403026" No entitlement to perform the operation. Export capability is off. - "REP-403027" Object without Hypercube or unsupported object type. - "REP-403048" Forbidden. User does not have permission to export the report (access control usePermission) - "REP-404000" Not found. The server can not find the requested resource. - "REP-404001" App not found, the app does not exist or it has been deleted. - "REP-404002" Chart not found, the chart does not exist or it has been deleted. - "REP-404003" Sheet not found, the sheet does not exist or it has been deleted or it is unavailable. - "REP-404004" Story not found, the story does not exist or it has been deleted or it is unavailable. - "REP-409001" App conflict. - "REP-409021" Reload timestamp constraint not met. - "REP-409046" Report aborted due to app reload. - "REP-422030" Apply variables error. - "REP-422051" There is no report to produce due to empty dataset or missing fields (the measure/dimension was removed or omitted in Section Access) - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429014" The export could not be completed within the requested deadline. - "REP-429016" Exceeded max session tenant quota per day. - "REP-429022" Enigma generic abort. - "REP-400064" Missing Bookmark  - "REP-500000" Fail to resolve resource. - "REP-500006" Fail to get report session parameters. - "REP-500014" The app did not open within 10 minutes. - "REP-500023" Validate Report Request Tags failure. - "REP-500045" Failure setting Bookmark timestamp. - "REP-500047" Error setting GroupState. - "REP-500053" Unexpected number of generated cycle reports. - "REP-500059" The App is corrupt. - "REP-500061" Engine Memory limit reached. - "REP-500062" Too many resolution attempts for a task. - "REP-500063" Engine terminated - "REP-500100" Image rendering generic error on Sense client. - "REP-500101" Image rendering could not set cookies error on Sense client. - "REP-500103" Image rendering JS timeout error on Sense client. - "REP-500104" Image rendering load URL timeout error on Sense client. - "REP-500105" Image rendering max paint attempts exceeded error on Sense client. - "REP-500106" Image rendering max JS attempts exceeded error on Sense client. - "REP-500107" Image rendering render timeout error on Sense client. - "REP-500108" Image rendering JS failure due to timeout error on Sense client. - "REP-500109" Image rendering generic JS failure error on Sense client. - "REP-500200" Report Generator error. - "REP-500240" Engine Global generic closure error. - "REP-500260" Engine Websocket generic closure error. - "REP-500280" Engine proxy generic closure error. - "REP-503001" Rest Engine Error. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-503060" Engine Service unavailable. |
| `meta` | object | No | Define the export error metadata. Each property is filled if it is related to the export error type. |
| `title` | string | Yes | A summary in english explaining what went wrong. |
| `detail` | string | No | Optional. MAY be used to provide more concrete details. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appErrors` | object[] | No | Errors occurring when dealing with the app. |
| `selectionErrors` | object[] | No | Errors occurring in selections. |

<details>
<summary>Properties of `appErrors`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `selectionErrors`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 429

Too many request. Indicates the user has sent too many requests in a given amount of time, aka "rate limiting".

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Errors occured during report generation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400009" Maximum 16384 columns limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of columns you can download. - "REP-400010" Maximum 1048566 rows limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of rows you can download. - "REP-400011" The size of the downloaded Excel file exceed 100 MB limit. Download data in a visualization can't generate an .xlsx file due to limitations to the amount of data you can download. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-400017" Static App size exceeded. - "REP-400018" Excel string length exceeded. - "REP-400020" Invalid Issuer. - "REP-400024" Cannot extract claims from JWT. - "REP-400028" Invalid Tags. - "REP-400029" Reload Entitlement Limit Reached. - "REP-400035" Multiple selections detected in a field having OneAndOnlyone attribute. - "REP-400036" No selection detected in a field having OneAndOnlyone attribute. - "REP-400037" Max number of images exceeded in a report. - "REP-400038" Max number of nested levels exceeded in report. - "REP-400039" Max number of objects exceeded in a report. - "REP-400040" Max number of templates exceeded in a report. - "REP-400041" Unsupported dimension type for level tag. - "REP-400050" Error retrieving outputs. - "REP-400052" Report Request Aborted from internal error. - "REP-400054" The number of generated cycle reports exceeds the maximum allowed. - "REP-400055" Export options not allowed for this object. - "REP-400057" The sense object has an empty GenericType. - "REP-400102" Image rendering invalid strategy error on Sense client. - "REP-400240" Engine Client Global generic closure error - "REP-400260" Engine Client generic closure error. - "REP-400280" Engine Client proxy generic closure error. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-403019" Export is not available for app with enabled directQuery feature. - "REP-403025" No entitlement to perform the operation. - "REP-403026" No entitlement to perform the operation. Export capability is off. - "REP-403027" Object without Hypercube or unsupported object type. - "REP-403048" Forbidden. User does not have permission to export the report (access control usePermission) - "REP-404000" Not found. The server can not find the requested resource. - "REP-404001" App not found, the app does not exist or it has been deleted. - "REP-404002" Chart not found, the chart does not exist or it has been deleted. - "REP-404003" Sheet not found, the sheet does not exist or it has been deleted or it is unavailable. - "REP-404004" Story not found, the story does not exist or it has been deleted or it is unavailable. - "REP-409001" App conflict. - "REP-409021" Reload timestamp constraint not met. - "REP-409046" Report aborted due to app reload. - "REP-422030" Apply variables error. - "REP-422051" There is no report to produce due to empty dataset or missing fields (the measure/dimension was removed or omitted in Section Access) - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429014" The export could not be completed within the requested deadline. - "REP-429016" Exceeded max session tenant quota per day. - "REP-429022" Enigma generic abort. - "REP-400064" Missing Bookmark  - "REP-500000" Fail to resolve resource. - "REP-500006" Fail to get report session parameters. - "REP-500014" The app did not open within 10 minutes. - "REP-500023" Validate Report Request Tags failure. - "REP-500045" Failure setting Bookmark timestamp. - "REP-500047" Error setting GroupState. - "REP-500053" Unexpected number of generated cycle reports. - "REP-500059" The App is corrupt. - "REP-500061" Engine Memory limit reached. - "REP-500062" Too many resolution attempts for a task. - "REP-500063" Engine terminated - "REP-500100" Image rendering generic error on Sense client. - "REP-500101" Image rendering could not set cookies error on Sense client. - "REP-500103" Image rendering JS timeout error on Sense client. - "REP-500104" Image rendering load URL timeout error on Sense client. - "REP-500105" Image rendering max paint attempts exceeded error on Sense client. - "REP-500106" Image rendering max JS attempts exceeded error on Sense client. - "REP-500107" Image rendering render timeout error on Sense client. - "REP-500108" Image rendering JS failure due to timeout error on Sense client. - "REP-500109" Image rendering generic JS failure error on Sense client. - "REP-500200" Report Generator error. - "REP-500240" Engine Global generic closure error. - "REP-500260" Engine Websocket generic closure error. - "REP-500280" Engine proxy generic closure error. - "REP-503001" Rest Engine Error. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-503060" Engine Service unavailable. |
| `meta` | object | No | Define the export error metadata. Each property is filled if it is related to the export error type. |
| `title` | string | Yes | A summary in english explaining what went wrong. |
| `detail` | string | No | Optional. MAY be used to provide more concrete details. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appErrors` | object[] | No | Errors occurring when dealing with the app. |
| `selectionErrors` | object[] | No | Errors occurring in selections. |

<details>
<summary>Properties of `appErrors`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `selectionErrors`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

##### 500

Internal server error.

**Content-Type:** `application/json`

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | object[] | No | Errors occured during report generation. |

<details>
<summary>Properties of `errors`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | string | Yes | The unique code for the error  - "REP-400000" Bad request. The server could not understand the request due to invalid syntax. - "REP-400008" Selections error. - "REP-400009" Maximum 16384 columns limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of columns you can download. - "REP-400010" Maximum 1048566 rows limit exceeded. Download data in a visualization can't generate an .xlsx file due to limitations to the number of rows you can download. - "REP-400011" The size of the downloaded Excel file exceed 100 MB limit. Download data in a visualization can't generate an .xlsx file due to limitations to the amount of data you can download. - "REP-400015" Bad request in enigma request. The patch value has invalid JSON format. - "REP-400017" Static App size exceeded. - "REP-400018" Excel string length exceeded. - "REP-400020" Invalid Issuer. - "REP-400024" Cannot extract claims from JWT. - "REP-400028" Invalid Tags. - "REP-400029" Reload Entitlement Limit Reached. - "REP-400035" Multiple selections detected in a field having OneAndOnlyone attribute. - "REP-400036" No selection detected in a field having OneAndOnlyone attribute. - "REP-400037" Max number of images exceeded in a report. - "REP-400038" Max number of nested levels exceeded in report. - "REP-400039" Max number of objects exceeded in a report. - "REP-400040" Max number of templates exceeded in a report. - "REP-400041" Unsupported dimension type for level tag. - "REP-400050" Error retrieving outputs. - "REP-400052" Report Request Aborted from internal error. - "REP-400054" The number of generated cycle reports exceeds the maximum allowed. - "REP-400055" Export options not allowed for this object. - "REP-400057" The sense object has an empty GenericType. - "REP-400102" Image rendering invalid strategy error on Sense client. - "REP-400240" Engine Client Global generic closure error - "REP-400260" Engine Client generic closure error. - "REP-400280" Engine Client proxy generic closure error. - "REP-401000" Unauthorized. The client must authenticate itself to get the requested response. - "REP-401001" Unauthorized, bad JWT. - "REP-403000" Forbidden. The client does not have access rights to the content. - "REP-403001" App forbidden, the user does not have read permission on the app. - "REP-403002" Chart type not supported. - "REP-403019" Export is not available for app with enabled directQuery feature. - "REP-403025" No entitlement to perform the operation. - "REP-403026" No entitlement to perform the operation. Export capability is off. - "REP-403027" Object without Hypercube or unsupported object type. - "REP-403048" Forbidden. User does not have permission to export the report (access control usePermission) - "REP-404000" Not found. The server can not find the requested resource. - "REP-404001" App not found, the app does not exist or it has been deleted. - "REP-404002" Chart not found, the chart does not exist or it has been deleted. - "REP-404003" Sheet not found, the sheet does not exist or it has been deleted or it is unavailable. - "REP-404004" Story not found, the story does not exist or it has been deleted or it is unavailable. - "REP-409001" App conflict. - "REP-409021" Reload timestamp constraint not met. - "REP-409046" Report aborted due to app reload. - "REP-422030" Apply variables error. - "REP-422051" There is no report to produce due to empty dataset or missing fields (the measure/dimension was removed or omitted in Section Access) - "REP-429000" Too many request. The user has sent too many requests in a given amount of time ("rate limiting"). - "REP-429012" Exceeded max session tenant quota. A tenant has opened too many different sessions at the same time. - "REP-429014" The export could not be completed within the requested deadline. - "REP-429016" Exceeded max session tenant quota per day. - "REP-429022" Enigma generic abort. - "REP-400064" Missing Bookmark  - "REP-500000" Fail to resolve resource. - "REP-500006" Fail to get report session parameters. - "REP-500014" The app did not open within 10 minutes. - "REP-500023" Validate Report Request Tags failure. - "REP-500045" Failure setting Bookmark timestamp. - "REP-500047" Error setting GroupState. - "REP-500053" Unexpected number of generated cycle reports. - "REP-500059" The App is corrupt. - "REP-500061" Engine Memory limit reached. - "REP-500062" Too many resolution attempts for a task. - "REP-500063" Engine terminated - "REP-500100" Image rendering generic error on Sense client. - "REP-500101" Image rendering could not set cookies error on Sense client. - "REP-500103" Image rendering JS timeout error on Sense client. - "REP-500104" Image rendering load URL timeout error on Sense client. - "REP-500105" Image rendering max paint attempts exceeded error on Sense client. - "REP-500106" Image rendering max JS attempts exceeded error on Sense client. - "REP-500107" Image rendering render timeout error on Sense client. - "REP-500108" Image rendering JS failure due to timeout error on Sense client. - "REP-500109" Image rendering generic JS failure error on Sense client. - "REP-500200" Report Generator error. - "REP-500240" Engine Global generic closure error. - "REP-500260" Engine Websocket generic closure error. - "REP-500280" Engine proxy generic closure error. - "REP-503001" Rest Engine Error. - "REP-503005" Engine unavailable, qix-sessions error no engines available. - "REP-503013" Session unavailable. The engine session used to create the report is unavailable. - "REP-503060" Engine Service unavailable. |
| `meta` | object | No | Define the export error metadata. Each property is filled if it is related to the export error type. |
| `title` | string | Yes | A summary in english explaining what went wrong. |
| `detail` | string | No | Optional. MAY be used to provide more concrete details. |

<details>
<summary>Properties of `meta`</summary>

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `appErrors` | object[] | No | Errors occurring when dealing with the app. |
| `selectionErrors` | object[] | No | Errors occurring in selections. |

<details>
<summary>Properties of `appErrors`</summary>

_Properties truncated due to depth limit._

</details>

<details>
<summary>Properties of `selectionErrors`</summary>

_Properties truncated due to depth limit._

</details>

</details>

</details>

#### Examples

**JavaScript:**

```javascript
// qlik-api has not implemented support for `GET /api/v1/reports/{id}/status` yet.
// In the meantime, you can use fetch like this:

const response = await fetch(
  '/api/v1/reports/{id}/status',
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
# qlik-cli has not implemented support for GET /api/v1/reports/{id}/status yet.
```

**cURL:**

```bash
curl "https://{tenant}.{region}.qlikcloud.com/api/v1/reports/{id}/status" \
-H "Authorization: Bearer <access_token>"
```

**Example Response:**

```json
{
  "status": "done",
  "results": [
    {
      "location": "https://qlikcloud.com:443/api/v1/temp-contents/619baab68023910001efcb86?inline=1",
      "outputId": "output1"
    }
  ],
  "statusLocation": "/reports/01562a37-23e3-4b43-865d-84c26122276c/status",
  "resolutionAttempts": 1
}
```

---
