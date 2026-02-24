"""
Lesson 8: Deployment & Continuous Improvement

This script simulates deployment of the agentic MCP solution and sets up a feedback loop for continuous improvement. It logs deployment status and allows for iterative updates.
"""

import json
import datetime
import os

DEPLOYMENT_LOG_PATH = "../out/deployment_log.json"


def log_deployment(status, notes):
    log_entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "status": status,
        "notes": notes
    }
    if os.path.exists(DEPLOYMENT_LOG_PATH):
        with open(DEPLOYMENT_LOG_PATH, "r") as f:
            log = json.load(f)
    else:
        log = []
    log.append(log_entry)
    with open(DEPLOYMENT_LOG_PATH, "w") as f:
        json.dump(log, f, indent=2)


def simulate_deployment():
    print("Deploying agentic MCP solution...")
    log_deployment("success", "Initial deployment completed.")
    print("Deployment logged.")


def collect_feedback():
    feedback = input("Enter feedback for improvement (or leave blank to skip): ")
    if feedback:
        log_deployment("feedback", feedback)
        print("Feedback logged.")
    else:
        print("No feedback provided.")


def main():
    simulate_deployment()
    collect_feedback()
    print(f"Deployment and feedback log saved to {DEPLOYMENT_LOG_PATH}")


if __name__ == "__main__":
    main()
