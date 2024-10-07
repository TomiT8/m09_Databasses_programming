from connect_mango import mydb_pr24

mycol = mydb_pr24["customers"]

myquery = {"surname": {"$exists": 0}}
print(mycol.find_one(myquery))
new_values = {"$set": {"surname": "Chýlková"}}

mycol.update_one(myquery, new_values)

myquery = {"name": "Ivana"}
print(mycol.find_one(myquery))

print("-"*100)
print("Zmena priezvyska u Jany Bledej")
myquery = {"name": "Jana", "surname": "Bledá"}
print(mycol.find_one(myquery))
new_values = {"$set": {"surname": "Veselá"}}
mycol.update_one(myquery, new_values)
print(mycol.find_one({"name": "Jana"}))

print("-"*100)
print("Všetkým zákazníkom z Ostravy pridáme informáciu o kraji.")
myquery = {"address": {"$regex": "Ostrava$"}}
for response in mycol.find(myquery):
    print(response)
new_values = {"$set": {"district": "Moravskoslezký kraj"}}
response = mycol.update_many(myquery, new_values)
print(f"Bolo zmenených {response.modified_count} záznamov.")
for response in mycol.find(myquery):
    print(response)