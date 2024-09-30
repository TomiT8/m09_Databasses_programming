from mysql.connector import connect, Error

"""Úloha 1
Pripojte sa k mysqlserveru a skontrolujte všetky existujúce databázy."""

try:
    with connect(host=host, user=user, password=password, database='cinematic') as conn:
        with conn.cursor() as cursor:
            sql_statement = """SHOW DATABASES;"""
            cursor.execute(sql_statement)
            databases = cursor.fetchall()
            for database in databases:
                print(database[0])

except Error as e:
    print(e)

print("")
print("Koniec")