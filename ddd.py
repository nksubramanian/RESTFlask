import requests
import pprint
api_key = "0727df6d2314a2aa171adfc210588a20"
api_key_v4 = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwNzI3ZGY2ZDIzMTRhMmFhMTcxYWRmYzIxMDU4OGEyMCIsInN1YiI6IjYwNjZlYjhlMTJjNjA0MDAyOTVjZDc1MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.9QIAJmZQebPbYlxvVyyZsDUDRzCSmu54XLVIGC5Uxno"

movie_id = 500
api_version = 3
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
r = requests.get(endpoint)
print(r.status_code)
print(r.text)


# using v4
movie_id = 550
api_version = 4
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
headers = {
    'Authorization': f'Bearer {api_key_v4}',
    'Content-Type': 'application/json;charset=utf-8'
}
r = requests.get(endpoint, headers=headers)
print(r.status_code)
print(r.text)


print("-------------------------------")

api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/search/movie"
searh_query = "The Matrix"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={searh_query}"
print(endpoint)
r = requests.get(endpoint)
pprint.pprint(r.json())
