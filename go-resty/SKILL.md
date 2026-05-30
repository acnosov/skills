---
name: go-resty
description: Use for Resty v3 Go HTTP, REST, and SSE client tasks.
---

# Go Resty

## Overview

Resty v3 is a simple HTTP, REST, and server-sent events client library for Go. It uses the `resty.dev/v3` module path.

```go
require resty.dev/v3
```

Resty v3 improves performance, memory efficiency, and features compared to Resty v2. This skill is for Resty v3 and above.

### Basic HTTP Client

```go
client := resty.New()
defer client.Close()

res, err := client.R().
    EnableTrace().
    Get("https://httpbin.org/get")
fmt.Println(err, res)
fmt.Println(res.Request.TraceInfo())
```

### Basic SSE Client

```go
es := NewEventSource().
    SetURL("https://sse.dev/test").
    OnMessage(func(e any) {
        fmt.Println(e.(*resty.Event))
    }, nil)

err := es.Get()
fmt.Println(err)
```

### Key Features

- Simple and chainable methods
- Multipart and form data
- Request path parameters
- Retry mechanism
- Circuit breaker and circuit breaker policies
- Goroutine and concurrent safety
- Automatic decompression for gzip and deflate
- Basic auth, digest auth, bearer auth, and custom auth
- Request tracing
- Curl command generation
- HTTP/1.1, HTTP/2, and HTTP/3 integration
- Automatic marshal and unmarshal
- Large file upload and progress callbacks
- Download to file
- Redirect policies
- Human-readable and JSON debug logs
- Load balancing and service discovery
- Response body limits and unlimited reads
- Bazel support
- Dynamic TLS certificate reloads
- Custom root and client certificates

### Extension Points

Resty can be extended through these interfaces and hooks:

- Request middleware
- Response middleware
- Content-Type encoder and decoder
- Content decompresser
- Load balancer and service discovery
- Retry strategy, conditions, and hooks
- Circuit breaker policy
- Request functions
- Redirect policy
- Transport `RoundTripper`
- Debug log formatter
- Logger

## Purpose

Use this skill to work with Resty v3 Go client code. Prefer the bundled references over guessing API names, method placement, defaults, or option semantics.

## Workflow

1. Identify the Resty feature area from the task.
2. Read only the relevant reference files from the index below.
3. Confirm whether the code targets Resty v3. If the code uses Resty v2 imports or APIs, call out the version mismatch before applying v3 patterns.
4. Preserve existing project conventions for client construction, error handling, context use, logging, tests, and dependency injection.
5. When adding or changing code, verify with the repository's Go tooling when available, such as `go test ./...`, focused package tests, or `go test` for the touched package.

## Request Construction

- Request bodies: `references/request-body-types.md`
- Query parameters: `references/request-query-params.md`
- Path and raw path parameters: `references/request-path-params.md`
- Form data: `references/form-data.md`
- Multipart forms and file uploads: `references/multipart.md`
- Payloads on methods that usually omit request bodies: `references/allow-payload-on.md`

## Authentication And Security

- Basic, digest, bearer, custom header, and middleware auth: `references/authentication.md`
- Root CA certificates: `references/root-certificates.md`
- Client root CA certificates: `references/client-root-certificates.md`
- Client certificates and mTLS: `references/client-certificates.md`
- OAuth2 client credentials example: `references/example-oauth2-client-credentials.md`
- TLS config on a custom RoundTripper example: `references/example-tls-client-config-on-custom-roundtriper.md`

## Reliability And Networking

- Timeouts: `references/timeout.md`
- Retry mechanism, retry conditions, hooks, and backoff: `references/retry-mechanism.md`
- Circuit breaker: `references/circuit-breaker.md`
- Hedging: `references/hedging.md`
- Redirect policies: `references/redirect-policy.md`
- Load balancer and service discovery: `references/load-balancer-and-service-discovery.md`
- SOCKS5 proxy example: `references/example-socks5-proxy.md`
- Custom DNS resolver example: `references/example-custom-dns-resolver.md`
- HTTP/3 example: `references/example-enable-http3.md`

## Middleware And Extension Points

- Request middleware: `references/request-middleware.md`
- Response middleware: `references/response-middleware.md`
- Content-Type encoders and decoders: `references/content-type-encoder-and-decoder.md`
- Content decompressers: `references/content-decompresser.md`
- Brotli decompression example: `references/example-decompress-brotli.md`
- Zstandard decompression example: `references/example-decompress-zstandard.md`

## Response Handling And Observability

- Automatic response parsing: `references/response-auto-parse.md`
- Save response to file: `references/save-response.md`
- Unlimited response body reads: `references/unlimited-response-body-reads.md`
- Request tracing: `references/request-tracing.md`
- Curl command generation: `references/curl-command.md`
- Debug logging: `references/debug-log.md`
- Redirect history example: `references/example-redirect-history.md`
- Dry run example: `references/example-how-to-do-dry-run.md`

## HTTP Methods And SSE Examples

- GET request example: `references/example-get-request.md`
- POST, PUT, and PATCH request example: `references/example-post-put-patch-request.md`
- DELETE request example: `references/example-delete-request.md`
- OPTIONS, HEAD, and TRACE request example: `references/example-options-head-trace-request.md`
- Server-sent events: `references/server-sent-events.md`

## Version And Feature Notes

- New features and enhancements: `references/new-features-and-enhancements.md`

## Error Handling

- If a requested API is not found in the selected reference file, search the other Resty references before inventing method names.
- If the project uses `github.com/go-resty/resty/v2`, avoid applying `resty.dev/v3` examples without explicitly migrating the import and API usage.
- If behavior depends on transport, TLS, redirects, or retries, read the specific reference for that feature before changing defaults.
