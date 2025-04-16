import csv
import random
from datetime import datetime, timedelta

def generate_csv(file_name, num_rows):
    # Define the column names
    columns = ["account_id", "date_created", "message_duplicates", "message_length_avg", "links_shared", "is_bot"]

    # Open the file for writing
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(columns)  # Write the header row

        # Generate rows
        for i in range(1, num_rows + 1):
            account_id = f"{i:05d}"  # 5-digit zero-padded integer
            date_created = (datetime.now() - timedelta(days=random.randint(0, 365))).strftime('%Y-%m-%d')  # Random date within the last year
            message_duplicates = random.randint(1, 20)  # Random integer between 1 and 200
            message_length_avg = random.randint(1, 500)  # Random integer for average message length
            links_shared = random.randint(0, 50)  # Random integer for links shared
            is_bot = random.randint(0, 1)  # Random 0 or 1

            # Write the row
            writer.writerow([account_id, date_created, message_duplicates, message_length_avg, links_shared, is_bot])

# Example usage
if __name__ == "__main__":
    generate_csv("./data/output.csv", 1000)  # Generate a CSV with 100 rows