package kubernetes.admission

default allow = false

allow {
    input.request.kind.kind == "Service"
    input.request.operation == "CREATE"
    input.request.object.metadata.name == "order-service"
    not forbidden_time_window
}

forbidden_time_window {
    time := time.now_ns() / 1000000000
    hour := time.clock(time)[0]
    hour >= 21  # 9 PM UTC
}

forbidden_time_window {
    time := time.now_ns() / 1000000000
    hour := time.clock(time)[0]
    hour < 6
}
