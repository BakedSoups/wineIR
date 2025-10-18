import kagglehub
import json


def get_dataset() -> dict:
    path = kagglehub.dataset_download("zynicide/wine-reviews")

    with open("{path}/winemag-data-130k-v2.json", "r") as file_data:
        data = json.load(file_data)
        # return data   
    


