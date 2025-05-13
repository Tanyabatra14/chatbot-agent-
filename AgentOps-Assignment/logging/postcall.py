def analyze_call(log_data):
    insights = {
        "user_satisfaction": "high" if "thank" in log_data.lower() else "unknown",
        "intent_fulfilled": "booking" in log_data.lower() or "timings" in log_data.lower(),
        "errors": "not found" in log_data.lower(),
    }
    return insights