from connect_mango import mydb_pr24

mycol = mydb_pr24["test_collection"]

# vkladanie dokkumentu do db
response = mycol.insert_one({"street_name": "jesenné", "number": 5, "city": "Košice"})

print(response.inserted_id)
