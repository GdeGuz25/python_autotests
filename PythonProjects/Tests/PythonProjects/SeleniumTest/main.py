import requests

URL = 'https://api.pokemonbattle.ru/v2'
Token = '4f10a21aafec52bad2dbcb07be66f9b1'
Header = {'Content-Type' : 'application/json','trainer_token':Token }

body_create = {
    "name": "Ulybka",
    "photo_id": -1
}
body_change = {
    "pokemon_id": "348991",
    "name": "Milashka",
    "photo_id": 2
}
body_catch = {
    "pokemon_id": "348991"
}

response_create = requests.post(url=f'{URL}/pokemons', headers=Header, json= body_create)
print(response_create.text)

message = response_create.json()['message']
print(message)

response_change = requests.put(url=f'{URL}/pokemons', headers=Header, json=body_change)
print(response_change.text)

response_catch = requests.post(url=f'{URL}/trainers/add_pokeball', headers=Header, json=body_catch)
print(response_catch.text)