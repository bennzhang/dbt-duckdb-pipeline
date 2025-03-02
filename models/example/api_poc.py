import requests
import json
import pandas as pd
import sys
import os

# Use current working directory as the project root
project_root = os.getcwd()
print(f"Using project root from os.getcwd(): {project_root}")

if project_root not in sys.path:
    sys.path.insert(0, project_root)

from utils.api_client import call_api_with_retries

def model(dbt, session):

    dbt.config(
        materialized='external',
        format='json',
        location='output/todos.json', 
    )

    df = dbt.source('local', 'posts').to_df()
    # Initialize list to store todos
    all_todos = []
    
    # Fetch todos for each post
    for post_id in df['post_id']:
        todo = call_api_with_retries(f'https://jsonplaceholder.typicode.com/todos/{post_id}')
        if todo:
            all_todos.append(todo)
    
    todos_df = pd.json_normalize(all_todos)
    return todos_df