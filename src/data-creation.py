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
            is_bot = random.randint(0, 1)  # Random 0 or 1

            # Adjust values based on whether it's a bot
            if is_bot:
                date_created = (datetime.now() - timedelta(days=random.randint(0, 30))).strftime('%Y-%m-%d')  # More recent account (last 30 days)
                message_duplicates = random.randint(10, 50)  # Higher range for bots
                message_length_avg = random.randint(100, 500)  # Longer average message length
                links_shared = random.randint(20, 50)  # More links shared
            else:
                date_created = (datetime.now() - timedelta(days=random.randint(0, 365))).strftime('%Y-%m-%d')  # Older account (31 to 365 days)
                message_duplicates = random.randint(1, 10)  # Lower range for non-bots
                message_length_avg = random.randint(1, 200)  # Shorter average message length
                links_shared = random.randint(0, 20)  # Fewer links shared

            # Write the row
            writer.writerow([account_id, date_created, message_duplicates, message_length_avg, links_shared, is_bot])

# Example usage
if __name__ == "__main__":
    generate_csv("./data/output.csv", 100000)  # Generate a CSV with 1000 rows