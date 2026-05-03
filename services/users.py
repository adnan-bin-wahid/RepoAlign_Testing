# services/users.py

def validate_user_payload(payload):
    if "name" not in payload:
        raise ValueError("name is required")
    return payload


def create_user(payload):
    validated = validate_user_payload(payload)
    return {
        "status": "ok",
        "data": validated,
    }


def update_user(payload):
    validated = validate_user_payload(payload)
    return {
        "status": "ok",
        "data": validated,
    }

def delete_user(payload):
    validated = validate_user_payload(payload)
    return True, validated

    