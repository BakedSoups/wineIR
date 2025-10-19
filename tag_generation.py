
import olama


# Read all reviews and hopefully come out with common keywords like "crispy":
def _pattern_keyword_detector():
    pass

# Use keywords to with an open ai call to hopefully filter out non relevant reviews 
def _relevancy_detector(): 
    pass


def generate_tags(reviews):
    pass


if __name__ == "__main__": 
    reviews = [
        "This Cabernet Sauvignon is absolutely stunning. The aroma is rich with notes of blackberry, cassis, and a hint of oak. On the palate, it is full-bodied, velvety, and incredibly balanced with layers of dark chocolate and subtle spices. The finish is long and lingering, making it a truly elegant wine that I would happily savor again and again.",
        "A delightful Chardonnay with a perfect balance of fruit and acidity. The nose is bright with hints of apple, pear, and vanilla. Each sip is creamy yet refreshing, with a smooth, buttery texture and a vibrant, lively finish. This wine is expressive, harmonious, and exceptionally well-structured, making it ideal for pairing with seafood or roasted chicken.",
        "An exceptional Pinot Noir that showcases finesse and depth. The bouquet is fragrant with aromas of cherry, raspberry, and subtle earthy undertones. On tasting, it is silky, round, and medium-bodied with a refined complexity. The finish is smooth and elegant, leaving a lasting impression of layered flavors that highlight the wine's expressive character and sophistication."
    ]

    generate_tags(reviews) 


