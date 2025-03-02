import os
import sys
import pandas as pd

project_root = os.getcwd()
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from utils.api_client import call_api_with_retries

OUTPUT_DIR = 'output'
BATCH_SIZE = 5

def process_batch(session, batch_df, batch_number):
    """Process a batch of rows and save results to JSON file"""
    batch_results = []
    for _, row in batch_df.iterrows():
        post_id = row['post_id']
        if post_id:
            todo = call_api_with_retries(f'https://jsonplaceholder.typicode.com/todos/{post_id}')
            if todo:
                batch_results.append(todo)

    if batch_results:
        df_batch = pd.DataFrame(batch_results)
        session.register('temp_batch', df_batch)
        output_file = os.path.join(OUTPUT_DIR, f"todos_batch_{batch_number}.json")
        session.execute(f"COPY temp_batch TO '{output_file}' (FORMAT JSON);")
        session.unregister('temp_batch')
        print(f"Batch {batch_number} saved to {output_file}")
    
    return len(batch_results)

def model(dbt, session):
    dbt.config(
        materialized='external',
        format='json',
        location='output/total_processed.json'
    )

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    relation = dbt.source('local', 'posts')
    total_rows = len(relation)
    num_batches = (total_rows + BATCH_SIZE - 1) // BATCH_SIZE
    total_processed = 0
    for batch_num in range(num_batches):
        batch_df = relation.limit(BATCH_SIZE, batch_num * BATCH_SIZE).to_df()
        processed = process_batch(session, batch_df, batch_num)
        total_processed += processed
        print(f"Batch {batch_num + 1}/{num_batches}: processed {processed} records")

    print(f"Processing {total_rows} rows in {num_batches} batches")
    return pd.DataFrame({
        "total_rows": [total_rows],
        "total_processed": [total_processed],
        "processed_at": [pd.Timestamp.now()]
    })