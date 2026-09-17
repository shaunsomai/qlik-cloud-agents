---
source: https://qlik.dev/toolkits/qlik-cli/scheduling/scheduling-task-update/
last_updated: 2026-06-03T09:30:31+02:00
---

# scheduling task update

## qlik scheduling task update

Replace a task

### Synopsis

Replaces the full definition of a specific task with the supplied payload. All fields not included in the request body are reset to their defaults. If the task is owned by another user, ownership is transferred to the requesting user. Use `PATCH` instead to apply a partial update.

```
qlik scheduling task update <taskId> [flags]
```

### Options

```
      --annotations strings                                       A list of terms describing the workflow's intended purpose, subject areas, or other important qualities.
      --description string                                        A human-readable description of the workflow's purpose.
      --enabled                                                   Indicates whether the task is enabled. Disabled tasks will not trigger automatically.
      --events-correlation-contextAttributeName string            The name of the CloudEvent extension context attribute to match on.
                                                                  Allowed values: "id", "status", "appId", "spaceId", "datasetId"
      --events-correlation-contextAttributeValue string           The expected value of the CloudEvent extension context attribute.
      --events-dataOnly                                           When ˋtrueˋ, only the event payload is accessible to consuming workflow states. When ˋfalseˋ, both the payload and context attributes are accessible.
      --events-name string                                        A unique name identifying this event definition within the workflow.
      --events-source string                                      The CloudEvents source attribute identifying the origin of the event.
                                                                  Allowed values: "system-events.task", "dataset.updated"
      --events-type string                                        The CloudEvents type attribute identifying the kind of event.
                                                                  Allowed values: "com.qlik.v1.task.run.finished", "com.qlik/active-analytics-orch"
  -f, --file file                                                 Read request body from the specified file
  -h, --help                                                      help for update
      --interval int                                              Duration in seconds to wait between retries, at least 1 (default 1)
      --keepActive                                                When ˋtrueˋ, workflow instances are not terminated when there are no active execution paths. Instances can be ended via a terminate end definition or a configured ˋworkflowExecTimeoutˋ.
      --key string                                                An optional expression used to generate a domain-specific workflow instance identifier.
      --metadata-createdBy string                                 The user ID of the user who created the task.
      --metadata-disabledCode string                              The reason the task is currently disabled.
                                                                  Allowed values: "MANUALLY", "CONSECUTIVE-FAILURES", "APP-SCRIPT-UPDATED", "OWNER-DELETED", "OWNER-DISABLED", "APP-MOVED-SPACE"
      --metadata-migratedFrom string                              The unique identifier of the legacy reload task this task was migrated from, if applicable.
      --metadata-orchestration-attrs key:string                   Additional attributes of the orchestration instance associated with this task in the scheduling service.
      --metadata-orchestration-id string                          (Required) The unique identifier of the orchestration instance associated with this task in the scheduling service.
      --metadata-orchestration-lastRun-executedAs string          The user ID of the user on whose behalf the task was executed.
      --metadata-orchestration-lastRun-id string                  (Required) The unique identifier of the task run.
      --metadata-orchestration-lastRun-status string              (Required) The current status of the task run.
                                                                  Allowed values: "RUNNING", "SUCCEEDED", "FAILED"
      --metadata-orchestration-lastRun-triggeredBy string         (Required) The identity or event that triggered the task run.
      --metadata-orchestration-lastRun-workerId string            (Required) The unique identifier of the worker that executed the job. For example, a reload run carries the reload ID from the engine, and an automation run carries the automation run ID.
      --metadata-orchestration-lastRun-workerType string          (Required) The type or name of the target system that executed the run.
      --metadata-orchestration-type int                           (Required) The type identifier of the orchestration system handling this task.
                                                                  Allowed values: "0", "1", "2", "3"
      --metadata-ownerId string                                   The user ID of the task owner.
      --metadata-resourceName string                              The name of the resource on which the task was created.
      --metadata-resourceSubType string                           The subtype of resource on which the task was created.
      --metadata-resourceType string                              The type of resource on which the task was created.
      --metadata-scriptOwnerId string                             The user ID of the owner whose script context is used when running the task.
      --metadata-spaceId string                                   The unique identifier of the space the task operates in.
      --metadata-spaceType string                                 The type of space the task operates in.
                                                                  Allowed values: "personal", "shared", "managed"
      --metadata-tenantId string                                  The unique identifier of the tenant the task operates in.
      --metadata-topology-isChild                                 When ˋtrueˋ, this task is triggered by one or more parent tasks.
      --metadata-topology-isParent                                When ˋtrueˋ, this task has one or more downstream dependent tasks.
      --metadata-trigger-id string                                (Required) The unique identifier of the trigger associated with this task.
      --metadata-trigger-type int                                 (Required) The type identifier of the trigger associated with this task.
                                                                  Allowed values: "0", "1", "2", "3", "4"
      --metadata-updatedAt string                                 The UTC timestamp when the task was last updated.
      --metadata-usage string                                     The product domain in which the resource is used. Defaults to ˋANALYTICSˋ when not present.
                                                                  Allowed values: "ANALYTICS", "DATA_PREPARATION", "DATAFLOW_PREP", "SINGLE_TABLE_PREP"
      --name string                                               (Required) The name that identifies the workflow definition. Combined with ˋversionˋ, the name forms a unique identifier for the task.
  -q, --quiet                                                     Return only IDs from the command
      --raw                                                       Return original response from server without any processing
      --resourceId string                                         The unique identifier of the resource this task operates on. The value supplied in a request body is ignored and is derived automatically from ˋstatesˋ.
      --retry int                                                 Number of retries to do before failing, max 10
      --specVersion string                                        (Required) The Serverless Workflow specification version used by this task.
      --start-schedule string|unknown                             The start definition for a workflow, including optional schedule configuration.
      --start-schedule-cron string                                The start definition for a workflow, including optional schedule configuration.
      --start-schedule-cron-expression string                     A cron expression describing when the workflow instance should be created.
      --start-schedule-cron-validUntil string                     The date and time (ISO 8601 format) after which this cron expression is no longer active.
      --start-schedule-endDateTime string                         The date and time (ISO 8601 format) when the workflow schedule ends.
      --start-schedule-interval string                            A repeating time interval in ISO 8601 format that defines when workflow instances are automatically created.
      --start-schedule-recurrence string                          An RRULE recurrence rule string defining when the workflow recurs.
      --start-schedule-startDateTime string                       The date and time (ISO 8601 format) when the workflow schedule begins.
      --start-schedule-timezone string                            The timezone name used to evaluate the interval and cron expression. Defaults to ˋUTCˋ.
      --start-stateName string                                    The name of the starting workflow state.
      --states unknowns                                           The list of state definitions that compose the workflow.
      --states-compensatedBy string                               The unique name of a workflow state responsible for compensating this state if it fails.
      --states-end                                                Marks this state as a terminal state in the workflow.
      --states-exclusive                                          When ˋtrueˋ, consuming any one of the defined events causes its associated actions to execute. When ˋfalseˋ, all defined events must be consumed before actions are performed.
      --states-name string                                        The name of this state, unique within the workflow.
      --states-onEvents-actionMode string                         Specifies whether actions are performed sequentially or in parallel.
                                                                  Allowed values: "SEQUENTIAL", "PARALLEL"
      --states-onEvents-actions unknowns                          Actions to perform when the matched events are consumed.
      --states-onEvents-actions-condition string                  An expression that must evaluate to ˋtrueˋ for this action to be performed. When ˋfalseˋ, the action is skipped.
      --states-onEvents-actions-functionRef string                A reference to a function to invoke, either as a name string or a structured object.
      --states-onEvents-actions-functionRef-arguments unknown     Arguments to pass to the function.
      --states-onEvents-actions-functionRef-invoke string         Specifies whether the function is invoked synchronously or asynchronously.
                                                                  Allowed values: "SYNC", "ASYNC"
      --states-onEvents-actions-functionRef-refName string        The name of the function to invoke.
                                                                  Allowed values: "app.reload"
      --states-onEvents-actions-functionRef-selectionSet string   A GraphQL selection set string. Only applicable when the function type is ˋgraphqlˋ.
      --states-onEvents-actions-name string                       A unique name for this action within the workflow.
      --states-onEvents-actions-nonRetryableErrors strings        Workflow error references for which this action must not be retried. Used only when ˋautoRetriesˋ is ˋtrueˋ.
      --states-onEvents-actions-retryRef string                   A reference to a defined workflow retry policy. If absent, the default retry policy applies.
      --states-onEvents-actions-retryableErrors strings           Workflow error references for which this action must be retried. Used only when ˋautoRetriesˋ is ˋfalseˋ.
      --states-onEvents-eventRefs strings                         References to one or more unique event names defined in the workflow events list.
      --states-timeouts-actionExecTimeout string                  The maximum duration for executing a single action, expressed as an ISO 8601 duration string or an expression that evaluates to one.
      --states-timeouts-eventTimeout string                       The maximum duration to wait for the defined events to be received, expressed as an ISO 8601 duration string or an expression that evaluates to one.
      --states-timeouts-stateExecTimeout string                   The maximum duration for executing this state, expressed as an ISO 8601 duration string or an expression that evaluates to one.
      --states-type string                                        The state type. Must be ˋEVENTˋ for event-driven states.
                                                                  Allowed values: "EVENT"
      --version string                                            The semantic version of the workflow definition.
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
