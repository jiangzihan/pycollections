import os

from opentelemetry.instrumentation.logging import LoggingInstrumentor


def logging_setup(log_level:str|None=None):
    """
    ### 使用方式

    ```python
    from pycollections.log.logging_setup import logging_setup
    from pycollections.tracing.tracing_setup import tracing_setup
    import logging

    tracing_setup("my-service", "http://192.168.66.196:14317")
    logging_setup("DEBUG")

    logger = logging.getLogger(__name__)

    logger.debug("test for debug log")
    with tracer.start_as_current_span("in_span_1",
        attributes={"task_id": "taskid"}) as span:

        logger.info("info log: %s", span.get_span_context().span_id)
    ```
    """

    log_level = log_level if log_level else os.getenv('PY_LOG', 'INFO').upper()
    LoggingInstrumentor().instrument(set_logging_format=True, log_level=log_level)
