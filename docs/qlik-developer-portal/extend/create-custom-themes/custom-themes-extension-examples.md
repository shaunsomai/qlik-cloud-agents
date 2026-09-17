---
source: https://qlik.dev/extend/create-custom-themes/custom-themes-extension-examples/
last_updated: 2025-11-21T14:05:39Z
---

# Enable themes in visualization extensions

In this example, you will create a visualization extension that supports usage
of custom themes.

- Create the container.
  Create a folder that will contain your assets.

- Create the QEXT file.
  Create a QEXT file in the folder you just created and name it `MyVizExtension.qext`.

  It should contain the following information:

  ```javascript
  {
  "name":"MyVizExtension",
  "description":"Basic empty visualization template",
  "type":"visualization",
  "version":"1.0.0",
  "icon":"extension"
  }
  ```

- Create the main script file.
  Create the main script file and place in the same folder as the QEXT file.
  Name it `MyVizExtension.js`.

- Define the namespace.
  In the script file, define the namespace to be used for the styling. It
  should be created using the following syntax:

  `"object.[Extension name as defined in the QEXT file]"`.

  ```javascript
  const extensionNamespace = "object.MyVizExtension";
  ```

- Apply background color for labels.
  Create a renderHTML function and get the styling of the background color
  for the labels from the primary data color in the current theme, that is
  the theme currently loaded for the app where the visualization extension
  is being used.

  ```javascript
  function renderHtml( $element, qtheme ) {
  const html = "";

  html += "<div style='background-color: " + 
  qtheme.properties.dataColors.primaryColor + "; display: flex; align-items: center; height: 100%'>";
  }
  ```

- Apply font color and font size for labels.
  Get the styling of the of the label's font color and font size from the
  current theme.

  ```javascript
  function renderHtml( $element, qtheme ) {
  var html = "";

  html += "<div style='background-color: " + qtheme.properties.dataColors.primaryColor + "; display: flex; align-items: center; height: 100%'>";

  html += "<div style='flex: 1 1 auto; text-align: center;";
  html += " color: " + qtheme.getStyle( extensionNamespace, "label.name", "color" ) + ";";
  html += " font-size: " + qtheme.getStyle( extensionNamespace, "label.name", "fontSize" ) + ";'>";
  html += "My Viz Extension</div>";

  html += "</div>";
  $element.html( html );
  }
  ```

- Render the visualization extension.
  In a `return` statement, enable snapshots and export.

  ```javascript
  return {
  support : {
    snapshot: true,
    export: true,
    exportData : false
  }
  };
  ```

  Then define the `paint` function.

  ```javascript
  return {
  support : {
    snapshot: true,
    export: true,
    exportData : false
  },
  paint: function ($element) {
    var app = qlik.currApp(this);

    app.theme.getApplied().then( function( qtheme ){
      renderHtml( $element, qtheme );

      //needed for export
      return qlik.Promise.resolve();
    });
  }
  };
  ```

- Style the extension.
  You can style your extension just like any other native Qlik Sense object.
  This is done in the JSON file of your custom theme.

  ```json
  "object": {
    "MyVizExtension": {
      "backgroundColor": "#eee",
      "label": {
        "name": {
          "color": "#fff",
          "fontSize": "50px"
        }
      }
    }
  }
  ```

## Source code

<details>
  <summary>MyVizExtension.qext</summary>

  ```javascript
  {
    "name":"MyVizExtension",
    "description":"Basic empty visualization template",
    "type":"visualization",
    "version":"1.0.0",
    "icon":"extension"
  }
  ```
</details>

<details>
  <summary>MyVizExtension.js</summary>

  ```javascript
  define( [ "qlik"
  ],
  function ( qlik) {

    // Define the namespace used for styling 
    // Should be "object.[Extension name as defined in QEXT file]"
    const extensionNamespace = "object.MyVizExtension";

    function renderHtml( $element, qtheme ) {
      const html = "";

      // Get background color for the labels box from primary data color in current theme
      html += "<div style='background-color: " + qtheme.properties.dataColors.primaryColor + "; display: flex; align-items: center; height: 100%'>";

      // Get styling for the extension's label from current theme
      html += "<div style='flex: 1 1 auto; text-align: center;";
      html += " color: " + qtheme.getStyle( extensionNamespace, "label.name", "color" ) + ";";
      html += " font-size: " + qtheme.getStyle( extensionNamespace, "label.name", "fontSize" ) + ";'>";
      html += "My Viz Extension</div>";

      html += "</div>";
      $element.html( html );
    }

    return {
      support : {
        snapshot: true,
        export: true,
        exportData : false
      },
      paint: function ($element) {
        const app = qlik.currApp(this);

        app.theme.getApplied().then( function( qtheme ){
          renderHtml( $element, qtheme );

          //needed for export
          return qlik.Promise.resolve();
        });
      }
    };

  } );
  ```
</details>
