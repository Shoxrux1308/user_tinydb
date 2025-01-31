import csv
from tinydb import TinyDB, Query

def read_csv(file_path):
    # Read and parse the CSV file
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
        print(data)
    return data

        
    


def insert_into_db(data, db_path):
    # Insert data into TinyDB
    pass


def query_db(db_path, query_field, query_value):
    # Query the database
    pass


if __name__ == "__main__":
    # Main execution logic
    file_path = '../user_data.csv'
    parsed_data = read_csv(file_path)
    
    
