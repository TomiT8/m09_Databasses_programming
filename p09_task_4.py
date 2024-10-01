from mysql.connector import connect, Error
from connection_details import *

"""Úloha 4
Napíšte funkciu get_instruments_count, ktorá zobrazí počet nástrojov pre každú kategóriu.
Funkcia by mala brať spojenie ako argument.
Vráti záznamy pozostávajúce zo slovníkov s dvoma kľúčmi – „rodina“ a „počet“.

Nápoveda
Ak chcete získať výsledok ako slovníky, pri vytváraní kurzora použite triedu DictCursor.
"""

try:
    with connect(host=host, user=user, password=password, database='music') as conn:
        with conn.cursor(dictionary=True) as cursor:
            get_instruments_count = """SELECT family, count(*) as count FROM instruments GROUP BY family;"""
            cursor.execute(get_instruments_count)
            instruments = cursor.fetchall()

            print("Family\t\t\tCount")
            for instrument in instruments:
                print(f"{instrument['family']}\t\t\t{instrument['count']}")

except Error as e:
    print(e)

print("")
print("Koniec")