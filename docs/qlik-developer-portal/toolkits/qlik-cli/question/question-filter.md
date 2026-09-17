---
source: https://qlik.dev/toolkits/qlik-cli/question/question-filter/
last_updated: 2025-06-18T09:34:47+02:00
---

# question filter

## qlik question filter

Returns NL metrics based on provided app IDs the user has access to

### Synopsis

Returns NL metrics based on provided app IDs the user has access to.

```
qlik question filter [flags]
```

### Options

```
  -f, --file file       Read request body from the specified file
      --filter string   (Required) The advanced filtering to use for the query. Refer to [RFC 7644](https://www.rfc-editor.org/rfc/rfc7644#section-3.4.2.2) for the syntax.
                        
                        Filter on createdAt and updatedAt fields are encouraged and support ˋeqˋ, ˋneˋ, ˋgtˋ, ˋgeˋ, ˋltˋ, ˋleˋ comparison operators along with ˋandˋ and ˋorˋ logical operators.
                        
                        Filter on tenantId field is not supported.
                        
                        ˋcoˋ, ˋswˋ and ˋewˋ operators are not supported.
                        
                        Examples:
                        ˋˋˋ
                        appId eq 'appId1'
                        ˋˋˋ
                        ˋˋˋ
                        (appId eq 'appId1' or appId eq 'appId2')
                        ˋˋˋ
                        ˋˋˋ
                        (appId eq 'appId1' or appId eq 'appId2') and (createdAt gt '2022-08-03T00:00:00.000Z' and createdAt lt '2022-08-04T00:00:00.000Z')
                        ˋˋˋ
                        
                        ˋˋˋ
                        (appId eq 'appId1') and (createdAt ge '2022-08-03T00:00:00.000Z')
                        ˋˋˋ
                        
                        ˋˋˋ
                        (appId eq 'appId1') and (createdAt le '2022-08-23:59:59.000Z')
                        ˋˋˋ
                        
                        ˋˋˋ
                        (appId eq 'appId1') and (questionId eq '12345')
                        ˋˋˋ
  -h, --help            help for filter
      --interval int    Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int       The preferred number of entries returned
      --page string     A cursor pointing to the page of data to retrieve.
  -q, --quiet           Return only IDs from the command
      --raw             Return original response from server without any processing
      --retry int       Number of retries to do before failing, max 10
      --sort string     A single field from the data model on which to sort the response. The '+' or '-' operator may be used to specify ascending or desending order.
                        Allowed values: "createdAt", "updatedAt", "+createdAt", "+updatedAt", "-createdAt", "-updatedAt"
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
