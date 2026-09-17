---
source: https://qlik.dev/extend/extensions/picasso-js/get-started/
last_updated: 2026-06-02T18:15:45+01:00
---

# What is picasso.js?

picasso.js is an open source charting library that's designed for building
custom, interactive, component-based powerful visualizations.

## Components

Components are the visual building blocks that make up the chart, by combining
them in various forms virtually any chart can be created. A bar chart, for
example, consists of a bar layer, a continuous and a discrete axis. Add a line
layer and you have a combo chart. Want a line chart with four axes? - Not a problem.

## Extensible

picasso.js provides a plugin system that makes it easy to extend existing
capabilities - you can register and use custom components that play well
with the existing ones, create a new theme, provide your own data parser or
even register a custom renderer that outputs sketchy graphics. picasso.js
uses D3.js for a lot of its features and strives to provide the D3
community with a way to repurpose and integrate their work into picasso.js.

## Interactive

Apart from basic interaction patterns, interactivity in the form of brushing and
linking is provided out of the box - drag a range on a linear axis to highlight
all values that fall within that range, or use the lasso tool to highlight a
cluster of points. The brushed values can then programmatically be linked and
highlighted in another chart instance.

## Responsive

By using relative units and a unique layout algorithm you can ensure the composed
charts are responsive. The same configuration can be used for a full sized chart
containing details, annotations etc., as for a sparkline version - components are
automatically resized or removed if they don't fit.

## Themeable

The visual look of labels, lines, shapes, color palettes etc. can all be modified
and a new theme created by just changing a few base variables that control the
look and feel throughout, including plugins.
