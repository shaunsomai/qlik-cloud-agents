---
source: https://qlik.dev/extend/extensions/picasso-js/components/axis/
last_updated: 2026-06-02T18:15:45+01:00
---

# Axis

## Data and scales

The axis component doesn't take any [data](https://qlik.dev/extend/extensions/picasso-js/components/main-concepts/data) as input directly, instead the
data is implicitly fetched from the referenced [scale](https://qlik.dev/extend/extensions/picasso-js/components/main-concepts/scales).

From the scale, which is either discrete or continuous, an axis is constructed.

### Discrete

![Example of a discrete axis](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAPkAAAAiCAYAAACdtn98AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAOqSURBVHhe7ZjdkeowDIVvmSkGOmFog/TA0w4t8JIm4o38Kwk7wIW1gzkP3wyJZcc60omz+2+eZwMA6BeYHIDOgckB6ByYHIDOgckB6JxVk1+vV3M+nwEAG4O8mfNsjo89ySnR3H1QBpo9Tw+aweRfBDR7Hpi8IWjY54FmzwOTN+SZv0mAA5o9Tw+afazJAQCPAZMD0DkwOQCdA5MD0DkwOQCdA5MD0DkwOQCdU9Xk02lvhmGQ7EYzxZjJjLvBHH+W3z/HOHY5DGZ/msRar2D3cbi4a/YcHVcLyu9Gl7C//+Tdmr17vb/H9dKrOvZAfZMrQ9kGv2OyPzX5BrAaiP283qBfb3J6eR+O5jgczSU3/kU0N/k8X5ZC+NN79SQfbdztKecN4cfcOnI+XUdj032+zlZOcm3oaTT7YW/GafldyiXGhfx9/HJ/XTOnudCB7tvnLMaIej66XqEGDaH90j7cvvnLSe41jnmNR6qFHVteDkxbvobV39+/0Wjnxly8fFarPtuAyXkhyiZPYvKXgh8La9KcB4whTKLiWmBzEKYh8lrQWNo/i6ExivPrOM38Keab1cW5ObFp9ctExcn1VmrA9WSN3wbaH8u90AciLpe7GMv8XuC529/sWUIXpVlNPsfkUayVJucNzObLOarQKq4FOj9HXgsaK+efkGuW41zzcZOnBuY6lWugm3ftWZWgPETu6aUjas9RuaeeXK7tizCNcdY0krTTZQMmd8nfM3kUfKHcYCy2aAxVaBXXgnxzsNxWcglx7pOw0KS6wWxDhzkEM3nhOfdqINeTsbWxeq7sh48LTVjuIl9hcqclX7ukUfiC4rG8V2vxMX+TcxOka9W8/toKnSlaWOMjTK4/owu5CJRmqeG4TvrFSNePmZw/M12z+X6sKVw3cS93EpdzF/qx+bqHtUZa83wN6tLc5LZZ4j0mhGrYdErJJhXzaQ4vWiy2mxOKsX2TOx3EHrO5KINRnJ+Ta7icya0WhUbXDbxag7BXf3qFsdrkeozvV+pC931OKncRVzS5W3dN83hta9hGl/omJ1E4oiBlk/P/7CYh05ywHhfRNp+9fzQja9gguL1WxW1B2icj7PUmppCLH3MmzDdc0IbXYX+6ZDWPcaKBH6uBHKuJMhbD6mdz88b0xH5RuQv9xJcAn7/cY/Ok5n7NELvoeDNeiaomv49sRgDA62zH5P4zr/WpCkBvbOwkBwC8G5gcgM6ByQHoHJgcgM6ByQHoHJgcgK6ZzS8vPc11M76UDAAAAABJRU5ErkJggg==)

### Continuous

![Example of a continuous axis](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAQ0AAAApCAYAAAAvWHycAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAL2SURBVHhe7djBdeIwFIXhlEkxcScctxF6YJXDggbYuAkUSxhbT0jCyuo99C++RYCZkZ6ursl83e93BwB7URoAmlAaAJpQGgCaUBoAmlRL43q9uvP5DOAD+fudu/fvVEvD/8W5161hH3pwFnr8dw+UhiE9B1Wbns+C0jCk56Bq0/NZUBqG9BxUbXo+C0rDkJ6Dqk3PZ0FpGNJzULXp+SwoDUN6Dqo2PZ9FtTRut1v2dWvYhx6chR7/3UO1NAAgRWkAaEJpAGhCaQBoQmkAaEJpAGhCaQBoQmkAaEJpAGhSLo3p5IbDwR284yX/GYUux2XNwegu0XvTz7C+N/7KP6dVWPP3yU3Ra9seB3ea5Oe1ic9j+Jm29yzl63dc95Cu1UKmwhrTGVfm/y5fhdK4uHEdwuRO38mBa+UPNxpA2Pzz53DwS4mEgem/cOvBRqUhSiTek0Ky8HymnjM3lC+RlWStBjK1lpoohvL89+QrXxphANuH5eEbEm067GEdnIUi9Gsc3HiUs/dFuK07PnxtHuvPXiJL+UouTvwg0p6psNZ5rhexzlll/nvylS8NP6j4EAuNo115GPLwNXoGUl6oRzC3Q9Rcfj5wozv59fsn3Wxdp6l8lZ/KVjIly21WnP++fGVLQwZ1ZrE0al8rZ7pL43Hh/LzlWaTNr700ohlH52EvX8te3szeSmmU578vX5/5TSMENN68naeC59f2XLs84Mch2imN+NeTaK2W8pWsLc6NlUylpVGe/758fd7/aYQBvP4uLQen/bI9nmrCMn8Z1PTJoEklgIby9VIEUYlYydRLaVTmvydf+dIQH9Z8wRLRV+CX9+InRu1zyqQXSvwc70khEVZR5obylcw4lEhu/ooz9VIalfnvyVehNGZhCMtTTvyDeoUNP9e82jYdv5+2p1biEBchuGEf+otvW2syc0P5krmSl8hCpsIa0xlX5v8uX+XSAIAMSgNAE0oDQBNKA0ATSgNAE0oDQBNKA0ATSgNAE0oDQIO7+wOBYpnzY3sA2QAAAABJRU5ErkJggg==)

## Layout

There are two directions in which the axis can be laid out, either horizontal or
vertical. Depending on direction, different labeling modes are available.

A vertical axis is limited to only horizontal labels. While a horizontal axis
have the option to show horizontal labels on two rows or show vertical labels
tilted at an angle.

### Tilted labels

Tilted labels are only supported on a discrete axis. When the `mode` property
is set to `auto`, labels are tilted when there is not enough space available.

```js
{
  type: 'axis',
  scale: 'myDiscreteScale',
  layout: {
    dock: 'bottom'
  },
  settings: {
    labels: {
      mode: 'tilted',
      tiltAngle: 35
    }
  }
}
```

![Example of a tilted axis](https://qlik.dev/_astro/axis-tilted-labels.DQ8hBA4I.png)

### Layered labels

Layered labels are only supported on a discrete axis.

```js
{
  type: 'axis',
  scale: 'myDiscreteScale',
  layout: {
    dock: 'bottom'
  },
  settings: {
    labels: {
      mode: 'layered'
    }
  }
}
```

![Example of an axis with layered labels](data:image/png;base64,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)

### Using maxGlyphCount

The `maxGlyphCount` property is used to measure the largest possible size of a
label. The size of a label primarily affects two things: first, when
determining the required size to render an axis (this can also be limited via the
`maxLengthPx` property), and second, when the `mode` is set to `auto`, it is
used to calculate the threshold for switching between horizontal and tilted
labels.

Under the hood, `maxGlyphCount` is a multiplier on the size of the character
`M`, as measured using the `fontSize` and `fontFamily`.

```js
{
  type: 'axis',
  scale: 'myDiscreteScale',
  settings: {
    labels: {
      mode: 'auto',
      maxGlyphCount: 20
    }
  }
}
```

### Using paddingStart

The `paddingStart` property adds padding to the opposite side of where the axis
is *docked* (or *aligned* when using `dock: center`). It can be specified as
either a number or a function (does not receive any parameters).

Specified as a number, in this case `100px` padding is added the right side
of the axis:

```js
{
  type: 'axis',
  scale: 'myScale',
  dock: 'left',
  settings: {
    paddingStart: 100,
  }
}
```

In this example, a function is used to move the axis next to a specific element
(for example useful when adding one axis per bar in a bar chart):

```js
{
  type: 'axis',
  scale: 'myScale',
  dock: 'center',
  settings: {
    align: 'left',
    paddingStart: () => {
      // Move the axis next to a specific element
      const label = 'A value on the major axis';
      const majorScale = chart.scale('myMajorScale');
      return chartWidth * (majorScale(label) + majorScale.bandwidth());
    }
  }
}
```

### Using paddingEnd

The `paddingEnd` property can be used in the same way as `paddingStart`. If not
specified it defaults to `10`. It adds padding to the same side as the axis
is *docked* (or *aligned* when using `dock: center`).

## Formatting

Label formatting is derived from the scale and the data itself. But as with any
component, it is possible to reference a [custom formatter](https://qlik.dev/extend/extensions/picasso-js/components/main-concepts/formatting) using
the `formatter` property.

### Custom formatting

```js
{
  type: 'axis',
  formatter: {
    formatter: 'd3', // The type of formatter to use
    type: 'number', // The type of data to format
    format: '-1.0%' // Format pattern
  }
}
```

## Interaction

On a discrete axis it possible to configure the axis to consume and trigger
[brush](https://qlik.dev/extend/extensions/picasso-js/components/main-concepts/brushing) events.

```js
{
  type: 'axis',
  scale: 'myDiscreteScale',
  brush: {
    trigger: [{
      on: 'tap',
      contexts: ['highlight']
    }],
    consume: [{
      context: 'highlight',
      style: {
        inactive: {
          opacity: 0.3
        }
      }
    }]
  }
}
```

For a continuous axis there is no direct way to configure interactions, instead
it is done via other components, such as
the [brush-range](https://qlik.dev/extend/extensions/picasso-js/components/brush-range/)
or [brush-area](https://qlik.dev/extend/extensions/picasso-js/components/brush-area-dir/) component.

## API Reference

For more information, see the [API reference](https://qlik.dev/apis/javascript/picasso-js/#definitions-componentaxis).
