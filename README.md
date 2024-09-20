# DTW internal components

1. [ready] Manual control oetl config for python project
2. [pedding] Distributed Lock for redis
3. [pedding] Distributed Lock for etcd

## pip

```sh
poetry add pycollections

# or

pip install pycollections
```

## opentelemetry lib

opentelemetry supplit asyncio for python3.10+

```python
from pycollections.log.logging_setup import logging_setup
from pycollections.tracing.tracing_setup import tracing_setup
from pycollections.oetl.metric.metric_setup import metric_setup

import logging

# init config tracing and logging
OETL_ENDPOINT = "http://192.168.66.196:14317"
APP_NAME = "my-app"

tracing_setup(APP_NAME, OETL_ENDPOINT)
logging_setup()
metric_setup(OETL_ENDPOINT)

logger = logging.getLogger(APP_NAME)

logger.debug("test for debug log")
with tracer.start_as_current_span("in_span_1",
    attributes={"task_id": "taskid"}) as span:
    logger.info("info log: %s", span.get_span_context().span_id)
```