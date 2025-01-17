# Original Author: CrewAI template
# Modified by: Cynthia Widjaja
# Email: cynthia.widjaja@cstu.edu
# Date of Modification: 13 Dec 2024
# Description: Modified the CrewAI template to generate a financial research report based on input for company name, stock ticker, and industry.
# Version: 1.0

#!/usr/bin/env python
import sys
from my_stock.crew import MyStockCrew

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew with specific company stock research inputs.
    """
    inputs = {
            'company_name': 'Microsoft',
            'stock_ticker': 'MSFT',
            'industry': 'Technology'
    } 
    

    MyStockCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
            'company_name': 'Microsoft',
            'stock_ticker': 'MSFT',
            'industry': 'Technology'
    } 
    
    try:
        MyStockCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        MyStockCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
            'company_name': 'Microsoft',
            'stock_ticker': 'MSFT',
            'industry': 'Technology'
    } 

    try:
        MyStockCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")



# inputs = {
#         'company_name': 'CostCo',
#         'stock_ticker': 'COST',
#         'industry': 'Retail'
# } 

# inputs = {
#         'company_name': 'Tesla',
#         'stock_ticker': 'TESL',
#         'industry': 'Automotive'
# } 

# inputs = {
#         'company_name': 'Microsoft',
#         'stock_ticker': 'MSFT',
#         'industry': 'Technology'
# } 

    # inputs = {
    #     'company_name': 'Bank Central Asia',
    #     'stock_ticker': 'BBCA.JK',  # Jakarta Stock Exchange ticker
    #     'industry': 'Banking'
    # }

# inputs = {
#     'company_name': 'Link Asset Management',
#     'stock_ticker': '823.HK',  # Hong Kong Stock Exchange ticker
#     'industry': 'Real Estate'
# }
