from connect_mango import mydb_pr24

mycol = mydb_pr24["customers"]

myquery = {"surname": "Adam"}
print(f"Výsledok dotazu: {myquery}")

for response in mycol.find(myquery):
    print(response)

mycol.delete_one(myquery)                                       # zmažeme (jeden) dokument

# Pre kontrolu vypíšeme znovu:
for response in mycol.find(myquery):
    print(response)

print("-"*100)
myquery = {"address": {"$regex": "Ostrava$"}}
for response in mycol.find(myquery):
    print(response)

response = mycol.delete_many(myquery)                           # zmažeme (všetky) dokumenty pre adresu Ostrava
print(f"Bolo zmazaných {response.deleted_count} záznamov.")

print("-"*100)
print("Zmaže všetky záznamy:")
response = mycol.delete_many({})
print(f"Bolo zmazaných {response.deleted_count} záznamov.")

print("-"*100)
print("Databáza je prázdna:")
for response in mycol.find():
    print(response)

print("="*100)
print("Zmažeme celú kolekciu:")
mycol.drop()

