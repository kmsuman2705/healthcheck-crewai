from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
import psutil
from datetime import datetime

@CrewBase
class SystemHealthCrew():
    """SystemHealthCrew: Monitors CPU, Memory, Disk and generates reports"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def system_monitor(self) -> Agent:
        return Agent(
            config=self.agents_config['system_monitor'],  # Ensure this matches 'system_monitor' in agents.yaml
            verbose=True
        )

    @task
    def system_check_task(self) -> Task:
        # Get live stats using psutil
        mem = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        cpu = psutil.cpu_percent(interval=1)

        stats = {
            "CPU Usage (%)": cpu,
            "Memory Used (GB)": round(mem.used / (1024**3), 2),
            "Memory Total (GB)": round(mem.total / (1024**3), 2),
            "Memory Usage (%)": mem.percent,
            "Disk Used (GB)": round(disk.used / (1024**3), 2),
            "Disk Total (GB)": round(disk.total / (1024**3), 2),
            "Disk Usage (%)": disk.percent
        }

        return Task(
            description="Analyze this system data and summarize its health. If any metric is above 85%, mark it critical:\n" + str(stats),
            expected_output="System health summary with warnings if any metric exceeds 85%",
            agent=self.system_monitor()  # Use the system_monitor agent
        )

    @task
    def system_report_task(self) -> Task:
        mem = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        cpu = psutil.cpu_percent(interval=1)

        stats = {
            "CPU Usage (%)": cpu,
            "Memory Used (GB)": round(mem.used / (1024**3), 2),
            "Memory Total (GB)": round(mem.total / (1024**3), 2),
            "Memory Usage (%)": mem.percent,
            "Disk Used (GB)": round(disk.used / (1024**3), 2),
            "Disk Total (GB)": round(disk.total / (1024**3), 2),
            "Disk Usage (%)": disk.percent
        }

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        return Task(
            description=f"Create a markdown-formatted system health report for the following data (taken at {timestamp}). Warn if any metric exceeds 85%:\n{stats}",
            expected_output="Clean markdown report with highlights for critical metrics.",
            agent=self.system_monitor(),  # Use the system_monitor agent
            output_file=f"system_health_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        )

    @crew
    def crew(self) -> Crew:
        """Creates the System Health Monitoring Crew"""
        return Crew(
            agents=self.agents,  # Includes system_monitor
            tasks=self.tasks,    # Includes system_check_task and report_task
            process=Process.sequential,
            verbose=True
        )
