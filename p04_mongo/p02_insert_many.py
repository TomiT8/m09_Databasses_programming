from connect_mango import mydb_pr24

mycol = mydb_pr24["customers"]

customers = [
    #{"name": "Adam", "surname": "Novák", "address": "Hlavná 22, Brno"},                        # vytvoria sa mi automatické id
    #{"name": "Peter", "surname": "Sloboda", "address": "Jarná 1, Praha"},
    #{"name": "Ctibor", "surname": "Novotný", "address": "Letná 13, Olomouc"}

    {"_id": 1, "name": "Dan", "surname": "Lejska", "address": "Zimná 12, Ostrava"},             # vytvoril som id
    {"_id": 2, "name": "Evžen", "surname": "Brzobohatý", "address": "Košická 25, Ostrava"},
    {"_id": 3, "name": "Filip", "surname": "Novák", "address": "Jesenského 15, Ostrava"},
    {"_id": 4, "name": "Gustáv", "surname": "Adam", "address": "Janka Kráľa 5, Ostrava"},
    {"_id": 5, "name": "Kamil", "surname": "Ludvík", "address": "Čemerná 22, Ostrava"}
]

response = mycol.insert_many(customers)

print(response.inserted_ids)
