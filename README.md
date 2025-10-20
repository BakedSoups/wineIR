## Turning Wine Reviews into Insights
Seeding Stage
The goal of this stage is to extract the three most insightful wine reviews based on several criteria:
- Reviews must have at least 50 words.
- Reviews should contain high-frequency descriptive words such as “full body”, “dry”, or “flavors”.
- Reviews must have a positive sentiment score, sorted from highest to lowest.
- Remove all spam reviews (e.g., “this review is bad” or filler text like AAAAAAA).
From these top reviews, we generate the “seed tags”, which help identify key descriptive characteristics of the wine.
 Example:
```
{
  "dry": 40,
  "full body": 40,
  "sweet": 20
}
```

These tags act as a foundation for further analysis. Using them, we can detect common patterns across all reviews, identify dominant flavor profiles (e.g., “dry” or “full body”), and filter out reviews that deviate significantly from the main descriptors.

Vectorization Stage
In this stage, we use the refined tags and the most descriptive reviews to build a vector representation (cluster) of the wine.
 Each wine’s vector reflects its defining characteristics, enabling more accurate analysis and comparison.

Comparison Stage
Using these vectors, we calculate wine similarity scores, allowing us to compare wines based on shared descriptive and sentiment-based features.


Running the Ollama Model

To create and run your custom model:

```
ollama create custom-model -f ./Modelfile
ollama run custom-model

```
