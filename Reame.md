## Turning wine reviews into insights

### Seeding stage 
Get the 3 most insightful reviews on wine
- Max word of 50+ criteria 
- High descriptive word frequency "full body" , "dry", "flavors" 
- Postive Sentiment Score (Sort by the highest) 
- Remove all spam "this review is bad using AAAAAAA to fill the required word count"

from this we create the "seed" tags that helps us anaylze the rest of the reviews as we build the wine profile 
ex: "dry" : 40, "full body": 40, "sweet" : 20  

### From the seed tags
 we can try to find common patterns in all the data, 
    we will try to see if all the reviews seem to follow the idea of "dry", "full body" 
    and we can also filter our reviews that seem compeltely off in terms of simulairty 


## Vectorize stage
 From this we get tags that perfectly descrive the wine, and a collection of reviews that perfectly describe the wine
    we use both of these variables to create a vector cluster that repersents the wine

## Comparing
 Finaly, we come out with wine simularity scores 
 
## Running ollama model
    ```bash
    ollama create custom-model -f ./Modelfile
    ollama run custom-model
    ```
