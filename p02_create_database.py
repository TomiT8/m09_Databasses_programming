from mysql.connector import connect, Error
from connection_details import *

"""Úloha 1
Z pythonu sa pripojte k serveru mysql. Potom vytvorte databázu cinematic."""
try:
    with connect(host=host, user=user, password=password) as conn:
        with conn.cursor() as cursor:
            cursor.execute("CREATE DATABASE cinematic;")
            print("Databáze 'cinematic' bola vytvorena.")

except Error as e:
    print(e)

print("Koniec")

""" Úloha 2
Pripojte sa k serveru mysql nastavením databáze cinematic ako domovskej / východzej databáze."""

try:
    with connect(host=host, user=user, password=password, database="cinematic") as conn:
        print(conn)

except Error as e:
    print(e)

print("Koniec")

"""Úloha 3
Napíšte SQL dotaz, ktorý vytvorí v databáze nasledujúce tabuľky cinematic:

riaditelia: director_id(PK), meno, priezvisko, rating
filmy: movie_id(PK), názov, rok, kategória, director_id(FK), hodnotenie
Dotaz SQL, ktorý si vpíšte cinematicvytvorte nasledujúce tabuľky:

riaditelia (režiséři): director_id(PK), meno, priezvisko, rating
filmy (filmy): movie_id(PK), názov, rok, kategória, director_id(FK), hodnotenie
"""

""" Úloha 4
Spustite, ktoré ste napsali dříve, a dotaz zobrazíte v databázi cinematic."""

try:
# vytvorenie databáze
    with connect(host=host, user=user, password=password, database="cinematic") as conn:
        create_table_directors = """
            CREATE TABLE IF NOT EXISTS directors (
                director_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                name VARCHAR(30),
                surname VARCHAR(30) NOT NULL,
                rating INT
            ) DEFAULT CHARACTER SET utf8;
        """
        create_table_movies = """
            CREATE TABLE IF NOT EXISTS movies (
                movie_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                title VARCHAR(50),
                year SMALLINT,
                category VARCHAR(30),
                director_id INT NOT NULL,
                rating INT,
                CONSTRAINT movies_director FOREIGN KEY (director_id) REFERENCES directors (director_id)
            ) DEFAULT CHARACTER SET utf8;
        """
    # Vytvorenie tabuliek
        with conn.cursor() as cursor:
            cursor.execute(create_table_directors)
            print("Tabuľka 'directors' bola vytvorená.")
            cursor.execute(create_table_movies)
            print("Tabuľka 'movies' bola vytvorená.")

except Error as e:
    print(e)

print("Koniec")