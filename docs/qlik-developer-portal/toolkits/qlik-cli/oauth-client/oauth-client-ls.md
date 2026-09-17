---
source: https://qlik.dev/toolkits/qlik-cli/oauth-client/oauth-client-ls/
last_updated: 2026-06-03T09:30:31+02:00
---

# oauth-client ls

## qlik oauth-client ls

List OAuth clients

### Synopsis

Retrieve all OAuth clients.

```
qlik oauth-client ls [flags]
```

### Options

```
      --filter string   The filter query that should be used to filter the list of oauth clients.  The filter syntax is defined in RFC 7644. Valid attributes for filtering are ˋclientIdˋ, ˋclientNameˋ, ˋappTypeˋ, and ˋtenantIdˋ.
  -h, --help            help for ls
      --interval int    Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int       The total number of resources to retrieve.
      --next string     The next page cursor
      --prev string     The previous page cursor
  -q, --quiet           Return only IDs from the command
      --raw             Return original response from server without any processing
      --retry int       Number of retries to do before failing, max 10
      --sort string     The attribute to sort by, beginning with + for ascending and - for descending. Valid attributes for sorting are clientId, clientName, appType, tenantId, createdAt, updatedAt.
      --totalResults    Boolean query parameter that determines if the total count of results should be included in the response. If true, the response includes the total number of results in the ˋtotalResultsˋ field. If false or not included in the query, ˋtotalResultsˋ will be excluded from the response.
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
