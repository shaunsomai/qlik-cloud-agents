---
source: https://qlik.dev/toolkits/qlik-cli/knowledgebase/knowledgebase-datasource-schedule-create/
last_updated: 2026-06-03T09:30:31+02:00
---

# knowledgebase datasource schedule create

## qlik knowledgebase datasource schedule create

Create a knowledgebase datasource schedule

### Synopsis

Creates or updates a specified datasource schedule.

```
qlik knowledgebase datasource schedule create [flags]
```

### Options

```
      --calendars-comment string         Description of the intention of this schedule
      --calendars-dayOfMonth-end int     End of the range (inclusive). If end < start, then end is interpreted as equal to start. Optional, defaulted to Start
      --calendars-dayOfMonth-start int   Start of the range (inclusive)
      --calendars-dayOfMonth-step int    Step to be take between each value. Optional, defaulted to 1
      --calendars-dayOfWeek-end int      End of the range (inclusive). If end < start, then end is interpreted as equal to start. Optional, defaulted to Start
      --calendars-dayOfWeek-start int    Start of the range (inclusive)
      --calendars-dayOfWeek-step int     Step to be take between each value. Optional, defaulted to 1
      --calendars-hour-end int           End of the range (inclusive). If end < start, then end is interpreted as equal to start. Optional, defaulted to Start
      --calendars-hour-start int         Start of the range (inclusive)
      --calendars-hour-step int          Step to be take between each value. Optional, defaulted to 1
      --calendars-minute-end int         End of the range (inclusive). If end < start, then end is interpreted as equal to start. Optional, defaulted to Start
      --calendars-minute-start int       Start of the range (inclusive)
      --calendars-minute-step int        Step to be take between each value. Optional, defaulted to 1
      --calendars-month-end int          End of the range (inclusive). If end < start, then end is interpreted as equal to start. Optional, defaulted to Start
      --calendars-month-start int        Start of the range (inclusive)
      --calendars-month-step int         Step to be take between each value. Optional, defaulted to 1
      --calendars-second-end int         End of the range (inclusive). If end < start, then end is interpreted as equal to start. Optional, defaulted to Start
      --calendars-second-start int       Start of the range (inclusive)
      --calendars-second-step int        Step to be take between each value. Optional, defaulted to 1
      --calendars-year-end int           End of the range (inclusive). If end < start, then end is interpreted as equal to start. Optional, defaulted to Start
      --calendars-year-start int         Start of the range (inclusive)
      --calendars-year-step int          Step to be take between each value. Optional, defaulted to 1
      --datasourceId string              (Required) The id of the datasource the schedule belongs to.
  -f, --file file                        Read request body from the specified file
  -h, --help                             help for create
      --interval int                     Duration in seconds to wait between retries, at least 1 (default 1)
      --intervals-every string           The period to repeat the interval
      --intervals-offset string          A fixed offset added to the intervals period. Optional, defaults to 0
      --knowledgebaseId string           (Required) The id of the knowledgebase the schedule belongs to.
  -q, --quiet                            Return only IDs from the command
      --raw                              Return original response from server without any processing
      --retry int                        Number of retries to do before failing, max 10
```

### Options inherited from parent commands

```
  -c, --config string            path/to/config.yml where parameters can be set instead of on the command line
      --context string           Name of the context used when connecting to Qlik Associative Engine
      --headers stringToString   HTTP headers to use when connecting to Qlik Associative Engine (default [])
      --insecure                 Allow connecting to hosts with self-signed certificates
      --json                     Returns output in JSON format, if possible. Disables verbose and traffic output
  -s, --server string            URL to Qlik Cloud or directly to a Qlik Associative Engine
      --server-type string       The type of server you are using: cloud, Windows (Enterprise on Windows) or engine
  -v, --verbose                  Log extra information
```
