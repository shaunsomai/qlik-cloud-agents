---
source: https://qlik.dev/toolkits/enigma-go/
last_updated: 2025-05-20T15:25:50Z
---

# Enigma-go overview

enigma-go is a library used for communication with the Qlik Associative Engine
in Golang environments. Examples of use may be building your own analytics tools,
back-end services, or other tools communicating with a Qlik Associative Engine.

## Installation

```bash
go get -u github.com/qlik-oss/enigma-go/v4
```

## Get started

Connecting to a Qlik Associative Engine and interacting with an app
involves at least the following steps:

1. Create and set up a Dialer object with TLS configuration, etc.
2. Open a WebSocket to the Qlik Associative Engine using the Dial function in
   the Dialer.
3. Open or create an app using openDoc or createApp.

Refer to the [examples](https://github.com/qlik-oss/enigma-go/tree/master/examples)
section for more information.

## Schemas

enigma-go includes generated API code that's based on the latest available
Qlik Associative Engine schema.

When a new schema is available, a new version of enigma-go is released as well.
