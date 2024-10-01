from mysql.connector import connect, Error
from connection_details import *

"""Úloha 3
Napíšte funkciu insert_instruments, ktorá bude zodpovedať za doplnenie údajov v tabuľke nástrojov.
Funkcia by mala mať dva argumenty – pripojenie k databáze a zoznam záznamov, ktoré sa majú zadať.
Otestujte funkciu podľa nasledujúceho zoznamu:"""

instruments = [
    ('guitar', 'strings', 'medium'),
    ('piano', 'keyboard', 'hard'),
    ('harp', 'strings', 'hard'),
    ('triangle', 'percussion', 'easy'),
    ('flute', 'woodwind', 'medium'),
    ('violin', 'string', 'medium'),
    ('tambourine', 'percussion', 'easy'),
    ('organ', 'keyboard', 'hard')]


# try:
#     with connect(host=host, user=user, password=password, database='music') as conn:
#         with conn.cursor() as cursor:
#             insert_instruments = """
#                 INSERT INTO instruments (name, family, difficulty)
#                 VALUES (%s, %s, %s)
#             """
#             cursor.executemany(insert_instruments, instruments)
#             conn.commit()
#             print("Tabuľka 'instruments' bola vyplnená.")
#
# except Error as e:
#     print(e)
#
# print("Koniec")

def insert_instruments(connection, instruments_list):
    with connection.cursor() as cursor:
        sql_statement = """
            INSERT INTO instruments
            (name, family, difficulty)
            VALUES (%s, %s, %s);
        """
        cursor.executemany(sql_statement, instruments_list)
        connection.commit()


print("Tabuľka 'instruments' bola vyplnená.")

try:
    with connect(host=host, user=user, password=password, database='music') as conn:
        insert_instruments(conn, instruments)

except Error as e:
    print(e)
