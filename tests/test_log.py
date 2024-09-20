from pycollections.oetl.log.logging_setup import logging_setup
from pycollections.oetl.tracing.tracing_setup import tracing_setup

from opentelemetry import trace
import logging

def test_logsetup():
    tracing_setup("my-service", "http://192.168.66.196:14317")
    logging_setup("DEBUG")

    logging.basicConfig(level=logging.DEBUG)

    logger = logging.getLogger(__name__)
    tracer = trace.get_tracer(__name__)

    logger.debug("输出")
    with tracer.start_as_current_span("开始启动",attributes={
        "task_id": "a"
    }) as span:
        logger.info("输出: %s", span.get_span_context().span_id)
