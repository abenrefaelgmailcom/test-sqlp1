import sqlite3

conn = sqlite3.connect('groupby.db')


'''Function to establish a connection to the SQLite database'''
def connect_db():
    return sqlite3.connect("movies.db")


'''Function to retrieve and print all movies from the database'''
def get_all_movies():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM movies")
    movies = cursor.fetchall()
    conn.close()
    for movie in movies:
        print(movie)


'''Function to search for movies by name (or part of the name) using the LIKE operator'''
def search_movie_by_name():
    name = input("Enter a movie name (or part of it): ")  # Get user input
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM movies WHERE movie_name LIKE ?", (f"%{name}%",))
    movies = cursor.fetchall()
    conn.close()
    if movies:
        for movie in movies:
            print(movie)
    else:
        print("No movies found with this name.")


'''Function to insert a new movie into the database'''
def insert_movie():
    movie_name = input("Enter movie name: ")
    genre = input("Enter genre: ")
    country = input("Enter country: ")
    language = input("Enter language: ")
    year = int(input("Enter release year (2009 or later): "))
    revenue = float(input("Enter revenue (in millions): "))

    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO movies (movie_name, genre, country, language, year, revenue)
            VALUES (?, ?, ?, ?, ?, ?)""",
                       (movie_name, genre, country, language, year, revenue))  # Insert query
        conn.commit()
        print("Movie added successfully!")
    except sqlite3.IntegrityError:
        print("Error: Movie name already exists or invalid data.")
    finally:
        conn.close()  #

#get_all_movies()
#search_movie_by_name()
#insert_movie()
