
logs = [
    {"service": "API", "level": "ERROR"},
    {"service": "Database", "level": "INFO"},
    {"service": "Payment", "level": "ERROR"},
    {"service": "Auth", "level": "ERROR"}
]

errors = [log for log in logs if log["level"] == "ERROR"]

for log in errors:
    print(f"Error in {log['service']}")

print(f"Latest errors: {errors[-2:]}")
