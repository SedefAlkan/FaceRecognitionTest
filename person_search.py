from opencv.fr.search.schemas import SearchRequest, SearchMode
from sdk import sdk


search_request = SearchRequest({"test/sedef3.png"})

result = sdk.search.search(search_request)

if result:
    print(result[0].person.name)
    print(result[0].score)

    # Kişinin ait olduğu koleksiyonları al
    person_id = result[0].person.id
    person_details = sdk.persons.get(person_id)  

    if person_details.collections:
        print("Bu kişi bu koleksiyona ait olabilir:")
        for collection in person_details.collections:
            print(f"-{collection.name}")
    else:
        print("Bu kişi herhangi bir koleksiyona ait görünmüyor.")

else:
    print("Eşleşen bir kişi bulunamadı.")
