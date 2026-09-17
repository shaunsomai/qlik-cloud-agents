---
source: https://qlik.dev/toolkits/qlik-cli/space/space-assignment-update/
last_updated: 2025-06-18T09:34:47+02:00
---

# space assignment update

## qlik space assignment update

Update an assignment for a space

### Synopsis

Updates a single assignment by assignment ID. Use `GET /spaces/{spaceId}/assignments` to list all users and groups assigned to the space and their assignment ID. The complete list of roles must be provided.

```
qlik space assignment update <assignmentId> [flags]
```

### Options

```
  -f, --file file        Read request body from the specified file
  -h, --help             help for update
      --interval int     Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet            Return only IDs from the command
      --raw              Return original response from server without any processing
      --retry int        Number of retries to do before failing, max 10
      --roles strings    The roles assigned to the assigneeId. For the full list of roles assignable in this space type, call ˋGET /spaces/{spaceId}ˋ and inspect the ˋmeta.assignableRolesˋ object.
                         Allowed values: "consumer", "contributor", "dataconsumer", "datapreview", "facilitator", "operator", "producer", "publisher", "basicconsumer", "codeveloper"
      --spaceId string   (Required) The ID of the space of the assignment.
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
