from sdk import sdk 
from opencv.fr.collections.schemas import UpdateCollectionRequest


#personlist
persons = sdk.persons.list()
print(persons)
print(persons.count)

#collectionlist
all_collections = sdk.collections.list()
print(all_collections)
print(all_collections.count)

update_collection_request1 = UpdateCollectionRequest()
update_collection_request1.collection_id = "4dfa8c90-3adf-4c08-b880-53e81d8281d2" 
update_collection_request1.new_person_ids= [
    "e5a2740f-9062-4bb6-bd6a-4e1ec9626e69",

]

update_collection_request = UpdateCollectionRequest()
update_collection_request.collection_id = "f62b20c3-2ef3-4832-8953-97b1f79ec1d4"  # Tek koleksiyon ID
update_collection_request.new_person_ids = [
    "7b8150b6-e2b0-44e1-b288-6d8907478bfb",
    "30031e8b-ff7d-4d08-9667-6940860f87fc",
    "28693cd8-dd27-487e-a632-4bb278600ada"
]

#update_collection_request.removed_person_ids = ["e5a2740f-9062-4bb6-bd6a-4e1ec9626e69"]  # Çıkarılacak kişi ID

update_collection_response = sdk.collections.update_collection_persons(update_collection_request)
update_collection_response = sdk.collections.update_collection_persons(update_collection_request1)


print(update_collection_response)