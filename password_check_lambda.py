
import json
import re

COMMON_PASSWORDS = {"password", "password123", "123456", "qwerty", "admin", "letmein", "welcome"}

def check_password_strength(password: str):
    reasons = []

    if len(password) < 8:
        reasons.append("too_short")

    if not re.search(r"[A-Z]", password):
        reasons.append("no_uppercase")

    if not re.search(r"[a-z]", password):
        reasons.append("no_lowercase")

    if not re.search(r"[0-9]", password):
        reasons.append("no_number")

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        reasons.append("no_special_char")

    if password.lower() in COMMON_PASSWORDS:
        reasons.append("common_password")

    ok = len(reasons) == 0
    return {"ok": ok, "reasons": reasons}


def lambda_handler(event, context=None):
    """
    AWS Lambda-style entry point
    Input event: { "password": "..." }
    Output: { "ok": bool, "reasons": [str] }
    """
    body = event if isinstance(event, dict) else json.loads(event)
    password = body.get("password", "")
    result = check_password_strength(password)
    return result


# For local testing
if __name__ == "__main__":
    test_event = {"password": "password123"}
    print(json.dumps(lambda_handler(test_event), indent=2))
