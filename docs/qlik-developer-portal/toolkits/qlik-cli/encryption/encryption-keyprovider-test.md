---
source: https://qlik.dev/toolkits/qlik-cli/encryption/encryption-keyprovider-test/
last_updated: 2025-06-18T09:34:47+02:00
---

# encryption keyprovider test

## qlik encryption keyprovider test

Validate AWS-KMS key access

### Synopsis

Validate a key to check if Qlik Cloud has required access to your AWS account and key policy, and the key configuration. If the key policy or configuration are changed from the required configuration, this may impact your ability to access your tenant.

```
qlik encryption keyprovider test <arnFingerPrint> [flags]
```

### Options

```
  -h, --help           help for test
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
