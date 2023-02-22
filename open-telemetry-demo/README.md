# OpenTelemetry

## Instrumentation

- `app.py`: A sample HTTP server with automatic and manual instrumentation.

- Run the `app.py` with the following code to output traces in the console.

    ```shell
    opentelemetry-instrument \
        --traces_exporter console \
        --metrics_exporter console \
        flask run
    ```

    Sample traces:

    ```json

    {
        "name": "do_roll",
        "context": {
            "trace_id": "0x017e43e3df28b000624dc285b83ea032",
            "span_id": "0x44a27aa40bfa3a77",
            "trace_state": "[]"
        },
        "kind": "SpanKind.INTERNAL",
        "parent_id": "0x1c18ad393745c67f",
        "start_time": "2023-02-22T04:08:05.765445Z",
        "end_time": "2023-02-22T04:08:05.765539Z",
        "status": {
            "status_code": "UNSET"
        },
        "attributes": {
            "roll.value": 6
        },
        "events": [],
        "links": [],
        "resource": {
            "attributes": {
                "telemetry.sdk.language": "python",
                "telemetry.sdk.name": "opentelemetry",
                "telemetry.sdk.version": "1.15.0",
                "telemetry.auto.version": "0.36b0",
                "service.name": "unknown_service"
            },
            "schema_url": ""
        }
    }
    {
        "name": "/",
        "context": {
            "trace_id": "0x017e43e3df28b000624dc285b83ea032",
            "span_id": "0x1c18ad393745c67f",
            "trace_state": "[]"
        },
        "kind": "SpanKind.SERVER",
        "parent_id": null,
        "start_time": "2023-02-22T04:08:05.762902Z",
        "end_time": "2023-02-22T04:08:05.766025Z",
        "status": {
            "status_code": "UNSET"
        },
        "attributes": {
            "http.method": "GET",
            "http.server_name": "127.0.0.1",
            "http.scheme": "http",
            "net.host.port": 5000,
            "http.host": "127.0.0.1:5000",
            "http.target": "/",
            "net.peer.ip": "127.0.0.1",
            "http.user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
            "net.peer.port": 62045,
            "http.flavor": "1.1",
            "http.route": "/",
            "http.status_code": 200
        },
        "events": [],
        "links": [],
        "resource": {
            "attributes": {
                "telemetry.sdk.language": "python",
                "telemetry.sdk.name": "opentelemetry",
                "telemetry.sdk.version": "1.15.0",
                "telemetry.auto.version": "0.36b0",
                "service.name": "unknown_service"
            },
            "schema_url": ""
        }
    }
    ```

## OpenTelemetry Collector

- Configure the OpenTelemetry collector with `/tmp/otel-collector-config.yaml`.

- Run the docker command to acquire and run the collector on port 4317.

    ```shell
    docker run -p 4317:4317 \
        -v `pwd`/tmp/otel-collector-config.yaml:`pwd`/etc/otel-collector-config.yaml \
        otel/opentelemetry-collector:latest \
        --config=`pwd`/etc/otel-collector-config.yaml
    ```

- Now we can run the application with:

    ```shell
    opentelemetry-instrument flask run
    ```

