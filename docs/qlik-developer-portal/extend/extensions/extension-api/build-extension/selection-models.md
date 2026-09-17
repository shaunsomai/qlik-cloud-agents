---
source: https://qlik.dev/extend/extensions/extension-api/build-extension/selection-models/
last_updated: 2026-06-02T18:15:45+01:00
---

# Selection models

You can choose between three options for selections in a visualization extension:

- No selections
- Standard Qlik Sense selection model with toolbar and wrapper around the object
  supported by methods in the Extension API.
- Quick selection, where selections are sent straight to the Qlik associative
  engine and immediately are reflected in the object supported by methods in the
  Backend API.

The selection model is defined in the `initialProperties` section in the
JavaScript file. You use `selectionMode : "CONFIRM"` for standard Qlik Sense
election model and you use `selectionMode : "QUICK"` for quick selection mode

Example: Defining standard Qlik Sense selection model

```javascript
    return {
        initialProperties : {
            version: 1.0,
            qListObjectDef : {
                qShowAlternatives : true,
                qFrequencyMode : "V",
                qInitialDataFetch : [{
                    qWidth : 2,
                    qHeight : 50
                }]
            },
            fixed : true,
            width : 25,
            percent : true,
            selectionMode : "CONFIRM"
        },
```

Example: Defining quick selection model

```javascript
    return {
        initialProperties : {
            version: 1.0,
            qListObjectDef : {
                qShowAlternatives : true,
                qFrequencyMode : "V",
                qInitialDataFetch : [{
                    qWidth : 2,
                    qHeight : 50
                }]
            },
            fixed : true,
            width : 25,
            percent : true,
            selectionMode : "QUICK"
        },
```

You then enable the selection model in the JavaScript.

Example: Defining standard Qlik Sense selection model

```javascript
    if(this.selectionsEnabled && layout.selectionMode !== "NO") {
        $element.find('li').on('click', function() {
            if(this.hasAttribute("data-value")) {
                var value = parseInt(this.getAttribute("data-value"), 10), dim = 0;
                if(layout.selectionMode === "CONFIRM") {
                    self.selectValues(dim, [value], true);
                    $(this).toggleClass("selected");
                } else {
                    self.backendApi.selectValues(dim, [value], true);
                }
            }
        });
    }
```

Example: Defining quick selection model

```javascript
    if(this.selectionsEnabled && layout.selectionMode !== "NO") {
        $element.find('li').on('click', function() {
            if(this.hasAttribute("data-value")) {
                var value = parseInt(this.getAttribute("data-value"), 10), dim = 0;
                if(layout.selectionMode === "QUICK") {
                    self.backendApi.selectValues(dim, [value], true);
                    $(this).toggleClass("selected");
                } else {
                    self.selectValues(dim, [value], true);
                }
            }
        });
    }
```
