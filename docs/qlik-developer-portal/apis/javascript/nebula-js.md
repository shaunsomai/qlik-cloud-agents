---
source: https://qlik.dev/apis/javascript/nebula-js/
last_updated: 2026-08-25T10:14:37+01:00
---

# nebula.js: stardust

`Version: 7.4.0` | _stable_

Product and framework agnostic integration API for Qlik's Associative Engine, commonly used with enigma.js. Consider using the qlik-embed toolkit for an easier embedding experience, whilst building on the same core technologies.

## Table of Contents

### Entries

- [embed](#embedapp-instanceconfig-function)
- [useState](#usestateinitialstate-function)
- [useEffect](#useeffecteffect-deps-function)
- [useMemo](#usememofactory-deps-function)
- [useRef](#userefinitialvalue-function)
- [usePromise](#usepromisefactory-deps-function)
- [useElement](#useelement-function)
- [useRect](#userect-function)
- [useLayout](#uselayout-function)
- [useStaleLayout](#usestalelayout-function)
- [useAppLayout](#useapplayout-function)
- [useModel](#usemodel-function)
- [useApp](#useapp-function)
- [useGlobal](#useglobal-function)
- [useSelections](#useselections-function)
- [useTheme](#usetheme-function)
- [useEmbed](#useembed-function)
- [useTranslator](#usetranslator-function)
- [useDeviceType](#usedevicetype-function)
- [useNavigation](#usenavigation-function-experimental)
- [usePlugins](#useplugins-function)
- [useAction](#useactionfactory-deps-function)
- [useConstraints](#useconstraints-function-deprecated)
- [useInteractionState](#useinteractionstate-function)
- [useOptions](#useoptions-function)
- [useImperativeHandle](#useimperativehandlefactory-deps-function)
- [onTakeSnapshot](#ontakesnapshotsnapshotcallback-function)
- [useRenderState](#userenderstate-function)
- [useEmitter](#useemitter-function)
- [useKeyboard](#usekeyboard-function)
- [Conversion](#conversion-namespace)
- [EnigmaMocker](#enigmamocker-namespace)

### Definitions

- [Translator](#translator-class)
- [Component](#component-interface)
- [LoadFallback](#loadfallbackundefined-function)
- [Configuration](#configuration-interface)
- [Context](#context-interface)
- [Galaxy](#galaxy-interface)
- [Embed](#embed-class)
- [Direction](#direction-union)
- [ListLayout](#listlayout-union)
- [FrequencyMode](#frequencymode-union)
- [SearchMode](#searchmode-union)
- [ToolbarMode](#toolbarmode-union)
- [FieldEventTypes](#fieldeventtypes-union)
- [FieldInstance](#fieldinstance-class)
- [ThemeJSON](#themejson-alias)
- [ThemeInfo](#themeinfo-interface)
- [QInfo](#qinfo-interface)
- [Sheet](#sheet-class-experimental)
- [Viz](#viz-class)
- [ActionToolbarElement](#actiontoolbarelement-interface)
- [ActionElement](#actionelement-interface)
- [CellElement](#cellelement-interface)
- [CellBody](#cellbody-interface)
- [CellFooter](#cellfooter-interface)
- [CellTitle](#celltitle-interface)
- [CellSubTitle](#cellsubtitle-interface)
- [SheetElement](#sheetelement-interface-experimental)
- [VizElementAttributes](#vizelementattributes-interface)
- [VizElement](#vizelement-interface)
- [Flags](#flags-interface)
- [AppSelections](#appselections-class)
- [ObjectSelections](#objectselections-class)
- [Field](#field-union)
- [CreateConfig](#createconfig-interface)
- [RenderConfig](#renderconfig-interface)
- [LibraryField](#libraryfield-interface)
- [Plugin](#plugin-interface-experimental)
- [LoadType](#loadtype-interface)
- [TypeInfo](#typeinfo-interface)
- [RenderError](#rendererrormessage-originalerror-class)
- [Navigation](#navigation-class-experimental)
- [Visualization](#visualization-interface)
- [VisualizationDefinition](#visualizationdefinition-interface)
- [SetStateFn](#setstatefn-interface)
- [EffectCallback](#effectcallback-function)
- [Ref](#ref-interface)
- [Rect](#rect-interface)
- [ActionDefinition](#actiondefinition-interface)
- [Constraints](#constraints-interface-deprecated)
- [Interactions](#interactions-interface)
- [RenderState](#renderstate-interface)
- [Emitter](#emitter-class)
- [Keyboard](#keyboard-interface)
- [importProperties](#importpropertiesargs-function)
- [exportProperties](#exportpropertiesargs-function)
- [onPropertyChange](#onpropertychangeproperties-function)
- [QAEProperties](#qaeproperties-interface)
- [QAEDefinition](#qaedefinition-interface)
- [DataTarget](#datatarget-interface)
- [fieldTargetAddedCallback](#fieldtargetaddedcallbackfield-properties-function)
- [fieldTargetRemovedCallback](#fieldtargetremovedcallbackfield-properties-index-function)
- [FieldTarget](#fieldtarget-interface)
- [Theme](#theme-class)
- [move](#movearray-oldindex-newindex-function)
- [ExportFormat](#exportformat-interface)
- [ExportDataDef](#exportdatadef-interface)
- [ConversionType](#conversiontype-interface)
- [hyperCubeConversion](#hypercubeconversion-interface)
- [EnigmaMockerOptions](#enigmamockeroptions-interface-experimental)
- [ScalePalette](#scalepalette-interface)
- [DataPalette](#datapalette-interface)
- [ColorPickerPalette](#colorpickerpalette-interface)
- [DataColorSpecials](#datacolorspecials-interface)

## Entries

### embed(app, instanceConfig?) `function`

Initiates a new `Embed` instance using the specified enigma `app`.

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `app` | qix.Doc | Yes | - |  |
| `instanceConfig` | [Configuration](#configuration-interface) | No | - |  |

#### Returns

[Embed](#embed-class)

<details>
<summary>Examples</summary>

```javascript
import { embed } from '@nebula.js/stardust'
const n = embed(app);
n.render({ id: 'abc' });
```

</details>

---

#### createConfiguration(configuration) `function`

Creates a new `embed` scope bound to the specified `configuration`.

The configuration is merged with all previous scopes.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `configuration` | [Configuration](#configuration-interface) | Yes | - | The configuration object |

##### Returns

[embed](#embedapp-instanceconfig-function)

<details>
<summary>Examples</summary>

```javascript
import { embed } from '@nebula.js/stardust';
// create a 'master' config which registers all types
const m = embed.createConfiguration({
  types: [{
    name: 'mekko',
    version: '1.0.0',
    load: () => Promise.resolve(mekko)
  }],
});

// create an alternate config with dark theme
// and inherit the config from the previous
const d = m.createConfiguration({
 context: {
   theme: 'dark'
 }
});

m(app).render({ type: 'mekko' }); // will render the object with default theme
d(app).render({ type: 'mekko' }); // will render the object with 'dark' theme
embed(app).render({ type: 'mekko' }); // will throw error since 'mekko' is not a register type on the default instance
```

</details>

---

### useState(initialState) `function`

Creates a stateful value.

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `initialState` | S \| function | Yes | - | The initial state. |

#### Returns

(S, [SetStateFn](#setstatefn-interface)<S>)[] - The value and a function to update it.

<details>
<summary>Examples</summary>

```javascript
import { useState } from '@nebula.js/stardust';
// ...
// initiate with simple primitive value
const [zoomed, setZoomed] = useState(false);

// update
setZoomed(true);

// lazy initiation
const [value, setValue] = useState(() => heavy());
```

</details>

---

### useEffect(effect, deps?) `function`

Triggers a callback function when a dependent value changes.

Omitting the dependency array will have the hook run on each update
and an empty dependency array runs only once.

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `effect` | [EffectCallback](#effectcallback-function) | Yes | - | The callback. |
| `deps` | any[] | No | - | The dependencies that should trigger the callback. |

<details>
<summary>Examples</summary>

```javascript
import { useEffect } from '@nebula.js/stardust';
// ...
useEffect(() => {
  console.log('mounted');
  return () => {
    console.log('unmounted');
  };
}, []);

useEffect(() => {
  const clickHandler = () => { console.log('click') };
  const button = element.querySelector('.button');
  button.addEventListener('click', clickHandler);
  return () => {
    button.removeEventListener('click', clickHandler);
  };
}, []);
```

</details>

---

### useMemo(factory, deps) `function`

Creates a stateful value when a dependent changes.

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `factory` | function | Yes | - | The factory function. |
| `deps` | any[] | Yes | - | The dependencies. |

#### Returns

`T` - The value returned from the factory function.

<details>
<summary>Examples</summary>

```javascript
import { useMemo } from '@nebula.js/stardust';
// ...
const v = useMemo(() => {
  return doSomeHeavyCalculation();
}), []);
```

</details>

---

### useRef(initialValue) `function`

Creates a reference to a value not needed for rendering

While Nebula does not have a virtual DOM, it is still useful
to have a reference to an object that is retained across
renders and in it self does not trigger a render.

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `initialValue` | R | Yes | - | The initial value. |

#### Returns

[Ref](#ref-interface)<R> - An object with the current value

<details>
<summary>Examples</summary>

```javascript
import { useRef } from '@nebula.js/stardust';
// ...
// initiate with simple value
const timesRendered = useRef(0);

useEffect(() => {
 render(layout);
 // increments the render counter, a useState would trigger another render
 timesRendered.current += 1;
},[layout]);
```

</details>

---

### usePromise(factory, deps?) `function`

Runs a callback function when a dependent changes.

Useful for async operations that otherwise cause no side effects.
Do not add for example listeners withing the callback as there is no teardown function.

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `factory` | function | Yes | - | The factory function that calls the promise. |
| `deps` | any[] | No | - | The dependencies. |

#### Returns

`(P, Error)[]` - The resolved value or rejected error

<details>
<summary>Examples</summary>

```javascript
import { usePromise } from '@nebula.js/stardust';
import { useModel } from '@nebula.js/stardust';
// ...
const model = useModel();
const [resolved, rejected] = usePromise(() => model.getLayout(), [model]);
```

</details>

---

### useElement() `function`

Gets the HTMLElement this visualization is rendered into.

#### Returns

`HTMLElement`

<details>
<summary>Examples</summary>

```javascript
import { useElement } from '@nebula.js/stardust';
// ...
const el = useElement();
el.innerHTML = 'Hello!';
```

</details>

---

### useRect() `function`

Gets the size of the HTMLElement the visualization is rendered into.

#### Returns

[Rect](#rect-interface) - The size of the element.

<details>
<summary>Examples</summary>

```javascript
import { useRect } from '@nebula.js/stardust';
// ...
const rect = useRect();
useEffect(() => {
  console.log('resize');
}, [rect.width, rect.height])
```

</details>

---

### useLayout() `function`

Gets the layout of the generic object associated with this visualization.

#### Returns

`qix.GenericObjectLayout`

<details>
<summary>Examples</summary>

```javascript
import { useLayout } from '@nebula.js/stardust';
// ...
const layout = useLayout();
console.log(layout);
```

</details>

---

### useStaleLayout() `function`

Gets the layout of the generic object associated with this visualization.

Unlike the regular layout, a _stale_ layout is not changed when a generic object enters
the modal state. This is mostly notable in that `qSelectionInfo.qInSelections` in the layout is
always `false`.
The returned value from `useStaleLayout()` and `useLayout()` are identical when the object
is not in a modal state.

#### Returns

`qix.GenericObjectLayout`

<details>
<summary>Examples</summary>

```javascript
import { useStaleLayout } from '@nebula.js/stardust';
// ...
const staleLayout = useStaleLayout();
console.log(staleLayout);
```

</details>

---

### useAppLayout() `function`

Gets the layout of the app associated with this visualization.

#### Returns

`qix.NxAppLayout` - The app layout

<details>
<summary>Examples</summary>

```javascript
import { useAppLayout } from '@nebula.js/stardust';
// ...
const appLayout = useAppLayout();
console.log(appLayout.qLocaleInfo);
```

</details>

---

### useModel() `function`

Gets the generic object API of the generic object connected to this visualization.

#### Returns

`qix.GenericObject | undefined`

<details>
<summary>Examples</summary>

```javascript
import { useModel } from '@nebula.js/stardust';
// ...
const model = useModel();
useEffect(() => {
  model.getInfo().then(info => {
    console.log(info);
  })
}, []);
```

</details>

---

### useApp() `function`

Gets the doc API.

#### Returns

`qix.Doc | undefined` - The doc API.

<details>
<summary>Examples</summary>

```javascript
import { useApp } from '@nebula.js/stardust';
// ...
const app = useApp();
useEffect(() => {
  app.getAllInfos().then(infos => {
    console.log(infos);
  })
}, []);
```

</details>

---

### useGlobal() `function`

Gets the global API.

#### Returns

`qix.Global | undefined` - The global API.

<details>
<summary>Examples</summary>

```javascript
import { useGlobal } from '@nebula.js/stardust';

// ...
const g = useGlobal();
useEffect(() => {
  g.engineVersion().then(version => {
    console.log(version);
  })
}, []);
```

</details>

---

### useSelections() `function`

Gets the object selections.

#### Returns

[ObjectSelections](#objectselections-class) - The object selections.

<details>
<summary>Examples</summary>

```javascript
import { useSelections } from '@nebula.js/stardust';
import { useElement } from '@nebula.js/stardust';
import { useEffect } from '@nebula.js/stardust';
// ...
const selections = useSelections();
const element = useElement();
useEffect(() => {
  const onClick = () => {
    selections.begin('/qHyperCubeDef');
  };
  element.addEventListener('click', onClick);
  return () => {
    element.removeEventListener('click', onClick);
  };
}, []);
```

</details>

---

### useTheme() `function`

Gets the theme.

#### Returns

[Theme](#theme-class) - The theme.

<details>
<summary>Examples</summary>

```javascript
import { useTheme } from '@nebula.js/stardust';

const theme = useTheme();
console.log(theme.getContrastingColorTo('#ff0000'));
```

</details>

---

### useEmbed() `function`

Available since: 1.7.0

Gets the embed instance used.

#### Returns

[Embed](#embed-class) - The embed instance used.

<details>
<summary>Examples</summary>

```javascript
import { useEmbed } from '@nebula.js/stardust';

const embed = useEmbed();
embed.render(...)
```

</details>

---

### useTranslator() `function`

Gets the translator.

#### Returns

[Translator](#translator-class) - The translator.

<details>
<summary>Examples</summary>

```javascript
import { useTranslator } from '@nebula.js/stardust';
// ...
const translator = useTranslator();
console.log(translator.get('SomeString'));
```

</details>

---

### useDeviceType() `function`

Gets the device type. ('touch' or 'desktop')

#### Returns

`string` - device type.

<details>
<summary>Examples</summary>

```javascript
import { useDeviceType } from '@nebula.js/stardust';
// ...
const deviceType = useDeviceType();
if (deviceType === 'touch') { ... };
```

</details>

---

### useNavigation() `function`  **[experimental]**

Available since: 5.4.0

Gets the navigation api to control sheet navigation. When useNavigation is used in Sense, it returns Sense.navigation.

#### Returns

[Navigation](#navigation-class-experimental) - navigation api.

<details>
<summary>Examples</summary>

```javascript
import { useNavigation } from "@nebula.js/stardust";
// ...
const navigation = useNavigation();
const [activeSheetId, setActiveSheetId] = useState(navigation?.getCurrentSheetId() || "");
```

</details>

---

### usePlugins() `function`

Gets the array of plugins provided when rendering the visualization.

#### Returns

[Plugin](#plugin-interface-experimental)[] - array of plugins.

<details>
<summary>Examples</summary>

```javascript
// provide plugins that can be used when rendering
embed(app).render({
  element,
  type: 'my-chart',
  plugins: [plugin]
});
```

```javascript
// It's up to the chart implementation to make use of plugins in any way
import { usePlugins } from '@nebula.js/stardust';
// ...
const plugins = usePlugins();
plugins.forEach((plugin) => {
  // Invoke plugin
  plugin.fn();
});
```

</details>

---

### useAction(factory, deps?) `function`

Registers a custom action.

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `factory` | function | Yes | - |  |
| `deps` | any[] | No | - |  |

#### Returns

`A`

<details>
<summary>Examples</summary>

```javascript
import { useAction } from '@nebula.js/stardust';
// ...
const [zoomed, setZoomed] = useState(false);
const act = useAction(() => ({
  hidden: false,
  disabled: zoomed,
  action() {
    setZoomed(prev => !prev);
  },
  icon: {}
}), [zoomed]);
```

</details>

---

### useConstraints() `function`  _(deprecated)_

Gets the desired constraints that should be applied when rendering the visualization.

The constraints are set on the embed configuration before the visualization is rendered
and should be respected when implementing the visualization.

#### Returns

[Constraints](#constraints-interface-deprecated)

<details>
<summary>Examples</summary>

```javascript
// configure embed to disallow active interactions when rendering
embed(app, {
 context: {
   constraints: {
     active: true, // do not allow interactions
   }
 }
}).render({ element, id: 'sdfsdf' });
```

```javascript
import { useConstraints } from '@nebula.js/stardust';
// ...
const constraints = useConstraints();
useEffect(() => {
  if (constraints.active) {
    // do not add any event listener if active constraint is set
    return undefined;
  }
  const listener = () => {};
  element.addEventListener('click', listener);
  return () => {
    element.removeEventListener('click', listener);
  };
}, [constraints])
```

</details>

---

### useInteractionState() `function`

Gets the desired interaction states that should be applied when rendering the visualization.

The interactions are set on the embed configuration before the visualization is rendered
and should be respected when implementing the visualization.

#### Returns

[Interactions](#interactions-interface)

<details>
<summary>Examples</summary>

```javascript
// configure embed to disallow active interactions when rendering
embed(app, {
 context: {
   interactions: {
     active: false, // do not allow interactions
   }
 }
}).render({ element, id: 'sdfsdf' });
```

```javascript
import { useInteractionState } from '@nebula.js/stardust';
// ...
const interactions = useInteractionState();
useEffect(() => {
  if (!interactions.active) {
    // do not add any event listener if active constraint is set
    return undefined;
  }
  const listener = () => {};
  element.addEventListener('click', listener);
  return () => {
    element.removeEventListener('click', listener);
  };
}, [interactions])
```

</details>

---

### useOptions() `function`

Gets the options object provided when rendering the visualization.

This is an empty object by default but enables customization of the visualization through this object.
Options are different from setting properties on the generic object in that options
are only temporary settings applied to the visualization when rendered.

You have the responsibility to provide documentation of the options you support, if any.

#### Returns

`object`

<details>
<summary>Examples</summary>

```javascript
// when embedding the visualization, anything can be set in options
embed(app).render({
  element,
  type: 'my-chart',
  options: {
    showNavigation: true,
  }
});
```

```javascript
// it is up to you use and implement the provided options
import { useOptions } from '@nebula.js/stardust';
import { useEffect } from '@nebula.js/stardust';
// ...
const options = useOptions();
useEffect(() => {
  if (!options.showNavigation) {
    // hide navigation
  } else {
    // show navigation
  }
}, [options.showNavigation]);
```

</details>

---

### useImperativeHandle(factory, deps?) `function`

This is an empty object by default, but enables you to provide a custom API of your visualization to
make it possible to control after it has been rendered.

You can only use this hook once, calling it more than once is considered an error.

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `factory` | function | Yes | - |  |
| `deps` | any[] | No | - |  |

<details>
<summary>Examples</summary>

```javascript
import { useImperativeHandle } form '@nebula.js/stardust';
// ...
useImperativeHandle(() => ({
  resetZoom() {
    setZoomed(false);
  }
}));
```

```javascript
// when embedding the visualization, you can get a handle to this API
// and use it to control the visualization
const ctl = await embed(app).render({
  element,
  type: 'my-chart',
});
ctl.getImperativeHandle().resetZoom();
```

</details>

---

### onTakeSnapshot(snapshotCallback) `function`

Registers a callback that is called when a snapshot is taken.

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `snapshotCallback` | function | Yes | - |  |

<details>
<summary>Examples</summary>

```javascript
import { onTakeSnapshot } from '@nebula.js/stardust';
import { useState } from '@nebula.js/stardust';
import { useLayout } from '@nebula.js/stardust';

const layout = useLayout();
const [zoomed] = useState(layout.isZoomed || false);

onTakeSnapshot((copyOfLayout) => {
  copyOfLayout.isZoomed = zoomed;
  return Promise.resolve(copyOfLayout);
});
```

</details>

---

### useRenderState() `function`

Gets render state instance.

Used to update properties and get a new layout without triggering onInitialRender.

#### Returns

[RenderState](#renderstate-interface) - The render state.

<details>
<summary>Examples</summary>

```javascript
import { useRenderState } from '@nebula.js/stardust';

const renderState = useRenderState();
useState(() => {
  if(needPropertiesUpdate(...)) {
     useRenderState.pending();
     updateProperties(...);
  } else {
     useRenderState.restore();
     ...
  }
}, [...]);
```

</details>

---

### useEmitter() `function`

Gets an event emitter instance for the visualization.

#### Returns

[Emitter](#emitter-class)

<details>
<summary>Examples</summary>

```javascript
// In a Nebula visualization
import { useEmitter } from '@nebula.js/stardust';
useEffect(()=> {
  // on some trigger
  emitter.emit("trigger", params)
}, [...])

// In a mashup
const viz = await n.render({
  element: el,
  id: 'abcdef'
});
viz.addListener("trigger", ()=> {
  // do something
})
```

</details>

---

### useKeyboard() `function`

Gets the desired keyboard settings and status to applied when rendering the visualization.
A visualization should in general only have tab stops if either `keyboard.enabled` is false or if active is true.
This means that either Nebula isn't configured to handle keyboard input or the chart is currently focused.
Enabling or disabling keyboardNavigation are set on the embed configuration and
should be respected by the visualization.

#### Returns

[Keyboard](#keyboard-interface)

<details>
<summary>Examples</summary>

```javascript
// configure nebula to enable navigation between charts
embed(app, {
  context: {
    keyboardNavigation: true, // tell Nebula to handle navigation
  }
}).render({ element, id: 'sdfsdf' });
```

```javascript
import { useKeyboard } from '@nebula.js/stardust';
// ...
const keyboard = useKeyboard();
useEffect(() => {
 // Set a tab stop on our button if in focus or if Nebulas navigation is disabled
 button.setAttribute('tabIndex', keyboard.active || !keyboard.enabled ? 0 : -1);
 // If navigation is enabled and focus has shifted, lets focus the button
 keyboard.enabled && keyboard.active && button.focus();
}, [keyboard])
```

</details>

---

### Conversion `namespace`

Available since: 1.1.0

Provides conversion functionality to extensions.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `hypercube` | [hyperCubeConversion](#hypercubeconversion-interface) | Yes | - | Provides conversion functionality to extensions with hyperCubes. |

<details>
<summary>Examples</summary>

```javascript
import { conversion } from '@nebula.js/stardust';

export default function() {
  return {
    qae: {
      ...
      importProperties: ( exportFormat, initialProperties ) =>  conversion.hyperCube.importProperties(exportFormat, initialProperties),
      exportProperties: ( fullPropertyTree ) => conversion.hyperCube.exportProperties(fullPropertyTree)
    },
    ...
  };
}
```

</details>

---

### EnigmaMocker `namespace`

Mocks Engima app functionality for demo and testing purposes.

---

#### fromGenericObjects(genericObjects, options?) `function`  **[experimental]**

Available since: 3.0.0

Mocks Engima app functionality. It accepts one / many generic objects as input argument and returns the mocked Enigma app. Each generic object represents one visualisation and specifies how it behaves. For example, what layout to use the data to present.

The generic object is represented with a Javascript object with a number of properties. The name of the property correlates to the name in the Enigma model for `app.getObject(id)`. For example, the property `getLayout` in the generic object is used to define `app.getObject(id).getLayout()`. Any property can be added to the fixture (just make sure it exists and behaves as in the Enigma model!).

The value for each property is either fixed (string / boolean / number / object) or a function. Arguments are forwarded to the function to allow for greater flexibility. For example, this can be used to return different hypercube data when scrolling in the chart.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `genericObjects` | object[] | Yes | - | Generic objects controlling behaviour of visualizations. |
| `options` | [EnigmaMockerOptions](#enigmamockeroptions-interface-experimental) | No | - | Options |

##### Returns

`Promise<qix.Doc>`

<details>
<summary>Examples</summary>

```javascript
const genericObject = {
  getLayout() {
    return {
      qInfo: {
        qId: 'qqj4zx',
        qType: 'sn-grid-chart'
      },
      ...
    }
  },
  getHyperCubeData(path, page) {
    return [ ... ];
  }
};
const app = await EnigmaMocker.fromGenericObjects([genericObject]);
```

</details>

---

## Definitions

### Translator() `class`

---

#### language(lang?) `function`

Returns current locale.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `lang` | string | No | - | language Locale to updated the currentLocale value |

##### Returns

`string` - current locale.

---

#### add(item) `function`

Registers a string in multiple locales

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `item` | object | Yes | - |  |

<details>
<summary>Examples</summary>

```javascript
translator.add({
  id: 'company.hello_user',
  locale: {
    'en-US': 'Hello {0}',
    'sv-SE': 'Hej {0}'
  }
});
translator.get('company.hello_user', ['John']); // Hello John
```

</details>

---

#### get(str, args?) `function`

Translates a string for current locale.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `str` | string | Yes | - | ID of the registered string. |
| `args` | string[] | No | - | Values passed down for string interpolation. |

##### Returns

`string` - The translated string.

---

### Component `interface`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `key` | string | Yes | - | The key of the component. Currently supporting components "theme" and "selections". |

<details>
<summary>Examples</summary>

```javascript
const n = embed(app);
const inst = await n.field('field_name');
inst.mount(document.querySelector('.listbox'), {
  components: [{
   key: 'theme',
   header: {
     fontColor: { color: '#f00' },
     fontSize: 23,
   },
   content: {
     fontSize: 16,
     useContrastColor: false,
   }
  },{
   key: 'selections',
   colors: {
     selected: { color: '#0f0' },
     alternative: { color: '#ededed' },
     excluded: { color: '#ccc' },
     selectedExcluded: { color: '#bbb' },
     possible: { color: '#fefefe' },
     possible: { color: '#fefefe' },
   }
 }]
});
```

</details>

---

### LoadFallback(undefined) `function`

Fallback load function for missing types

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
|  | [LoadType](#loadtype-interface) | Yes | - |  |

#### Returns

Promise<[Visualization](#visualization-interface)>

---

### Configuration `interface`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `load` | [LoadFallback](#loadfallbackundefined-function) | No | - | Fallback load function for missing types |
| `context` | [Context](#context-interface) | No | - | Settings for the rendering instance |
| `types` | [TypeInfo](#typeinfo-interface)[] | No | - | Visualization types to register |
| `themes` | [ThemeInfo](#themeinfo-interface)[] | No | - | Themes to register |
| `hostConfig` | object | No | - | Qlik api compatible host config, see https://github.com/qlik-oss/qlik-api-ts/blob/main/docs/authentication.md#the-host-config |
| `anything` | object | No | - |  |

<details>
<summary>Examples</summary>

```javascript
import { embed } from '@nebula.js/stardust'
n = embed(app, {
  context: {
    keyboardNavigation: true,
    theme: 'purple',
  },
  load: ({ name, version }) => {
    if (name === 'linechart') {
      return Promise.resolve(line);
    }
  },
  types: [
    {
      name: 'bar',
      load: () => Promise.resolve(bar),
    },
  ],
  themes: [
    {
      id: 'purple',
      load: () => Promise.resolve(purpleThemeJson),
    },
  ],
});
```

</details>

---

### Context `interface`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `theme` | string | No | "light" |  |
| `language` | string | No | "en-US" |  |
| `deviceType` | string | No | "auto" |  |
| `constraints` | [Constraints](#constraints-interface-deprecated) | No | - | _(deprecated)_ |
| `interactions` | [Interactions](#interactions-interface) | No | - |  |
| `keyboardNavigation` | boolean | No | false |  |
| `disableCellPadding` | boolean | No | false |  |
| `dataViewType` | string | No | "sn-table" | Type used for toggling to the data view (toggleDataView) This type need to be registered as well |
| `navigation` | [Navigation](#navigation-class-experimental) | No | - |  |

---

### Galaxy `interface`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `translator` | [Translator](#translator-class) | Yes | - |  |
| `theme` | [Theme](#theme-class) | Yes | - |  |
| `flags` | [Flags](#flags-interface) | Yes | - |  |
| `deviceType` | string | Yes | - |  |
| `hostConfig` | object | Yes | - |  |
| `anything` | object | Yes | - |  |

---

### Embed() `class`

---

#### render(cfg) `function`

Renders a visualization or sheet into an HTMLElement.
Visualizations can either be existing objects or created on the fly.
Support for sense sheets is experimental.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `cfg` | [RenderConfig](#renderconfig-interface) | Yes | - | The render configuration. |

##### Returns

Promise<[Viz](#viz-class) | [Sheet](#sheet-class-experimental)> - A controller to the rendered visualization or sheet.

<details>
<summary>Examples</summary>

```javascript
// render from existing object
n.render({
  element: el,
  id: 'abcdef'
});
```

```javascript
// render on the fly
n.render({
  element: el,
  type: 'barchart',
  fields: ['Product', { qLibraryId: 'u378hn', type: 'measure' }]
});
```

```javascript
// with AbortSignal
const controller = new AbortController();
n.render({
  element: el,
  type: 'barchart',
  fields: ['Product', '=Sum(Sales)'],
  signal: controller.signal
});
// Later: cancel the render
controller.abort();
```

</details>

---

#### create(cfg) `function`

Creates a visualization model

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `cfg` | [CreateConfig](#createconfig-interface) | Yes | - | The create configuration. |

##### Returns

`Promise<qix.GenericObject>` - An engima model

<details>
<summary>Examples</summary>

```javascript
// create a barchart in the app and return the model
const model = await n.create({
    type: 'barchart',
    fields: ['Product', { qLibraryId: 'u378hn', type: 'measure' }],
    properties: { showTitle: true }
  }
);
```

</details>

---

#### generateProperties(cfg) `function`

Generates properties for a visualization object

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `cfg` | [CreateConfig](#createconfig-interface) | Yes | - | The create configuration. |

##### Returns

`Promise<object>` - The objects properties

<details>
<summary>Examples</summary>

```javascript
// generate properties for a barchart
const properties = await n.generateProperties({
    type: 'barchart',
    fields: ['Product', { qLibraryId: 'u378hn', type: 'measure' }],
    properties: { showTitle: true }
  },
);
```

</details>

---

#### context(ctx) `function`

Updates the current context of this embed instance.
Use this when you want to change some part of the current context, like theme.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `ctx` | [Context](#context-interface) | Yes | - | The context to update. |

##### Returns

`Promise<undefined>`

<details>
<summary>Examples</summary>

```javascript
// change theme
n.context({ theme: 'dark'});
```

```javascript
// change interactions
n.context({ interactions: { select: false } });
```

</details>

---

#### selections() `function`

Gets the app selections of this instance.

##### Returns

Promise<[AppSelections](#appselections-class)>

<details>
<summary>Examples</summary>

```javascript
const selections = await n.selections();
selections.mount(element);
```

</details>

---

#### field(fieldIdentifier) `function`

Available since: 1.1.0

Gets the listbox instance of the specified field

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `fieldIdentifier` | string \| [LibraryField](#libraryfield-interface) \| [QInfo](#qinfo-interface) | Yes | - | Fieldname as a string, a Library dimension or an object id |

##### Returns

Promise<[FieldInstance](#fieldinstance-class)>

<details>
<summary>Examples</summary>

```javascript
const fieldInstance = await n.field("MyField");
fieldInstance.mount(element, { title: "Hello Field"});
```

</details>

---

#### getRegisteredTypes() `function`

Gets a list of registered visualization types and versions

##### Returns

`Object[]` - types

<details>
<summary>Examples</summary>

```javascript
const types = n.getRegisteredTypes();
// Contains
//[
// {
//   name: "barchart"
//   versions:[undefined, "1.2.0"]
// }
//]
```

</details>

---

### Direction `union`

---

### ListLayout `union`

---

### FrequencyMode `union`

---

### SearchMode `union`

---

### ToolbarMode `union`

---

### FieldEventTypes `union`

---

### FieldInstance() `class`

Available since: 1.1.0

---

#### on(eventType, callback) `function`

Event listener function on instance

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `eventType` | [FieldEventTypes](#fieldeventtypes-union) | Yes | - | event type that function needs to listen |
| `callback` | function | Yes | - | a callback function to run when event emits |

<details>
<summary>Examples</summary>

```javascript
const handleSomeEvent () => {...};
fieldInstance.on('someEvent', handleSomeEvent);
...
fieldInstance.removeListener('someEvent', handleSomeEvent);
```

</details>

---

#### removeListener(eventType, callback) `function`

Remove listener on instance

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `eventType` | [FieldEventTypes](#fieldeventtypes-union) | Yes | - | event type |
| `callback` | function | Yes | - | handler |

---

#### mount(element, options?) `function`

Available since: 1.1.0

Mounts the field as a listbox into the provided HTMLElement.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `element` | HTMLElement | Yes | - |  |
| `options` | object | No | - | Settings for the embedded listbox |

##### Returns

`Promise<void>` - A promise that resolves when the data is fetched.

<details>
<summary>Examples</summary>

```javascript
fieldInstance.mount(element);
```

</details>

---

#### unmount() `function`

Available since: 1.1.0

Unmounts the field listbox from the DOM.

<details>
<summary>Examples</summary>

```javascript
listbox.unmount();
```

</details>

---

### ThemeJSON `alias`

---

### ThemeInfo `interface`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `id` | string | Yes | - | Theme identifier |

---

#### load() `function`

A function that should return a Promise that resolves to a raw JSON theme.

##### Returns

Promise<[ThemeJSON](#themejson-alias)>

---

### QInfo `interface`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qId` | string | Yes | - | Generic object id |

---

### Sheet() `class`  **[experimental]**

Available since: 3.1.0

A controller to further modify a visualization after it has been rendered.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `id` | string | Yes | - | The id of this sheets's generic object. |
| `model` | string | Yes | - | This sheets Enigma model, a representation of the generic object. |
| `navigation` | [Navigation](#navigation-class-experimental) | Yes | - | **[experimental]** The navigation api to control sheet navigation. |

<details>
<summary>Examples</summary>

```javascript
const sheet = await embed(app).render({
  element,
  id: "jD5Gd"
});
sheet.destroy();
```

</details>

---

#### destroy() `function`

Destroys the sheet and removes it from the the DOM.

<details>
<summary>Examples</summary>

```javascript
const sheet = await embed(app).render({
  element,
  id: "jD5Gd"
});
sheet.destroy();
```

</details>

---

### Viz() `class`

A controller to further modify a visualization after it has been rendered.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `id` | string | Yes | - | The id of this visualization's generic object. |
| `model` | qix.GenericObject | Yes | - | This visualizations Enigma model, a representation of the generic object. |
| `viewDataToggled` | boolean | Yes | - | Whether or not the chart has the data view toggled on. |

<details>
<summary>Examples</summary>

```javascript
const viz = await embed(app).render({
  element,
  type: 'barchart'
});
viz.destroy();
```

</details>

---

#### destroy() `function`

Destroys the visualization and removes it from the the DOM.

##### Returns

`Promise<void>`

<details>
<summary>Examples</summary>

```javascript
const viz = await embed(app).render({
  element,
  id: 'abc'
});
viz.destroy();
```

</details>

---

#### convertTo(newType, forceUpdate?, forcePatch?) `function`

Available since: 1.1.0

Converts the visualization to a different registered type.

Will update properties if permissions allow, else will patch (can be forced with forcePatch parameter)

Not all chart types are compatible, similar structures are required.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `newType` | string | Yes | - | Which registered type to convert to. |
| `forceUpdate` | boolean | No | - | Whether to apply the change or not, else simply returns the resulting properties, defaults to true. |
| `forcePatch` | boolean | No | - | Whether to always patch the change instead of making a permanent change |

##### Returns

`Promise<object>` - Promise object that resolves to the full property tree of the converted visualization.

<details>
<summary>Examples</summary>

```javascript
const viz = await embed(app).render({
  element,
  id: 'abc'
});
await viz.convertTo('barChart');
// Change the barchart to a linechart, only in the current session
const newProperties = await viz.convertTo('lineChart', false, true);
// Remove the conversion by clearing the patches
await viz.model.clearSoftPatches();
```

</details>

---

#### toggleDataView(showDataView?) `function`  **[experimental]**

Available since: 4.9.0

Toggles the chart to a data view of the chart.

The chart will be toggled to the type defined in the nebula context (dataViewType).

The default dataViewType for nebula is sn-table. The specified chart type needs to be registered as well, in order to make it possible to render the data view.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `showDataView` | boolean | No | - | If included, forces the chart into a specific state. True will show data view, and false will show the original chart. If not included it will always toggle between the two views. |

---

#### addListener(eventName, listener) `function`

Listens to custom events from inside the visualization. See useEmitter

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `eventName` | string | Yes | - | Event name to listen to |
| `listener` | function | Yes | - | Callback function to invoke |

---

#### removeListener(eventName, listener) `function`

Removes a listener

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `eventName` | string | Yes | - | Event name to remove from |
| `listener` | function | Yes | - | Callback function to remove |

---

#### getImperativeHandle() `function`

Gets the specific api that a Viz exposes.

##### Returns

`Promise<object>` - object that contains the internal Viz api.

---

### ActionToolbarElement `interface`

Available since: 2.1.0

extends `HTMLElement`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `className` | 'njs-action-toolbar-popover' | Yes | - |  |

---

### ActionElement `interface`

Available since: 2.0.0

extends `HTMLElement`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `className` | 'njs-cell-action' | Yes | - |  |

---

### CellElement `interface`

extends `HTMLElement`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `className` | 'njs-cell' | Yes | - |  |

---

### CellBody `interface`

extends `HTMLElement`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `className` | 'njs-cell-body' | Yes | - |  |

---

### CellFooter `interface`

Available since: 2.0.0

extends `HTMLElement`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `className` | 'njs-cell-footer' | Yes | - |  |

---

### CellTitle `interface`

Available since: 2.0.0

extends `HTMLElement`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `className` | 'njs-cell-title' | Yes | - |  |

---

### CellSubTitle `interface`

Available since: 2.0.0

extends `HTMLElement`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `className` | 'njs-cell-sub-title' | Yes | - |  |

---

### SheetElement `interface`  **[experimental]**

Available since: 3.1.0

extends `HTMLElement`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `className` | 'njs-sheet' | Yes | - |  |

---

### VizElementAttributes `interface`

extends `NamedNodeMap`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `data-render-count` | string | Yes | - |  |

---

### VizElement `interface`

extends `HTMLElement`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `attributes` | [VizElementAttributes](#vizelementattributes-interface) | Yes | - |  |
| `className` | 'njs-viz' | Yes | - |  |

---

### Flags `interface`

---

#### isEnabled(flag) `function`

Checks whether the specified flag is enabled.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `flag` | string | Yes | - | The value flag to check. |

##### Returns

`boolean` - True if the specified flag is enabled, false otherwise.

---

### AppSelections() `class`

---

#### mount(element) `function`

Mounts the app selection UI into the provided HTMLElement.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `element` | HTMLElement | Yes | - |  |

<details>
<summary>Examples</summary>

```javascript
selections.mount(element);
```

</details>

---

#### unmount() `function`

Unmounts the app selection UI from the DOM.

<details>
<summary>Examples</summary>

```javascript
selections.unmount();
```

</details>

---

### ObjectSelections() `class`

---

#### addListener(eventType, callback) `function`

Event listener function on instance

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `eventType` | string | Yes | - | event type that function needs to listen |
| `callback` | function | Yes | - | a callback function to run when event emits |

<details>
<summary>Examples</summary>

```javascript
api.addListener('someEvent', () => {...});
```

</details>

---

#### removeListener(eventType, callback) `function`

Remove listener function on instance

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `eventType` | string | Yes | - | event type that function needs to listen |
| `callback` | function | Yes | - | a callback function to run when event emits |

<details>
<summary>Examples</summary>

```javascript
api.removeListener('someEvent', () => {...});
```

</details>

---

#### begin(paths) `function`

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `paths` | string[] | Yes | - |  |

##### Returns

`Promise<undefined>`

---

#### clear() `function`

##### Returns

`Promise<undefined>`

---

#### confirm() `function`

##### Returns

`Promise<undefined>`

---

#### cancel() `function`

##### Returns

`Promise<undefined>`

---

#### select(s) `function`

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `s` | object | Yes | - |  |

##### Returns

`Promise<boolean>`

---

#### canClear() `function`

##### Returns

`boolean`

---

#### canConfirm() `function`

##### Returns

`boolean`

---

#### canCancel() `function`

##### Returns

`boolean`

---

#### isActive() `function`

##### Returns

`boolean`

---

#### isModal() `function`

##### Returns

`boolean`

---

#### goModal(paths) `function`

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `paths` | string[] | Yes | - |  |

##### Returns

`Promise<undefined>`

---

#### noModal(accept?) `function`

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `accept` | boolean | No | false |  |

##### Returns

`Promise<undefined>`

---

### Field `union`

---

### CreateConfig `interface`

Rendering configuration for creating and rendering a new object

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | string | Yes | - |  |
| `version` | string | No | - |  |
| `fields` | [Field](#field-union)[] | No | - |  |
| `properties` | qix.GenericObjectProperties | No | - |  |

---

### RenderConfig `interface`

Configuration for rendering a visualisation, either creating or fetching an existing object.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `element` | HTMLElement | Yes | - | Target html element to render in to |
| `options` | object | No | - | Options passed into the visualisation |
| `plugins` | [Plugin](#plugin-interface-experimental)[] | No | - | plugins passed into the visualisation |
| `signal` | AbortSignal | No | - | Optional AbortSignal to cancel the render operation. When aborted, destroy() is called for cleanup before onError() is called with the AbortError. |
| `id` | string | No | - | For existing objects: Engine identifier of object to render |
| `type` | string | No | - | For creating objects: Type of visualisation to render |
| `version` | string | No | - | For creating objects: Version of visualization to render |
| `fields` | [Field](#field-union)[] | No | - | For creating objects: Data fields to use |
| `extendProperties` | boolean | No | false | For creating objects: Whether to deeply extend properties or not. If false then subtrees will be overwritten. |
| `properties` | qix.GenericObjectProperties | No | - | For creating objects: Explicit properties to set |

<details>
<summary>Examples</summary>

```javascript
// A config for Creating objects:
const createConfig = {
  type: 'bar',
  element: document.querySelector('.bar'),
  extendProperties: true,
  fields: ['[Country names]', '=Sum(Sales)'],
  properties: {
    legend: {
      show: false,
    },
  }
};
nebbie.render(createConfig);
// A config for rendering an existing object:
const renderConfig = {
  id: 'jG5LP',
  element: document.querySelector('.line'),
};
nebbie.render(renderConfig);
// Using AbortSignal to cancel rendering:
const controller = new AbortController();
const abortConfig = {
  type: 'bar',
  element: document.querySelector('.bar'),
  fields: ['Country', '=Sum(Sales)'],
  signal: controller.signal,
  onError: (err) => {
    if (err.name === 'AbortError') {
      console.log('Render was cancelled');
    } else {
      console.error('Render failed:', err);
    }
  }
};
const vizPromise = nebbie.render(abortConfig);
// Cancel the render operation
controller.abort();
```

</details>

---

#### onRender() `function`

Callback function called after rendering successfully

---

#### onError(undefined) `function`

Callback function called if an error occurs. Also called with AbortError when signal aborts.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
|  | [RenderError](#rendererrormessage-originalerror-class) | Yes | - |  |

---

### LibraryField `interface`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qLibraryId` | string | Yes | - |  |
| `type` | 'dimension' \| 'measure' | Yes | - |  |

---

### Plugin `interface`  **[experimental]**

Available since: 1.2.0

An object literal containing meta information about the plugin and a function containing the plugin implementation.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `info` | object | Yes | - | Object that can hold various meta info about the plugin |
| `fn` | function | Yes | - | The implementation of the plugin. Input and return value is up to the plugin implementation to decide based on its purpose. |

<details>
<summary>Properties of `info`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `name` | string | Yes | - | The name of the plugin |

</details>

<details>
<summary>Examples</summary>

```javascript
const plugin = {
  info: {
    name: "example-plugin",
    type: "meta-type",
  },
  fn: () => {
    // Plugin implementation goes here
  }
};
```

</details>

---

### LoadType `interface`

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `type` | object | Yes | - |  |

#### Returns

Promise<[Visualization](#visualization-interface)>

---

### TypeInfo `interface`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `name` | string | Yes | - |  |
| `version` | string | No | - |  |
| `load` | [LoadType](#loadtype-interface) | Yes | - |  |
| `meta` | object | No | - |  |

---

### RenderError(message, originalError) `class`

extends `Error`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `originalError` | Error | Yes | - |  |

---

### Navigation() `class`  **[experimental]**

Available since: 5.4.0

implements [Emitter](#emitter-class)

The navigation api instance.

<details>
<summary>Examples</summary>

```javascript
const navigation = useNavigation();
//...
useEffect(() => {
  const onSheetChanged = () => {
    // do something
  };
  if (navigation?.addListener) {
    navigation.addListener("sheetChanged", onSheetChanged);
  }
  return () => {
    if (navigation?.removeListener) {
      navigation.removeListener("sheetChanged", onSheetChanged);
    }
  };
}, [navigation]);

const onSheetClick = (sheetId: string) => {
  navigation?.goToSheet(sheetId);
};
```

</details>

---

#### goToSheet(sheetId) `function`  **[experimental]**

Available since: 5.4.0

Navigate to the supplied sheet and emit 'sheetChanged' event if the target sheet Id is valid.
This allows a navigation object to synchronize its current sheet item with the active sheet.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `sheetId` | string | Yes | - | Id of the sheet to navigate to |

---

#### getCurrentSheetId() `function`  **[experimental]**

Available since: 5.4.0

Return the current sheet id

##### Returns

`string | false` - The current sheet Id. false means there is no current sheet.

---

### Visualization `interface`

The entry point for defining a visualization.

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `galaxy` | [Galaxy](#galaxy-interface) | Yes | - |  |

#### Returns

[VisualizationDefinition](#visualizationdefinition-interface)

<details>
<summary>Examples</summary>

```javascript
import { useElement, useLayout } from '@nebula.js/stardust';

export default function() {
  return {
    qae: {
      properties: {
        dude: 'Heisenberg',
      }
    },
    component() {
      const el = useElement();
      const layout = useLayout();
      el.innerHTML = `What's my name? ${layout.dude}!!!`;
    }
  };
}
```

</details>

---

### VisualizationDefinition `interface`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qae` | [QAEDefinition](#qaedefinition-interface) | Yes | - |  |

---

#### component() `function`

##### Returns

`void`

---

### SetStateFn `interface`

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `newState` | S \| function | Yes | - | The new state |

---

### EffectCallback() `function`

Callback function that should return a function that in turns gets
called before the hook runs again or when the component is destroyed.
For example to remove any listeners added in the callback itself.

#### Returns

`void | function`

---

### Ref `interface`

Reference object returned from useRef

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `current` | R | Yes | - | Current value |

---

### Rect `interface`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `top` | number | Yes | - |  |
| `left` | number | Yes | - |  |
| `width` | number | Yes | - |  |
| `height` | number | Yes | - |  |

---

### ActionDefinition `interface`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `action` | A | Yes | - |  |
| `hidden` | boolean | No | - |  |
| `disabled` | boolean | No | - |  |
| `icon` | object | No | - |  |

<details>
<summary>Properties of `icon`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `viewBox` | string | No | "0 0 16 16" |  |
| `shapes` | object[] | Yes | - |  |

</details>

---

### Constraints `interface`  _(deprecated)_

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `passive` | boolean | No | false | Whether or not passive constraints are on. Should block any passive interaction by users, ie: tooltips |
| `active` | boolean | No | false | Whether or not active constraints are on. Should block any active interaction by users, ie: scroll, click |
| `select` | boolean | No | false | Whether or not select constraints are on. Should block any selection action. Implied when active is true. |
| `edit` | boolean | No | true | Whether or not edit actions are available. Should block any edit action. |

---

### Interactions `interface`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `passive` | boolean | No | true | Whether or not passive interactions are on. Allows passive interaction by users, ie: tooltips |
| `active` | boolean | No | true | Whether or not active interactions are on. Allows active interaction by users, ie: scroll, click |
| `select` | boolean | No | true | Whether or not select interactions are on. Allows selection actions. Implied when active is false. |
| `edit` | boolean | No | false | Whether or not edit actions are on. Allows edit actions. |

---

### RenderState `interface`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `pending` | any | Yes | - |  |
| `restore` | any | Yes | - |  |

---

### Emitter() `class`

The emitter instance. Implements https://nodejs.org/api/events.html#class-eventemitter.

---

### Keyboard `interface`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `enabled` | boolean | Yes | - | Whether or not Nebula handles keyboard navigation or not. |
| `active` | boolean | Yes | - | Set to true when the chart is activated, ie a user tabs to the chart and presses Enter or Space. |

---

#### blur(undefined) `function`

Function used by the visualization to tell Nebula it wants to relinquish focus

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
|  | boolean | Yes | - |  |

---

#### focus() `function`

Function used by the visualization to tell Nebula it wants to focus

---

#### focusSelection(undefined) `function`

Function used by the visualization to tell Nebula that focus the selection toolbar

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
|  | boolean | Yes | - |  |

---

### importProperties(args) `function`

Available since: 1.1.0

Imports properties for a chart with a hypercube.

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `args` | object | Yes | - |  |

#### Returns

`Object` - A properties tree

---

### exportProperties(args) `function`

Available since: 1.1.0

Exports properties for a chart with a hypercube.

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `args` | object | Yes | - |  |

#### Returns

[ExportFormat](#exportformat-interface)

---

### onPropertyChange(properties) `function`

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `properties` | qix.GenericObjectProperties | Yes | - |  |

---

### QAEProperties `interface`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `initial` | qix.GenericObjectProperties | No | - |  |
| `onChange` | [onPropertyChange](#onpropertychangeproperties-function) | No | - |  |

---

### QAEDefinition `interface`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `properties` | [QAEProperties](#qaeproperties-interface) \| qix.GenericObjectProperties | No | - |  |
| `data` | object | No | - |  |
| `importProperties` | [importProperties](#importpropertiesargs-function) | No | - |  |
| `exportProperties` | [exportProperties](#exportpropertiesargs-function) | No | - |  |

<details>
<summary>Properties of `data`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `targets` | [DataTarget](#datatarget-interface)[] | Yes | - |  |

</details>

---

### DataTarget `interface`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `path` | string | Yes | - |  |
| `dimensions` | [FieldTarget](#fieldtarget-interface)<qix.NxDimension> | No | - |  |
| `measures` | [FieldTarget](#fieldtarget-interface)<qix.NxMeasure> | No | - |  |

---

### fieldTargetAddedCallback(field, properties) `function`

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `field` | T | Yes | - |  |
| `properties` | qix.GenericObjectProperties | Yes | - |  |

---

### fieldTargetRemovedCallback(field, properties, index) `function`

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `field` | T | Yes | - |  |
| `properties` | qix.GenericObjectProperties | Yes | - |  |
| `index` | number | Yes | - |  |

---

### FieldTarget `interface`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `min` | function \| number | No | - | Number or function that returns the minimum number of fields |
| `max` | function \| number | No | - | Number or function that returns the maximum number of fields |
| `added` | [fieldTargetAddedCallback](#fieldtargetaddedcallbackfield-properties-function)<T> | No | - |  |
| `removed` | [fieldTargetRemovedCallback](#fieldtargetremovedcallbackfield-properties-index-function)<T> | No | - |  |

---

### Theme() `class`

---

#### name() `function`

Returns theme name

##### Returns

`string` - Current theme.

<details>
<summary>Examples</summary>

```javascript
theme.name();
```

</details>

---

#### getDataColorScales() `function`

##### Returns

[ScalePalette](#scalepalette-interface)[]

---

#### getDataColorPalettes() `function`

##### Returns

[DataPalette](#datapalette-interface)[]

---

#### getDataColorPickerPalettes() `function`

##### Returns

[ColorPickerPalette](#colorpickerpalette-interface)[]

---

#### getDataColorSpecials() `function`

##### Returns

[DataColorSpecials](#datacolorspecials-interface)

---

#### getColorPickerColor(c) `function`

Resolve a color object using the color picker palette from the provided JSON theme.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `c` | object | Yes | - |  |

##### Returns

`string` - The resolved color.

<details>
<summary>Examples</summary>

```javascript
theme.getColorPickerColor({ index: 1 });
theme.getColorPickerColor({ color: 'red' });
```

</details>

---

#### getContrastingColorTo(color) `function`

Get the best contrasting color against the specified `color`.
This is typically used to find a suitable text color for a label placed on an arbitrarily colored background.

The returned colors are derived from the theme.

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `color` | string | Yes | - | A color to measure the contrast against |

##### Returns

`string` - - The color that has the best contrast against the specified `color`.

<details>
<summary>Examples</summary>

```javascript
theme.getContrastingColorTo('#400');
```

</details>

---

#### getStyle(basePath, path, attribute) `function`

Get the value of a style attribute in the theme
by searching in the theme's JSON structure.
The search starts at the specified base path
and continues upwards until the value is found.
If possible it will get the attribute's value using the given path.
When attributes separated by dots are provided, such as 'hover.color',
they are required in the theme JSON file

##### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `basePath` | string | Yes | - | Base path in the theme's JSON structure to start the search in (specified as a name path separated by dots). |
| `path` | string | Yes | - | Expected path for the attribute (specified as a name path separated by dots). |
| `attribute` | string | Yes | - | Name of the style attribute. (specified as a name attribute separated by dots). |

##### Returns

`string | undefined` - The style value or undefined if not found

<details>
<summary>Examples</summary>

```javascript
theme.getStyle('object', 'title.main', 'fontSize');
theme.getStyle('object', 'title', 'main.fontSize');
theme.getStyle('object', '', 'title.main.fontSize');
theme.getStyle('', '', 'fontSize');
```

</details>

---

### move(array, oldIndex, newIndex) `function`

Move an element from position old_index to position new_index in
the array.

#### Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `array` | any | Yes | - |  |
| `oldIndex` | any | Yes | - |  |
| `newIndex` | any | Yes | - |  |

---

### ExportFormat `interface`

Available since: 1.1.0

Used for exporting and importing properties between backend models. An object that exports to
ExportFormat should put dimensions and measures inside one data group. If an object has two hypercubes,
each of the cubes should export dimensions and measures in two separate data groups.
An object that imports from this structure is responsible for putting the existing properties where they should be
in the new model.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `data` | [ExportDataDef](#exportdatadef-interface)[] | No | - |  |
| `properties` | object | No | - |  |

---

### ExportDataDef `interface`

Available since: 1.1.0

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `dimensions` | qix.NxDimension[] | Yes | - |  |
| `measures` | qix.NxMeasure[] | Yes | - |  |
| `excludedDimensions` | qix.NxDimension[] | Yes | - |  |
| `excludedMeasures` | qix.NxMeasure[] | Yes | - |  |
| `interColumnSortOrder` | number[] | Yes | - |  |

---

### ConversionType `interface`

Available since: 1.1.0

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `importProperties` | [importProperties](#importpropertiesargs-function) | Yes | - |  |
| `exportProperties` | [exportProperties](#exportpropertiesargs-function) | Yes | - |  |

---

### hyperCubeConversion `interface`

Available since: 1.1.0

implements [ConversionType](#conversiontype-interface)

---

### EnigmaMockerOptions `interface`  **[experimental]**

Available since: 3.0.0

Options for Enigma Mocker

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `appMethods` | object | No | - | Object with methods to add to the mocked app. |
| `delay` | number | Yes | - | Simulate delay (in ms) for calls in enigma-mocker. |

---

### ScalePalette `interface`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `key` | string | Yes | - |  |
| `type` | 'gradient' \| 'class-pyramid' | Yes | - |  |
| `colors` | string[] \| string[][] | Yes | - |  |

---

### DataPalette `interface`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `key` | string | Yes | - |  |
| `type` | 'pyramid' \| 'row' | Yes | - |  |
| `colors` | string[] \| string[][] | Yes | - |  |

---

### ColorPickerPalette `interface`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `key` | string | Yes | - |  |
| `colors` | string[] | Yes | - |  |

---

### DataColorSpecials `interface`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `primary` | string | Yes | - |  |
| `nil` | string | Yes | - |  |
| `others` | string | Yes | - |  |

---
