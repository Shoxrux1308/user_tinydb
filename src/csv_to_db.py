import csv
from tinydb import TinyDB, Query

def read_csv(file_path):
    # Read and parse the CSV file
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        raise ValueError(f"File {file_path} not found")

        
    


def insert_into_db(data, db_path):
    # Insert data into TinyDB
    if not data:
        raise ValueError('Data must not be empty')
    db = TinyDB(db_path)
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

    


if __name__ == "__main__":
    # Main execution logic
        file_path = './user_data.csv'
    db_path='./user_db.json'   
    data = read_csv(file_path)
    insert_into_db(data, db_path)
    query_db(db_path)
    
    
    
