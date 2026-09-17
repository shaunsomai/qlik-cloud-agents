---
source: https://qlik.dev/toolkits/qlik-cli/user/user-ls/
last_updated: 2026-06-03T09:30:31+02:00
---

# user ls

## qlik user ls

List users

### Synopsis

Returns a list of users using cursor-based pagination.

```
qlik user ls [flags]
```

### Options

```
      --fields string   A comma-delimited string of the requested fields per entity. If the 'links' value is omitted, then the entity HATEOAS link will also be omitted.
      --filter string   The advanced filtering to use for the query. Refer to [RFC 7644](https://datatracker.ietf.org/doc/rfc7644/) for the syntax. Cannot be combined with any of the fields marked as deprecated. All conditional statements within this query parameter are case insensitive.
                        
                        The following fields support the ˋeqˋ operator: ˋidˋ, ˋsubjectˋ, ˋnameˋ, ˋemailˋ, ˋstatusˋ, ˋclientIdˋ, ˋassignedRoles.idˋ ˋassignedRoles.nameˋ, ˋassignedGroups.idˋ, ˋassignedGroupsAssignedRoles.nameˋ
                        
                        Additionally, the following fields support the ˋcoˋ operator: ˋnameˋ, ˋemailˋ, ˋsubjectˋ
                        
                        Queries may be rate limited if they differ greatly from these examples:
                        
                        ˋˋˋ
                        (id eq "62716ab404a7bd8626af9bd6" or id eq "62716ac4c7e500e13ff5fa22") and (status eq "active" or status eq "disabled")
                        ˋˋˋ
                        
                        ˋˋˋ
                        name co "query" or email co "query" or subject co "query" or id eq "query" or assignedRoles.name eq "query"
                        ˋˋˋ
                        
                        Any filters for status must be grouped together and applied to the whole query.
                        
                        Valid:
                        
                        ˋˋˋ
                        (name eq "Bob" or name eq "Alice") and (status eq "active" or status eq "disabled")
                        ˋˋˋ
                        
                        Invalid:
                        
                        ˋˋˋ
                        name eq "Bob" or name eq "Alice" and (status eq "active" or status eq "disabled")
                        ˋˋˋ
  -h, --help            help for ls
      --interval int    Duration in seconds to wait between retries, at least 1 (default 1)
      --limit int       The total number of resources to retrieve.
      --next string     Get users that come after this cursor value when sorted. Cannot be used in conjunction with ˋprevˋ.
      --prev string     Get users that come before this cursor value when sorted. Cannot be used in conjunction with ˋnextˋ.
  -q, --quiet           Return only IDs from the command
      --raw             Return original response from server without any processing
      --retry int       Number of retries to do before failing, max 10
      --sort string     The field to sort by, with +/- prefix indicating sort order
                        Allowed values: "name", "+name", "-name", "_id", "+_id", "-_id", "id", "+id", "-id", "tenantId", "+tenantId", "-tenantId", "clientId", "+clientId", "-clientId", "status", "+status", "-status", "subject", "+subject", "-subject", "email", "+email", "-email", "inviteExpiry", "+inviteExpiry", "-inviteExpiry", "createdAt", "+createdAt", "-createdAt"
      --totalResults    Whether to return a total match count in the result. Defaults to false. It will trigger an extra DB query to count, reducing the efficiency of the endpoint.
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
