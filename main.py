# Stupid cod


# Formating libraries 
from typing import Dict, List 
import logging 

# custom modules  lib
from tag_generation import *
from seeding_stage  import get_seed_reviews
from data_retrieval import get_dataset, get_reviews 

logging.basicConfig(
    level = logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def product_emebedding() ->  Dict[str, List[str]]: 

    # returns a list of reviews:
    reviews: list[str] = get_reviews(get_dataset(), count=3)
    print(reviews)

    # return top 3 reviews 
    # input: 
    #   ["all","the","reviews"]
    # output: 
    #   {"product_name": ["really","goood","reviews"]}
    
    insightful_reviews = reviews.get_seed_reviews()
    
    
    # generate tags based patterns in reviews 
    tags = []

    # input: 
    #   {"product_name": ["really","goood","reviews"]} 
    # output:
    #   [tags]
    
    seed_tags = insightful_reviews.generate_tags()     
    

    # worry about this laterz
    tags = seed_tags.generate_tags(seed_tags)


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
    