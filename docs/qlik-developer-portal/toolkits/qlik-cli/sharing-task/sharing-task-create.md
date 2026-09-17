---
source: https://qlik.dev/toolkits/qlik-cli/sharing-task/sharing-task-create/
last_updated: 2026-06-03T09:30:31+02:00
---

# sharing-task create

## qlik sharing-task create

Create sharing task

### Synopsis

Creates a new recurring sharing task.

```
qlik sharing-task create [flags]
```

### Options

```
      --appName string                                                (Deprecated) Name of the app associated (through the templates) with this sharing task
      --cleanupStrategy string                                        A bookmark is considered old if its modification date is older than the app creation date.
                                                                      Allowed values: "noCleanup", "removeOldBookmarks"
      --dataConnectionID string                                       the id of the data connection
      --description string                                            Description of the sharing task
      --distributionListId string                                     the id of the distribution list associated to the app
      --emailContent-body string                                      
      --emailContent-subject string                                   
      --enabled                                                       Toggle for enabling sharing task.
      --executeOnCreation                                             making this true will execute the sharing task upon creation regardless of next trigger
      --expiration string                                             Timestamp for the termination of the task
  -f, --file file                                                     Read request body from the specified file
  -h, --help                                                          help for create
      --interval int                                                  Duration in seconds to wait between retries, at least 1 (default 1)
      --message string                                                Message along with sharing task
      --name string                                                   (Required) Name of this sharing task
  -q, --quiet                                                         Return only IDs from the command
      --raw                                                           Return original response from server without any processing
      --recipients-DLGroups unknowns                                  List of recipients. An internal recipient is represented by their user id.
      --recipients-DLUsers unknowns                                   List of recipients. An internal recipient is represented by their user id.
      --recipients-emailAddresses strings                             List of recipients. An internal recipient is represented by their user id.
      --recipients-userIds-alertingTaskRecipientErrors-added string   Timestamp for the creation of the error
      --recipients-userIds-alertingTaskRecipientErrors-value string   Identifier for type of error occurring on alerting task
                                                                      Allowed values: "USER_IS_DELETED", "USER_DISABLED_IN_QCS", "NO_ACCESS_TO_APP", "UNSUBSCRIBED_FROM_ALERT", "CONDITION_EVAL_ERROR", "USER_DISABLED_IN_ALERT_BY_OWNER", "MAX_ALERTS_LIMIT_REACHED"
      --recipients-userIds-enabled                                    Whether this recipient can receive alerts.
      --recipients-userIds-groups strings                             A list of associated groups. If a user is added individually the "addedIndividually" pseudo group is included
      --recipients-userIds-subscribed                                 Whether this recipient is subscribed to alerts of a task
      --recipients-userIds-taskRecipientErrors-timestamp string       Timestamp for the creation of the error
      --recipients-userIds-taskRecipientErrors-value string           Identifier for type of error occurring on sharing task specific for recipient
                                                                      Allowed values: "USER_IS_DELETED", "USER_DISABLED_IN_QCS", "NO_ACCESS_TO_APP", "UNSUBSCRIBED_FROM_SHARING", "USER_DISABLED_IN_SHARING_BY_OWNER", "CHART_NOT_FOUND", "APP_NOT_FOUND", "SHEET_NOT_FOUND", "ENGINE_POD_NOT_AVAILABLE", "CHART_TYPE_NOT_ALLOWED", "GENERIC_EXECUTION_FAILURE", "USER_NOT_FOUND_DL", "USER_DISABLED_IN_DL", "FILTER_NOT_FOUND", "BOOKMARK_NOT_FOUND"
      --recipients-userIds-value string                               User ID of recipient (internal user).
      --retentionPolicy-historySize int                               Number indicating the size of the window which stores the history. For Chart monitoring, the size should be 10.
      --retentionPolicy-overrideInterval string                       Using RFC-5545 provide the time interval in which the previous generated can be overridden with the newly generated report. For Chart monitoring, interval should be FREQ=DAILY;INTERVAL=1
      --retry int                                                     Number of retries to do before failing, max 10
      --scheduleOptions-endDateTime string                            EndDateTime is a local date time with respect to the above timezone parameter. If the timezone parameter is missing, then the timezone used is the one retrieved from user infos. Therefore ISO8601 time offsets are not allowed (e.g. "2026-01-02T16:04:05Z" or "2026-01-02T16:04:05+01"), if passed an error will be returned. EndDateTime is an optional parameter, when not set or when it's an empty string, the recurrence is intended to be never ending.
      --scheduleOptions-recurrence strings                            List of RRULEs for SCHEDULED triggers, as specified in RFC5545. Note that DTSTART and DTEND, UNTIL lines are not allowed in this field; start and end times are specified in the start and end fields. RDATE and EXDATE lines are not currently supported. EXRULE is not supported since it is deprecated by RFC5545. It is mandatory if the trigger type is SCHEDULED. At least 1 rule must be set and maximum 5 rules are allowed.
      --scheduleOptions-startDateTime string                          StartDateTime is a local date time with respect to the above timezone parameter. If the timezone parameter is missing, then the timezone used is the one retrieved from user infos. Therefore ISO8601 time offsets are not allowed (e.g. "2026-01-02T16:04:05Z" or "2026-01-02T16:04:05+01"), if passed an error will be returned. StartDateTime should not be older than 1 year from current date. StartDateTime is an optional parameter, when not set or when it's an empty string, its value is set to the current local date time.
      --scheduleOptions-timezone string                               The timezone for time calculations in SCHEDULED triggers, optional.
      --sharePointFolder string                                       the SharePoint folder to upload the report to
      --spaceId string                                                Space ID of the sharing task
      --startTime string                                              Time to start capturing the history
      --state-fields unknowns                                         Selected fields that led to discovery of monitored Insight Advisor chart
      --state-queryItems unknowns                                     Query that led to discovery of monitored Insight Advisor chart
      --state-selections-displayName string                           State of the selections and jsOpts
      --state-selections-displayValues strings                        State of the selections and jsOpts
      --state-selections-isNumeric                                    State of the selections and jsOpts
      --state-selections-name string                                  State of the selections and jsOpts
      --state-selections-stateName string                             State of the selections and jsOpts
      --state-selections-values strings                               State of the selections and jsOpts
      --subType string                                                (Deprecated) the sharing task resource mashup sub type.
                                                                      Allowed values: "pdf", "pptx", "xlsx", "html", "docx"
      --tags strings                                                  used to assign sharing task to a collection bucket (tags)
      --templates unknowns                                            
      --templates-chartData-appId string                              ID of app
      --templates-chartData-heightPx int                              heightPx of chart
      --templates-chartData-jsOpts unknown                            Visualization state from client as a string json value. Can include language, theme, viewState etc.
      --templates-chartData-objectDef unknown                         Session chart object definition
      --templates-chartData-objectId string                           ID of object
      --templates-chartData-outDpi int                                outDpi of chart
      --templates-chartData-outZoom int                               outZoom of chart
      --templates-chartData-patches unknowns                          Soft property changes on chart
      --templates-chartData-persistentBookmarkIncludeVariables        Flag to configure the persistent bookmark to use variables.
      --templates-chartData-sheetId string                            sheetId of app
      --templates-chartData-widthPx int                               widthPx of chart
      --templates-fileAlias string                                    fileAlias provide an opaqueId for the client which can be used to filter and select the report generated
      --templates-fileName string                                     fileName to be used when generating the report
      --templates-fileTimeStamp string                                file name timestamp to be used when generating the report
                                                                      Allowed values: "yyyy-MM-dd", "yyyy-MM-dd_HH-mm", "yyyyMMdd", "yyyyMMdd_HH-mm"
      --templates-multiSheetData-appId string                         ID of app
      --templates-multiSheetData-heightPx int                         heightPx of chart, must be 0 or omitted for autofit.
      --templates-multiSheetData-isPrivate                            optional value to indicate that this sheet is private
      --templates-multiSheetData-jsOpts unknown                       Sheet state from client as a string json value. Can include language, theme, viewState etc.
      --templates-multiSheetData-jsOptsById key:unknown               array of sheet data for multi-sheet type template
      --templates-multiSheetData-patchesById key:unknowns             array of sheet data for multi-sheet type template
      --templates-multiSheetData-persistentBookmarkIncludeVariables   Flag to configure the persistent bookmark to use variables
      --templates-multiSheetData-resizeType string                    Currently only autofit is supported.
                                                                      If omitted, autofit is the default.
                                                                      The type of resize to be performed:
                                                                        - none is used to export a visualization, sheet as is (e.g. normal size), regardless its size. This may result in cropping.
                                                                        - autofit automatically fits the visualization, sheet into the output size (i.e. A4, A3 etc.). Any provided resizeData parameter will be ignored for this configuration.
                                                                        - fit fits the visualization, sheet into the area specified in resizeData. The content will be rescaled to fit in that area.
                                                                      Allowed values: "none", "fit", "autofit"
      --templates-multiSheetData-sheetId string                       ID of sheet
      --templates-multiSheetData-sheetName string                     an optional name for the sheet
      --templates-multiSheetData-widthPx int                          widthPx of chart, must be 0 or omitted for autofit.
      --templates-sheetData-appId string                              (Deprecated) ID of app
      --templates-sheetData-heightPx int                              (Deprecated) heightPx of chart
      --templates-sheetData-isPrivate                                 (Deprecated) optional value to indicate that this sheet is private (used in multi-sheet sharing)
      --templates-sheetData-jsOpts unknown                            (Deprecated) Sheet state from client as a string json value. Can include language, theme, viewState etc.
      --templates-sheetData-jsOptsById key:unknown                    (Deprecated) 
      --templates-sheetData-patchesById key:unknowns                  (Deprecated) 
      --templates-sheetData-sheetId string                            (Deprecated) ID of sheet
      --templates-sheetData-sheetName string                          (Deprecated) an optional name for the sheet (used in multi-sheet sharing)
      --templates-sheetData-widthPx int                               (Deprecated) widthPx of chart
      --templates-storyData-appId string                              ID of app
      --templates-storyData-storyId string                            ID of story
      --templates-subType string                                      
                                                                      Allowed values: "image", "snapshot", "pdf", "pptx", "xlsx", "qpxp", "qhtml", "docx"
      --templates-type string                                         
                                                                      Allowed values: "file", "chart", "story", "sheet", "multi-sheet", "excel", "pixel-perfect", "html", "powerpoint", "word"
      --transportChannels strings                                     the transport type for the report
                                                                      Allowed values: "email", "sharepoint"
      --trigger-executeOnAppReload                                    Toggle for executing sharing task on app reload.
      --trigger-executionHistoryInterval string                       To prevent overflow in the history, setting this to daily store the chart of a previous day in the history and maintain the live version with the tag latest.
                                                                      Allowed values: "minutely", "hourly", "daily", "weekly", "monthly", "quarterly", "yearly"
      --trigger-recurrence strings                                    List of RRULE lines for a recurring event, as specified in RFC5545. Note that DTSTART and DTEND, UNTIL lines are not allowed in this field; event start and end times are specified in the start and end fields. RDATE and EXDATE lines are not currently supported. EXRULE is not supported since it is deprecated by RFC5545. This field is omitted for single events.
      --type string                                                   (Required) the sharing task resource type.
                                                                      Allowed values: "chart-monitoring", "chart-sharing", "sheet-sharing", "template-sharing"
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
