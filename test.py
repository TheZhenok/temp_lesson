import requests
from typing import Union, TypeAlias

dtype: TypeAlias = list[dict[str, Union[str, int]]]
url = "https://radio-world-75-000-worldwide-fm-radio-stations.p.rapidapi.com/api.php"

querystring: requests.sessions._Params = {
    "count": "50",
    "page": "1",
    "radios": ""
}

headers: requests.sessions._HeadersUpdateMapping = {
	"X-RapidAPI-Key": "acd59aae3emsh93ef919f01829c4p170d14jsne067e455ac6b",
	"X-RapidAPI-Host": "radio-world-75-000-worldwide-fm-radio-stations.p.rapidapi.com"
}

response: requests.Response = \
    requests.request(
        "GET", 
        url, 
        headers=headers, 
        params=querystring
    )

data: dtype = response.json()
print(data)
print(len(data))

# http://localhost:7000?a=5&b=10