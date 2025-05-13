def determine_next_state(user_input, current_state):
    if current_state == "greeting":
        if "book" in user_input.lower():
            return "booking"
        elif "timings" in user_input.lower() or "open" in user_input.lower():
            return "faq"
        else:
            return "fallback"

    elif current_state == "faq":
        return "completed"

    elif current_state == "booking":
        if "confirm" in user_input.lower():
            return "confirmed"
        else:
            return "awaiting_confirmation"

    return "fallback"