from pymongo  import MongoClient 
client=MongoClient('mongodb://localhost:27017/')
db=client['demo_cmr_db']

collection=db['employee']

print('connected to mongodb')

    # user = {"name":"psych","age":23,"city":"hogwards"}

    # insert_result=collection.insert_one(user)
    # print(insert_result)
    # print('inserted id',insert_result.inserted_id)

    # for user in collection.find():
    #     print(user)
        
        
    # users = [
    #     {'name':"alice","age":23,"city":"los angels"},
    #     {'name':"bob","age":29,"city":"Chicago"},
    # ]
    # insert_many_result=collection.insert_many(users)
    # print("inserted ids:",insert_many_result.inserted_ids)

for user in collection.find():
    print(user)

for user in collection.find({"city":"los angles"}):
    print(user)

user=collection.find_one({"name":"psych"})
if(user):
    print(user)
else:
    print('no user')
    
collection.update_one({"name":"alice"},{"$set":{"city":"los angels"}})

collection.delete_one({"name":"alice"})
# collection.drop()
# print("Collection deleted")