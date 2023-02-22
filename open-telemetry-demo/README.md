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
