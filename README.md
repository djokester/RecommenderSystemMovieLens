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

##Requirements 
1. Numpy
2. Pandas
3. Scipy 
4. Matplotlib

#Simple Recommender System
This is a very simple SQL-like manipulation of the datasets using Pandas. 

              



