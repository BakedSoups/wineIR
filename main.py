# Stupid cod


# Formating libraries 
from typing import Dict, List 
import logging 

# custom modules  lib
from tag_generation import *
from seeding_stage  import *
from data_retrieval import * 

logging.basicConfig(
    level = logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def product_emebedding() ->  Dict[str, List[str]]: 

    # returns a dictionary of reviews 
    reviews = data_retrieval.get_review("link?")
    
    # return top 3 reviews 
    insightful_reviews = reviews.get_seed_reviews()
    
    
    # generate tags based patterns in reviews 
    tags = []

    # example "crisp", "dry"
    tags = insightful_reviews.generate_tags()     
    

    # we will either save this in a db or embed it here 
    result = {
        "product": insightful_reviews,
        "tags": tags,
        "reviews" : reviews
    }


    return result

    

if __name__ == "__main__": 
    logging.info(f"Running tag generation.")
    main() 
    