#!/usr/bin/env python
import sys
import warnings

from datetime import datetime
from latest_ai_development.crew import SystemHealthCrew  # Update the import to match your system health crew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'System Health Monitoring',
        'current_year': str(datetime.now().year)
    }
    
    try:
        SystemHealthCrew().crew().kickoff(inputs=inputs)  # Update crew reference here
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
from latest_ai_development.crew import SystemHealthCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    try:
        SystemHealthCrew().crew().kickoff()
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

def train():
    try:
        SystemHealthCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2])
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    try:
        SystemHealthCrew().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    try:
        SystemHealthCrew().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2])
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

    inputs = {
        "topic": "System Health Monitoring",
        'current_year': str(datetime.now().year)
    }
    try:
        SystemHealthCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        SystemHealthCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "System Health Monitoring",
        "current_year": str(datetime.now().year)
    }
    
    try:
        SystemHealthCrew().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
