---
source: https://qlik.dev/toolkits/qlik-cli/task/task-create/
last_updated: 2026-06-03T09:30:31+02:00
---

# task create

## qlik task create

Create a task

### Synopsis

Creates a new task.

```
qlik task create [flags]
```

### Options

```
      --annotations strings                                       List of helpful terms describing the workflows intended purpose, subject areas, or other important qualities
      --description string                                        Workflow description
      --enabled                                                   Indicates whether the task is enabled or not
      --events-correlation-contextAttributeName string            CloudEvent Extension Context Attribute name
                                                                  Allowed values: "id", "status"
      --events-correlation-contextAttributeValue string           CloudEvent Extension Context Attribute value
      --events-dataOnly                                           If ˋtrueˋ, only the Event payload is accessible to consuming Workflow states. If ˋfalseˋ, both event payload and context attributes should be accessible
      --events-name string                                        Unique event name
      --events-source string                                      CloudEvent source
                                                                  Allowed values: "system-events.task"
      --events-type string                                        CloudEvent type
                                                                  Allowed values: "com.qlik.v1.task.run.finished"
  -f, --file file                                                 Read request body from the specified file
  -h, --help                                                      help for create
      --interval int                                              Duration in seconds to wait between retries, at least 1 (default 1)
      --keepActive                                                If 'true', workflow instances is not terminated when there are no active execution paths. Instance can be terminated via 'terminate end definition' or reaching defined 'workflowExecTimeout'
      --key string                                                Optional expression that will be used to generate a domain-specific workflow instance identifier
      --metadata-createdBy string                                 The user ID of the user that created the task
      --metadata-disabledCode string                              why the Task is disabled
                                                                  Allowed values: "MANUALLY", "CONSECUTIVE-FAILURES", "APP-SCRIPT-UPDATED", "OWNER-DELETED", "OWNER-DISABLED"
      --metadata-migratedFrom string                              The ID of the reload-task this one was migrated from (if applicable)
      --metadata-orchestration-attrs key:string                   
      --metadata-orchestration-id string                          (Required) The ID of the orchestration associated with the task in the choreographer
      --metadata-orchestration-type int                           (Required) orchestration system type
                                                                  Allowed values: "0", "1", "2", "3"
      --metadata-ownerId string                                   The user ID of the owner of the task
      --metadata-spaceId string                                   The space ID that the Task will operate in
      --metadata-tenantId string                                  The tenant ID that the Task will operate in
      --metadata-trigger-id string                                (Required) The ID of the Trigger associated with the task in the choreographer
      --metadata-trigger-type int                                 (Required) trigger type
                                                                  Allowed values: "0", "1", "2", "3"
      --metadata-updatedAt string                                 The UTC timestamp when the task was last updated
      --metadata-usage string                                     resource usage. Normally it means in which product domain the resource is used. if this field is not presented, it has default of ˋANALYTICSˋ
                                                                  Allowed values: "ANALYTICS", "DATA_PREPARATION", "DATAFLOW_PREP", "SINGLE_TABLE_PREP"
      --migrateFrom string                                        ID of the reload-task to migrate from the old system (optional).
      --name string                                               (Required) The name that identifies the workflow definition, and which, when combined with its version, forms a unique identifier.
  -q, --quiet                                                     Return only IDs from the command
      --raw                                                       Return original response from server without any processing
      --resourceId string                                         The resource ID of the task. The ˋTask.resourceIdˋ value from user input is ignored and will be calculated automatically from ˋTask.statesˋ.
      --retry int                                                 Number of retries to do before failing, max 10
      --specVersion string                                        (Required) Serverless Workflow schema version
      --start-schedule string|unknown                             
      --start-schedule-cron string                                
      --start-schedule-cron-expression string                     Repeating interval (cron expression) describing when the workflow instance should be created
      --start-schedule-cron-validUntil string                     Specific date and time (ISO 8601 format) when the cron expression invocation is no longer valid
      --start-schedule-endDateTime string                         Specific date and time (ISO 8601 format) when the workflow instance should be terminated
      --start-schedule-interval string                            Time interval (must be repeating interval) described with ISO 8601 format. Declares when workflow instances will be automatically created.
      --start-schedule-recurrence string                          The RRULE recurrence string for chronos job
      --start-schedule-startDateTime string                       Specific date and time (ISO 8601 format) when the workflow instance should be created
      --start-schedule-timezone string                            Timezone name used to evaluate the interval & cron-expression. (default: UTC)
      --start-stateName string                                    Name of the starting workflow state
      --states unknowns                                           State definitions
      --states-compensatedBy string                               Unique Name of a workflow state which is responsible for compensation of this state
      --states-end                                                State end definition
      --states-exclusive                                          If true consuming one of the defined events causes its associated actions to be performed. If false all of the defined events must be consumed in order for actions to be performed
      --states-name string                                        State name
      --states-onEvents-actionMode string                         Specifies how actions are to be performed (in sequence or in parallel)
                                                                  Allowed values: "SEQUENTIAL", "PARALLEL"
      --states-onEvents-actions unknowns                          Actions to be performed if expression matches
      --states-onEvents-actions-condition string                  Expression, if defined, must evaluate to true for this action to be performed. If false, action is disregarded
      --states-onEvents-actions-functionRef string                Actions to be performed if expression matches
      --states-onEvents-actions-functionRef-arguments unknown     Function arguments/inputs
      --states-onEvents-actions-functionRef-invoke string         Specifies if the function should be invoked sync or async
                                                                  Allowed values: "SYNC", "ASYNC"
      --states-onEvents-actions-functionRef-refName string        Name of the referenced function
                                                                  Allowed values: "app.reload"
      --states-onEvents-actions-functionRef-selectionSet string   Only used if function type is 'graphql'. A string containing a valid GraphQL selection set
      --states-onEvents-actions-name string                       Unique action definition name
      --states-onEvents-actions-nonRetryableErrors strings        List of unique references to defined workflow errors for which the action should not be retried. Used only when ˋautoRetriesˋ is set to ˋtrueˋ
      --states-onEvents-actions-retryRef string                   References a defined workflow retry definition. If not defined the default retry policy is assumed
      --states-onEvents-actions-retryableErrors strings           List of unique references to defined workflow errors for which the action should be retried. Used only when ˋautoRetriesˋ is set to ˋfalseˋ
      --states-onEvents-eventRefs strings                         References one or more unique event names in the defined workflow events
      --states-timeouts-actionExecTimeout string                  Action execution timeout duration (literal ISO 8601 duration format or expression which evaluation results in an ISO 8601 duration)
      --states-timeouts-eventTimeout string                       Timeout duration to wait for consuming defined events (literal ISO 8601 duration format or expression which evaluation results in an ISO 8601 duration)
      --states-timeouts-stateExecTimeout string                   Workflow state execution timeout duration (literal ISO 8601 duration format or expression which evaluation results in an ISO 8601 duration)
      --states-type string                                        State type
                                                                  Allowed values: "EVENT"
      --version string                                            Workflow version
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
