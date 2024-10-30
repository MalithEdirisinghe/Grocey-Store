import csv

def load_csv(file_path):
    """Load data from a CSV file and return as a list of lists."""
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            return list(reader)
    except Exception as e:
        print(f"Error loading CSV file {file_path}: {e}")
        return []

def save_csv(file_path, data):
    """Save data to a CSV file."""
    try:
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print(f"Data successfully saved to {file_path}")
    except Exception as e:
        print(f"Error saving data to {file_path}: {e}")
