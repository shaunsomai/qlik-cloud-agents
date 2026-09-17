---
source: https://qlik.dev/toolkits/qlik-cli/reload-task/reload-task-create/
last_updated: 2026-06-03T09:30:31+02:00
---

# reload-task create

## qlik reload-task create

(Deprecated) Create a task

### Synopsis

(Deprecated) Creates a task for a specified app.

```
qlik reload-task create [flags]
```

### Options

```
      --appId string           The ID of the app.
      --autoReload             A flag that indicates whether a reload is triggered when data of the app is changed
      --autoReloadPartial      A flag that indicates whether it is a partial reload or not for the auto reload
      --endDateTime string     The time that the task will stop recurring. If the time zone is missing, this is a combined date-time value expressing a time with a fixed UTC offset (formatted according to RFC3339). If a time zone is given, the zone offset must be omitted.
  -f, --file file              Read request body from the specified file
  -h, --help                   help for create
      --interval int           Duration in seconds to wait between retries, at least 1 (default 1)
      --partial                The task is partial reload or not
  -q, --quiet                  Return only IDs from the command
      --raw                    Return original response from server without any processing
      --recurrence strings     List of RECUR lines for a recurring event, as specified in RFC5545. Note that DTSTART and DTEND lines are not allowed in this field; event start and end times are specified in the start and end fields. This field is omitted for single events or instances of recurring events
      --retry int              Number of retries to do before failing, max 10
      --startDateTime string   The time that the task execution start recurring. If the time zone is missing, this is a combined date-time value expressing a time with a fixed UTC offset (formatted according to RFC3339). If a time zone is given, the zone offset must be omitted. Field startDateTime should not be before the Unix epoch 00:00:00 UTC on 1 January 1970. Note that the empty string value with the empty recurrence array indicates the scheduled job is not set.
      --timeZone string        The time zone in which the time is specified. (Formatted as an IANA Time Zone Database name, e.g. Europe/Zurich.) This field specifies the time zone in which the event start/end are expanded. If missing the start/end fields must specify a UTC offset in RFC3339 format.
      --type string            (Deprecated) Type of task being created - only contains the "scheduled_reload" value. Type value is not used for creating a schedule reload. It has been deprecated since 2022-04-05.
                               Allowed values: "scheduled_reload"
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
