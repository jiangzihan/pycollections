import time
from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader


def metric_setup(otlp_endopint:str, insecure:bool=True, export_interval_millis:int=5000):
    """
    ### 使用方式
    使用方式, 如果需要通过http或grpc, 务必将trace_id传递到header(请求头)或者metadata(元数据)中

    ```python
    from opentelemetry import metrics

    # 初始化tracing
    metric_setup("http://192.168.66.196:14317")

    # 创建整体追踪器
    meter = metrics.get_meter(__name__)

    # 创建一个计数器 (Counter) 指标
    # 格式: http_requests_total{environment="production",job="unknown_service"} 87
    request_counter = meter.create_counter(
        name="http_requests_total",
        description="Total number of HTTP requests",
        unit="ci",
    )
    # 添加指标
    request_counter.add(1, {"my-tag": "abc"})
    ```
    """
    # 设置 OpenTelemetry Meter Provider
    exporter = OTLPMetricExporter(endpoint=otlp_endopint, insecure=insecure)
    reader = PeriodicExportingMetricReader(exporter, export_interval_millis=export_interval_millis)

    provider = MeterProvider(metric_readers=[reader])
    metrics.set_meter_provider(provider)




if __name__=="__main__":
    from opentelemetry import metrics
    # 获取 meter 实例
    meter = metrics.get_meter(__name__)

    # 创建一个计数器 (Counter) 指标
    # 格式: http_requests_total{environment="production",job="unknown_service"} 87
    request_counter = meter.create_counter(
        name="http_requests_total",
        description="Total number of HTTP requests",
        unit="ci",
    )

    # 模拟发送指标
    while True:
        request_counter.add(1, {"environment": "production", "age": 192})
        print("Metric sent to OpenTelemetry Collector")
        time.sleep(5)

