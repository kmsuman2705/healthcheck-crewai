# Use the official Python base image (adjust if you need a different version of Python)
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install dependencies (including CrewAI and any other dependencies you need)
RUN pip install --no-cache-dir -r requirements.txt

# Install CrewAI directly in case it's not in requirements.txt
RUN pip install crewai

# Copy the entire project directory into the container
COPY . .

# Set the environment variable to not buffer the output (helps with logging)
ENV PYTHONUNBUFFERED=1

# Expose any port you need (e.g., port 5000 if you are running a web app)
EXPOSE 5000

# Set the command to run your Python app
CMD ["python", "run.py"]

