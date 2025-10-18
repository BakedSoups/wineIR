import kagglehub
import json 
import duckdb
import pandas as pd

path = f"{kagglehub.dataset_download("zynicide/wine-reviews")}/winemag-data-130k-v2.json"

def get_dataset() -> list[dict]:
    with open(path, "r") as file_data:
        data = json.load(file_data)    
    return data
    
def get_reviews(dataset: list[dict], count: int) -> list[str]:
    return [entry["description"] for entry in dataset[:count]]
    
def get_df(): 
    return pd.read_json(path)

def duckify():
    df = get_df()
    connection = duckdb.connect(database='ducking_databse.ddb')
    ## connection.execute("CREATE TABLE reviews AS SELECT * FROM df")
    
    #duckdb.sql("CREATE TABLE reviews AS SELECT * FROM df")
    #duckdb.sql("INSERT INTO reviews SELECT * FROM df")
    result = connection.execute("SELECT * FROM reviews").fetchdf()
    print(result)
    connection.close()
    
duckify()