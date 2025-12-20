import time 
import random 
import os
from datetime import datetime

SERVICES = ["payments", "orders", "auth", "inventory"]
LEVELS = ["INFO", "WARN", "ERROR", "DEBUG"]
ERROR_MESSAGES = [
    "DB_TIMEOUT",
    "NULL_POINTER",
    "AUTH_FAILED",
    "CACHE_MISS",
    "SERVICE_UNAVAILABLE"
]

LOG_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../app.log")
)
print("🔥 LOG_GENERATOR.PY LOADED") 

def generate_log():
    service = random.choice(SERVICES)
    level = random.choice(LEVELS)

    if level == "ERROR":
        message = random.choice(ERROR_MESSAGES)
    else:
        message = "OK"

    return (
        f"{datetime.utcnow().isoformat()} "
        f"level={level} "
        f"service={service} "
        f"message={message}"
    )


if __name__ == "__main__":
    print(f"Writing logs to: {LOG_PATH}")

    with open(LOG_PATH, "a") as f:
        while True:
            log = generate_log()
            print(log)
            f.write(log + "\n")
            f.flush()
            time.sleep(1)
