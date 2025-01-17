# Original Author: CrewAI template
# Modified by: Cynthia Widjaja
# Email: cynthia.widjaja@cstu.edu
# Date of Modification: 13 Dec 2024
# Description: Modified the CrewAI template to generate a financial research report based on input for company name, stock ticker, and industry.
# Version: 1.0

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

import os
import pandas as pd
import time
# Check our tools documentations for more information on how to use them
from crewai_tools import ScrapeWebsiteTool, SerperDevTool

search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

@CrewBase
class MyStockCrew():
    """Stock Research Crew for Comprehensive Financial Analysis"""

    @agent
    def researcher(self) -> Agent:
        """Creates the Researcher Agent for gathering company information"""
        return Agent(
            config=self.agents_config['researcher'],
            verbose=True,
            allow_delegation=True,
            tools = [scrape_tool, search_tool]
        )

    @agent
    def fundamental_analyst(self) -> Agent:
        """Creates the Fundamental Analyst Agent for financial statement review"""
        return Agent(
            config=self.agents_config['fundamental_analyst'],
#           tools=[SerperDevTool()],
            verbose=True,
            allow_delegation=True,
            tools = [scrape_tool, search_tool]
        )

    @agent
    def technical_analyst(self) -> Agent:
        """Creates the Technical Analyst Agent for stock performance analysis"""
        return Agent(
            config=self.agents_config['technical_analyst'],
#           tools=[SerperDevTool()],
            verbose=True,
            allow_delegation=True,
            tools = [scrape_tool, search_tool]
        )

    @agent
    def industry_analyst(self) -> Agent:
        """Creates the Industry Analyst Agent for market trend evaluation"""
        return Agent(
            config=self.agents_config['industry_analyst'],
#           tools=[SerperDevTool()],
            verbose=True,
            allow_delegation=True,
            tools = [scrape_tool, search_tool]
        )

    @agent
    def risk_analyst(self) -> Agent:
        """Creates the Risk Analyst Agent for investment risk assessment"""
        return Agent(
            config=self.agents_config['risk_analyst'],
#           tools=[SerperDevTool()],
            verbose=True,
            allow_delegation=True,
            tools = [scrape_tool, search_tool]
        )

    @agent
    def decision_analyst(self) -> Agent:
        """Creates the Decision Analyst Agent for investment recommendations"""
        return Agent(
            config=self.agents_config['decision_analyst'],
#           tools=[SerperDevTool()],
            verbose=True,
            allow_delegation=True,
            tools = [scrape_tool, search_tool]
        )

    @agent
    def reporting_analyst(self) -> Agent:
        """Creates the Reporting Analyst Agent for synthesizing insights"""
        return Agent(
            config=self.agents_config['reporting_analyst'],
#           tools=[SerperDevTool()],
            verbose=True,
            allow_delegation=True,
            tools = [scrape_tool, search_tool]
        )

#     @agent
#     def metric_agent(self) -> Agent:
#         """Creates the Metric Agent for calculating time and cost metrics"""
#         return Agent(
#             config=self.agents_config['metric_agent'],
# #            tools=[],
#             verbose=True
#         )

    @task
    def researcher_task(self) -> Task:
        """Defines the research task for gathering company information"""
        return Task(
            config=self.tasks_config['researcher_task'],
            output_file='01_company_research.md'
        )

    @task
    def fundamental_analyst_task(self) -> Task:
        """Defines the fundamental analysis task for financial review"""
        return Task(
            config=self.tasks_config['fundamental_analyst_task'],
            output_file='02_fundamental_research.md'
        )

    @task
    def technical_analyst_task(self) -> Task:
        """Defines the technical analysis task for stock performance"""
        return Task(
            config=self.tasks_config['technical_analyst_task'],
            output_file='03_technical_research.md'
        )

    @task
    def industry_analyst_task(self) -> Task:
        """Defines the industry analysis task for market trends"""
        return Task(
            config=self.tasks_config['industry_analyst_task'],
            output_file='04_industry_research.md'
        )

    @task
    def risk_analyst_task(self) -> Task:
        """Defines the risk analysis task for investment assessment"""
        return Task(
            config=self.tasks_config['risk_analyst_task'],
            output_file='05_risk_research.md'
        )

    @task
    def decision_analyst_task(self) -> Task:
        """Defines the decision analysis task for investment recommendations"""
        return Task(
            config=self.tasks_config['decision_analyst_task'],
            output_file='06_decision_research.md'
        )

    @task
    def reporting_analyst_task(self) -> Task:
        """Defines the reporting task for final insights compilation"""
        return Task(
            config=self.tasks_config['reporting_analyst_task'],
            output_file='07_report_research.md'
        )

    # @task
    # def metric_agent_task(self) -> Task:
    #     """Defines the metric analysis task for tracking time and cost"""
    #     return Task(
    #         config=self.tasks_config['metric_agent_task'],
    #         output_file='08_performance_metrics.md'
    #    )

    @crew
    def crew(self) -> Crew:
        """Creates the Stock Research Crew with sequential processing"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            output_log_file='crew_execution_log.txt'  # Optional: log file for detailed tracking

        )

    # def calculate_metrics(self, crew):
    #     """
    #     Calculate and analyze performance metrics for the crew's execution
        
    #     Args:
    #         crew (Crew): The executed crew instance
        
    #     Returns:
    #         dict: Performance metrics summary
    #     """
    #     # Start with tracking total execution time
    #     start_time = time.time()
        
    #     # Assuming the crew has a usage_metrics attribute
    #     if hasattr(crew, 'usage_metrics'):
    #         # Convert UsageMetrics to DataFrame
    #         df_usage_metrics = pd.DataFrame([crew.usage_metrics.dict()])
            
    #         # Calculate costs (adjust the rate based on your actual API pricing)
    #         # Example pricing: $0.150 per million tokens
    #         costs = 0.150 * (crew.usage_metrics.prompt_tokens + crew.usage_metrics.completion_tokens) / 1_000_000
            
    #         # Calculate total execution time
    #         total_execution_time = time.time() - start_time
            
    #         # Prepare metrics summary
    #         metrics_summary = {
    #             'total_execution_time': total_execution_time,
    #             'total_prompt_tokens': crew.usage_metrics.prompt_tokens,
    #             'total_completion_tokens': crew.usage_metrics.completion_tokens,
    #             'total_cost': f'${costs:.4f}'
    #         }
            
    #         # Optional: Save metrics to a file
    #         with open('performance_metrics.txt', 'w') as f:
    #             for key, value in metrics_summary.items():
    #                 f.write(f"{key}: {value}\n")
            
    #         return metrics_summary
        
    #     return {}