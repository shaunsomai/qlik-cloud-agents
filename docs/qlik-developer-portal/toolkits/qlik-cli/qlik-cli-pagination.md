---
source: https://qlik.dev/toolkits/qlik-cli/qlik-cli-pagination/
last_updated: 2025-03-13T10:47:32+01:00
---

# How pagination works in qlik-cli

## Pagination

Pagination is the process of retrieving data efficiently by breaking down complex outputs into smaller manageable sets.
This helps to save resources and also provides a better experience for the user.

There are several ways to handle pagination. This resource is the technical documentation of specific functionality and
design flows in `qlik-cli`.

To learn more about pagination, sorting and filtering on the Qlik platform, see [Pagination, sorting, filtering](https://qlik.dev/apis/rest/pagination-sorting-filtering).

The `qlik-cli` has built-in logic around pagination, to simplify the tool's usage across different APIs and resources.

Most API endpoints expose a *limit* query parameter, with a *default*, *minimum* and *maximum* value.

> **Note:** `qlik-cli` paginates automatically in the background if needed, fetching and returning resources up to the number
> specified with the `--limit` flag.
>
> - If you don't specify `--limit`, `qlik-cli` , the API's default per-request maximum limit applies. `qlik-cli` may
>   return only a subset of all resources.
> - If you set `--limit` to a value higher than the API's per-request maximum limit, `qlik-cli` makes additional requests
>   automatically until it retrieves the specified number of resources or there are no more results.
> - There's no flag to fetch all resources explicitly. To fetch all resources, you must set `--limit` to a value higher
>   than the total number of resources.
> - You can use the `--verbose` flag to inspect the API requests.
> - The `--raw` flag disables automatic pagination and returns only the first page of results, including pagination
>   details such as `links.next`.

Check the *verbose* logs for a more detailed example of how the pagination works.
In the example below [`GET /v1/items`](https://qlik.dev/apis/rest/items/#%23%2Fentries%2Fv1%2Fitems-get)
has a maximum limit of `100`. If `200` is passed using the `--limit` flag to `qlik-cli`,
then the tool will paginate once.

```shell
$ qlik item ls --resourceType "app,qvapp" --limit 200 --verbose | grep GET

GET https://qcs.us.qlikcloud.com/api/v1/items?limit=100&resourceType=app%2Cqvapp
* Establishing connection to: qcs.us.qlikcloud.com:443
* TLS Handshake started
* TLS Handshake done (101ms), version: TLS v1.3
* Connection established (200ms)
> Host: qcs.us.qlikcloud.com
> User-Agent: qlik-cli/v2.15.1-dev (darwin)
> Authorization: Bearer **omitted**
> Content-Type: application/json
> Referer: https://qcs.us.qlikcloud.com/
> Accept-Encoding: gzip
< Cache-Control: no-store
< Connection: keep-alive
< Content-Type: application/json; charset=utf-8
< Date: Mon, 17 Oct 2022 10:49:59 GMT
< Pragma: no-cache
< Ratelimit-Limit: 10
< Ratelimit-Remaining: 10
< Ratelimit-Reset: 1666003857
< Strict-Transport-Security: max-age=15724800; includeSubDomains
< X-B3-Traceid: 000000000000000096d6858d0439d090
Response time: 2s
Status: 200 OK
GET https://qcs.us.qlikcloud.com/api/v1/items?limit=100&next=KQAAAAljcmVhdGVkQXQASTXjAWoBAAAHX2lkAFysg-R3lykAAcwBjwA&resourceType=app%2Cqvapp
* Establishing connection to: qcs.us.qlikcloud.com:443
* Connection established (0ms)
> Host: qcs.us.qlikcloud.com
> User-Agent: qlik-cli/v2.15.1-dev (darwin)
> Authorization: Bearer **omitted**
> Content-Type: application/json
> Referer: https://qcs.us.qlikcloud.com/
> Accept-Encoding: gzip
< Cache-Control: no-store
< Connection: keep-alive
< Content-Type: application/json; charset=utf-8
< Date: Mon, 17 Oct 2022 10:49:59 GMT
< Pragma: no-cache
< Ratelimit-Limit: 10
< Ratelimit-Remaining: 10
< Ratelimit-Reset: 1666003859
< Strict-Transport-Security: max-age=15724800; includeSubDomains
< X-B3-Traceid: 0000000000000000b27fdb1a38a07999
Response time: 401ms
Status: 200 OK
```
