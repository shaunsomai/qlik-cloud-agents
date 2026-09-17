---
source: https://qlik.dev/toolkits/qlik-cli/encryption/encryption-keyprovider-migrate/
last_updated: 2025-06-18T09:34:47+02:00
---

# encryption keyprovider migrate

## qlik encryption keyprovider migrate

Migrate existing cipherkeys from current key provider to requested key provider

### Synopsis

Migrate the active key from one provider to another. The migration process may take some time to complete, however this process will not impact users, and the tenant will continue to function normally during the migration. Use the migration details endpoint to monitor migration progress.

```
qlik encryption keyprovider migrate <arnFingerPrint> [flags]
```

### Options

```
  -h, --help           help for migrate
      --interval int   Duration in seconds to wait between retries, at least 1 (default 1)
  -q, --quiet          Return only IDs from the command
      --raw            Return original response from server without any processing
      --retry int      Number of retries to do before failing, max 10
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
