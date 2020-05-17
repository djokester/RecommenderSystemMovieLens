# RecommenderSystemMovieLens

A Recommender System based on the MovieLens website. 
## Information about the Data Set 
The dataset can be found at [MovieLens 100k Dataset](http://grouplens.org/datasets/movielens/100k/ "MovieLens Page"). It has 100,000 ratings from 1000 users on 1700 movies. Released 4/1998. The basic data files used in the code are: 

1. u.data:     -- The full u data set, 100000 ratings by 943 users on 1682 items.
              Each user has rated at least 20 movies.  Users and items are
              numbered consecutively from 1.  The data is randomly
              ordered. This is a tab separated list of 
	            user id | item id | rating | timestamp. 
              The time stamps are unix seconds since 1/1/1970 UTC
2. u.item     -- Information about the items (movies); this is a tab separated
              list of
              movie id | movie title | release date | video release date |
              IMDb URL | unknown | Action | Adventure | Animation |
              Children's | Comedy | Crime | Documentary | Drama | Fantasy |
              Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi |
              Thriller | War | Western |
              The last 19 fields are the genres, a 1 indicates the movie
              is of that genre, a 0 indicates it is not; movies can be in
              several genres at once.
              The movie ids are the ones used in the u.data data set.
3. u.user     -- Demographic information about the users; this is a tab
              separated list of
              user id | age | gender | occupation | zip code
              The user ids are the ones used in the u.data data set.

## Requirements 
1. Numpy
2. Pandas
3. Scipy 
4. Matplotlib

# Simple Recommender System
This is a very simple SQL-like manipulation of the datasets using Pandas. For a detailed guide on how to create such a recommender system visit this [Link](https://acodeforthought.wordpress.com/2016/12/26/building-a-simple-recommender-system-with-movie-lens-data-set/  "Blog Post on Simple Rcommender Systems").

# Recommender System Based on User-Based Collaborative Filtering
We used only two of the three data files in this one; u.data and u.item. We used Eucledian Distance as a measure of similarity between users. 
In case two users have less than 4 movies in common they were automatically assigned a high EucledianScore. Otherwise EuclediaScore was calculated as the square root of the sum of squares of the difference in ratings of the movies that the users have in common. For more information about this program visit this [Link](https://acodeforthought.wordpress.com/2016/12/29/building-a-recommender-system-on-user-user-collaborative-filtering-movielens-dataset/ "Blog poston Recommender System on User-User Collaborative Filtering")



              



