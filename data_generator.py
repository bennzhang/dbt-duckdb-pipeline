import csv
import random

# Open the CSV file for writing
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    # Write the header
    writer.writerow(['video_id', 'visitor_id', 'time_stamp'])
    
    # Generate the data and write to the CSV file
    for i in range(1000):
        video_id = random.randint(1, 100)
        visitor_id = random.randint(1, 100)
        time_stamp = "2023-05-19 09:00:00"
        writer.writerow([video_id, visitor_id, time_stamp])
