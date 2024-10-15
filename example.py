from otel_metric_base.otel_metrics import OtelMetricBase

# Initialize OtelMetrics with OTLP endpoint
otel_metrics = OtelMetricBase(otlp_endpoint="http://localhost:4317")

# Define tags
tags = {"environment": "production", "region": "us-east"}

# Create a counter with tags
counter = otel_metrics.create_metric(
    "counter", name="dynamic_counter", description="A dynamic counter", tags=tags
)
counter.add(5, attributes=tags)  # Add tags when updating the counter

# Create an observable gauge with a callback and tags
def get_gauge_value() -> float:
    return 42.0 


observable_gauge_callback = otel_metrics.create_observable_callback(get_gauge_value)
otel_metrics.create_metric(
    "observable_gauge", name="dynamic_gauge", callback=observable_gauge_callback, tags=tags
)

# Create an observable counter with a callback and tags
def get_counter_value() -> float:
    return 1.0


observable_counter_callback = otel_metrics.create_observable_callback(get_counter_value)
otel_metrics.create_metric(
    "observable_counter",
    name="observable_counter",
    callback=observable_counter_callback,
    tags=tags
)

# Create an observable up-down counter with a callback and tags
def get_updown_counter_value() -> float:
    return -10.0


observable_updown_callback = otel_metrics.create_observable_callback(
    get_updown_counter_value
)
otel_metrics.create_metric(
    "observable_up_down_counter",
    name="observable_updown_counter",
    callback=observable_updown_callback,
    tags=tags
)
