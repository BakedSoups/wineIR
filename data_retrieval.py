import kagglehub
import json 
import duckdb
import pandas as pd

path = f"{kagglehub.dataset_download("zynicide/wine-reviews")}/winemag-data-130k-v2.json"

# TEMP START #

def get_dataset() -> list[dict]:
    with open(path, "r") as file_data:
        data = json.load(file_data)
    return data
    
def get_reviews(dataset: list[dict], count: int) -> list[str]:
    return [entry["description"] for entry in dataset[:count]]

# TEMP END # 

def get_df(): 
    return pd.read_json(path)

def duckify(start: int = 0, end: int = 5) -> pd.DataFrame:
    df = get_df()
    connection = duckdb.connect(database='ducking_databse.ddb')

    # Only run once to create table
    # connection.execute("CREATE TABLE reviews AS SELECT * FROM df")

    # Fetch rows x:y using SQL LIMIT and OFFSET
    query = f"SELECT * FROM reviews LIMIT {end - start} OFFSET {start}"
    result = connection.execute(query).fetchdf()

    connection.close()
    return result
    
duckify()