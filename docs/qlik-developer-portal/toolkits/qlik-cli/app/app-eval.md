---
source: https://qlik.dev/toolkits/qlik-cli/app/app-eval/
last_updated: 2025-06-18T09:34:47+02:00
---

# app eval

## qlik app eval

Evaluate a list of measures and dimensions

### Synopsis

Evaluate a list of measures and dimensions. To evaluate a measure for a specific dimension use the \<measure> by \<dimension> notation. If dimensions are omitted then the eval will be evaluated over all dimensions. Default number of rows returned is 20, but can be specified using the rows flag.

```
qlik app eval [<measure>...] [by <dimension>...] [where [<dimension> is <value>]...] [flags]
```

### Examples

```
qlik app eval "Count(a)" // returns the number of values in field "a"
qlik app eval "1+1" // returns the calculated value for 1+1
qlik app eval "Avg(Sales)" by "Region" "Category" // returns the average of measure "Sales" for dimension "Region" and "Category"
qlik app eval by "Region" // Returns the values for dimension "Region"
qlik app eval by "Region" --rows 5000 // Specifies the number of rows that should be returned in the result
qlik app eval "Count(Dishes)" by "Restaurant" where "Cuisine" is "Italian" // Count the number of dishes for Italian restaurants
```

### Options

```
  -a, --app string   Name or identifier of the app
  -h, --help         help for eval
      --no-data      Open app without data
      --rows int     Number of rows that should be included in the eval result (default 20)
  -t, --traffic      Log JSON websocket traffic to stderr
      --ttl string   The Engine session's time to live in seconds (default "0")
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