- Traces:

    ```shell
    2023-02-21 23:25:47 Resource SchemaURL: 
    2023-02-21 23:25:47 Resource attributes:
    2023-02-21 23:25:47      -> telemetry.sdk.language: Str(python)
    2023-02-21 23:25:47      -> telemetry.sdk.name: Str(opentelemetry)
    2023-02-21 23:25:47      -> telemetry.sdk.version: Str(1.15.0)
    2023-02-21 23:25:47      -> telemetry.auto.version: Str(0.36b0)
    2023-02-21 23:25:47      -> service.name: Str(unknown_service)
    2023-02-21 23:25:47 ScopeSpans #0
    2023-02-21 23:25:47 ScopeSpans SchemaURL: 
    2023-02-21 23:25:47 InstrumentationScope app 
    2023-02-21 23:25:47 Span #0
    2023-02-21 23:25:47     Trace ID       : 5f4f1847915160c6e9f8d78784d47748
    2023-02-21 23:25:47     Parent ID      : 1b7679b1d2ffb203
    2023-02-21 23:25:47     ID             : 8e7a4858819d7309
    2023-02-21 23:25:47     Name           : do_roll
    2023-02-21 23:25:47     Kind           : Internal
    2023-02-21 23:25:47     Start time     : 2023-02-22 04:25:45.813508 +0000 UTC
    2023-02-21 23:25:47     End time       : 2023-02-22 04:25:45.813551 +0000 UTC
    2023-02-21 23:25:47     Status code    : Unset
    2023-02-21 23:25:47     Status message : 
    2023-02-21 23:25:47 Attributes:
    2023-02-21 23:25:47      -> roll.value: Int(3)
    2023-02-21 23:25:47 Span #1
    2023-02-21 23:25:47     Trace ID       : 55ddd12b096d0bbda6d697fcf4f4ef85
    2023-02-21 23:25:47     Parent ID      : 9dffe39fdb8db767
    2023-02-21 23:25:47     ID             : bdf0227df1e702a6
    2023-02-21 23:25:47     Name           : do_roll
    2023-02-21 23:25:47     Kind           : Internal
    2023-02-21 23:25:47     Start time     : 2023-02-22 04:25:47.512873 +0000 UTC
    2023-02-21 23:25:47     End time       : 2023-02-22 04:25:47.513008 +0000 UTC
    2023-02-21 23:25:47     Status code    : Unset
    2023-02-21 23:25:47     Status message : 
    2023-02-21 23:25:47 Attributes:
    2023-02-21 23:25:47      -> roll.value: Int(4)
    2023-02-21 23:25:47 ScopeSpans #1
    2023-02-21 23:25:47 ScopeSpans SchemaURL: 
    2023-02-21 23:25:47 InstrumentationScope opentelemetry.instrumentation.flask 0.36b0
    2023-02-21 23:25:47 Span #0
    2023-02-21 23:25:47     Trace ID       : 5f4f1847915160c6e9f8d78784d47748
    2023-02-21 23:25:47     Parent ID      : 
    2023-02-21 23:25:47     ID             : 1b7679b1d2ffb203
    2023-02-21 23:25:47     Name           : /
    2023-02-21 23:25:47     Kind           : Server
    2023-02-21 23:25:47     Start time     : 2023-02-22 04:25:45.812607 +0000 UTC
    2023-02-21 23:25:47     End time       : 2023-02-22 04:25:45.813736 +0000 UTC
    2023-02-21 23:25:47     Status code    : Unset
    2023-02-21 23:25:47     Status message : 
    2023-02-21 23:25:47 Attributes:
    2023-02-21 23:25:47      -> http.method: Str(GET)
    2023-02-21 23:25:47      -> http.server_name: Str(127.0.0.1)
    2023-02-21 23:25:47      -> http.scheme: Str(http)
    2023-02-21 23:25:47      -> net.host.port: Int(5000)
    2023-02-21 23:25:47      -> http.host: Str(127.0.0.1:5000)
    2023-02-21 23:25:47      -> http.target: Str(/)
    2023-02-21 23:25:47      -> net.peer.ip: Str(127.0.0.1)
    2023-02-21 23:25:47      -> http.user_agent: Str(Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15)
    2023-02-21 23:25:47      -> net.peer.port: Int(62397)
    2023-02-21 23:25:47      -> http.flavor: Str(1.1)
    2023-02-21 23:25:47      -> http.route: Str(/)
    2023-02-21 23:25:47      -> http.status_code: Int(200)
    2023-02-21 23:25:47 Span #1
    2023-02-21 23:25:47     Trace ID       : 55ddd12b096d0bbda6d697fcf4f4ef85
    2023-02-21 23:25:47     Parent ID      : 
    2023-02-21 23:25:47     ID             : 9dffe39fdb8db767
    2023-02-21 23:25:47     Name           : /
    2023-02-21 23:25:47     Kind           : Server
    2023-02-21 23:25:47     Start time     : 2023-02-22 04:25:47.512001 +0000 UTC
    2023-02-21 23:25:47     End time       : 2023-02-22 04:25:47.513228 +0000 UTC
    2023-02-21 23:25:47     Status code    : Unset
    2023-02-21 23:25:47     Status message : 
    2023-02-21 23:25:47 Attributes:
    2023-02-21 23:25:47      -> http.method: Str(GET)
    2023-02-21 23:25:47      -> http.server_name: Str(127.0.0.1)
    2023-02-21 23:25:47      -> http.scheme: Str(http)
    2023-02-21 23:25:47      -> net.host.port: Int(5000)
    2023-02-21 23:25:47      -> http.host: Str(127.0.0.1:5000)
    2023-02-21 23:25:47      -> http.target: Str(/)
    2023-02-21 23:25:47      -> net.peer.ip: Str(127.0.0.1)
    2023-02-21 23:25:47      -> http.user_agent: Str(Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15)
    2023-02-21 23:25:47      -> net.peer.port: Int(62398)
    2023-02-21 23:25:47      -> http.flavor: Str(1.1)
    2023-02-21 23:25:47      -> http.route: Str(/)
    2023-02-21 23:25:47      -> http.status_code: Int(200)
    2023-02-21 23:25:47     {"kind": "exporter", "data_type": "traces", "name": "logging"}
    2023-02-21 23:26:42 2023-02-22T04:26:42.938Z    info    MetricsExporter {"kind": "exporter", "data_type": "metrics", "name": "logging", "#metrics": 20}
    2023-02-21 23:26:42 2023-02-22T04:26:42.942Z    info    ResourceMetrics #0
    2023-02-21 23:26:42 Resource SchemaURL: 
    2023-02-21 23:26:42 Resource attributes:
    2023-02-21 23:26:42      -> telemetry.sdk.language: Str(python)
    2023-02-21 23:26:42      -> telemetry.sdk.name: Str(opentelemetry)
    2023-02-21 23:26:42      -> telemetry.sdk.version: Str(1.15.0)
    2023-02-21 23:26:42      -> telemetry.auto.version: Str(0.36b0)
    2023-02-21 23:26:42      -> service.name: Str(unknown_service)
    2023-02-21 23:26:42 ScopeMetrics #0
    2023-02-21 23:26:42 ScopeMetrics SchemaURL: 
    2023-02-21 23:26:42 InstrumentationScope opentelemetry.instrumentation.flask 0.36b0
    2023-02-21 23:26:42 Metric #0
    2023-02-21 23:26:42 Descriptor:
    2023-02-21 23:26:42      -> Name: http.server.active_requests
    2023-02-21 23:26:42      -> Description: measures the number of concurrent HTTP requests that are currently in-flight
    2023-02-21 23:26:42      -> Unit: requests
    2023-02-21 23:26:42      -> DataType: Sum
    2023-02-21 23:26:42      -> IsMonotonic: false
    2023-02-21 23:26:42      -> AggregationTemporality: Cumulative
    2023-02-21 23:26:42 NumberDataPoints #0
    2023-02-21 23:26:42 Data point attributes:
    2023-02-21 23:26:42      -> http.method: Str(GET)
    2023-02-21 23:26:42      -> http.host: Str(127.0.0.1:5000)
    2023-02-21 23:26:42      -> http.scheme: Str(http)
    2023-02-21 23:26:42      -> http.flavor: Str(1.1)
    2023-02-21 23:26:42      -> http.server_name: Str(127.0.0.1)
    2023-02-21 23:26:42 StartTimestamp: 2023-02-22 04:25:45.812656 +0000 UTC
    2023-02-21 23:26:42 Timestamp: 2023-02-22 04:26:42.68696 +0000 UTC
    2023-02-21 23:26:42 Value: 0
    ```
