from mysql.connector import connect, Error
from connection_details import *

"""Úloha 6
Napíšte SQL dotaz, ktorý vráti všetky filmy od roku 2002. Urobte dopyt."""

try:
    with connect(host=host, user=user, password=password, database='cinematic') as conn:
        with conn.cursor() as cursor:
            sql_statement = """SELECT * FROM movies;"""
            cursor.execute(sql_statement)
            movies = cursor.fetchall()
            print("================= MOVIES =================")
            print("id\ttitle\tyear\tcategory\tdirector_id\trating")
            for movie in movies:
                print(f"{movie[0]}\t{movie[1]}\t{movie[2]}\t{movie[3]}\t{movie[4]}\t{movie[5]}")
            print("")
            print("Koniec")
            print("")

            sql_statement = """SELECT * FROM directors;"""
            cursor.execute(sql_statement)
            directors = cursor.fetchall()
            print("================= DIRECTOR =================")
            print("director_id\tname\tsurname\trating")
            for direct in directors:
                print(f"{direct[0]}\t{direct[1]}\t{direct[2]}\t{direct[3]}")

            sql_statement = "SELECT * FROM movies WHERE year = 2008;"
            cursor.execute(sql_statement)
            movies = cursor.fetchall()

            print("")
            for movie in movies:
                print(movie)

            sql_statement = "SELECT * FROM movies WHERE year = 1994;"
            cursor.execute(sql_statement)
            movies = cursor.fetchall()

            print("")
            for movie in movies:
                print(movie)


except Error as e:
    print(e)

print("")
print("Koniec")
