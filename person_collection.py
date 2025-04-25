from opencv.fr.collections.schemas import CollectionBase
from sdk import sdk 


normal_people=CollectionBase(
name="Normal Pesople",
description="Person Test"

)
sdk.collections.create(normal_people)

famous_people=CollectionBase(
name="Famous People",
description="Person Test"

)
sdk.collections.create(famous_people)
