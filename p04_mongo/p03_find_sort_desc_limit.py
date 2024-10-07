from connect_mango import mydb_pr24

mycol = mydb_pr24["customers"]

print("-"*100)
print("Find one:")
print("")

response = mycol.find_one()
print(response)

print("")
print("-"*100)
print("Find:")
print("")

for response in mycol.find():
    print(response)

print("")
print("-"*100)
print("Find (iba vybrané atribúty):")
print("")

for response in mycol.find({}, {"name": 1, "surname": 1}):
    print(response)

print("")
print("-"*100)
print("Find (základné atribúty):")
print("")

for response in mycol.find({}, {"address": 0, "email": 0, "phone_number": 0}):
    print(response)

print("")
print("-"*100)
print("Tie 0 a 1 vo find nemôžem kombinovať - výnimka je id_:")
print("")

for response in mycol.find({}, {"_id": 0, "name": 1, "surname": 1}):
    print(response)

print("")
print("="*100)

myquery = {"surname": "Novák"}
print(f"Výsledok pre dotaz: {myquery}:")
print("")

for response in mycol.find(myquery, {"_id": 0, "name": 1, "surname": 1}):
    print(response)

print("")
print("-"*100)
print("Všetci zákazníci priezvisko začína na N a väčie:")
print("")

myquery = {"surname": {"$gt": "N"}}
for response in mycol.find(myquery, {"_id": 0, "name": 1, "surname": 1}):
    print(response)

print("")
print("-"*100)
print("Všetci zákazníci priezvisko začína na N (pomocou regex):")
print("")

myquery = {"surname": {"$regex": "^N"}}
for response in mycol.find(myquery, {"_id": 0, "name": 1, "surname": 1}):
    print(response)

print("")
print("-"*100)
print("Všetci zákazníci, ktorých adresa končí mestom Ostrava (pomocou regex):")
print("")

myquery = {"address": {"$regex": "Ostrava$"}}
for response in mycol.find(myquery, {"_id": 0, "name": 1, "surname": 1, "address": 1}):
    print(response)

print("")
print("-"*100)
print("Všetci zákazníci, ktorých meno je Novák a adresa končí mestom Ostrava (pomocou regex):")
print("")

myquery = {"surname": "Novák", "address": {"$regex": "Ostrava$"}}
for response in mycol.find(myquery, {"_id": 0, "name": 1, "surname": 1, "address": 1}):
    print(response)

print("")
print("-"*100)
print("Všetci zákazníci usporiadaný podľa priezvyska:")
print("")

for response in mycol.find().sort("surname"):
    print(response)

print("")
print("-"*100)
print("Všetci zákazníci usporiadaný podľa priezvyska vzostupne:")
print("")

for response in mycol.find().sort("surname", -1):
    print(response)

print("")
print("-"*100)
print("Všetci zákazníci usporiadaný podľa priezvyska a mena:")
print("")

for response in mycol.find().sort("name").sort("surname"):
    print(response)

print("")
print("-"*100)
print("Všetci zákazníci, ktorý majú uvedené priezvisko a meno:")
print("")

myquery = {"surname": {"$exists": "true"}, "name": {"$exists": "true"}}
for response in mycol.find(myquery, {"_id": 0, "name": 1, "surname": 1}):
    print(response)

print("")
print("-"*100)
print("Všetci zákazníci s vyplneným emailom:")
print("")

myquery = {"email": {"$exists": "true"}}
for response in mycol.find(myquery, {"_id": 0, "name": 1, "surname": 1, "email": 1}):
    print(response)

print("")
print("-"*100)
print("Všetci zákazníci bez vyplneného emailu (s not):")
print("")

myquery = {"email": {"$not": {"$exists": "true"}}}
for response in mycol.find(myquery, {"_id": 0, "name": 1, "surname": 1, "email": 1}):
    print(response)

print("")
print("-"*100)
print("Všetci zákazníci bez vyplneného emailu (s 0):")
print("")

myquery = {"email": {"$exists": 0}}
for response in mycol.find(myquery, {"_id": 0, "name": 1, "surname": 1, "email": 1}):
    print(response)

print("")
print("-"*100)
print("Všetci zákazníci bez vyplneného priezviska:")
print("")

myquery = {"surname": {"$exists": 0}}
for response in mycol.find(myquery, {"_id": 0, "name": 1, "surname": 1}):
    print(response)

print("")
print("-"*100)
print("Prvý traja zákazníci:")
print("")

for response in mycol.find().sort("surname").limit(3):
    print(response)
