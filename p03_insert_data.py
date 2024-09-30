from mysql.connector import connect, Error
from connection_details import *

"""Úloha 5
Napíšte dotaz SQL pre vyplnenie tabuliek directorsa movies. Prosím, uveďte. Údaje sú na prespríštím slajdu.

"""

directors = [('Frank', 'Darabont', 7), ('Francis Ford', 'Coppola', 8),
             ('Quentin', 'Tarantino', 10), ('Christopher', 'Nolan', 9),
             ('David', 'Fincher', 7)]

movies = [('Vykúpenie z väznice Shawshank', 1994, 'Dráma', 1, 8),
          ('Zelená míľa', 1999, 'Dráma', 1, 6),
          ('Krstný otec', 1972, 'Zločin', 2, 7),
          ('Kmotr III', 1990, 'Zločin', 2, 6),
          ('Pulp Fiction', 1994, 'Zločin', 3, 9),
          ('Inglourious Basterds', 2009, ' Vojna', 3, 8),
          ('Temný rytier', 2008, 'Akcia', 4, 9),
          ('Interstellar', 2014, 'Sci-fi', 4, 8),
          ('The Prestige', 2006, 'Dráma', 4, 10),
          ('Klub bitkárov', 1999, 'Dráma', 5, 7),
          ('Zodiac', 2007, 'Crime', 5, 5),
          ('Seven', 1995, 'Drama', 5, 8),
          ('Alien 3', 1992, 'Horror', 5, 5)]

try:
    with connect(host=host, user=user, password=password, database='cinematic') as conn:
        with conn.cursor() as cursor:
            insert_directors_query = """
                INSERT INTO directors (name, surname, rating)
                VALUES (%s, %s, %s)
            """
            cursor.executemany(insert_directors_query, directors)
            conn.commit()
            print("Tabuľka 'directors' bola vyplnená.")

            insert_movies_query = """
                INSERT INTO movies (title, year, category, director_id, rating)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.executemany(insert_movies_query, movies)
            conn.commit()
            print("Tabuľka 'movies' bola vyplnená.")

except Error as e:
    print(e)

print("Koniec")
