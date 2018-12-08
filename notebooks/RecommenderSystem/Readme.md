## Recommender Systems

Two different types of recommender systems built for Google and Apple App stores
- Simple Recommender
- Content-Based Recommender
- Collaborative-Filtering Based Recommender

### Simple Recommender

- Returns top 15 apps based on weighted metrics 
- Weighted rating computed for each app based on average rating per app and number of reviews 
- **Pros** - Easy to implement
- **Cons** -  Only provides generalized recommendations

### Content Based Recommender
- Recommends apps similar to other apps
- Computes pairwise similarity scores based on app description 
- Calculate TF-IDF vectors for each app
- Different measures of similarity applied- cosine similarity, Euclidean
- Applied a popularity filter to improve recommendations - based on ratings 
- **Pros** - Does a good job recommending apps that belong to the similar categories 
- **Cons** - Does not take user input(rating per app etc) into consideration

### Collaborative Filtering
#### User-based filtering
- Recommendations based on similar interests with other users

#### Item-based filtering 
- Similar to content-based 
- Recommend based on past ratings from users
