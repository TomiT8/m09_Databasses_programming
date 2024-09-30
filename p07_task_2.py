from mysql.connector import connect, Error
from connection_details import *

"""Úloha 2
Napíšte skript, ktorý vytvorí music databázu s tabuľkou:

instruments: instrument_id(PK, autoincrement), name, family, difficulty(enum - easy, medium, hard)"""

try:
# vytvorenie databázy
    with connect(host=host, user=user, password=password) as conn:
        with conn.cursor() as cursor:
            sql_statement = "CREATE DATABASE IF NOT EXISTS music;"
            cursor.execute(sql_statement)
            print("Databáza 'music' bola vytvorená.")
            cursor.execute("USE music;")

            create_table_instruments = """
                CREATE TABLE IF NOT EXISTS instruments (
                    instrument_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                    name VARCHAR(30) NOT NULL,
                    family VARCHAR(30) NOT NULL,
                    difficulty ENUM('easy', 'medium', 'hard') NOT NULL
                ) DEFAULT CHARACTER SET utf8;
            """

# Vytvorenie tabuľky
            cursor.execute(create_table_instruments)
            print("Tabuľka 'instruments' bola vytvorená.")

except Error as e:
    print(e)

print("Koniec")
