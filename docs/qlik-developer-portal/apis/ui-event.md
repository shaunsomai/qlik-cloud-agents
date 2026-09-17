---
source: https://qlik.dev/apis/ui-event/
last_updated: 2025-05-09T12:52:37+02:00
---

# Qlik Cloud UI events

Qlik Cloud UI events are a category of events that track interactions within the Qlik Cloud user interface.

These events are available via the [Audits API](https://qlik.dev/apis/rest/audits/).

## Use cases

You can use UI events to:

- Track how users interact with apps and sheets.
- Build dashboards or reports based on usage.

## Event structure

UI events use a standardized JSON format aligned with CloudEvents principles.
Each event includes fields like `id`, `type`, `source`, and `time`, along with an event-specific `data` object.

Example:

```json
{
  "id": "60143626-36a8-4661-9afe-8080a01d89e7",
  "time": "2025-04-25T07:06:22Z",
  "type": "string",
  "source": "string",
  "specversion": "1.0",
  "data": {
    "appId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
    "sheetId": "c35f4b70-3ce4-4a30-b62b-2aef16943bc4",
    "sheetState": "analysis",
    "sheetTitle": "My Sheet"
  }
}
```

## Reference documentation
