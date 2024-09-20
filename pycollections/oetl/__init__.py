from .log.logging_setup import logging_setup
from .tracing.tracing_setup import tracing_setup
from .metric.metric_setup import metric_setup


def oetl_init(service_name:str, otlp_endopint:str, 
              insecure:bool=True, log_level:str="INFO",
              **kwargs):
    tracing_setup(service_name,otlp_endopint,insecure, **kwargs)
    logging_setup(log_level)
    metric_setup(otlp_endopint,insecure, **kwargs)