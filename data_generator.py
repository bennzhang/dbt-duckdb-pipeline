import csv
import random
from datetime import datetime, timedelta

start_timestamp = datetime(2023, 5, 1, 0, 0, 0)
end_timestamp = datetime(2023, 6, 30, 0, 0, 0)

# Open the CSV file for writing
with open('data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    
    # Write the header
    writer.writerow(['video_id', 'visitor_id', 'time_stamp'])
    
    # Generate the data and write to the CSV file
    for i in range(1000):
        video_id = random.randint(1, 100)
        visitor_id = random.randint(1, 100)
        random_seconds = random.randint(0, int((end_timestamp - start_timestamp).total_seconds()))
        random_timestamp = start_timestamp + timedelta(seconds=random_seconds)
        writer.writerow([video_id, visitor_id, random_timestamp])
