---
source: https://qlik.dev/extend/extensions/extension-api/build-extension/navigation-getting-started/
last_updated: 2026-06-02T18:15:45+01:00
---

# Get started with the Navigation API

The Navigation API allows you to navigate within a Qlik Sense app, and is meant
to be used in visualization extensions. It will not work in mashup scenarios.

The Navigation API can be used when creating navigation button widgets.

```html
<div class="lui-buttongroup">
  <lui-button ng-click="navigation.nextSheet()">Next sheet</lui-button>
  <lui-button ng-click="navigation.prevSheet()">Previous sheet</lui-button>
  <lui-button ng-click="navigation.setMode('edit')">Edit mode</lui-button>
</div>
```

## API members

| Name     | Type   | Description             |
| -------- | ------ | ----------------------- |
| analysis | String | Used for analysis mode. |
| edit     | String | Used for edit mode.     |
