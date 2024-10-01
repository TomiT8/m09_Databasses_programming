from mysql.connector import connect, Error
from connection_details import *

"""Úloha 7
Napíšte SQL dotaz, ktorý odstráni tabuľky z cinematicdatabázy. Urobte dopyt."""

try:
    with connect(host=host, user=user, password=password, database='cinematic') as conn:
        with conn.cursor() as cursor:
            sql_statement = """DROP TABLE movies;"""
            cursor.execute(sql_statement)
            print("Tabuľka 'movies' bola zmazaná.")

            sql_statement = """DROP TABLE directors;"""
            cursor.execute(sql_statement)
            print("Tabuľka 'directors' bola zmazaná.")

except Error as e:
    print(e)

print("")
print("Koniec")
