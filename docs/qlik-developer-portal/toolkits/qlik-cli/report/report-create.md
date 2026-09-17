---
source: https://qlik.dev/toolkits/qlik-cli/report/report-create/
last_updated: 2026-06-03T09:30:31+02:00
---

# report create

## qlik report create

Queue a new report request generation

### Synopsis

Queue a new report request generation.

```
qlik report create [flags]
```

### Options

```
      --compositionTemplates-senseImageTemplate-appId string                                                          Used to export a single visualization as pdf, pptx or png.
      --compositionTemplates-senseImageTemplate-persistentBookmark-id string                                          Sense Persistence Bookmark id.
      --compositionTemplates-senseImageTemplate-reloadTimestampMatchType string                                       Choose the reloadTimestamp constraint to apply. An empty value leads to the default noCheck.
                                                                                                                      Allowed values: "noCheck", "requestTimeExact"
      --compositionTemplates-senseImageTemplate-selectionStrategy string                                              Used to export a single visualization as pdf, pptx or png.
                                                                                                                      Allowed values: "failOnErrors", "ignoreErrorsReturnDetails", "ignoreErrorsNoDetails"
      --compositionTemplates-senseImageTemplate-selectionType string                                                  Used to export a single visualization as pdf, pptx or png.
                                                                                                                      Allowed values: "selectionsByState", "temporaryBookmark", "persistentBookmark", "temporaryBookmarkV2"
      --compositionTemplates-senseImageTemplate-selectionsByState-defaultIsNumeric key:bool[=true]                    Default value that QFieldValue isNumeric property takes if missing.
      --compositionTemplates-senseImageTemplate-selectionsByState-fieldName key:string                                The name of the field to be selected.
      --compositionTemplates-senseImageTemplate-selectionsByState-values-isNumeric key:bool[=true]                    IsNumeric tells whether the field value is text or number. Default value is equal to defaultIsNumeric property in QSelection.
      --compositionTemplates-senseImageTemplate-selectionsByState-values-number key:int                               The values of the field to be selected.
      --compositionTemplates-senseImageTemplate-selectionsByState-values-text key:string                              String value of the field value.
      --compositionTemplates-senseImageTemplate-selectionsByStateDef string                                           The definition ID referring to a selectionsByState definition declared in definitions.
      --compositionTemplates-senseImageTemplate-temporaryBookmarkV2-id string                                         Sense Temporary Bookmark id.
      --compositionTemplates-senseImageTemplate-visualization-heightPx int                                            Height in pixels.
      --compositionTemplates-senseImageTemplate-visualization-id string                                               The sense visualization id or json definition.
      --compositionTemplates-senseImageTemplate-visualization-jsOpts unknown                                          A JSON object that is passed as-is to the mashup page while rendering.
      --compositionTemplates-senseImageTemplate-visualization-patches-qOp string                                      Soft properties, aka patches, to be applied to the visualization.
                                                                                                                      Allowed values: "add", "remove", "replace"
      --compositionTemplates-senseImageTemplate-visualization-patches-qPath string                                    Path to the property to add, remove or replace.
      --compositionTemplates-senseImageTemplate-visualization-patches-qValue string                                   Corresponds to the value of the property to add or to the new value of the property to update.
      --compositionTemplates-senseImageTemplate-visualization-type string                                             Choose visualization to export an image of a sense chart, sessionobject for a visualization to be created on-the-fly. An empty value leads to the type being inferred by its id.
                                                                                                                      Allowed values: "visualization", "sessionobject"
      --compositionTemplates-senseImageTemplate-visualization-widthPx int                                             Width in pixels.
      --compositionTemplates-senseSheetTemplate-appId string                                                          Used to export a sheet as pdf or pptx.
      --compositionTemplates-senseSheetTemplate-persistentBookmark-id string                                          Sense Persistence Bookmark id.
      --compositionTemplates-senseSheetTemplate-reloadTimestampMatchType string                                       Choose the reloadTimestamp constraint to apply. An empty value leads to the default noCheck.
                                                                                                                      Allowed values: "noCheck", "requestTimeExact"
      --compositionTemplates-senseSheetTemplate-selectionStrategy string                                              Used to export a sheet as pdf or pptx.
                                                                                                                      Allowed values: "failOnErrors", "ignoreErrorsReturnDetails", "ignoreErrorsNoDetails"
      --compositionTemplates-senseSheetTemplate-selectionType string                                                  Used to export a sheet as pdf or pptx.
                                                                                                                      Allowed values: "selectionsByState", "temporaryBookmark", "persistentBookmark", "temporaryBookmarkV2"
      --compositionTemplates-senseSheetTemplate-selectionsByState-defaultIsNumeric key:bool[=true]                    Default value that QFieldValue isNumeric property takes if missing.
      --compositionTemplates-senseSheetTemplate-selectionsByState-fieldName key:string                                The name of the field to be selected.
      --compositionTemplates-senseSheetTemplate-selectionsByState-values-isNumeric key:bool[=true]                    IsNumeric tells whether the field value is text or number. Default value is equal to defaultIsNumeric property in QSelection.
      --compositionTemplates-senseSheetTemplate-selectionsByState-values-number key:int                               The values of the field to be selected.
      --compositionTemplates-senseSheetTemplate-selectionsByState-values-text key:string                              String value of the field value.
      --compositionTemplates-senseSheetTemplate-selectionsByStateDef string                                           The definition ID referring to a selectionsByState definition declared in definitions.
      --compositionTemplates-senseSheetTemplate-sheet-heightPx int                                                    The height of the sheet in pixels. Default value is: - 1120 pixels for responsive sheet - 1680 pixels for extended sheet - same height set in sheet properties for custom sheet
      --compositionTemplates-senseSheetTemplate-sheet-id string                                                       The id of the sheet.
      --compositionTemplates-senseSheetTemplate-sheet-jsOpts unknown                                                  A JSON object that is passed as-is to the mashup page while rendering, this will be applied to all charts within the sheet. It includes properties of the whole sheet such as theme, gradient etc.
      --compositionTemplates-senseSheetTemplate-sheet-jsOptsById key:unknown                                          A map for applying jsOpts to specific visualization IDs within the sheet.
      --compositionTemplates-senseSheetTemplate-sheet-patchesById-qOp key:string                                      A map for applying soft properties, aka patches, to specific visualization IDs within the sheet.
                                                                                                                      Allowed values: "add", "remove", "replace"
      --compositionTemplates-senseSheetTemplate-sheet-patchesById-qPath key:string                                    Path to the property to add, remove or replace.
      --compositionTemplates-senseSheetTemplate-sheet-patchesById-qValue key:string                                   Corresponds to the value of the property to add or to the new value of the property to update.
      --compositionTemplates-senseSheetTemplate-sheet-widthPx int                                                     The width of the sheet in pixels. Default value is: - 1680 pixels for responsive sheet - 1120 pixels for extended sheet - same width set in sheet properties for custom sheet
      --compositionTemplates-senseSheetTemplate-temporaryBookmarkV2-id string                                         Sense Temporary Bookmark id.
      --compositionTemplates-type string                                                                              Template type and version using semantic versioning. It must have the following name convention, dashed-separated-template-name-MAJOR.MINOR
                                                                                                                      Allowed values: "sense-image-1.0", "sense-sheet-1.0"
      --definitions-selectionsByState-defaultIsNumeric key:key:bool[=true]                                            Default value that QFieldValue isNumeric property takes if missing.
      --definitions-selectionsByState-fieldName key:key:string                                                        The name of the field to be selected.
      --definitions-selectionsByState-values-isNumeric key:key:bool[=true]                                            IsNumeric tells whether the field value is text or number. Default value is equal to defaultIsNumeric property in QSelection.
      --definitions-selectionsByState-values-number key:key:int                                                       The values of the field to be selected.
      --definitions-selectionsByState-values-text key:key:string                                                      String value of the field value.
  -f, --file file                                                                                                     Read request body from the specified file
  -h, --help                                                                                                          help for create
      --interval int                                                                                                  Duration in seconds to wait between retries, at least 1 (default 1)
      --meta-exportDeadline string                                                                                    The maximum interval, starting from the time the API request is received, within which a report must be produced, past this interval the report generation fails. The default value is 10 minutes, the maximum allowed value is 4 hours. The recommended value for standard apps and exports (image, data, sheet) is 10 minutes, for larger apps or reports using composition or file based templates (Excel, PixelPerfect, HTML...) it should be set to 1 hour.
      --meta-outputTtl string                                                                                         Time to live of the final result artifacts in ISO8601 duration format. After that duration the request and underlying output files will not be guaranteed to be available. Default is 1 hour.
      --output-callBackAction-httpRequest-uri string                                                                  (Required) URI of the request.
      --output-cycleOutput-excelOutput-outFormat string                                                               (Required) The output format of the report to be produced.
                                                                                                                      Allowed values: "xlsx"
      --output-cycleOutput-namingPattern string                                                                       (Required) not needed at initial phase
                                                                                                                      Allowed values: "fieldValueWithUnderscore"
      --output-cycleOutput-pdfOutput-align-horizontal string                                                          (Required) Content alignment.
                                                                                                                      Allowed values: "left", "center", "right"
      --output-cycleOutput-pdfOutput-align-vertical string                                                            (Required) Content alignment.
                                                                                                                      Allowed values: "top", "middle", "bottom"
      --output-cycleOutput-pdfOutput-imageRenderingDpi int                                                            (Required) This value is used for rendered images only, set to a default of 300 dpi.
      --output-cycleOutput-pdfOutput-orientation string                                                               (Required) P for portrait, L for landscape and A for auto-detect. Auto-detect sets the orientation depending on the content width and height proportions: if content width > height the orientation is automatically set to landscape, portrait otherwise.
                                                                                                                      Allowed values: "P", "L", "A"
      --output-cycleOutput-pdfOutput-properties-author string                                                         (Required) Properties of the document. In case of multiple composition, only properties specified in the composition output are taken and the ones specified in each output item are ignored.
      --output-cycleOutput-pdfOutput-properties-subject string                                                        (Required) Properties of the document. In case of multiple composition, only properties specified in the composition output are taken and the ones specified in each output item are ignored.
      --output-cycleOutput-pdfOutput-properties-title string                                                          (Required) Properties of the document. In case of multiple composition, only properties specified in the composition output are taken and the ones specified in each output item are ignored.
      --output-cycleOutput-pdfOutput-resizeData-fit string                                                            (Required) The size of the area in the following format ˋ{width}{cm|mm}x{height}{cm|mm}ˋ (e.g. "297mmx210mm"). Please remember that PDF page orientation (landscape or portrait) should match the width and height set for this field (eg. A4 landscape is "297mmx210mm", A4 portrait is "210mmx287mm"). Note that the minimum printable area is 1.5cmx1.5cm (corresponding to 0.6x0.6 inches at 96 DPI).
      --output-cycleOutput-pdfOutput-resizeType string                                                                (Required) The type of resize to be performed:
                                                                                                                        - none is used to export a visualization, sheet or story as is (e.g. normal size), regardless of its size. This may result in cropping.
                                                                                                                        - autofit automatically fits the visualization, sheet or story into the output size (i.e. A4, A3 etc.). Any provided resizeData parameter will be ignored for this configuration.
                                                                                                                        - fit fits the visualization, sheet or story into the area specified in resizeData. The content will be rescaled to fit in that area.
                                                                                                                      Allowed values: "none", "autofit", "fit"
      --output-cycleOutput-pdfOutput-size string                                                                      (Required) Size of the pdf page.
                                                                                                                      Allowed values: "A1", "A2", "A3", "A4", "A5", "A6", "Letter", "Legal", "Tabloid"
      --output-cycleOutput-type string                                                                                (Required) 
                                                                                                                      Allowed values: "excel", "pdf", "html", "powerpoint", "word"
      --output-excelOutput-outFormat string                                                                           (Required) The output format of the report to be produced.
                                                                                                                      Allowed values: "xlsx"
      --output-imageOutput-outDpi int                                                                                 (Required) Image resolution in DPI (default 96 DPI).
      --output-imageOutput-outFormat string                                                                           (Required) The image format of the report to be produced.
                                                                                                                      Allowed values: "png", "jsondata"
      --output-imageOutput-outZoom int                                                                                (Required) The scale factor to be applied in image scaling. A zoom greater than 5 will not be applied to the device pixel ratio which will remain fixed at 5.
      --output-outputId string                                                                                        (Required) The output identifier which uniquely identifies an output (PDF, image etc.) within the same request. It does not need to be a GUID. No spaces and colons are allowed in the outputId string.
      --output-pdfCompositionOutput-pdfOutputs-align-horizontal string                                                Content alignment.
                                                                                                                      Allowed values: "left", "center", "right"
      --output-pdfCompositionOutput-pdfOutputs-align-vertical string                                                  Content alignment.
                                                                                                                      Allowed values: "top", "middle", "bottom"
      --output-pdfCompositionOutput-pdfOutputs-imageRenderingDpi int                                                  This value is used for rendered images only, set to a default of 300 dpi.
      --output-pdfCompositionOutput-pdfOutputs-orientation string                                                     P for portrait, L for landscape and A for auto-detect. Auto-detect sets the orientation depending on the content width and height proportions: if content width > height the orientation is automatically set to landscape, portrait otherwise.
                                                                                                                      Allowed values: "P", "L", "A"
      --output-pdfCompositionOutput-pdfOutputs-properties-author string                                               Properties of the document. In case of multiple composition, only properties specified in the composition output are taken and the ones specified in each output item are ignored.
      --output-pdfCompositionOutput-pdfOutputs-properties-subject string                                              Properties of the document. In case of multiple composition, only properties specified in the composition output are taken and the ones specified in each output item are ignored.
      --output-pdfCompositionOutput-pdfOutputs-properties-title string                                                Properties of the document. In case of multiple composition, only properties specified in the composition output are taken and the ones specified in each output item are ignored.
      --output-pdfCompositionOutput-pdfOutputs-resizeData-fit string                                                  The size of the area in the following format ˋ{width}{cm|mm}x{height}{cm|mm}ˋ (e.g. "297mmx210mm"). Please remember that PDF page orientation (landscape or portrait) should match the width and height set for this field (eg. A4 landscape is "297mmx210mm", A4 portrait is "210mmx287mm"). Note that the minimum printable area is 1.5cmx1.5cm (corresponding to 0.6x0.6 inches at 96 DPI).
      --output-pdfCompositionOutput-pdfOutputs-resizeType string                                                      The type of resize to be performed:
                                                                                                                        - none is used to export a visualization, sheet or story as is (e.g. normal size), regardless of its size. This may result in cropping.
                                                                                                                        - autofit automatically fits the visualization, sheet or story into the output size (i.e. A4, A3 etc.). Any provided resizeData parameter will be ignored for this configuration.
                                                                                                                        - fit fits the visualization, sheet or story into the area specified in resizeData. The content will be rescaled to fit in that area.
                                                                                                                      Allowed values: "none", "autofit", "fit"
      --output-pdfCompositionOutput-pdfOutputs-size string                                                            Size of the pdf page.
                                                                                                                      Allowed values: "A1", "A2", "A3", "A4", "A5", "A6", "Letter", "Legal", "Tabloid"
      --output-pdfCompositionOutput-properties-author string                                                          (Required) Properties of the document. In case of multiple composition, only properties specified in the composition output are taken and the ones specified in each output item are ignored.
      --output-pdfCompositionOutput-properties-subject string                                                         (Required) Properties of the document. In case of multiple composition, only properties specified in the composition output are taken and the ones specified in each output item are ignored.
      --output-pdfCompositionOutput-properties-title string                                                           (Required) Properties of the document. In case of multiple composition, only properties specified in the composition output are taken and the ones specified in each output item are ignored.
      --output-pdfOutput-align-horizontal string                                                                      (Required) Content alignment.
                                                                                                                      Allowed values: "left", "center", "right"
      --output-pdfOutput-align-vertical string                                                                        (Required) Content alignment.
                                                                                                                      Allowed values: "top", "middle", "bottom"
      --output-pdfOutput-imageRenderingDpi int                                                                        (Required) This value is used for rendered images only, set to a default of 300 dpi.
      --output-pdfOutput-orientation string                                                                           (Required) P for portrait, L for landscape and A for auto-detect. Auto-detect sets the orientation depending on the content width and height proportions: if content width > height the orientation is automatically set to landscape, portrait otherwise.
                                                                                                                      Allowed values: "P", "L", "A"
      --output-pdfOutput-properties-author string                                                                     (Required) Properties of the document. In case of multiple composition, only properties specified in the composition output are taken and the ones specified in each output item are ignored.
      --output-pdfOutput-properties-subject string                                                                    (Required) Properties of the document. In case of multiple composition, only properties specified in the composition output are taken and the ones specified in each output item are ignored.
      --output-pdfOutput-properties-title string                                                                      (Required) Properties of the document. In case of multiple composition, only properties specified in the composition output are taken and the ones specified in each output item are ignored.
      --output-pdfOutput-resizeData-fit string                                                                        (Required) The size of the area in the following format ˋ{width}{cm|mm}x{height}{cm|mm}ˋ (e.g. "297mmx210mm"). Please remember that PDF page orientation (landscape or portrait) should match the width and height set for this field (eg. A4 landscape is "297mmx210mm", A4 portrait is "210mmx287mm"). Note that the minimum printable area is 1.5cmx1.5cm (corresponding to 0.6x0.6 inches at 96 DPI).
      --output-pdfOutput-resizeType string                                                                            (Required) The type of resize to be performed:
                                                                                                                        - none is used to export a visualization, sheet or story as is (e.g. normal size), regardless of its size. This may result in cropping.
                                                                                                                        - autofit automatically fits the visualization, sheet or story into the output size (i.e. A4, A3 etc.). Any provided resizeData parameter will be ignored for this configuration.
                                                                                                                        - fit fits the visualization, sheet or story into the area specified in resizeData. The content will be rescaled to fit in that area.
                                                                                                                      Allowed values: "none", "autofit", "fit"
      --output-pdfOutput-size string                                                                                  (Required) Size of the pdf page.
                                                                                                                      Allowed values: "A1", "A2", "A3", "A4", "A5", "A6", "Letter", "Legal", "Tabloid"
      --output-pptxCompositionOutput-pptxOutput-imageRenderingDpi int                                                 (Required) This value is used for rendered images only, set to a default of 300 dpi.
      --output-pptxCompositionOutput-pptxOutput-orientation string                                                    (Required) L for landscape, P for portrait and A for auto-detect. Auto-detect sets landscape, the default PowerPoint orientation.
                                                                                                                      Allowed values: "L", "P", "A"
      --output-pptxCompositionOutput-pptxOutput-properties-author string                                              (Required) Properties of the document. In case of multiple composition, only properties specified in the composition output are taken and the ones specified in each output item are ignored.
      --output-pptxCompositionOutput-pptxOutput-properties-subject string                                             (Required) Properties of the document. In case of multiple composition, only properties specified in the composition output are taken and the ones specified in each output item are ignored.
      --output-pptxCompositionOutput-pptxOutput-properties-title string                                               (Required) Properties of the document. In case of multiple composition, only properties specified in the composition output are taken and the ones specified in each output item are ignored.
      --output-pptxCompositionOutput-pptxOutput-resizeType string                                                     (Required) The type of resize to be performed. Autofit automatically fits the visualization, sheet or story into the output size (i.e. Widescreen, OnScreen etc.).
                                                                                                                      Allowed values: "autofit"
      --output-pptxCompositionOutput-pptxOutput-size string                                                           (Required) Size of the PowerPoint slide:
                                                                                                                        - Widescreen: 960x540
                                                                                                                        - OnScreen: 720x540
                                                                                                                        - OnScreen16x9: 720x405
                                                                                                                        - OnScreen16x10: 720x450
                                                                                                                      Allowed values: "Widescreen", "OnScreen", "OnScreen16x9", "OnScreen16x10"
      --output-pptxOutput-imageRenderingDpi int                                                                       (Required) This value is used for rendered images only, set to a default of 300 dpi.
      --output-pptxOutput-orientation string                                                                          (Required) L for landscape, P for portrait and A for auto-detect. Auto-detect sets landscape, the default PowerPoint orientation.
                                                                                                                      Allowed values: "L", "P", "A"
      --output-pptxOutput-properties-author string                                                                    (Required) Properties of the document. In case of multiple composition, only properties specified in the composition output are taken and the ones specified in each output item are ignored.
      --output-pptxOutput-properties-subject string                                                                   (Required) Properties of the document. In case of multiple composition, only properties specified in the composition output are taken and the ones specified in each output item are ignored.
      --output-pptxOutput-properties-title string                                                                     (Required) Properties of the document. In case of multiple composition, only properties specified in the composition output are taken and the ones specified in each output item are ignored.
      --output-pptxOutput-resizeType string                                                                           (Required) The type of resize to be performed. Autofit automatically fits the visualization, sheet or story into the output size (i.e. Widescreen, OnScreen etc.).
                                                                                                                      Allowed values: "autofit"
      --output-pptxOutput-size string                                                                                 (Required) Size of the PowerPoint slide:
                                                                                                                        - Widescreen: 960x540
                                                                                                                        - OnScreen: 720x540
                                                                                                                        - OnScreen16x9: 720x405
                                                                                                                        - OnScreen16x10: 720x450
                                                                                                                      Allowed values: "Widescreen", "OnScreen", "OnScreen16x9", "OnScreen16x10"
      --output-type string                                                                                            (Required) The generated report type.
                                                                                                                      
                                                                                                                      Each template type supports specific output types:
                                                                                                                         - composition-1.0 supports only pdfcomposition and pptxcomposition output types
                                                                                                                         - sense-excel-template-1.0 supports only excel and pdf output type
                                                                                                                         - sense-pixel-perfect-template-1.0 supports only pdf output type
                                                                                                                         - sense-html-template-1.0 supports only html output type
                                                                                                                         - sense-powerpoint-template-1.0 supports powerpoint and pdf output types
                                                                                                                         - sense-word-template-1.0 supports word and pdf output types
                                                                                                                         - sense-image-1.0 supports pdf, pptx and image output types
                                                                                                                         - sense-sheet-1.0 supports pdf and pptx output type
                                                                                                                         - sense-data-1.0 supports xlsx output type
                                                                                                                      
                                                                                                                      Each output type requires a specific output to be provided:
                                                                                                                         - excel requires excelOutput to be set
                                                                                                                         - pdfcomposition requires pdfCompositionOutput to be set
                                                                                                                         - pptxcomposition requires pptxCompositionOutput to be set
                                                                                                                         - pdf requires pdfOutput to be set
                                                                                                                         - pptx requires pptxOutput to be set
                                                                                                                         - image requires imageOutput to be set
                                                                                                                         - csv doesn't have csv output
                                                                                                                         - xlsx requires xlsxOutput to be set
                                                                                                                      Allowed values: "image", "pdf", "xlsx", "jsondata", "pdfcomposition", "excel", "pptx", "pptxcomposition", "csv", "cycle", "html", "powerpoint", "word"
  -q, --quiet                                                                                                         Return only IDs from the command
      --raw                                                                                                           Return original response from server without any processing
      --requestCallBackAction-httpRequest-uri string                                                                  URI of the request.
      --retry int                                                                                                     Number of retries to do before failing, max 10
      --senseDataTemplate-appId string                                                                                (Required) 
      --senseDataTemplate-exportOptions-showSelections                                                                Show the Selections Applied to the Visualization in the artifact produced
      --senseDataTemplate-exportOptions-showTitles                                                                    Show Visualization Title, SubTitle, Footnote in the artifact produced
      --senseDataTemplate-exportOptions-showTotals                                                                    Show Visualization Totals in the artifact produced
      --senseDataTemplate-id string                                                                                   (Required) Sense visualization id. Visualizations created "on the fly" are not supported.
      --senseDataTemplate-patches-qOp string                                                                          
                                                                                                                      Allowed values: "add", "remove", "replace"
      --senseDataTemplate-patches-qPath string                                                                        Path to the property to add, remove or replace.
      --senseDataTemplate-patches-qValue string                                                                       Corresponds to the value of the property to add or to the new value of the property to update.
      --senseDataTemplate-persistentBookmark-id string                                                                (Required) Sense Persistence Bookmark id.
      --senseDataTemplate-reloadTimestampMatchType string                                                             Choose the reloadTimestamp constraint to apply. An empty value leads to the default noCheck.
                                                                                                                      Allowed values: "noCheck", "requestTimeExact"
      --senseDataTemplate-selectionStrategy string                                                                    
                                                                                                                      Allowed values: "failOnErrors", "ignoreErrorsReturnDetails", "ignoreErrorsNoDetails"
      --senseDataTemplate-selectionType string                                                                        
                                                                                                                      Allowed values: "selectionsByState", "temporaryBookmark", "persistentBookmark", "temporaryBookmarkV2"
      --senseDataTemplate-selectionsByState-defaultIsNumeric key:bool[=true]                                          Default value that QFieldValue isNumeric property takes if missing.
      --senseDataTemplate-selectionsByState-fieldName key:string                                                      The name of the field to be selected.
      --senseDataTemplate-selectionsByState-values-isNumeric key:bool[=true]                                          IsNumeric tells whether the field value is text or number. Default value is equal to defaultIsNumeric property in QSelection.
      --senseDataTemplate-selectionsByState-values-number key:int                                                     The values of the field to be selected.
      --senseDataTemplate-selectionsByState-values-text key:string                                                    String value of the field value.
      --senseDataTemplate-temporaryBookmarkV2-id string                                                               (Required) Sense Temporary Bookmark id.
      --senseDataTemplate-variables unknowns                                                                          
      --senseExcelTemplate-cycleFields strings                                                                        The values of the field to be selected.
      --senseExcelTemplate-jsOpts unknown                                                                             A JSON object that is passed as-is to the mashup page while rendering, this will be applied to all charts within the sheet. It includes properties of the whole sheet such as theme, gradient etc. Currently only the "theme" and "language" properties are supported.
      --senseExcelTemplate-reloadTimestampMatchType string                                                            Choose the reloadTimestamp constraint to apply. An empty value leads to the default noCheck.
                                                                                                                      Allowed values: "noCheck", "requestTimeExact"
      --senseExcelTemplate-selectionChain-persistentBookmark-id string                                                Sense Persistence Bookmark id.
      --senseExcelTemplate-selectionChain-selectionFilter-patchesById-qOp key:string                                  A map for applying soft properties, aka patches, to specific visualization IDs within the sheet.
                                                                                                                      Allowed values: "add", "remove", "replace"
      --senseExcelTemplate-selectionChain-selectionFilter-patchesById-qPath key:string                                Path to the property to add, remove or replace.
      --senseExcelTemplate-selectionChain-selectionFilter-patchesById-qValue key:string                               Corresponds to the value of the property to add or to the new value of the property to update.
      --senseExcelTemplate-selectionChain-selectionFilter-selectionsByState-defaultIsNumeric key:bool[=true]          Default value that QFieldValue isNumeric property takes if missing.
      --senseExcelTemplate-selectionChain-selectionFilter-selectionsByState-fieldName key:string                      The name of the field to be selected.
      --senseExcelTemplate-selectionChain-selectionFilter-selectionsByState-values-isNumeric key:bool[=true]          IsNumeric tells whether the field value is text or number. Default value is equal to defaultIsNumeric property in QSelection.
      --senseExcelTemplate-selectionChain-selectionFilter-selectionsByState-values-number key:int                     The values of the field to be selected.
      --senseExcelTemplate-selectionChain-selectionFilter-selectionsByState-values-text key:string                    String value of the field value.
      --senseExcelTemplate-selectionChain-selectionFilter-variables unknowns                                          Array of ChainableSelection
      --senseExcelTemplate-selectionChain-selectionType string                                                        Array of ChainableSelection
                                                                                                                      Allowed values: "selectionFilter", "persistentBookmark", "temporaryBookmarkV2"
      --senseExcelTemplate-selectionChain-temporaryBookmarkV2-id string                                               Sense Temporary Bookmark id.
      --senseExcelTemplate-templateLocation-format string                                                             (Required) The location of the report template. Currently it can be an absolute or relative URL to a persisted report template, or to a template file saved as temporary content, as in the following examples: - https://qlikcloud.com:443/api/v1/report-templates/223940f7-3170-46b7-91ea-e0c81230adf7 - https://qlikcloud.com:443/api/v1/temp-contents/653bb4acae966r0730da15fc
                                                                                                                      Allowed values: "url"
      --senseExcelTemplate-templateLocation-path string                                                               (Required) The report template location path.
      --senseHtmlTemplate-cycleFields strings                                                                         The values of the field to be selected.
      --senseHtmlTemplate-jsOpts unknown                                                                              A JSON object that is passed as-is to the mashup page while rendering, this will be applied to all charts within the sheet. It includes properties of the whole sheet such as theme, gradient etc. Currently only the "theme" and "language" properties are supported.
      --senseHtmlTemplate-reloadTimestampMatchType string                                                             Choose the reloadTimestamp constraint to apply. An empty value leads to the default noCheck.
                                                                                                                      Allowed values: "noCheck", "requestTimeExact"
      --senseHtmlTemplate-selectionChain-persistentBookmark-id string                                                 Sense Persistence Bookmark id.
      --senseHtmlTemplate-selectionChain-selectionFilter-patchesById-qOp key:string                                   A map for applying soft properties, aka patches, to specific visualization IDs within the sheet.
                                                                                                                      Allowed values: "add", "remove", "replace"
      --senseHtmlTemplate-selectionChain-selectionFilter-patchesById-qPath key:string                                 Path to the property to add, remove or replace.
      --senseHtmlTemplate-selectionChain-selectionFilter-patchesById-qValue key:string                                Corresponds to the value of the property to add or to the new value of the property to update.
      --senseHtmlTemplate-selectionChain-selectionFilter-selectionsByState-defaultIsNumeric key:bool[=true]           Default value that QFieldValue isNumeric property takes if missing.
      --senseHtmlTemplate-selectionChain-selectionFilter-selectionsByState-fieldName key:string                       The name of the field to be selected.
      --senseHtmlTemplate-selectionChain-selectionFilter-selectionsByState-values-isNumeric key:bool[=true]           IsNumeric tells whether the field value is text or number. Default value is equal to defaultIsNumeric property in QSelection.
      --senseHtmlTemplate-selectionChain-selectionFilter-selectionsByState-values-number key:int                      The values of the field to be selected.
      --senseHtmlTemplate-selectionChain-selectionFilter-selectionsByState-values-text key:string                     String value of the field value.
      --senseHtmlTemplate-selectionChain-selectionFilter-variables unknowns                                           Array of ChainableSelection
      --senseHtmlTemplate-selectionChain-selectionType string                                                         Array of ChainableSelection
                                                                                                                      Allowed values: "selectionFilter", "persistentBookmark", "temporaryBookmarkV2"
      --senseHtmlTemplate-selectionChain-temporaryBookmarkV2-id string                                                Sense Temporary Bookmark id.
      --senseHtmlTemplate-templateLocation-format string                                                              (Required) The location of the report template. Currently it can be an absolute or relative URL to a persisted report template, or to a template file saved as temporary content, as in the following examples: - https://qlikcloud.com:443/api/v1/report-templates/223940f7-3170-46b7-91ea-e0c81230adf7 - https://qlikcloud.com:443/api/v1/temp-contents/653bb4acae966r0730da15fc
                                                                                                                      Allowed values: "url"
      --senseHtmlTemplate-templateLocation-path string                                                                (Required) The report template location path.
      --senseImageTemplate-appId string                                                                               (Required) Used to export a single visualization as pdf, pptx or png.
      --senseImageTemplate-persistentBookmark-id string                                                               (Required) Sense Persistence Bookmark id.
      --senseImageTemplate-reloadTimestampMatchType string                                                            Choose the reloadTimestamp constraint to apply. An empty value leads to the default noCheck.
                                                                                                                      Allowed values: "noCheck", "requestTimeExact"
      --senseImageTemplate-selectionStrategy string                                                                   Used to export a single visualization as pdf, pptx or png.
                                                                                                                      Allowed values: "failOnErrors", "ignoreErrorsReturnDetails", "ignoreErrorsNoDetails"
      --senseImageTemplate-selectionType string                                                                       Used to export a single visualization as pdf, pptx or png.
                                                                                                                      Allowed values: "selectionsByState", "temporaryBookmark", "persistentBookmark", "temporaryBookmarkV2"
      --senseImageTemplate-selectionsByState-defaultIsNumeric key:bool[=true]                                         Default value that QFieldValue isNumeric property takes if missing.
      --senseImageTemplate-selectionsByState-fieldName key:string                                                     The name of the field to be selected.
      --senseImageTemplate-selectionsByState-values-isNumeric key:bool[=true]                                         IsNumeric tells whether the field value is text or number. Default value is equal to defaultIsNumeric property in QSelection.
      --senseImageTemplate-selectionsByState-values-number key:int                                                    The values of the field to be selected.
      --senseImageTemplate-selectionsByState-values-text key:string                                                   String value of the field value.
      --senseImageTemplate-selectionsByStateDef string                                                                The definition ID referring to a selectionsByState definition declared in definitions.
      --senseImageTemplate-temporaryBookmarkV2-id string                                                              (Required) Sense Temporary Bookmark id.
      --senseImageTemplate-visualization-heightPx int                                                                 (Required) Height in pixels.
      --senseImageTemplate-visualization-id string                                                                    (Required) The sense visualization id or json definition.
      --senseImageTemplate-visualization-jsOpts unknown                                                               (Required) A JSON object that is passed as-is to the mashup page while rendering.
      --senseImageTemplate-visualization-patches-qOp string                                                           Soft properties, aka patches, to be applied to the visualization.
                                                                                                                      Allowed values: "add", "remove", "replace"
      --senseImageTemplate-visualization-patches-qPath string                                                         Path to the property to add, remove or replace.
      --senseImageTemplate-visualization-patches-qValue string                                                        Corresponds to the value of the property to add or to the new value of the property to update.
      --senseImageTemplate-visualization-type string                                                                  (Required) Choose visualization to export an image of a sense chart, sessionobject for a visualization to be created on-the-fly. An empty value leads to the type being inferred by its id.
                                                                                                                      Allowed values: "visualization", "sessionobject"
      --senseImageTemplate-visualization-widthPx int                                                                  (Required) Width in pixels.
      --sensePixelPerfectTemplate-cycleFields strings                                                                 The values of the field to be selected.
      --sensePixelPerfectTemplate-jsOpts unknown                                                                      A JSON object that is passed as-is to the mashup page while rendering, this will be applied to all charts within the sheet. It includes properties of the whole sheet such as theme, gradient etc. Currently only the "theme" and "language" properties are supported.
      --sensePixelPerfectTemplate-reloadTimestampMatchType string                                                     Choose the reloadTimestamp constraint to apply. An empty value leads to the default noCheck.
                                                                                                                      Allowed values: "noCheck", "requestTimeExact"
      --sensePixelPerfectTemplate-selectionChain-persistentBookmark-id string                                         Sense Persistence Bookmark id.
      --sensePixelPerfectTemplate-selectionChain-selectionFilter-patchesById-qOp key:string                           A map for applying soft properties, aka patches, to specific visualization IDs within the sheet.
                                                                                                                      Allowed values: "add", "remove", "replace"
      --sensePixelPerfectTemplate-selectionChain-selectionFilter-patchesById-qPath key:string                         Path to the property to add, remove or replace.
      --sensePixelPerfectTemplate-selectionChain-selectionFilter-patchesById-qValue key:string                        Corresponds to the value of the property to add or to the new value of the property to update.
      --sensePixelPerfectTemplate-selectionChain-selectionFilter-selectionsByState-defaultIsNumeric key:bool[=true]   Default value that QFieldValue isNumeric property takes if missing.
      --sensePixelPerfectTemplate-selectionChain-selectionFilter-selectionsByState-fieldName key:string               The name of the field to be selected.
      --sensePixelPerfectTemplate-selectionChain-selectionFilter-selectionsByState-values-isNumeric key:bool[=true]   IsNumeric tells whether the field value is text or number. Default value is equal to defaultIsNumeric property in QSelection.
      --sensePixelPerfectTemplate-selectionChain-selectionFilter-selectionsByState-values-number key:int              The values of the field to be selected.
      --sensePixelPerfectTemplate-selectionChain-selectionFilter-selectionsByState-values-text key:string             String value of the field value.
      --sensePixelPerfectTemplate-selectionChain-selectionFilter-variables unknowns                                   Array of ChainableSelection
      --sensePixelPerfectTemplate-selectionChain-selectionType string                                                 Array of ChainableSelection
                                                                                                                      Allowed values: "selectionFilter", "persistentBookmark", "temporaryBookmarkV2"
      --sensePixelPerfectTemplate-selectionChain-temporaryBookmarkV2-id string                                        Sense Temporary Bookmark id.
      --sensePixelPerfectTemplate-templateLocation-format string                                                      (Required) The location of the report template. Currently it can be an absolute or relative URL to a persisted report template, or to a template file saved as temporary content, as in the following examples: - https://qlikcloud.com:443/api/v1/report-templates/223940f7-3170-46b7-91ea-e0c81230adf7 - https://qlikcloud.com:443/api/v1/temp-contents/653bb4acae966r0730da15fc
                                                                                                                      Allowed values: "url"
      --sensePixelPerfectTemplate-templateLocation-path string                                                        (Required) The report template location path.
      --sensePowerPointTemplate-cycleFields strings                                                                   The values of the field to be selected.
      --sensePowerPointTemplate-jsOpts unknown                                                                        A JSON object that is passed as-is to the mashup page while rendering, this will be applied to all charts within the sheet. It includes properties of the whole sheet such as theme, gradient etc. Currently only the "theme" and "language" properties are supported.
      --sensePowerPointTemplate-reloadTimestampMatchType string                                                       Choose the reloadTimestamp constraint to apply. An empty value leads to the default noCheck.
                                                                                                                      Allowed values: "noCheck", "requestTimeExact"
      --sensePowerPointTemplate-selectionChain-persistentBookmark-id string                                           Sense Persistence Bookmark id.
      --sensePowerPointTemplate-selectionChain-selectionFilter-patchesById-qOp key:string                             A map for applying soft properties, aka patches, to specific visualization IDs within the sheet.
                                                                                                                      Allowed values: "add", "remove", "replace"
      --sensePowerPointTemplate-selectionChain-selectionFilter-patchesById-qPath key:string                           Path to the property to add, remove or replace.
      --sensePowerPointTemplate-selectionChain-selectionFilter-patchesById-qValue key:string                          Corresponds to the value of the property to add or to the new value of the property to update.
      --sensePowerPointTemplate-selectionChain-selectionFilter-selectionsByState-defaultIsNumeric key:bool[=true]     Default value that QFieldValue isNumeric property takes if missing.
      --sensePowerPointTemplate-selectionChain-selectionFilter-selectionsByState-fieldName key:string                 The name of the field to be selected.
      --sensePowerPointTemplate-selectionChain-selectionFilter-selectionsByState-values-isNumeric key:bool[=true]     IsNumeric tells whether the field value is text or number. Default value is equal to defaultIsNumeric property in QSelection.
      --sensePowerPointTemplate-selectionChain-selectionFilter-selectionsByState-values-number key:int                The values of the field to be selected.
      --sensePowerPointTemplate-selectionChain-selectionFilter-selectionsByState-values-text key:string               String value of the field value.
      --sensePowerPointTemplate-selectionChain-selectionFilter-variables unknowns                                     Array of ChainableSelection
      --sensePowerPointTemplate-selectionChain-selectionType string                                                   Array of ChainableSelection
                                                                                                                      Allowed values: "selectionFilter", "persistentBookmark", "temporaryBookmarkV2"
      --sensePowerPointTemplate-selectionChain-temporaryBookmarkV2-id string                                          Sense Temporary Bookmark id.
      --sensePowerPointTemplate-templateLocation-format string                                                        (Required) The location of the report template. Currently it can be an absolute or relative URL to a persisted report template, or to a template file saved as temporary content, as in the following examples: - https://qlikcloud.com:443/api/v1/report-templates/223940f7-3170-46b7-91ea-e0c81230adf7 - https://qlikcloud.com:443/api/v1/temp-contents/653bb4acae966r0730da15fc
                                                                                                                      Allowed values: "url"
      --sensePowerPointTemplate-templateLocation-path string                                                          (Required) The report template location path.
      --senseSheetTemplate-appId string                                                                               (Required) Used to export a sheet as pdf or pptx.
      --senseSheetTemplate-persistentBookmark-id string                                                               (Required) Sense Persistence Bookmark id.
      --senseSheetTemplate-reloadTimestampMatchType string                                                            Choose the reloadTimestamp constraint to apply. An empty value leads to the default noCheck.
                                                                                                                      Allowed values: "noCheck", "requestTimeExact"
      --senseSheetTemplate-selectionStrategy string                                                                   Used to export a sheet as pdf or pptx.
                                                                                                                      Allowed values: "failOnErrors", "ignoreErrorsReturnDetails", "ignoreErrorsNoDetails"
      --senseSheetTemplate-selectionType string                                                                       Used to export a sheet as pdf or pptx.
                                                                                                                      Allowed values: "selectionsByState", "temporaryBookmark", "persistentBookmark", "temporaryBookmarkV2"
      --senseSheetTemplate-selectionsByState-defaultIsNumeric key:bool[=true]                                         Default value that QFieldValue isNumeric property takes if missing.
      --senseSheetTemplate-selectionsByState-fieldName key:string                                                     The name of the field to be selected.
      --senseSheetTemplate-selectionsByState-values-isNumeric key:bool[=true]                                         IsNumeric tells whether the field value is text or number. Default value is equal to defaultIsNumeric property in QSelection.
      --senseSheetTemplate-selectionsByState-values-number key:int                                                    The values of the field to be selected.
      --senseSheetTemplate-selectionsByState-values-text key:string                                                   String value of the field value.
      --senseSheetTemplate-selectionsByStateDef string                                                                The definition ID referring to a selectionsByState definition declared in definitions.
      --senseSheetTemplate-sheet-heightPx int                                                                         (Required) The height of the sheet in pixels. Default value is: - 1120 pixels for responsive sheet - 1680 pixels for extended sheet - same height set in sheet properties for custom sheet
      --senseSheetTemplate-sheet-id string                                                                            (Required) The id of the sheet.
      --senseSheetTemplate-sheet-jsOpts unknown                                                                       (Required) A JSON object that is passed as-is to the mashup page while rendering, this will be applied to all charts within the sheet. It includes properties of the whole sheet such as theme, gradient etc.
      --senseSheetTemplate-sheet-jsOptsById key:unknown                                                               A map for applying jsOpts to specific visualization IDs within the sheet.
      --senseSheetTemplate-sheet-patchesById-qOp key:string                                                           A map for applying soft properties, aka patches, to specific visualization IDs within the sheet.
                                                                                                                      Allowed values: "add", "remove", "replace"
      --senseSheetTemplate-sheet-patchesById-qPath key:string                                                         Path to the property to add, remove or replace.
      --senseSheetTemplate-sheet-patchesById-qValue key:string                                                        Corresponds to the value of the property to add or to the new value of the property to update.
      --senseSheetTemplate-sheet-widthPx int                                                                          (Required) The width of the sheet in pixels. Default value is: - 1680 pixels for responsive sheet - 1120 pixels for extended sheet - same width set in sheet properties for custom sheet
      --senseSheetTemplate-temporaryBookmarkV2-id string                                                              (Required) Sense Temporary Bookmark id.
      --senseWordTemplate-cycleFields strings                                                                         The values of the field to be selected.
      --senseWordTemplate-jsOpts unknown                                                                              A JSON object that is passed as-is to the mashup page while rendering, this will be applied to all charts within the sheet. It includes properties of the whole sheet such as theme, gradient etc. Currently only the "theme" and "language" properties are supported.
      --senseWordTemplate-reloadTimestampMatchType string                                                             Choose the reloadTimestamp constraint to apply. An empty value leads to the default noCheck.
                                                                                                                      Allowed values: "noCheck", "requestTimeExact"
      --senseWordTemplate-selectionChain-persistentBookmark-id string                                                 Sense Persistence Bookmark id.
      --senseWordTemplate-selectionChain-selectionFilter-patchesById-qOp key:string                                   A map for applying soft properties, aka patches, to specific visualization IDs within the sheet.
                                                                                                                      Allowed values: "add", "remove", "replace"
      --senseWordTemplate-selectionChain-selectionFilter-patchesById-qPath key:string                                 Path to the property to add, remove or replace.
      --senseWordTemplate-selectionChain-selectionFilter-patchesById-qValue key:string                                Corresponds to the value of the property to add or to the new value of the property to update.
      --senseWordTemplate-selectionChain-selectionFilter-selectionsByState-defaultIsNumeric key:bool[=true]           Default value that QFieldValue isNumeric property takes if missing.
      --senseWordTemplate-selectionChain-selectionFilter-selectionsByState-fieldName key:string                       The name of the field to be selected.
      --senseWordTemplate-selectionChain-selectionFilter-selectionsByState-values-isNumeric key:bool[=true]           IsNumeric tells whether the field value is text or number. Default value is equal to defaultIsNumeric property in QSelection.
      --senseWordTemplate-selectionChain-selectionFilter-selectionsByState-values-number key:int                      The values of the field to be selected.
      --senseWordTemplate-selectionChain-selectionFilter-selectionsByState-values-text key:string                     String value of the field value.
      --senseWordTemplate-selectionChain-selectionFilter-variables unknowns                                           Array of ChainableSelection
      --senseWordTemplate-selectionChain-selectionType string                                                         Array of ChainableSelection
                                                                                                                      Allowed values: "selectionFilter", "persistentBookmark", "temporaryBookmarkV2"
      --senseWordTemplate-selectionChain-temporaryBookmarkV2-id string                                                Sense Temporary Bookmark id.
      --senseWordTemplate-templateLocation-format string                                                              (Required) The location of the report template. Currently it can be an absolute or relative URL to a persisted report template, or to a template file saved as temporary content, as in the following examples: - https://qlikcloud.com:443/api/v1/report-templates/223940f7-3170-46b7-91ea-e0c81230adf7 - https://qlikcloud.com:443/api/v1/temp-contents/653bb4acae966r0730da15fc
                                                                                                                      Allowed values: "url"
      --senseWordTemplate-templateLocation-path string                                                                (Required) The report template location path.
      --type string                                                                                                   (Required) Template type and version using semantic versioning. It must have the following name convention: dashed-separated-template-name-MAJOR.MINOR.
                                                                                                                      Please note that sense-powerpoint-template-1.0, sense-word-template-1.0, sense-story-x.0 and qv-data-x.0 are only for internal use.
                                                                                                                      
                                                                                                                      Each type requires a specific template to be provided:
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
                                                                                                                        - composition-1.0 supports pdfcomposition and pptxcomposition output type
                                                                                                                        - sense-excel-template-1.0 supports excel and pdf output type
                                                                                                                        - sense-image-1.0 supports pdf, pptx and png output types
                                                                                                                        - sense-sheet-1.0 supports pdf, pptx output type
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
                                                                                                                      Allowed values: "composition-1.0", "sense-image-1.0", "sense-data-1.0", "sense-sheet-1.0", "sense-story-1.0", "qv-data-1.0", "qv-data-2.0", "sense-excel-template-1.0", "sense-pixel-perfect-template-1.0", "sense-html-template-1.0", "sense-powerpoint-template-1.0", "sense-word-template-1.0"
```

### Options inherited from parent commands

```
  -c, --config string            path/to/config.yml where parameters can be set instead of on the command line
      --context string           Name of the context used when connecting to Qlik Associative Engine
      --headers stringToString   HTTP headers to use when connecting to Qlik Associative Engine (default [])
      --insecure                 Allow connecting to hosts with self-signed certificates
      --json                     Returns output in JSON format, if possible. Disables verbose and traffic output
  -s, --server string            URL to Qlik Cloud or directly to a Qlik Associative Engine
      --server-type string       The type of server you are using: cloud, Windows (Enterprise on Windows) or engine
  -v, --verbose                  Log extra information
```
