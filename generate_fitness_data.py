import json
import random

NUM_RECORDS = 100
FILENAME = 'fitness_data.json'

def generate_record():
    """Generate a single fitness record with sleep, heart rate, and steps."""
    return {
        "SleepHours": round(random.uniform(4, 10), 1),
        "HeartRate": random.randint(50, 100),
        "Steps": random.randint(1000, 20000)
    }

def generate_data(num_records):
    """Generate a list of fitness records."""
    return [generate_record() for _ in range(num_records)]

def save_to_json(data, filename):
    """Save data to a JSON file with indentation."""
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    fitness_data = generate_data(NUM_RECORDS)
    save_to_json(fitness_data, FILENAME)
