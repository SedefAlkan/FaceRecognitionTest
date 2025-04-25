from opencv.fr.persons.schemas import PersonBase
from sdk import sdk 

persons = [
    PersonBase(
        images=[
            "register/mine1.webp",
            "register/mine2.webp",
            "register/mine5.webp",
        ],
        name="Mine Tugay"
    ),
    PersonBase(
        images=[
            "register/burcu1.webp",
            "register/burcu2.jpg",
            "register/burcu3.webp",
        ],
        name="Burcu Özerk"
    ),
    PersonBase(
        images=[
            "register/hande2.jpg",
            "register/hande3.jpg",
            "register/hande4.webp",
        ],
        name="Hande Erçel"
    ),

    PersonBase(
        images=[
            "register/sedef1.png",
            "register/sedef2.png",
        ],
        name="Sedef Alkan"
    )

]

for person in persons:
    sdk.persons.create(person)