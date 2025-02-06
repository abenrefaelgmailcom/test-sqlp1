import sqlite3

# a---show tourists names alongside the countries they came from ---
SELECT
    tourists.id,
    tourists.first_name,
    tourists.last_name,
    countries.country_name
FROM tourists
INNER JOIN countries ON tourists.country_id = countries.id;



# b --- show the tourists list and the plans of the trips they are selected (selected tourists only)---
SELECT
    tourists.id,
    tourists.first_name,
    tourists.last_name,
    tours.tour_name,
    tours.start_date,
    tours.end_date,
    tours.price
FROM tourists
INNER JOIN tours ON tourists.tour_id = tours.id;


# c---View the list of all tourists and the details of the trip to which they are assigned, where the tourist is not assigned---
# ---NULL will appear in the columns of trip details---
SELECT
    tourists.id,
    tourists.first_name,
    tourists.last_name,
    tours.tour_name,
    tours.start_date,
    tours.end_date,
    tours.price
FROM tourists
LEFT JOIN tours ON tourists.tour_id = tours.id;

# d ---View the list of all tourists and the details of the trip to which they are assigned, where the tourist is not assigned
# ---NULL will appear in the columns of trip details + and + all trip details, where there are no tourists
# ---Embedded for the same trip, NULL will appear in the columns of the tourist's details.

SELECT
    tourists.id AS tourist_id,
    tourists.first_name,
    tourists.last_name,
    tours.id AS tour_id,
    tours.tour_name,
    tours.start_date,
    tours.end_date,
    tours.price
FROM tourists
LEFT JOIN tours ON tourists.tour_id = tours.id
UNION
SELECT
    tourists.id AS tourist_id,
    tourists.first_name,
    tourists.last_name,
    tours.id AS tour_id,
    tours.tour_name,
    tours.start_date,
    tours.end_date,
    tours.price
FROM tours
LEFT JOIN tourists ON tourists.tour_id = tours.id;


# e1 ---See the list of tourists who are not assigned to any trip
# ---In a separate query, it says a query that deletes one of the tourists who didn't sign up for any trip
SELECT
    id,
    first_name,
    last_name
FROM tourists
WHERE tour_id IS NULL;

# e2 ---Delete a tourist who didn't sign up for any trip---
DELETE FROM tourists
WHERE tour_id IS NULL
LIMIT 1;

# f1 ---View the list of trips that no tourist is assigned to
SELECT *
FROM tours
WHERE id NOT IN (SELECT DISTINCT tour_id FROM tourists WHERE tour_id IS NOT NULL);

# f2 ---In order to have enough time to register, change the date of the trips (for which there are no registrants at all), one year
# ---One forward.
UPDATE tours
SET start_date = DATE(start_date, '+1 year'),
    end_date = DATE(end_date, '+1 year')
WHERE id NOT IN (SELECT DISTINCT tour_id FROM tourists WHERE tour_id IS NOT NULL);

# g ---Count how many trips there is no tourist (not even one)
SELECT COUNT(*) AS count_of_empty_tours
FROM tours
WHERE id NOT IN (SELECT DISTINCT tour_id FROM tourists WHERE tour_id IS NOT NULL);


# h ---See all possible combinations of all tourists vs. all excursions
SELECT
    tourists.first_name,
    tourists.last_name,
    tours.tour_name
FROM tourists
CROSS JOIN tours;





