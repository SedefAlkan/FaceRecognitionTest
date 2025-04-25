from opencv.fr.compare.schemas import CompareRequest
from opencv.fr.search.schemas import SearchMode
from sdk import sdk


image_path_1 = "register/burcu1.webp"

image_path_2 = "register/burcu3.webp"

compare_request = CompareRequest([image_path_1], [image_path_2], 
                                 search_mode=SearchMode.FAST)
score = sdk.compare.compare_image_sets(compare_request)
print(score)

