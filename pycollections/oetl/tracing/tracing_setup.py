from opentelemetry.sdk.resources import Resource
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor


def tracing_setup(service_name:str, otlp_endopint:str, insecure:bool=True):
    """
    ### 使用方式
    使用方式, 如果需要通过http或grpc, 务必将trace_id传递到header(请求头)或者metadata(元数据)中

    ```python
    from opentelemetry import trace

    # 初始化tracing
    tracing_setup("my-service", "http://192.168.66.196:14317")

    # 创建整体追踪器
    tracer = trace.get_tracer(__name__)

    with tracer.start_as_current_span("task1-span",
        attributes={"task_id": "task1232456668"}
    ) as span:
        trace_id = span.get_span_context().trace_id
        span.add_event("启动1")
        # span.set_status(trace.Status(trace.StatusCode.ERROR, str(err)))
    ```
    """

    # 配置 OpenTelemetry
    resource = Resource.create({"service.name": service_name})
    provider = TracerProvider(resource=resource)
    trace.set_tracer_provider(provider)

    # 使用 OTLP 导出器
    otlp_exporter = OTLPSpanExporter(endpoint=otlp_endopint, insecure=insecure)

    # 使用异步的批处理 Span 处理器
    span_processor = BatchSpanProcessor(otlp_exporter)
    provider.add_span_processor(span_processor)


if __name__=="__main__":
    # 使用方式
    from opentelemetry import trace

    # 初始化tracing
    tracing_setup("async-service", "http://192.168.66.196:14317")

    # 创建整体追踪器
    tracer = trace.get_tracer(__name__)

    # 推荐方式
    with tracer.start_as_current_span("task1-span", attributes={"task_id": "task1232456668"}) as span:
        trace_id = span.get_span_context().trace_id
        print("Performing async task... %s", trace_id)
        span.add_event("启动1")
        span.set_attribute("id", 1000)

        with tracer.start_as_current_span("task2-span", attributes={"task_id": "task1232456668"}) as span:
            try:
                span.add_event("启动任务2")
                # raise RuntimeError("错误粗否哦随哦杜甫iosdufiosdufio速度哦发iusio")
            except Exception as err:
                span.set_status(trace.Status(trace.StatusCode.ERROR, str(err)))

            print("Performing async task...2222222")
            span.add_event("结束任务2")

        with tracer.start_as_current_span("task3-span", attributes={"task_id": "task1232456668"}) as span:
            try:
                span.add_event("启动任务3")
                # raise RuntimeError("错误粗否哦随哦杜甫iosdufiosdufio速度哦发iusio")
            except Exception as err:
                span.set_status(trace.Status(trace.StatusCode.ERROR, str(err)))

            print("Performing async task...3333")
            span.add_event("结束任务3")


    # # 简单使用，但是无法实现链路追踪
    # @tracer.start_as_current_span("do_work")
    # def test_run()->str:
    #     print("okok")
    #     return "ok"

    # @tracer.start_as_current_span("master_work")
    # def test_master():
    #     print("okok")
    #     test_run()
    #     return "ok"
    
    # test_master()