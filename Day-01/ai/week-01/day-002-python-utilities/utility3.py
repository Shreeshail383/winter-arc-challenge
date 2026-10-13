
task = {
    "role": "Python AI Assistant",
    "goal": "Analyze application errors",
    "logs": ["API timeout", "Database failure", "API timeout"]
}

unique_logs = list(dict.fromkeys(task["logs"]))

prompt = (
    f"You are a {task['role']}.\n"
    f"Task: {task['goal']}.\n"
    f"Logs: {', '.join(unique_logs[:2])}"
)

print(prompt)
