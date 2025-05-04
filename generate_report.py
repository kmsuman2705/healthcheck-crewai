from src.latest_ai_development.crew import SystemHealthCrew  # Adjust the import based on your existing code

def generate_system_report():
    inputs = {}
    try:
        result = SystemHealthCrew().crew().kickoff(inputs=inputs)  # Assuming this generates the report
        return result
    except Exception as e:
        return f"Error: {e}"
