---
source: https://qlik.dev/extend/extensions/picasso-js/components/text/
last_updated: 2026-06-02T18:15:45+01:00
---

# Text

A component that adds a descriptive text, commonly used as axis title or chart title.

## Data

Does not support a data source. Text is either set explicitly or extracted from
the data source of a scale.

## Layout

The component adjusts to the `dock` setting and rotates the text to perpendicular
to the docking direction.

## Interaction

Interaction is not supported.

## Example

### Explicitly set text

```js
{
  type: 'text',
  text: 'My title',
}
```

### Extract title from the data source of the scale

```js
{
  type: 'text',
  scale: '<name-of-scale>'
}
```

## API Reference

For more information, see the [API reference](https://qlik.dev/apis/javascript/picasso-js/#definitions-componenttext).
