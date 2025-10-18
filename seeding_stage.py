import re
from typing import List, Tuple 
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def _analyze_sentiment(review: str)-> float:
    scores = analyzer.polarity_scores(review)
    return scores["compound"]


def _keyword_frequency(review) -> float:
    wine_keywords = [
        # Aroma and bouquet
        "aroma", "bouquet", "nose", "fragrance", "perfume", "floral", "herbal", "earthy", "spicy",
        "woody", "smoky", "fruity", "fresh", "minerality", "buttery", "caramel", "chocolate",

        # Taste and flavor profile
        "flavor", "taste", "notes", "layers", "complex", "depth", "balanced", "rich", "vibrant",
        "refined", "elegant", "expressive", "lively", "intense", "bold", "subtle", "delicate",
        "concentrated", "harmonious", "round", "structured", "mellow",

        # Fruit and sweetness
        "sweet", "dry", "semi-dry", "cherry", "plum", "blackberry", "blueberry", "raspberry",
        "strawberry", "currant", "apple", "pear", "peach", "apricot", "citrus", "lemon", "lime",
        "grapefruit", "fig", "melon",

        # Mouthfeel and body
        "smooth", "silky", "velvety", "full-bodied", "medium-bodied", "light-bodied", "creamy",
        "crisp", "soft", "round", "tannic", "drying", "chewy", "supple",

        # Finish and aftertaste
        "finish", "aftertaste", "lingering", "long", "clean", "pleasant", "lasting", "freshness",
        "bright", "zesty", "vibrant", "sharp",

        # Aging and oak
        "oak", "aged", "barrel", "vanilla", "toasty", "nutty", "cedar", "spice", "tobacco", "leather",

        # Acidity and balance
        "acidic", "acidity", "balanced", "round", "smoothness", "grip",

        # Misc descriptive
        "complexity", "depth", "finish", "texture", "character", "elegance", "refinement", "subtlety"
    ]
    review_lower =review.lower()
    count = sum(1 for keyword in wine_keywords if keyword in review_lower)
    review_len = max(1, len(review_lower.split()))
    return count / review_len
    
def _spam_filter(reviews: list[str]) -> list[str]: 
    rx = re.compile(r'(.)\1{5,}')  # matches 6+ repeated characters
    spam_reviews = []

    for review in reviews:
        if rx.search(review):
            spam_reviews.append(review)
    return spam_reviews



# uses old method of finding top reivews to help create a seeding stage 
def get_seed_reviews(review) -> List[str]:

    # filter if less than 50 words
    review_sample = [r for r in review if len(r.split()) >= 50]
    if len(review_sample) < 3: 
        review_sample = [r for r in review if len(r.split()) >= 5]
    
    # filter out spam 
    review_sample = [r for r in reviews if r not in _spam_filter(reviews)]
    scored_reviews = [] 
    
    for review in review_sample:
        score = _analyze_sentiment(review) 
        keyword_score = _keyword_frequency(review)
        scored_reviews.append((review, score, keyword_score))
    sorted_score_reviews = sorted(scored_reviews, key=lambda x: (x[1], x[2]), reverse=True)
    return sorted_score_reviews


if __name__ == "__main__":
    reviews = [
        "This product is amazing! I LOVE WINE BRO I NEED IT NOW",
        "It’s fine but a bit overpriced. abit crisp",
        "Worst purchase I’ve made all year.",
        "I love the design and feel!",
        "BUY IT BUY IT NOW BUYYYYYYYYYYY",
        "AAAAAAAAAAAAAAAAAAAAA",
        "It broke after one day I hate this wine and I hate this life crisp tho."

    ]

    # top = get_seed_reviews(reviews)
    # print("Top reviews by sentiment:")
    # for review, score, key_score in top:
    #     print(f"{review}, {score}, {key_score}") 

