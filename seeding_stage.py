from typing import List, Tuple 
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def _anaylze_sentiment(review: str)-> float:
    scores = analyzer.polarity_scores(review)
    return scores["compound"]


# uses old method of finding top reivews to help create a seeding stage 
def get_seed_reviews(reviews:List[str]) -> List[str]:


    scored_reviews = [] 
    
    # create a
    for review in reviews:
        score = _anaylze_sentiment(review) 
        scored_reviews.append((review, score))

    scored_reviews = sorted(scored_reviews, key=lambda x: x[1], reverse=True)

    top_reviews = sorted(scored_reviews, key=lambda x: x[1], reverse=True)[:3]


    # Return only the text of top reviews
    return top_reviews



if __name__ == "__main__":
    reviews = [
        "This product is amazing! I LOVE WINE BRO I NEED IT NOW",
        "It’s fine but a bit overpriced. abit crisp",
        "Worst purchase I’ve made all year.",
        "I love the design and feel!",
        "It broke after one day."
    ]

    top = get_seed_reviews(reviews)
    print("Top 3 reviews by sentiment:")
    for r in top:
        print("-", r)

