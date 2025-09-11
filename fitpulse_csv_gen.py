import csv
import random

NUM_RECORDS = 100
FILENAME = "fitness_data.csv"

def generate_record():
    """Generate a single fitness record with sleep, heart rate, and steps."""
    sleep_hours = round(random.uniform(4, 10), 1)
    heart_rate = random.randint(50, 100)
    steps = random.randint(1000, 20000)
    return [sleep_hours, heart_rate, steps]

def generate_csv(filename, num_records):
    """Generate fitness data and save it to a CSV file."""
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["SleepHours", "HeartRate", "Steps"])  # header
        writer.writerows(generate_record() for _ in range(num_records))

if __name__ == "__main__":
    generate_csv(FILENAME, NUM_RECORDS)

