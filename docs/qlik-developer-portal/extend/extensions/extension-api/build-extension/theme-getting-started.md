---
source: https://qlik.dev/extend/extensions/extension-api/build-extension/theme-getting-started/
last_updated: 2026-06-02T18:15:45+01:00
---

# Get started with the Theme API

The Theme API is the external interface to Qlik Sense themes. It allows
customization of visualizations, including extensions, outside of Qlik Sense.

The Theme API is available for mashup developers as the `qlik.theme` namespace.
You can retrieve a `QTheme` object with the `theme.get(id)` method. The QTheme
object consists of a theme and helper methods. The `id` parameter, which
is the value of `qextFilename`, is mandatory
when `theme.get` is used in a global context but optional when used in an app
context: `app.theme.get()`.

## Examples of use

Learn what you can do with the Theme API.

### Retrieve a theme in a global context

```javascript
qlik.theme.get('<id>').then((qtheme) => {
  alert('Theme background color: ' + qtheme.properties.backgroundColor);
});
```

### Apply a theme to all visualizations on a web page

```javascript
qlik.theme.apply('<id>').then((result) => {
  alert('theme applied with result: ' + result);
 });
```

### Retrieve the currently applied theme

The `app.theme.getApplied()` method can be used for visualization extensions so
these can use styling from the current theme.

```javascript
app.theme.getApplied().then((qtheme) => {
  alert('Current theme background color: ' + qtheme.properties.backgroundColor);
});
```
