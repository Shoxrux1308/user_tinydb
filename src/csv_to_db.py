import csv
from tinydb import TinyDB, Query
import argparse

def read_csv(file_path):
    # Read and parse the CSV file
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        raise ValueError(f"File {file_path} not found")

        
    


def insert_into_db(data, db_path=None):
    # Insert data into TinyDB
    if not data:
        raise ValueError('Data must not be empty')
    db = TinyDB(db_path,indent=4)
    db.insert_multiple(data)
    return db.all()
    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 


def query_db(db_path, query_field=None, query_value=None):
    # Query the database
    db = TinyDB(db_path)
    query = Query()
    if query_field and query_value:
        result = db.search(query[query_field] == query_value)
    else:
        result = db.all()
    return result

def main():
    parser = argparse.ArgumentParser(description='CSV to TinyDB importer')
    parser.add_argument('csv_file', help='Path to the CSV file')
    parser.add_argument('--db',  help='Path to the TinyDB JSON file')
    parser.add_argument('--query_field', help='Field to query')
    parser.add_argument('--query_value', help='Value to query')
    args = parser.parse_args()
    data = read_csv(args.csv_file)
    insert_into_db(data, args.db)
    if args.query_field and args.query_value:
        query_db(args.db, args.query_field, args.query_value)


if __name__ == "__main__":
    # Main execution logic
    main()
    
    
    
    
