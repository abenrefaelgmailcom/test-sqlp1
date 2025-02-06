import sqlite3

# a ---Count how many movies there are from each genre?

SELECT genre, COUNT(*) AS movie_count
FROM movies
GROUP BY genre;

# b ---How much revenue was there each year in the film industry?

SELECT year, SUM(revenue) AS total_revenue
FROM movies
GROUP BY year;

# c --- What is the average earnings for each genre?

SELECT genre, AVG(revenue) AS avg_revenue
FROM movies
GROUP BY genre;

# d--- What is the average earnings for each genre for each language separately?

SELECT genre, language, AVG(revenue) AS avg_revenue
FROM movies
GROUP BY genre, language;

# e --- What language has the least movies?

SELECT language, COUNT(*) AS movie_count
FROM movies
GROUP BY language
ORDER BY movie_count ASC
LIMIT 1;

# f ---Which country has the most movies?

SELECT country, COUNT(*) AS movie_count
FROM movies
GROUP BY country
ORDER BY movie_count DESC
LIMIT 1;

# g ---See the genres where there are more than 2 movies

SELECT genre, COUNT(*) AS movie_count
FROM movies
GROUP BY genre
HAVING COUNT(*) > 2;

# h ---Show years (years) in which the total earnings were greater than 1,000

SELECT year, SUM(revenue) AS total_revenue
FROM movies
GROUP BY year
HAVING total_revenue > 1000;

# i ---Show languages with at least 3 movies

SELECT language, COUNT(*) AS movie_count
FROM movies
GROUP BY language
HAVING movie_count >= 3;