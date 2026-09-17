---
source: https://qlik.dev/apis/javascript/capability/
last_updated: 2026-01-19T15:48:02Z
---

# Capability APIs

`Version: 1.8.1` | _stable_

The Capability APIs are a collection of JavaScript APIs that allows you to easily embed Qlik Sense content into a web page, and interact with data. With just a few lines of code, it is possible to create a visualization that leverages the Qlik Sense visualization library. Consider using the qlik-embed toolkit with the classic/chart or analytics/chart UI for a more modern embedding experience.

## Table of Contents

### Entries

- [js/qlik](#jsqlik-module)

### Definitions

- [Notification](#notification-class)
- [ObjectMetricSize](#objectmetricsize-object)
- [ObjectPixelSize](#objectpixelsize-object)
- [QApp](#qapp-class)
- [QAppTheme](#qapptheme-class)
- [QAppVisualization](#qappvisualization-class)
- [QBookmark](#qbookmark-class)
- [QDimensionCell](#qdimensioncell-class)
- [QField](#qfield-class)
- [QFieldSelections](#qfieldselections-class)
- [QFieldValue](#qfieldvalue-class)
- [QGlobal](#qglobal-class)
- [QGlobalTheme](#qglobaltheme-class)
- [QHeader](#qheader-class)
- [QMeasureCell](#qmeasurecell-class)
- [QNavigation](#qnavigation-class)
- [QNavigationModeResult](#qnavigationmoderesult-object)
- [QNavigationSheetResult](#qnavigationsheetresult-object)
- [QNavigationStoryResult](#qnavigationstoryresult-object)
- [QRow](#qrow-class)
- [QSelectionState](#qselectionstate-class)
- [QTable](#qtable-class)
- [QTheme](#qtheme-class)
- [QVariable](#qvariableapp-qapp-class)
- [QVisualization](#qvisualizationqapp-model-class)
- [getContentCallback](#getcontentcallbackdata-qapp-function)

## Entries

### js/qlik `module`

External interface to qlik, for mashups and including qlik in foreign web pages.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `navigation` | [QNavigation](#qnavigation-class) | Yes | - |  |
| `theme` | [QGlobalTheme](#qglobaltheme-class) | Yes | - |  |

<details>
<summary>Examples</summary>

```javascript
var config = {
	 host: "myhost.com",
	 prefix: "/",
	 port: window.location.port,
	 isSecure: true
};
requirejs(["js/qlik"], function(qlik) {
	 // open the app
  var app = qlik.openApp("c31e2aba-3b46-4b13-8b87-c5c2514dea1d", config);
	 // insert Qlik objects into the page.
	 app.getObject(document.getElementById("LB01"), "uPyZavD");
}
```

</details>

---

#### callRepository(path, method?, body?) `function`  _(deprecated)_

Call Qlik repository.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `path` | string | Yes | - | Path to the Qlik Sense repository. Refer to Qlik Sense repository documentation for the available paths. |
| `method` | string | No | "GET" | HTTP method. |
| `body` | string | No | - | Body of the post. |

##### Returns

`Promise<object>` - A promise of a Qlik repository reply.

<details>
<summary>Examples</summary>

```javascript
qlik.callRepository("/qrs/extension/schema").then(function(reply) {
		console.log(JSON.stringify(reply));
	  });
```

</details>

---

#### currApp(reference?) `function`

Get a reference to the current app. Use in an extension to get a reference to the app displayed.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `reference` | object | No | - | Reference to extension object. Since Qlik Sense 1.1 |

##### Returns

[QApp](#qapp-class) - An App JavaScript object with app methods.

<details>
<summary>Examples</summary>

```javascript
var app = qlik.currApp(this);
   app.clearAll();
```

</details>

---

#### getAppList(callback, config?) `function`

Get a list of Qlik apps and register a callback to receive the data.
The reply will contain all apps the user has access to.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `callback` | function | Yes | - | Callback method. |
| `config` | object | No | - | Additional configuration parameters. |

<details>
<summary>Examples</summary>

```javascript
var config = {
		host: "myhost.com",
		prefix: "/",
		port: window.location.port,
		isSecure: true
	};
 qlik.getAppList(function(list){
		var str = "";
		list.forEach(function(value) {
			str +=  value.qDocName + "("+ value.qDocId +") ";
		});
		console.log(str);
	}, config);
```

</details>

---

#### getExtensionList(callback?) `function`  _(deprecated)_

Get the list of extensions installed in the system.
The reply will contain all extensions such as visualizations, mashups, and so on.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `callback` | function | No | - | Callback method. |

##### Returns

`Promise` - A promise of a Qlik engine reply.

<details>
<summary>Examples</summary>

```javascript
qlik.getExtensionList(function(list){
		var str = "";
		list.forEach(function(value) {
			str +=  value.id + "(" + value.data.type + ") ";
		});
		console.log(str);
	});
```

</details>

---

#### getGlobal(config?) `function`

Open a connection with a Web Socket to engine for global methods.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | object | No | - | Additional configuration parameters. |

##### Returns

[QGlobal](#qglobal-class) - A global JavaScript object with global methods.

<details>
<summary>Examples</summary>

```javascript
var config = {
		host: "myhost.com",
		prefix: "/",
		port: window.location.port,
		isSecure: true
	  };
   var global = qlik.getGlobal(config);
   global.getAuthenticatedUser(function(reply){
		console.log("User:"+reply.qReturn);
	  });
```

</details>

---

#### getThemeList() `function`

Get a list of themes from the system. The list will contain both default and custom themes.

##### Returns

`Promise` - A promise of a list of themes including the ID and the metadata name.

<details>
<summary>Examples</summary>

```javascript
qlik.getThemeList().then(function(list){
		var str = "";
		list.forEach(function(value) {
			str += value.name + '(' + value.id + ")\n";
		});
		console.log(str);
	});
```

</details>

---

#### off(eventName?) `function`

Remove listener(s) for the qlik instance events.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `eventName` | string | No | - | Name of the event. If no eventName is provided, removes all listeners. |

<details>
<summary>Examples</summary>

```javascript
qlik.on("error", err=>{
  console.error(err);
});
qlik.off("error");
```

</details>

---

#### on(eventName, callback) `function`

Add listener(s) to the qlik instance events. Possible events are error, warning, and closed. Multiple listeners can be added to an event.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `eventName` | string | Yes | - | Name of the event. Can be: error, warning, closed. Note: this event handler will be overridden by app event handlers or global event handlers if set. |
| `callback` | function | Yes | - | Callback method. |

<details>
<summary>Examples</summary>

```javascript
qlik.on("error", err=>{
  console.error(err);
});
qlik.on("warning", warn=>{
  console.warn(warn);
});
```

</details>

---

#### openApp(appId, config?) `function`

Opens the app. You can open multiple apps. Most other methods are defined on the app. Introduced in Qlik Sense 1.0.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `appId` | string | Yes | - | The app ID. |
| `config` | object | No | - | Additional configuration parameters. |

##### Returns

[QApp](#qapp-class) - An App JavaScript object with app methods.

<details>
<summary>Examples</summary>

```javascript
var app = qlik.openApp("2abac31e-3b46-4b78-8bxf-c5cea1d2514d");
     var config = {
		  host: "myhost.com",
		  prefix: "/",
		  port: window.location.port,
		  isSecure: true
	    };
     var app2 = qlik.openApp("c31e2aba-3b46-4b13-8b87-c5c2514dea1d", config);
```

</details>

---

#### Promise(executor) `function`

Promise utility that can be used for asynchronous operations. Very useful for the paint method to
indicate that the rendering is complete. Full documentation available on:
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `executor` | function | Yes | - | The executing function with two parameters: resolve and reject. |

<details>
<summary>Examples</summary>

```javascript
var Promise = qlik.Promise;
qlik.registerExtension("dumpchart",
       {
     	paint:function($element,layout) {
       		return new Promise(function(resolve, reject) {
       	    	setTimeout(function() {
       	        	$element.html(JSON.stringify(layout));
       	        	resolve(); // Extension painted successfully
       	    	}, 1000);
       		});
       	}
   });
```

</details>

---

#### registerExtension(id, impl, metadata?) `function`

Register an extension for use in this mashup.
The extension will not be installed on Qlik Sense server, but only available in the session where it
is created.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `id` | string | Yes | - | Set the ID of the visualization extension. |
| `impl` | object | Yes | - | Set the extension implementation. |
| `metadata` | object | No | "{\"type\":\"visualization\"}" | Extension metadata, same format as QEXT file. |

<details>
<summary>Examples</summary>

```javascript
qlik.registerExtension("dumpchart",

   {
       paint:function($element,layout){
           $element.html(JSON.stringify(layout));
       }
   });
```

```javascript
requirejs([path +"/wordcloud/wordcloud.js"],function(wordcloud)
{
   qlik.registerExtension( "wordcloud", wordcloud );
});
```

</details>

---

#### resize(ID?) `function`

Sends a resize event to all Qlik objects.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `ID` | string | No | - | Object ID. Optional: if no ID, resize event will be sent to all objects. |

<details>
<summary>Examples</summary>

```javascript
//create the tabs and make qlik objects resize
 //when a new tab is selected
 $("#tabs").tabs().bind("tabsselect", function(event, ui) {
		qlik.resize();
	});
```

</details>

---

#### sessionApp(config?) `function`

Creates a session/cached QApp object.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | object | No | - | Additional configuration parameters. |

##### Returns

[QApp](#qapp-class) - An app JavaScript object with app methods.

<details>
<summary>Examples</summary>

_Basic usage_

```javascript
var sessionApp = qlik.sessionApp();
```

_Basic usage with config_

```javascript
var config = {
  host: "myhost.com",
  prefix: "/",
  port: window.location.port,
  isSecure: true
};
var sessionApp =  qlik.sessionApp(config);
```

</details>

---

#### sessionAppFromApp(appId, config?) `function`

Creates a session/cached QApp object from an existing app.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `appId` | string | Yes | - | App ID of the app to base the session app upon. |
| `config` | object | No | - | Additional configuration parameters. |

##### Returns

[QApp](#qapp-class) - An app JavaScript object with app methods.

<details>
<summary>Examples</summary>

_Basic usage_

```javascript
var sessionApp = qlik.sessionAppFromApp("2abac31e-3b46-4b78-8bxf-c5cea1d2514d");
```

_Basic usage with config_

```javascript
var config = {
  host: "myhost.com",
  prefix: "/",
  port: window.location.port,
  isSecure: true
};
var sessionApp = qlik.sessionAppFromApp("2abac31e-3b46-4b78-8bxf-c5cea1d2514d", config);
```

_Multiple apps_

```javascript
var sessionApp = qlik.sessionAppFromApp("2abac31e-3b46-4b78-8bxf-c5cea1d2514d");
var sessionApp2 = qlik.sessionAppFromApp("c31e2aba-3b46-4b13-8b87-c5c2514dea1d");
```

</details>

---

#### setDeviceType(deviceType) `function`

Sets device type, which modifies the UI accordingly.
The device type is automatically detected if it is not manually set.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `deviceType` | string | Yes | - | Type of device. One of: auto, touch, desktop. |

<details>
<summary>Examples</summary>

```javascript
qlik.setDeviceType('desktop');
```

</details>

---

#### setLanguage(lang) `function`

Set language.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `lang` | string | Yes | - | Language code |

<details>
<summary>Examples</summary>

```javascript
qlik.setLanguage("es");
```

</details>

---

#### setOnError(onError, onWarning?) `function`  _(deprecated)_

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `onError` | function | Yes | - | Error handling function. |
| `onWarning` | function | No | - | Warning handling function. Since Qlik Sense 2.1. |

<details>
<summary>Examples</summary>

```javascript
qlik.setOnError(function(error) {
  //contains code, message
	 console.log(error.message);
},
function(warning){
	 windows.console.log(warning);
});
```

</details>

---

#### table(ext, path?) `function`

Create a QTable object that wraps data in your extension and provides an object-oriented interface.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `ext` | object | Yes | - | Extension or angular scope for the extension. |
| `path` | string | No | "qHyperCube" | Path to the hypercube. |

##### Returns

[QTable](#qtable-class) - table - A QTable object that holds data and options for the table.

<details>
<summary>Examples</summary>

```javascript
$scope.table = qlik.table(this);

<tr ng-repeat="row in table.rows">
   <td ng-repeat="cell in row.cells"> {{cell.qText}} </td>
</tr>
```

</details>

---

## Definitions

### Notification() `class`

---

#### bind(observer) `function`

Observe a Notification by sending in an observer function.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `observer` | function | Yes | - | The observer function to handle the notification. |

---

#### unbind(observer) `function`

Stop observing a notification.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `observer` | function | Yes | - | The observer function that now should ignore any future notifications. |

---

### ObjectMetricSize `object`

Describes the size, in millimeters (mm), of a 2D object.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `height` | number | Yes | - | Object height in millimeters (mm). |
| `width` | number | Yes | - | Object width in millimeters (mm). |

---

### ObjectPixelSize `object`

Describes the size, in pixels, of a 2D object.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `height` | number | Yes | - | Object height in pixels. |
| `width` | number | Yes | - | Object width in pixels. |

---

### QApp() `class`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `bookmark` | [QBookmark](#qbookmark-class) | Yes | - |  |
| `theme` | [QAppTheme](#qapptheme-class) | Yes | - |  |
| `variable` | [QVariable](#qvariableapp-qapp-class) | Yes | - |  |
| `visualization` | [QAppVisualization](#qappvisualization-class) | Yes | - |  |

---

#### addAlternateState(qStateName) `function`

Add an alternate state.

Introduced in Qlik Sense 1.1.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qStateName` | string | Yes | - | Alternate state name. |

##### Returns

`Promise` - A promise of a Qlik engine reply.

<details>
<summary>Examples</summary>

```javascript
app.addAlternateState("X");
```

</details>

---

#### back() `function`

Back to prev selection.

##### Returns

`Promise` - A promise of a Qlik engine reply.

<details>
<summary>Examples</summary>

```javascript
var app = qlik.openApp('2abac31e-3b46-4b78-8bxf-c5cea1d2514d');
app.back();
```

</details>

---

#### clearAll(lockedAlso?, state?) `function`

Clear all selections.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `lockedAlso` | boolean | No | false | Also clear locked fields. Since Qlik Sense 2.1 |
| `state` | string | No | "$" | Alternate state name. Since Qlik Sense 2.1 |

##### Returns

`Promise` - A promise of a Qlik engine reply.

<details>
<summary>Examples</summary>

```javascript
var app = qlik.openApp('2abac31e-3b46-4b78-8bxf-c5cea1d2514d');
app.clearAll();
```

</details>

---

#### close() `function`

Close an app.

Will also close the web socket and clear out client side data.

Introduced in Qlik Sense 1.1

##### Returns

`Promise` - A promise of a Qlik engine reply.

<details>
<summary>Examples</summary>

```javascript
var app = qlik.openApp('2abac31e-3b46-4b78-8bxf-c5cea1d2514d');
app.close();
```

</details>

---

#### createCube(qHyperCubeDef, callback?) `function`

Defines a Qlik Hypercube and registers a callback to receive the data.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qHyperCubeDef` | object | Yes | - | Cube definition. |
| `callback` | function | No | - | Callback method. Parameter will contain a qHyperCube. |

##### Returns

`Promise` - A promise of an object model.

<details>
<summary>Examples</summary>

```javascript
app.createCube({
  qDimensions : [{
    qDef : {
      qFieldDefs : ["FirstName"]
    }
  }, {
    qDef : {
      qFieldDefs : ["LastName"]
  }
}],
qMeasures : [{
  qDef : {
    qDef : "1"
  }
}],
qInitialDataFetch : [{
  qTop : 0,
  qLeft : 0,
  qHeight : 20,
  qWidth : 3
}]
}, function(reply) {
  var str = "";
  $.each(reply.qHyperCube.qDataPages[0].qMatrix, function(key, value) {
    str += '<li>' + value[0].qText + ':' + value[1].qText + '</li>';
  });
  $('#list').html(str);
});
```

</details>

---

#### createGenericObject(param, callback?) `function`

Creates a Qlik Generic object and registers a callback to receive the data.
The generic object can contain qHyperCubeDef, qListObjectDef and/or
qStringExpression and qValueExpression.
It will be a session object and disppears when the session is closed.
The callback method will be called whenever the selection state changes in a way
that affects the generic object. The parameter will be the evaluated version of the definition.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `param` | object | Yes | - | Generic object definition. |
| `callback` | function | No | - | Callback method. |

##### Returns

`Promise` - A promise of an object model.

<details>
<summary>Examples</summary>

```javascript
app.createGenericObject( {
  user: {
    qStringExpression: "=QVUser ()"
  },
  version : {
    qStringExpression: "=QlikViewVersion ()"
  },
  fields: {
    qValueExpression: "=Count (DISTINCT $Field)"
  }
}, function ( reply ) {
  var str = "Version:" + reply.version + " Fields:" + reply.fields;
  if ( reply.user ) {
    str += " User:" + reply.user;
  }
  $( "#info" ).html(str);
});
```

</details>

---

#### createList(qListObjectDef, callback?) `function`

Defines a Qlik list of field values and registers a callback to receive the data.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qListObjectDef` | object | Yes | - | List definition. |
| `callback` | function | No | - | Callback method. Parameter will contain a qListObject. |

##### Returns

`Promise` - A promise of an object model.

<details>
<summary>Examples</summary>

```javascript
app.createList({
  "qDef": {
    "qFieldDefs": [
      "LastName"
    ]
   },
   "qInitialDataFetch": [{
     qTop : 0,
     qLeft : 0,
     qHeight : 20,
     qWidth : 1
   }]
   }, function(reply) {
     var str = "";
     $.each(reply.qListObject.qDataPages[0].qMatrix, function(key, value) {
       str += '<li>' + value[0].qText + '</li>';
     });
     $('#list').html(str);
   });
```

</details>

---

#### createTable(dimensions, measures, options?) `function`

Defines a Qlik Hypercube and creates a table object wrapping the hypercube.

Introduced in Qlik Sense 2.1.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `dimensions` | string \| NxDimension[] | Yes | - | Dimensions to use. Should be a field name or a NxDimension structure for each entry. |
| `measures` | string \| NxMeasure[] | Yes | - | Measures to use. Should be an expression or a NxMeasure structure for each entry. |
| `options` | object | No | - | Options to set. |

##### Returns

[QTable](#qtable-class) - A table object of type QTable, which is initially empty but eventually will contain data. The table object will be updated when selection state changes.

<details>
<summary>Examples</summary>

```javascript
var users = app.createTable(["FirstName", "LastName"], ["Count(Case Id)"],{rows:200});
```

</details>

---

#### destroySessionObject(id) `function`

Destroys a Qlik Session object created with createGenericObject or any of
createCube, createList, or getList calls.

The object will be removed from engine, no more updates will be sent to the client
and all methods on the object will be invalid.

Introduced in Qlik Sense 1.1.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `id` | string | Yes | - | Session object ID. |

##### Returns

`Promise` - A promise of a Qlik engine reply.

<details>
<summary>Examples</summary>

```javascript
app.destroySessionObject( 'xcVtY');
app.destroySessionObject(reply.qInfo.qId);
```

</details>

---

#### doReload(qMode?, qPartial?, qDebug?) `function`

Reload the app.

Introduced in Qlik Sense 1.1

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qMode` | number | No | - | Error handling mode: 0 = default mode, 1 = attempt recovery on all errors, 2 = fail on all errors. |
| `qPartial` | boolean | No | - | Set to true for partial reload. |
| `qDebug` | boolean | No | - | Set to true if debug breakpoints are honored. Execution of the script will be in debug mode. |

##### Returns

`Promise` - A promise of a Qlik engine reply.

<details>
<summary>Examples</summary>

```javascript
app.doReload();
```

</details>

---

#### doSave(qFileName?) `function`

Save the app.

Introduced in Qlik Sense 1.1.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qFileName` | string | No | - | File name of the file to save. |

##### Returns

`Promise` - A promise of a Qlik engine reply.

<details>
<summary>Examples</summary>

```javascript
app.doReload().then(function(){
   app.doSave();
});
```

</details>

---

#### field(fld, statename?) `function`

Get a field reference with methods to manipulate field.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `fld` | string | Yes | - | Name of the field. |
| `statename` | string | No | "$" | Alternate state name. |

##### Returns

[QField](#qfield-class) - A QField object with methods and properties that can be used to manipulate the field.

---

#### forward() `function`

Forward

##### Returns

`Promise` - A promise of a Qlik engine reply.

<details>
<summary>Examples</summary>

```javascript
var app = qlik.openApp('2abac31e-3b46-4b78-8bxf-c5cea1d2514d');
app.forward();
```

</details>

---

#### getAppLayout(callback?) `function`

Get layout for this app and register a callback to receive the data.

Introduced in Qlik Sense 1.1.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `callback` | function | No | - | Callback method. |

##### Returns

`Promise` - A promise of a Qlik engine reply.

<details>
<summary>Examples</summary>

```javascript
app.getAppLayout(function(layout){
  console.log(layout.qTitle);
});
```

</details>

---

#### getAppObjectList(type?, callback?) `function`  _(deprecated)_

Get a list of Qlik application objects and register a callback to receive the data.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | string | No | "sheet" | Type of object. One of: sheet, MasterObject. |
| `callback` | function | No | - | Callback method. |

<details>
<summary>Examples</summary>

```javascript
app.getAppObjectList( 'sheet', function(reply){
  var str = "";
  $.each(reply.qAppObjectList.qItems, function(key, value) {
    str +=  value.qData.title + ' ';
    $.each(value.qData.cells, function(k,v){
      str +=  v.name + ' ';
    });
  });
  console.log(str);
});
```

</details>

---

#### getFullPropertyTree(id) `function`

Get properties for a Qlik object including children properties.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `id` | string | Yes | - | Object ID. |

##### Returns

`Promise` - A promise of an object model.

<details>
<summary>Examples</summary>

```javascript
app.getFullPropertyTree(value.qInfo.qId).then(function(model){
  console.log(model.propertyTree.qChildren.length + ' children');
});
```

</details>

---

#### getList(type, callback?) `function`

Get a list of internal Qlik objects and register a callback to receive the data.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | string | Yes | - | Type of object. One of: FieldList, MeasureList, DimensionList,   BookmarkList, SelectionObject, SnapshotList Since Qlik Sense 1.1,   MediaList Since Qlik Sense 1.1, sheet Since Qlik Sense 1.1, MasterObject Since Qlik Sense 1.1,   VariableList Since Qlik Sense 2.0, story Since Qlik Sense 2.1 |
| `callback` | function | No | - | Registers a callback that is executed every time data is returned. |

##### Returns

`Promise` - A promise of an object model.

<details>
<summary>Examples</summary>

```javascript
app.getList("FieldList", function(reply){
  var str = "";
  $.each(reply.qFieldList.qItems, function(key, value) {
    str +=  value.qName + ' ';
  });
 console.log(str);
});
```

</details>

---

#### getObject(elem?, id, options?) `function`

Inserts a Qlik object into an HTML element.
The object will fill the HTML object, so you can size and position
the element to determine how large the Qlik object will be.

If you only supply one parameter, you will just get the model without displaying the object.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `elem` | HTMLElement \| string | No | - | HTML element. Since version 1.1, it is also possible to define a string of the HTML element ID. |
| `id` | string | Yes | - | Object ID or 'CurrentSelections' if used for Selections bar. Since version November 2017 it is also possible to use 'AppNavigationBar' to on-demand app navigation bar. |
| `options` | object | No | - | Additional options. |

##### Returns

`Promise` - A promise of an object model.

<details>
<summary>Examples</summary>

```javascript
app.getObject(document.getElementById("LB01"), "uPyZavD");
```

```javascript
app.getObject("LB01","uPyZavD");
```

```javascript
app1.getObject('MyAppNavigationToolbarDIVid', 'AppNavigationBar', { sheetId: "RWcstb", openAppCallback: function ( appId, targetSheetId ) {
  console.log("Open generated app event handled.  App ID: " + appId + " target sheet to open by default: " + targetSheetId);
}});
```

</details>

---

#### getObjectProperties(id) `function`

Get properties for a Qlik object.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `id` | string | Yes | - | Object ID. |

##### Returns

`Promise` - A promise of an object model.

<details>
<summary>Examples</summary>

```javascript
app.getObjectProperties("uPyZavD").then(function(model){
  this.title = model.properties.title;
});
```

</details>

---

#### getScript() `function`

Gets the data load script of this app.

Introduced in Qlik Sense 4.0

##### Returns

`Promise` - A promise of a qScript object with the load script values.

<details>
<summary>Examples</summary>

```javascript
var app = qlik.openApp( "MY_APP_ID");
app.getScript().then( function(script){
  console.log(script);
});
```

</details>

---

#### getSnapshot(element?, id) `function`

Inserts a Qlik snapshot into an HTML element.
The snapshot will fill the HTML object, so you can size and position
the element to determine how large the Qlik object will be.

If you only supply one parameter you will just get the model without displaying the object.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `element` | HTMLElement \| string | No | - | HTML element or string with HTML element id. |
| `id` | string | Yes | - | Snapshot ID. |

##### Returns

`Promise` - A promise of an object model.

<details>
<summary>Examples</summary>

```javascript
app.getSnapshot(document.getElementById("SNAPSHOT"), "uPyZavD");
```

</details>

---

#### lockAll(state?) `function`

Lock all selections.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `state` | string | No | "$" | Alternate state name. Since Qlik Sense 2.1. |

##### Returns

`Promise` - A promise of a Qlik engine reply.

<details>
<summary>Examples</summary>

```javascript
var app = qlik.openApp('2abac31e-3b46-4b78-8bxf-c5cea1d2514d');
app.lockAll();
```

</details>

---

#### off(eventName?) `function`

Remove listener(s) for the app events.

Introduced in Qlik Sense February 2018.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `eventName` | string | No | - | Name of the event. Can be: error, warning, closed. If no eventName is provided, removes all listeners. |

<details>
<summary>Examples</summary>

```javascript
var app = qlik.openApp("MY_APP_ID");
app.on("error", function ( error ) {
  console.log("error listener called for app", error);
});
app.off("error");
```

</details>

---

#### on(eventName, callback) `function`

Add listener(s) to the app events. Possible events are error, warning and closed. Multiple listeners can be added to an event.

Introduced in Qlik Sense February 2018.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `eventName` | string | Yes | - | Name of the event. Can be: error, warning, closed. |
| `callback` | function | Yes | - | Callback method. |

<details>
<summary>Examples</summary>

```javascript
var app = qlik.openApp("MY_APP_ID");
app.on("error", function ( error ) {
  console.log("error listener called for app", error);
});
app.on("warning", function ( warning ) {
  console.log("warning listener called for app", warning);
});
app.on("closed", function ( closed ) {
  console.log("closed listener called for app", closed);
});
```

</details>

---

#### removeAlternateState(qStateName) `function`

Remove an alternate state.

Introduced in Qlik Sense 1.1.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qStateName` | string | Yes | - | Alternate state name |

##### Returns

`Promise` - A promise of a Qlik engine reply.

<details>
<summary>Examples</summary>

```javascript
app.removeAlternateState("X");
```

</details>

---

#### searchAssociations(qTerms, qPage, qOptions?, callback?) `function`  _(deprecated)_

Searches for one or more terms in the values of an app.

Introduce in Qlik Sense 1.1.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qTerms` | string[] | Yes | - | Terms to search for. |
| `qPage` | object | Yes | - |  |
| `qOptions` | object | No | - | Search options. |
| `callback` | function | No | - | Callback method. |

##### Returns

`Promise` - A promise of a Qlik engine reply.

<details>
<summary>Examples</summary>

```javascript
app.searchAssociations(["se"],
  {qOffset:0,qCount:15,qMaxNbrFieldMatches:5},
  {qContext: 'CurrentSelections'},
  function(reply){
    var str = "";
    reply.qResults.qFieldDictionaries.forEach(function(dic){
      dic.qResult.forEach(function(result){
        str += result.qText;
      });
    });
    console.log(str);
});
```

</details>

---

#### searchResults(qTerms, qPage, qOptions?, callback?) `function`

Searches for one or more terms in the values of an app.

Introduced in Qlik Sense 2.2.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qTerms` | string[] | Yes | - | Terms to search for. |
| `qPage` | object | Yes | - |  |
| `qOptions` | object | No | - | Search options. |
| `callback` | function | No | - | Callback method. |

##### Returns

`Promise` - A promise of a Qlik engine reply.

<details>
<summary>Examples</summary>

```javascript
app.searchResults( ["ma"],
  { qOffset: 0, qCount: 15},
  {qContext: 'CurrentSelections'},
  function ( reply ) {
    if ( reply.qResult.qTotalNumberOfGroups === 0 ) {
      console.log('No matches');
    } else {
      var str = "";
      reply.qResult.qSearchGroupArray.forEach( function ( value ) {
        value.qItems.forEach( function ( item ) {
          str += item.qIdentifier +": ";
          item.qItemMatches.forEach( function ( match ) {
            str += match.qText + ' ';
          });
        });
      });
      console.log(str);
    }
});
```

</details>

---

#### searchSuggest(qTerms, qOptions?, callback?) `function`

Returns search suggestions.

Introduced in Qlik Sense 1.1.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qTerms` | string[] | Yes | - | Terms to search for. |
| `qOptions` | object | No | - | Search options. |
| `callback` | function | No | - | Callback method. |

##### Returns

`Promise` - A promise of a Qlik engine reply.

<details>
<summary>Examples</summary>

```javascript
app.searchSuggest(["se"], {}, function(reply) {
  var str = "";
  reply.qResult.qSuggestions.forEach(function(sugg){
    str += sugg.qValue + ' ';
  });
  console.log(str);
});
```

</details>

---

#### selectAssociations(qMatchIx?, qTerms?, qOptions?, qSoftLock?) `function`

Make a selection based on searchAssociaton results.

Introduced in Qlik Sense 1.1.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qMatchIx` | number | No | - | Index to search result. |
| `qTerms` | string[] | No | - | Values to select. |
| `qOptions` | object | No | - | Parameter sent to the Qlik engine containing information about the search fields and the search context. |
| `qSoftLock` | boolean | No | - | Use the qOptions.qContext parameter instead. |

##### Returns

`Promise` - A promise of a Qlik engine reply.

<details>
<summary>Examples</summary>

```javascript
app.selectAssociations( 0, ["May","Mar"] );
```

</details>

---

#### selectionState(state?) `function`

Creates a SelectionState object that encapsulates the selection state.

Introduced in Qlik Sense 2.2.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `state` | string | No | "$" | Sets the state. |

##### Returns

[QSelectionState](#qselectionstate-class) - A selection state object for the selection state of type QSelectionState.

---

#### setScript(script) `function`

Sets the data load script of this app. Also validates the script syntax and returns the syntax errors if errors exist.

Introduced in Qlik Sense 4.0.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `script` | string | Yes | - | The script content. |

##### Returns

`Promise` - A promise of an empty object or a list of syntax errors depending on the validation result.

<details>
<summary>Examples</summary>

_Load script inline_

```javascript
var script = "Load Chr(RecNo()+Ord('A')-1) as Alpha, RecNo() as Num autogenerate 26;"
var app = qlik.openApp( "MY_APP_ID");
app.setScript(script).then( function(result){
	console.log(result);
});
```

_Load script from file_

```javascript
var script = 'LOAD Sales FROM [lib://data/sample.xlsx];';
var app = qlik.openApp( "MY_APP_ID");
app.setScript(script).then( function(result){
  console.log(result);
});
```

</details>

---

#### unlockAll(state?) `function`

Unlock all selections.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `state` | string | No | "$" | Alternate state name. Since Qlik Sense 2.1. |

##### Returns

`Promise` - A promise of a Qlik engine reply.

<details>
<summary>Examples</summary>

```javascript
var app = qlik.openApp('2abac31e-3b46-4b78-8bxf-c5cea1d2514d');
app.unlockAll();
```

</details>

---

### QAppTheme() `class`

---

#### get(id?) `function`

Get theme as a QTheme object.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `id` | string | No | - | Theme ID. If no ID is specified, the theme saved for the app is returned. |

##### Returns

Promise<[QTheme](#qtheme-class)> - A promise of a QTheme object.

<details>
<summary>Examples</summary>

```javascript
app.theme.get('my-theme-id').then(function(qtheme){
   console.log('Theme background color: ' + qtheme.properties.backgroundColor);
	});
```

</details>

---

#### getApplied() `function`

Get currently applied theme as a QTheme object.

##### Returns

Promise<[QTheme](#qtheme-class)> - A promise of a QTheme object.

<details>
<summary>Examples</summary>

```javascript
app.theme.getApplied().then(function(qtheme){
   console.log('Current theme background color: ' + qtheme.properties.backgroundColor);
	});
```

</details>

---

#### save(id) `function`

Save a theme ID of an app.

Introduced in Qlik Sense February 2018.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `id` | string | Yes | - | Theme ID. |

<details>
<summary>Examples</summary>

```javascript
app.theme.save('my-theme-id');
```

</details>

---

### QAppVisualization() `class`

---

#### create(type, cols?, options?) `function`

Create a new visualization. The visualization will be based on a session object and not persisted in the app.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | string | Yes | - | Visualization type. Built-in visualization like barchart, piechart, linechart, combochart or an extension. |
| `cols` | string \| NxDimension \| NxMeasure[] | No | - | Column definitions, dimensions and measures. Each entry can be a string, an NxDimension                      or NxMeasure structure. If the NxDimension or NxMeasure refers to a library dimension or measure,                      you also might need to add qType measure or dimension. |
| `options` | object | No | - | Options to set. Refer to documentation for the visualization used for additional options. |

##### Returns

Promise<[QVisualization](#qvisualizationqapp-model-class)> - A promise of a {@link QVisualization}.

<details>
<summary>Examples</summary>

```javascript
create a barchart on the fly
var app = qlik.openApp('c31e2aba-3b46-4b13-8b87-c5c2514dea1d');
app.visualization.create('barchart',["Case Owner Group","=Avg([Case Duration Time])"],{title:"Great on-the-fly barchart"}).then(function(bar){
  bar.show('QV04');
});
```

```javascript
create a table
app.visualization.create( 'table', ["Case Owner Group", "=Avg([Case Duration Time])", "Priority", "Quarter"] ).then( function ( table ) {
  table.show( 'QV04' );
});
```

```javascript
create a toolbar using an extension
app.visualization.create('com-qliktech-toolbar',null,
  {"buttons":{"clear":true,"back":true,"forward":true}}).then(function(vis){
    vis.show("QV05");
});
```

</details>

---

#### get(id) `function`

Get an existing visualization.

Introduced in Qlik Sense 2.2.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `id` | string | Yes | - | ID for an existing visualization. |

##### Returns

Promise<[QVisualization](#qvisualizationqapp-model-class)> - A promise of a {@link QVisualization}.

<details>
<summary>Examples</summary>

```javascript
var app = qlik.openApp('c31e2aba-3b46-4b13-8b87-c5c2514dea1d');
   app.visualization.get('xGhjKl').then(function(vis){
     vis.show("QV01");
   });
```

</details>

---

### QBookmark() `class`

---

#### apply(id) `function`

Apply bookmark.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `id` | string | Yes | - | Bookmark ID. |

##### Returns

`Promise` - A promise of a Qlik engine reply. Since Qlik Sense 1.2.

<details>
<summary>Examples</summary>

```javascript
var app = qlik.openApp("c31e2aba-3b46-4b13-8b87-c5c2514dea1d");
app.bookmark.apply("pPvpTN");
```

</details>

---

#### create(title, description, sheetId?) `function`

Create bookmark based on current selection.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `title` | string | Yes | - | Bookmark title. |
| `description` | string | Yes | - | Bookmark description. |
| `sheetId` | string | No | - | Bookmark sheet ID. Since Qlik Sense 2.2. |

##### Returns

`Promise` - A promise of a Qlik engine reply. Since Qlik Sense 1.2.

<details>
<summary>Examples</summary>

```javascript
var app = qlik.openApp("c31e2aba-3b46-4b13-8b87-c5c2514dea1d");
app.bookmark.create("Test","Test bookmark","fmcJkH");
```

</details>

---

#### remove(id) `function`

Remove bookmark.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `id` | string | Yes | - | Bookmark ID. |

##### Returns

`Promise` - A promise of a Qlik engine reply. Since Qlik Sense 1.2.

<details>
<summary>Examples</summary>

```javascript
var app = qlik.openApp("c31e2aba-3b46-4b13-8b87-c5c2514dea1d");
app.bookmark.remove("pPvpTN");
```

</details>

---

### QDimensionCell() `class`

Wrapper around a HyperCube dimension cell.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qText` | string | Yes | - | Cell value formatted as set up in properties. |
| `qElemNumber` | number | Yes | - | Cell value index. |
| `qState` | string | Yes | - | Cell state. |
| `qNum` | number | No | - | Cell numeric value, if cell is numeric. |

---

#### select() `function`

Select the value contained in this cell.

<details>
<summary>Examples</summary>

```javascript
<div class="selectable" ng-class="{'selected':cell.selected}" ng-click="cell.select($event)">{{cell.qText}}</div>
```

</details>

---

### QField() `class`

External interface to the fields in a Qlik Sense app and contains methods for field level commands.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `OnData` | [Notification](#notification-class) | Yes | - | OnData notification |
| `qStateCounts` | object | Yes | - | Object with number of values in different states. Only after getData() call.  Introduced in Qlik Sense 2.1. |
| `rowCount` | number | Yes | - | Number of different values. Only after getData() call.  Introduced in Qlik Sense 2.1. |
| `rows` | [QFieldValue](#qfieldvalue-class)[] | Yes | - | Field values. You need to call getData() method to make this available. Since Qlik Sense 2.1. |

---

#### clear() `function`

Clears a field selection.

##### Returns

`Promise` - A promise of an engine response.

<details>
<summary>Examples</summary>

```javascript
var app = qlik.openApp('c31e2aba-3b46-4b13-8b87-c5c2514dea1d');
app.field('LastName').clear();
```

</details>

---

#### clearOther(softlock?) `function`

Clears all field selections except this one.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `softlock` | boolean | No | - | If true, locked selections can be overridden. |

##### Returns

`Promise` - A promise of an engine response.

<details>
<summary>Examples</summary>

```javascript
var app = qlik.openApp('c31e2aba-3b46-4b13-8b87-c5c2514dea1d');
app.field('LastName').clearOther(true);
```

</details>

---

#### getData(options?) `function`

Gets field data.
The values are available as QFieldValue in array field.rows and is updated when the selection state changes.
Notification OnData will be triggered after each update.

Introduced in Qlik Sense 2.1

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `options` | object | No | - | Object containing options for the getData call. |

##### Returns

[QField](#qfield-class) - The field object.

<details>
<summary>Examples</summary>

```javascript
var app = qlik.openApp("c31e2aba-3b46-4b13-8b87-c5c2514dea1d");
$scope.months = app.field("Month").getData();

<button ng-repeat="row in months.rows" class="btn" ng-click="row.select();"
  ng-class="{'btn-success':row.qState === 'S'}">{{row.qText}}</button>
```

</details>

---

#### getMoreData() `function`

Get more data for your field.
Notification OnData will be triggered when complete.

Introduced in Qlik Sense 2.1

##### Returns

[QField](#qfield-class) - The field object

<details>
<summary>Examples</summary>

```javascript
<button ng-if="fieldMonth.rowCount>fieldMonth.rows.length" ng-click="fieldMonth.getMoreData()">More</button>
```

</details>

---

#### lock() `function`

Locks a field selection.

##### Returns

`Promise` - A promise of an engine response.

<details>
<summary>Examples</summary>

```javascript
var app = qlik.openApp('c31e2aba-3b46-4b13-8b87-c5c2514dea1d');
app.field('LastName').lock();
```

</details>

---

#### select(Array, toggle?, softlock?) `function`

Select field values using indexes.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `Array` | any[] | Yes | - | of indexes to values to select. |
| `toggle` | boolean | No | - | If true, toggle selected state. |
| `softlock` | boolean | No | - | If true, locked selections can be overridden. |

##### Returns

`Promise` - A promise of an engine response.

<details>
<summary>Examples</summary>

```javascript
var app = qlik.openApp('c31e2aba-3b46-4b13-8b87-c5c2514dea1d');
app.field('LastName').select([0, 1, 2], true, true);
```

</details>

---

#### selectAll(softlock?) `function`

Select all values in field.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `softlock` | boolean | No | - | If true, locked selections can be overridden. |

##### Returns

`Promise` - A promise of an engine response.

<details>
<summary>Examples</summary>

```javascript
var app = qlik.openApp('c31e2aba-3b46-4b13-8b87-c5c2514dea1d');
app.field('LastName').selectAll();
```

</details>

---

#### selectAlternative(softlock?) `function`

Select alternative values in field.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `softlock` | boolean | No | - | If true, locked selections can be overridden. |

##### Returns

`Promise` - A promise of an engine response.

<details>
<summary>Examples</summary>

```javascript
var app = qlik.openApp('c31e2aba-3b46-4b13-8b87-c5c2514dea1d');
app.field('LastName').selectAlternative();
```

</details>

---

#### selectExcluded(softlock?) `function`

Select excluded values in field.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `softlock` | boolean | No | - | If true, locked selections can be overridden. |

##### Returns

`Promise` - A promise of an engine response.

<details>
<summary>Examples</summary>

```javascript
var app = qlik.openApp('c31e2aba-3b46-4b13-8b87-c5c2514dea1d');
app.field('LastName').selectExcluded();
```

</details>

---

#### selectMatch(match, softlock?) `function`

Select matching field values.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `match` | string | Yes | - | Match string. |
| `softlock` | boolean | No | - | If true, locked selections can be overridden. |

##### Returns

`Promise` - A promise of an engine response.

<details>
<summary>Examples</summary>

```javascript
var app = qlik.openApp('c31e2aba-3b46-4b13-8b87-c5c2514dea1d');
app.field('LastName').selectMatch('A', true);
```

</details>

---

#### selectPossible(softlock?) `function`

Select possible values in field.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `softlock` | boolean | No | - | If true, locked selections can be overridden. |

##### Returns

`Promise` - A promise of an engine response.

<details>
<summary>Examples</summary>

```javascript
var app = qlik.openApp('c31e2aba-3b46-4b13-8b87-c5c2514dea1d');
app.field('LastName').selectPossible();
```

</details>

---

#### selectValues(values, toggle?, softlock?) `function`

Select field values.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `values` | object[] | Yes | - | Array of qFieldValues to select. Since 1.1, a simplified syntax with strings OR numbers also works. Note that for a numeric field, you need to provide the numeric value. |
| `toggle` | boolean | No | - | If true, toggle selected state. If false replace the current selection. |
| `softlock` | boolean | No | - | If true, locked selections can be overridden. |

##### Returns

`Promise` - A promise of an engine response.

<details>
<summary>Examples</summary>

```javascript
app.field("Month").selectValues([5], true, true);
app.field(fld).selectValues(["Wetterberg"], true, true);
```

</details>

---

#### toggleSelect(match, softlock?) `function`

Toggle field selection.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `match` | string | Yes | - | Match string. |
| `softlock` | boolean | No | - | If true, locked selections can be overridden. |

##### Returns

`Promise` - A promise of an engine response.

<details>
<summary>Examples</summary>

```javascript
var app = qlik.openApp('c31e2aba-3b46-4b13-8b87-c5c2514dea1d');
app.field('LastName').toggleSelect('A', true);
```

</details>

---

#### unlock() `function`

Unlocks a field selection.

##### Returns

`Promise` - A promise of an engine response.

<details>
<summary>Examples</summary>

```javascript
var app = qlik.openApp('c31e2aba-3b46-4b13-8b87-c5c2514dea1d');
app.field('LastName').unlock();
```

</details>

---

### QFieldSelections() `class`

Selection state for a field.

Introduced in Qlik Sense 2.2.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `fieldName` | string | Yes | - | The field name. |
| `qSortIndex` | number | Yes | - | Sort index, starting from 0. |
| `field` | [QField](#qfield-class) | Yes | - | Reference to the field. |
| `locked` | boolean | Yes | - | Is field locked? |
| `isNumeric` | boolean | Yes | - | Is field numeric? |
| `totalCount` | number | Yes | - | Total number of values in field. |
| `selectedCount` | number | Yes | - | Number of selected values. |
| `qSelectionThreshold` | number | Yes | - | Number of values that will be listed. |
| `qStateCounts` | object | Yes | - | Object with number of values in different states. |
| `qSelected` | string | Yes | - | Concatenated string of selected values if # of values are less than the threshold or string of format "7 of 123". |
| `selectedValues` | number[] | Yes | - | Array with a maximum of qSelectionThreshold values that are selected. For each value the text plus the selection mode (NORMAL/AND/NOT). |
| `notSelectedValues` | number[] | Yes | - | Array with a maximum of qSelectionThreshold values that are not selected. For each value the text plus the selection mode (NORMAL/AND/NOT). |

---

### QFieldValue() `class`

Field value for a Qlik Field.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qText` | string | Yes | - | Cell value formatted as set up in properties. |
| `qElemNumber` | number | Yes | - | Cell value index. |
| `qState` | string | Yes | - | Cell state. |
| `qNum` | number | No | - | Cell numeric value, if cell is numeric. |
| `qFrequency` | string | No | - | Frequency, if calculated by engine. |

---

#### select(toggle?, softlock?) `function`

Select field value.

Introduced in Qlik Sense 2.1.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `toggle` | boolean | No | - | If true, toggle selected state. |
| `softlock` | boolean | No | - | If true, locked selections can be overridden. |

##### Returns

`Promise` - A promise.

<details>
<summary>Examples</summary>

```javascript
var app = qlik.openApp('c31e2aba-3b46-4b13-8b87-c5c2514dea1d');
var field = app.field('LastName');
field.getData();
//after data is loaded fieldvalues will be in rows array
field.rows[0].select();
```

</details>

---

### QGlobal() `class`

---

#### cancelReload() `function`

Cancel reload.

##### Returns

`Promise` - A promise of a Qlik engine reply.

<details>
<summary>Examples</summary>

```javascript
var global = qlik.getGlobal(config);
global.cancelReload();
```

</details>

---

#### getAppList(callback) `function`

Get app list.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `callback` | function | Yes | - | callback method. |

<details>
<summary>Examples</summary>

```javascript
qlik.getGlobal(config).getAppList(function(list){
  var str = "";
  $.each(list, function(key, value) {
    str +=  value.qDocName + '('+ value.qDocId + ')';
  });
  console.log(str);
});
```

</details>

---

#### getAuthenticatedUser(callback?) `function`

Retrieves information about the authenticated user.
Note: This method is only applicable to Qlik Sense Enterprise on Windows. For Qlik Sense Enterprise SaaS, use {@link https://qlik.dev/apis/rest/users#%23%2Fentries%2Fusers%2Fme-get|User API}

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `callback` | function | No | - | callback method. |

##### Returns

`Promise` - A promise of a Qlik engine reply.

<details>
<summary>Examples</summary>

```javascript
var global = qlik.getGlobal(config);
global.getAuthenticatedUser(function(reply){
  console.log('User:'+reply.qReturn);
});
```

</details>

---

#### getProductVersion(callback?) `function`  _(deprecated)_

Get Product Version.

Introduced in Qlik Sense 1.2.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `callback` | function | No | - | callback method. |

##### Returns

`Promise` - A promise of a Qlik engine reply.

<details>
<summary>Examples</summary>

```javascript
var global = qlik.getGlobal(config);
global.getProductVersion(function(reply){
  console.log('Product Version:'+reply.qReturn);
});
```

</details>

---

#### getProgress(qRequestId, callback?) `function`

Get Progress.

Introduced in Qlik Sense 2.1.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qRequestId` | number | Yes | - | RequestId from doReload call or 0. Complete information is returned if the identifier of the request is specified. If qRequestId = 0, less information is returned. |
| `callback` | function | No | - | callback method. |

##### Returns

`Promise` - A promise of a Qlik engine reply.

<details>
<summary>Examples</summary>

```javascript
var global = qlik.getGlobal(config);
global.getProgress();
```

</details>

---

#### getQTProduct(callback?) `function`

Get QT Product.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `callback` | function | No | - | callback method. |

##### Returns

`Promise` - A promise of a Qlik engine reply.

<details>
<summary>Examples</summary>

```javascript
var global = qlik.getGlobal(config);
global.getQTProduct(function(reply){
  console.log('QT Product:'+reply.qReturn);
});
```

</details>

---

#### isPersonalMode(callback?) `function`

Get isPersonalMode.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `callback` | function | No | - | callback method. |

##### Returns

`Promise` - A promise of a Qlik engine reply.

<details>
<summary>Examples</summary>

```javascript
var global = qlik.getGlobal(config);
global.isPersonalMode(function(reply){
  console.log('Personal mode:'+reply.qReturn);
});
```

</details>

---

#### off(eventName?) `function`

Remove listener(s) for the global events.

Introduced in Qlik Sense February 2018.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `eventName` | string | No | - | Name of the event. Can be: error, warning, closed. Removes all listeners if no eventName is provided. |

<details>
<summary>Examples</summary>

```javascript
var global = qlik.getGlobal(config);
global.on("error", function (error) {
  console.log("error listener called for global", error);
});
global.off("error");
```

</details>

---

#### on(eventName, callback) `function`

Adds listeners to the global events. Possible events are error, warning, and closed. Multiple listeners can be added to an event.

Introduced in Qlik Sense February 2018

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `eventName` | string | Yes | - | Name of the event. Can be: error, warning, closed. |
| `callback` | function | Yes | - | Callback method. |

<details>
<summary>Examples</summary>

```javascript
var global = qlik.getGlobal(config);
global.on("error", function (error) {
  console.log("error listener called for global", error);
});
global.on("warning", function (warning) {
  console.log("warning listener called for global", warning);
});
global.on("closed", function (closed) {
  console.log("closed listener called for global", closed);
});
```

</details>

---

### QGlobalTheme() `class`

---

#### apply(id) `function`

Apply a theme to all visualizations on the web page.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `id` | string | Yes | - | ID of theme to apply. |

##### Returns

`Promise<boolean>` - Promise of a boolean to indicate success or not.

<details>
<summary>Examples</summary>

```javascript
qlik.theme.apply('my-theme-id').then(function(result){
  console.log('theme applied with result: ' + result);
});
```

</details>

---

#### get(id) `function`

Get theme as a QTheme object.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `id` | string | Yes | - | Theme id |

##### Returns

Promise<[QTheme](#qtheme-class)> - A promise of a QTheme object.

<details>
<summary>Examples</summary>

```javascript
qlik.theme.get('my-theme-id').then(function(qtheme){
  console.log('Theme background color: ' + qtheme.properties.backgroundColor);
});
```

</details>

---

### QHeader() `class`

Wrapper around a HyperCube header cell.

Introduced in Qlik Sense 2.1.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qFallbackTitle` | string | Yes | - | Column title. |
| `qSortIndicator` | string | Yes | - | A: ascending, D:Descending |
| `isOrderedBy` | boolean | Yes | - | Is this the first column for sort? |
| `qReverseSort` | boolean | Yes | - | Is sort order currently reversed for this column? |
| `col` | number | Yes | - | Column number. |
| `qCardinal` | number | No | - | Number of different values. Only for dimensions. |
| `qStateCounts` | object | No | - | Object with number of values in different states. Only for dimensions. |
| `field` | [QField](#qfield-class) | No | - | Field object with methods to manipulate the underlying field. Only used for dimensions. |
| `qMin` | number | No | - | Minimum value. Only for measures. |
| `qMax` | number | No | - | Maximum value. Only for measures. |
| `errorCode` | number | No | - | Error code for this column. Only if column has an error. Since Qlik Sense 2.2. |
| `errorMessage` | string | No | - | Error message for this column. Only if column has an error. Since Qlik Sense 2.2. |

<details>
<summary>Examples</summary>

```javascript
<th ng-repeat="head in data.headers" class="header" ng-click="head.orderBy()">
  {{head.qFallbackTitle}}
       <i ng-if="head.isOrderedBy" ng-click="head.reverseOrder()"
           ng-class="{ 'icon-triangle-top': head.qSortIndicator === 'A',
			'icon-triangle-bottom': head.qSortIndicator === 'D'}">
       </i>
</th>
```

</details>

---

#### orderBy() `function`

Set this column to be the first in the sort order.

---

#### reverseOrder() `function`

Reverse the sorting order for the column.

---

#### selectRange(min, max, inclMin?, inclMax?) `function`

Select a range in this measure.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `min` | number | Yes | - | Sets the minimum value of the range. |
| `max` | number | Yes | - | Sets the maximum value of the range. |
| `inclMin` | boolean | No | - | Set to true to include minimum value. |
| `inclMax` | boolean | No | - | Set to true to include maximum value. |

##### Returns

`Promise`

<details>
<summary>Examples</summary>

```javascript
this.table.headers[1].selectRange( this.minval, this.maxval );
```

</details>

---

### QMeasureCell() `class`

Wrapper around a HyperCube measure cell.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qText` | string | Yes | - | Cell value formatted as set up in properties. |
| `qNum` | number | No | - | Cell numeric value, if cell is numeric. |

---

#### getPercent() `function`

Get the value of this cell as percent of total. Note that this might be more than 100% if this is an average.

<details>
<summary>Examples</summary>

```javascript
<div class="bar" style="width:{{row.measures[0].getPercent()}}%">
```

</details>

---

#### getPercentOfMax() `function`

Get the value of this cell as percent of maximum.

<details>
<summary>Examples</summary>

```javascript
<div class="bar" style="width:{{row.measures[0].getPercentOfMax()}}%">
```

</details>

---

### QNavigation() `class`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `ANALYSIS` | string | Yes | - | Used for analysis mode. |
| `EDIT` | string | Yes | - | Used for edit mode. |

---

#### getCurrentSheetId() `function`

Get current sheet ID.

##### Returns

[QNavigationSheetResult](#qnavigationsheetresult-object) - The result of the navigation

<details>
<summary>Examples</summary>

```javascript
var result = qlik.navigation.getCurrentSheetId();
console.log('sheet id: ' + result.sheetId);
```

</details>

---

#### getMode() `function`

Get current mode.

##### Returns

`string` - mode The current mode.

<details>
<summary>Examples</summary>

```javascript
var mode = qlik.navigation.getMode();
console.log('mode: ' + mode);
```

</details>

---

#### gotoSheet(sheetId) `function`

Navigates to a given sheet in the current app.
Note that the method will return before the actual navigation takes place.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `sheetId` | string | Yes | - | The ID of the sheet to navigate to. |

##### Returns

[QNavigationSheetResult](#qnavigationsheetresult-object) - The result of the navigation operation.

<details>
<summary>Examples</summary>

```javascript
var navigationResult = qlik.navigation.gotoSheet('xYgfJ');
```

</details>

---

#### gotoStory(storyId) `function`

Navigates to a given story in the current app.
Note that the method will return before the actual navigation takes place.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `storyId` | string | Yes | - | The ID of the story to navigate to. |

##### Returns

[QNavigationStoryResult](#qnavigationstoryresult-object) - The result of the navigation operation.

<details>
<summary>Examples</summary>

```javascript
var navigationResult = qlik.navigation.gotoStory('xYgfJ');
```

</details>

---

#### isModeAllowed(mode) `function`

Checks if a given mode is allowed.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `mode` | string | Yes | - | The mode to check availability of. Can be either {@link QNavigaton#EDIT} or {@link QNavigaton#ANALYSIS}. |

##### Returns

`boolean` - If the mode is allowed or not.

<details>
<summary>Examples</summary>

```javascript
if (qlik.navigation.isModeAllowed(QNavigation#EDIT)) {
  //enable edit button
};
```

</details>

---

#### nextSheet() `function`

Navigates to the next sheet in the current app. It will do nothing if you do not have sheets in the current context.
Note that the method will return before the actual navigation takes place.

##### Returns

[QNavigationSheetResult](#qnavigationsheetresult-object) - The result of the navigation operation.

<details>
<summary>Examples</summary>

```javascript
var navigationResult = qlik.navigation.nextSheet();
```

</details>

---

#### prevSheet() `function`

Navigates to the previous sheet in the current app. It will do nothing if you do not have sheets in the current context.
Note that the method will return before the actual navigation takes place.

##### Returns

[QNavigationSheetResult](#qnavigationsheetresult-object) - The result of the navigation operation.

<details>
<summary>Examples</summary>

```javascript
var navigationResult = qlik.navigation.prevSheet();
```

</details>

---

#### setMode(mode) `function`

Set current mode.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `mode` | string | Yes | - | The mode to change to. Can be either {@link QNavigation#EDIT} or {@link QNavigation#ANALYSIS}. |

##### Returns

[QNavigationModeResult](#qnavigationmoderesult-object) - The result of the mode change.

<details>
<summary>Examples</summary>

```javascript
var result = qlik.navigation.setMode(QNavigation#EDIT);
console.log('mode: ' + result.mode);
```

</details>

---

### QNavigationModeResult `object`

Return value from mode related navigation methods.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `success` | boolean | Yes | - | true if the operation was successful. |
| `mode` | string | No | - | The new mode. Can be either {@link QNavigation#EDIT} or {@link QNavigation#ANALYSIS}. |
| `error` | string | No | - | The error code if an error occurred, for example, MODENOTALLOWED. |
| `errorMsg` | string | No | - | The error message, for example, 'Mode not allowed'. |

---

### QNavigationSheetResult `object`

Return value from sheet navigation methods.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `success` | boolean | Yes | - | true if the navigation was successful. |
| `sheetId` | string | No | - | The new sheet ID. |
| `error` | string | No | - | The error code if an error occurred, for example, NOSUCHSHEET or NOCURRENTSHEET. |
| `errorMsg` | string | No | - | The error message, for example, 'No current sheet'. |

---

### QNavigationStoryResult `object`

Return value from story navigation methods.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `success` | boolean | Yes | - | true if the navigation was successful. |
| `storyId` | string | No | - | The new story ID. |
| `error` | string | No | - | The error code if an error occurred, for example, NOSUCHSTORY. |
| `errorMsg` | string | No | - | The error message, for example, 'No such story'. |

---

### QRow() `class`

Wrapper around a HyperCube data row.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `dimensions` | [QDimensionCell](#qdimensioncell-class)[] | Yes | - | Dimension cells. |
| `measures` | [QMeasureCell](#qmeasurecell-class)[] | Yes | - | Measure cells. |
| `cells` | any[] | Yes | - | All cells, in the order defined in properties. |

<details>
<summary>Examples</summary>

```javascript
<div ng-repeat="row in data.rows" class="row"  title="{{row.dimensions[0].qText}}"
   data-value="{{ row.dimensions[0].qElemNumber }}">
   <div class="bar" style="width:{{row.measures[0].getPercent()}}%">
       <span>{{row.dimensions[0].qText}}</span>
   </div>
   <div class="per">
       <span class="{{row.measures[0].getPercent()>95 ? 'over':'' }}">{{row.measures[0].qText}}</span>
   </div>
</div>
```

</details>

---

### QSelectionState() `class`

The SelectionState API allows developers to work with selection state data returned from the Qlik engine without having deeper
knowledge of internal constructs.

Notification is sent when data is available. Notification will be triggered after each update. To receive
notification, bind a listener on <i>'OnData'</i> of QSelectionState instance.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `stateName` | string | Yes | - | State name, '$' for default state. |
| `selections` | [QFieldSelections](#qfieldselections-class)[] | Yes | - | Selections |
| `backCount` | number | Yes | - | Number of back steps available. |
| `forwardCount` | number | Yes | - | Number of forward steps available. |
| `OnData` | [Notification](#notification-class) | Yes | - | OnData notification. |

<details>
<summary>Examples</summary>

```javascript
// create an object
const selState = app.selectionState();

const listener = function() {
  console.log('Back count:' + selState.backCount);
  selState.OnData.unbind( listener );  //unregister the listener when no longer notification is needed.
};
selState.OnData.bind( listener ); //bind the listener
```

```javascript
Example based on using AngularJS.

Your main script:

$scope.selState = app.selectionState();

In your AngularJS template:
<button type="button" class="btn btn-default btn-xs" ng-click="selState.clearAll()" aria-label="Clear">
  <span class="glyphicon glyphicon-remove" aria-hidden="true"></span>
</button>

<li ng-repeat="sel in selState.selections">{{sel.fieldName}}: {{sel.qSelected}}
  <button type="button" class="btn btn-default btn-xs" ng-click="sel.field.clear()" aria-label="Lock">
    <span class="glyphicon glyphicon-remove" aria-hidden="true"></span>
  </button>
</li>
```

</details>

---

#### clearAll(lockedAlso?) `function`

Clear all selections in this state.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `lockedAlso` | boolean | No | - | Clear locked fields also. |

##### Returns

`Promise` - A promise of a Qlik engine reply.

<details>
<summary>Examples</summary>

```javascript
var app = qlik.openApp('c31e2aba-3b46-4b13-8b87-c5c2514dea1d');
var selState = app.selectionState();
selState.clearAll(true);
```

</details>

---

#### lockAll() `function`

Lock all selections in this state.

##### Returns

`Promise` - A promise of a Qlik engine reply.

<details>
<summary>Examples</summary>

```javascript
var app = qlik.openApp('c31e2aba-3b46-4b13-8b87-c5c2514dea1d');
var selState = app.selectionState();
selState.lockAll();
```

</details>

---

#### unlockAll() `function`

Unlock all selections in this state.

##### Returns

`Promise` - A promise of a Qlik engine reply

<details>
<summary>Examples</summary>

```javascript
var app = qlik.openApp('c31e2aba-3b46-4b13-8b87-c5c2514dea1d');
var selState = app.selectionState();
selState.unlockAll();
```

</details>

---

### QTable() `class`

The Table API allow developers to work with tabular data returned from the Qlik engine without having deeper
knowledge of internal constructs like, for example, a hypercube.
From a technical perspective it is a wrapper around HyperCube data from engine.

Notification is sent when data is available. Notification will be triggered after each update. To receive
notification bind a listener on <i>'OnData'</i> of QTable instance.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `rows` | [QRow](#qrow-class)[] | Yes | - | Data rows. |
| `headers` | [QHeader](#qheader-class)[] | Yes | - | Header information. |
| `totals` | [QMeasureCell](#qmeasurecell-class)[] | Yes | - | Total information for measures. |
| `rowCount` | number | Yes | - | Total number of rows for the qHyperCube, including rows not fetched from server. |
| `colCount` | number | Yes | - | Total number of columns for the qHyperCube. |

<details>
<summary>Examples</summary>

```javascript
// Initialization using the hypercube of the current visualization
var table = qlik.table( this );

var listener = function() {
  var rowCount = table.rowCount;
  var colCount = table.colCount;
  table.OnData.unbind( listener );  //unregister the listener when no longer notification is needed.
};
table.OnData.bind( listener ); //bind the listener
```

```javascript
// Example based on using AngularJS.

// Your main script:

if ( !this.$scope.table ) {
  this.$scope.table = qlik.table( this );
}

// In your AngularJS template:

<tr ng-repeat="row in table.rows">
   <td ng-repeat="cell in row.cells"> {{cell.qText}} </td>
</tr>
```

</details>

---

#### exportData(options?, callback?) `function`

Export data of the underlying hyperCube in OOXML or CSV format.

Note: The entire hyperCube will be exported, not just the current data-page. On Cloud this functionality will go through the Reports API, which limits the available options

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `options` | object | No | - |  |
| `callback` | function | No | - | Callback function returning the link to the exported file. |

<details>
<summary>Examples</summary>

```javascript
var qTable = qlik.table(this);

var $exportButton = $( document.createElement('button'));
$exportButton.html('Export');
$exportButton.bind('click', function (  ) {
			qTable.exportData({download: true});
		});
$element.append($exportButton);
```

```javascript
// Example using AngularJS in a Qlik Sense visualization extension:

// Main script:
...
paint: function ( ) {
		//setup scope.table
		if ( !this.$scope.table ) {
			this.$scope.table = qlik.table( this );
		}
	}
...

// In your template:
<button ng-click="table.exportData({download:true})">Create Excel file</button>
```

</details>

---

#### getColByName(fld) `function`

Get column number for a given field name.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `fld` | string | Yes | - | Field name. |

##### Returns

`number` - Column number, starting with zero. Undefined if no column with that name.

<details>
<summary>Examples</summary>

```javascript
var table = qlik.table( this );
var colNumber = table.getColByName('Closed cases');
```

</details>

---

#### getMoreData() `function`

Get more data for your qHyperCube.

<details>
<summary>Examples</summary>

```javascript
// Example based on using AngularJS in a Qlik Sense visualization extension.

// Main extension script file:
...
paint: function ( ) {
		//setup scope.data
		if ( !this.$scope.data ) {
			this.$scope.data = qlik.table( this );
		}
	}
...

// AngularJS template:
<button ng-if="data.rowcount>data.rows.length" ng-click="data.getMoreData()">More</button>
```

</details>

---

### QTheme() `class`

Wrapper for a theme with helper methods.

Introduced in Qlik Sense February 2018.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `id` | string | Yes | - | Theme id |
| `properties` | object | Yes | - | Theme properties tree structure with calculated styling values. 								   Functions, variables, and inheritance have been computed from the original theme JSON file. |

---

#### apply() `function`

Apply theme to all visualizations on the web page.

##### Returns

`Promise<boolean>` - Promise of a boolean to indicate success or not.

<details>
<summary>Examples</summary>

```javascript
qlik.theme.get('my-theme-id').then(function(qtheme){
  qtheme.apply().then(function(result){
    console.log('theme applied with result: ' + result);
  });
});
```

</details>

---

#### getStyle(basePath, path, attribute) `function`

Get the value of a style attribute in the theme by searching in the theme's JSON structure.
The search starts at the specified base path and continues upwards until the value is found.
If possible, it will get the attribute's value using the given path.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `basePath` | string | Yes | - | Base path in the theme's json structure to start the search in (specified as a name path separated by dots). |
| `path` | string | Yes | - | Expected path for the attribute (specified as a name path separated by dots). |
| `attribute` | string | Yes | - | Name of the style attribute. |

##### Returns

`string` - The style value.

<details>
<summary>Examples</summary>

```javascript
qlik.theme.get('my-theme-id').then(function(qtheme){
  console.log('Object title font size: ' + qtheme.getStyle('object', 'title.main', 'fontSize'));
});
```

</details>

---

### QVariable(app, qapp) `class`

Creates an instance of the Variable API.

---

#### create() `function`

Create variable.

##### Returns

`Promise` - Promise of a Variable model.

<details>
<summary>Examples</summary>

```javascript
var app = qlik.openApp('c31e2aba-3b46-4b13-8b87-c5c2514dea1d');
app.variable.create('myvar').then(function(model){
  // do something with myvar
});
```

</details>

---

#### createSessionVariable(qProp) `function`

Create session variable, which is a temporary variable that is not persisted and needs to be recreated for each new session.

Introduced in Qlik Sense 2.1.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qProp` | object | Yes | - | Variable properties. |

##### Returns

`Promise` - Promise of a Variable model.

<details>
<summary>Examples</summary>

```javascript
var app = qlik.openApp('c31e2aba-3b46-4b13-8b87-c5c2514dea1d');
app.variable.createSessionVariable({qName : 'myvar', qDefinition: 'Month'}).then(function(model){
  // do something with myvar
});
```

</details>

---

#### get(qId) `function`

Get a variable by ID.

Introduced in Qlik Sense 2.1.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qId` | string | Yes | - | Variable ID. |

##### Returns

`Promise` - Promise of a Variable model.

<details>
<summary>Examples</summary>

```javascript
var app = qlik.openApp('c31e2aba-3b46-4b13-8b87-c5c2514dea1d');
app.variable.get('yTgsRI').then(function(model){
  // do something with myvar
});
```

</details>

---

#### getByName(qName) `function`

Get a variable by name.

Introduced in Qlik Sense 2.1.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qName` | string | Yes | - | Variable name. |

##### Returns

`Promise` - A promise of a Variable model.

<details>
<summary>Examples</summary>

```javascript
var app = qlik.openApp('c31e2aba-3b46-4b13-8b87-c5c2514dea1d');
app.variable.getByName('myvar').then(function(model){
  // do something with myvar
});
```

</details>

---

#### getContent(name, callback) `function`

Get variable content.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `name` | string | Yes | - | Variable name. |
| `callback` | [getContentCallback](#getcontentcallbackdata-qapp-function) | Yes | - | Callback to receive the content. |

##### Returns

`Promise` - A promise of a Qlik engine reply.

<details>
<summary>Examples</summary>

```javascript
var app = qlik.openApp('c31e2aba-3b46-4b13-8b87-c5c2514dea1d');
app.variable.getContent('myvar',function ( reply ) {
  console.log( JSON.stringify( reply ) );
});
```

</details>

---

#### setContent(name, content) `function`  _(deprecated)_

Set variable content.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `name` | string | Yes | - | Variable name. |
| `content` | string | Yes | - | Variable content. |

##### Returns

`Promise` - A promise of a Qlik engine reply.

<details>
<summary>Examples</summary>

```javascript
var app = qlik.openApp('c31e2aba-3b46-4b13-8b87-c5c2514dea1d');
app.variable.setContent('myvar','=(1+1)');
```

</details>

---

#### setNumValue(qName, qVal) `function`

Set variable numeric value.

Introduced in Qlik Sense 2.1.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qName` | string | Yes | - | Variable name. |
| `qVal` | number | Yes | - | Variable value. |

##### Returns

`Promise` - A promise of a Qlik engine reply.

<details>
<summary>Examples</summary>

```javascript
var app = qlik.openApp('c31e2aba-3b46-4b13-8b87-c5c2514dea1d');
app.variable.setNumValue('myvar',5);
```

</details>

---

#### setStringValue(qName, qVal) `function`

Set variable string value.

Introduced in Qlik Sense 2.1.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qName` | string | Yes | - | Variable name. |
| `qVal` | string | Yes | - | Variable value. |

##### Returns

`Promise` - A promise of a Qlik engine reply.

<details>
<summary>Examples</summary>

```javascript
var app = qlik.openApp('c31e2aba-3b46-4b13-8b87-c5c2514dea1d');
app.variable.setStringValue('myvar','=(1+1)');
```

</details>

---

### QVisualization(qapp, model) `class`

The Visualization API allows developers to get visualizations defined in an app and to
create temporary visualizations on the fly.

Introduced in Qlik Sense 2.2.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `table` | [QTable](#qtable-class) | Yes | - | Table object for this visualization. Only for visualizations built on a hypercube. |

---

#### close() `function`

Close visualization.

##### Returns

`Promise`

---

#### exportData(options) `function`

Export data of the underlying hyperCube in OOXML or CSV format.
Note: The entire hyperCube will be exported, not just the current data-page.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `options` | object | Yes | - |  |

##### Returns

`any` - Promise<string> - A promise of the file location URL.

<details>
<summary>Examples</summary>

```javascript
var app = qlik.openApp('c31e2aba-3b46-4b13-8b87-c5c2514dea1d');
app.visualization.get('xGhjKl').then(function(vis){
  vis.exportData({format:'CSV_T', state: 'A'}).then(function (link) {
    window.open(link);
  });
});
```

</details>

---

#### exportImg(settings) `function`

Exports a QVisualization instance to an image.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `settings` | object | Yes | - | Image export settings. |

##### Returns

`any` - Promise<string> - A promise of a link to the exported file.

<details>
<summary>Examples</summary>

```javascript
var element = document.getElementById('QV01');
var settings = { imageType: 'png', height: element.offsetHeight, width: element.offsetWidth }

var app = qlik.openApp('c31e2aba-3b46-4b13-8b87-c5c2514dea1d');
app.visualization.get('xGhjKl').then(function(vis){
  vis.exportImg(settings).then(function (result) {
    console.log('Image download link: ', result);
  });
});
```

</details>

---

#### exportPdf(settings) `function`

Exports a QVisualization instance to PDF.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `settings` | object | Yes | - | PDF export settings. |

##### Returns

`any` - Promise<string> - A promise of a link to the exported file.

<details>
<summary>Examples</summary>

```javascript
var settings = {
  documentSize: "a4",
  aspectRatio: 2,
  orientation: "landscape"
};
var app = qlik.openApp('c31e2aba-3b46-4b13-8b87-c5c2514dea1d');
app.visualization.get('xGhjKl').then(function(vis){
  vis.exportPdf(settings).then(function (result) {
    console.log('PDF download link: ', result);
  });
});
```

</details>

---

#### resize() `function`

Inform the visualization it has been resized and should repaint.

---

#### setOptions(options) `function`

Set visualization options.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `options` | object | Yes | - | Options to set. Refer to visualization.create for documentation. |

##### Returns

`Promise` - A promise of the RPC call's response.

<details>
<summary>Examples</summary>

```javascript
var app = qlik.openApp('c31e2aba-3b46-4b13-8b87-c5c2514dea1d');
app.visualization.get('xGhjKl').then(function(vis){
  vis.setOptions({title:"Now improved"});
});
```

</details>

---

#### show(element?, options?) `function`

Show visualization in HTML element.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `element` | HTMLElement \| string | No | - | HTML element or HTML element ID. |
| `options` | object | No | - | Options to set. Since Qlik Sense 3.0. |

##### Returns

`object` - Scope of the visualization.

<details>
<summary>Examples</summary>

```javascript
var app = qlik.openApp('c31e2aba-3b46-4b13-8b87-c5c2514dea1d');
app.visualization.get('xGhjKl').then(function(vis){
  vis.show("QV01");
});
```

</details>

---

#### toggleDataView() `function`

Toggles data view.

Creates a DataView object if it doesn't already exist and toggles data view.

Introduced in Qlik Sense June 2018.

Disclaimer:
The element that is provided as a parameter to the QVisualization.show method must have
CSS property position set to relative and must not have any padding. If these rules are
not followed, the visualization object may not calculate its width and height correctly
and you may not be able to scroll and navigate after toggling data view.

Proposed action:
Wrap the element with another element. The wrapper can then be styled without any limitations.

<details>
<summary>Examples</summary>

```javascript
var app = qlik.openApp('c31e2aba-3b46-4b13-8b87-c5c2514dea1d');
app.visualization.get('xGhjKl').then(function(vis){
  vis.show("QV01");
  vis.toggleDataView().then(function(toggled){
    if(toggled){
      this.getElementsByClassName('qv-st')[0].focus();
    }
  }
});
```

</details>

---

### getContentCallback(data, qapp) `function`

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `data` | object | Yes | - | Content of the variable. |
| `qapp` | object | Yes | - | The qlik.app object wrapping the app. |

---
