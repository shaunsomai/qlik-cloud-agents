---
source: https://qlik.dev/toolkits/qlik-cli/data-alert/data-alert-validate/
last_updated: 2026-06-03T09:30:31+02:00
---

# data-alert validate

## qlik data-alert validate

Validate data alert task

### Synopsis

Validates a new data alerting task. Current support includes validation for recipients only.

```
qlik data-alert validate [flags]
```

### Options

```
      --appId string                                                        (Required) appId associated to this alert definition
      --bookmarkId string                                                   bookmarkId associated to this alert definition
      --conditionId string                                                  (Required) the id of the condition that determines if this data alert should be triggered
      --description string                                                  description associated to alerting task
      --enabled                                                             if the alerting task is enabled
  -f, --file file                                                           Read request body from the specified file
  -h, --help                                                                help for validate
      --interval int                                                        Duration in seconds to wait between retries, at least 1 (default 1)
      --name string                                                         (Required) name associated to alerting task
  -q, --quiet                                                               Return only IDs from the command
      --raw                                                                 Return original response from server without any processing
      --recipients-DLGroups unknowns                                        List of recipients. An internal recipient is represented by either their user id or group id.
      --recipients-DLListId string                                          (Required) List of recipients. An internal recipient is represented by either their user id or group id.
      --recipients-DLUsers unknowns                                         List of recipients. An internal recipient is represented by either their user id or group id.
      --recipients-groupIds-alertingTaskGroupRecipientErrors-added string   Timestamp for the creation of the error
      --recipients-groupIds-alertingTaskGroupRecipientErrors-value string   Identifier for type of error occurring on alerting task
                                                                            Allowed values: "GROUP_IS_DISABLED", "MAX_ALERTS_LIMIT_REACHED", "GROUP_WITH_NO_APP_ACCESS", "GROUP_IS_DELETED"
      --recipients-groupIds-enabled                                         Whether this recipient can receive alerts.
      --recipients-groupIds-taskGroupRecipientErrors-timestamp string       Timestamp for the creation of the error
      --recipients-groupIds-taskGroupRecipientErrors-value string           Identifier for type of error occurring on sharing task specific for group recipient
                                                                            Allowed values: "GROUP_IS_DISABLED", "MAX_ALERTS_LIMIT_REACHED", "GROUP_WITH_NO_APP_ACCESS", "GROUP_IS_DELETED", "GROUP_NOT_FOUND_DL", "GROUP_DISABLED_IN_DL"
      --recipients-groupIds-value string                                    Group ID of recipient.
      --recipients-userIds-alertingTaskRecipientErrors-added string         Timestamp for the creation of the error
      --recipients-userIds-alertingTaskRecipientErrors-value string         Identifier for type of error occurring on alerting task
                                                                            Allowed values: "USER_IS_DELETED", "USER_DISABLED_IN_QCS", "NO_ACCESS_TO_APP", "UNSUBSCRIBED_FROM_ALERT", "CONDITION_EVAL_ERROR", "USER_DISABLED_IN_ALERT_BY_OWNER", "MAX_ALERTS_LIMIT_REACHED"
      --recipients-userIds-enabled                                          Whether this recipient can receive alerts.
      --recipients-userIds-groups strings                                   A list of associated groups. If a user is added individually the "addedIndividually" pseudo group is included
      --recipients-userIds-subscribed                                       Whether this recipient is subscribed to alerts of a task
      --recipients-userIds-taskRecipientErrors-timestamp string             Timestamp for the creation of the error
      --recipients-userIds-taskRecipientErrors-value string                 Identifier for type of error occurring on sharing task specific for recipient
                                                                            Allowed values: "USER_IS_DELETED", "USER_DISABLED_IN_QCS", "NO_ACCESS_TO_APP", "UNSUBSCRIBED_FROM_SHARING", "USER_DISABLED_IN_SHARING_BY_OWNER", "CHART_NOT_FOUND", "APP_NOT_FOUND", "SHEET_NOT_FOUND", "ENGINE_POD_NOT_AVAILABLE", "CHART_TYPE_NOT_ALLOWED", "GENERIC_EXECUTION_FAILURE", "USER_NOT_FOUND_DL", "USER_DISABLED_IN_DL", "FILTER_NOT_FOUND", "BOOKMARK_NOT_FOUND"
      --recipients-userIds-value string                                     User ID of recipient (internal user).
      --retry int                                                           Number of retries to do before failing, max 10
      --scheduleOptions-endDateTime string                                  EndDateTime is a local date time with respect to the above timezone parameter. If the timezone parameter is missing, then the timezone used is the one retrieved from user infos. Therefore ISO8601 time offsets are not allowed (e.g. "2026-01-02T16:04:05Z" or "2026-01-02T16:04:05+01"), if passed an error will be returned. EndDateTime is an optional parameter, when not set or when it's an empty string, the recurrence is intended to be never ending.
      --scheduleOptions-recurrence strings                                  List of RRULEs for SCHEDULED triggers, as specified in RFC5545. Note that DTSTART and DTEND, UNTIL lines are not allowed in this field; start and end times are specified in the start and end fields. RDATE and EXDATE lines are not currently supported. EXRULE is not supported since it is deprecated by RFC5545. It is mandatory if the trigger type is SCHEDULED. At least 1 rule must be set and maximum 5 rules are allowed.
      --scheduleOptions-startDateTime string                                StartDateTime is a local date time with respect to the above timezone parameter. If the timezone parameter is missing, then the timezone used is the one retrieved from user infos. Therefore ISO8601 time offsets are not allowed (e.g. "2026-01-02T16:04:05Z" or "2026-01-02T16:04:05+01"), if passed an error will be returned. StartDateTime should not be older than 1 year from current date. StartDateTime is an optional parameter, when not set or when it's an empty string, its value is set to the current local date time.
      --scheduleOptions-timezone string                                     The timezone for time calculations in SCHEDULED triggers, optional.
      --sheetId string                                                      sheetId associated to this alert definition
      --throttling-capacity int                                             the maximum number of tokens that the bucket can contain
      --throttling-initialTokenCount int                                    the initial amount of tokens in the bucket upon creation. cannot exceed capacity.
      --throttling-recurrenceRule string                                    A string that supports a subset of RFC5545 recurrence rule directives.
      --throttling-referenceTimestamp string                                a date and time reference specified in RFC3339 format
      --throttling-replenishRate int                                        the amount of tokens to insert into the bucket on the specified interval. (tokens exceeding capacity are discarded)
      --throttling-timezone string                                          the timezone for time calculations in this throttlingresource, for current time and time reference.
      --triggerType string                                                  (Required) Type of job that triggered the task
                                                                            Allowed values: "RELOAD", "SCHEDULED"
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
