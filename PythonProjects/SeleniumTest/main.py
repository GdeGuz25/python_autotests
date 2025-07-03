import requests

URL = 'https://api.pokemonbattle.ru/v2'
Token = '4f10a21aafec52bad2dbcb07be66f9b1'
Header = {'Content-Type' : 'application/json','trainer_token': Token}

body_confirmation = {
    "trainer_token": Token
}

body_create = {
    "name": "Ulybka",
    "photo_id": 619
    }

response_create = requests.post(url=f'{URL}/pokemons', headers=Header, json= body_create)
print(response_create.text)
if response_create.status_code == 200:
   print(f"Error creating Pokemon: {response_create.text}")
else:
   pokemon_id = response_create.json().get('id')
   if not pokemon_id:
      raise ValueError("Pokemon ID is missing in the response")
   else:
      print(f"Pokemon created with ID:{pokemon_id}")


body_rename = {
    "id": "pokemon_id",
    "name": "Milashka",
    }

message = response_create.json()['message']
print(message)

response_rename = requests.put(url=f'{URL}/pokemons',headers=Header, json=body_rename)
if response_rename.status_code == 200:
  print(f"Error renaming Pokemon:{response_rename.text}")
else:
   print("Pokemon renamed successfully.")

body_catch = {
    "pokemon_id": pokemon_id
}

response_catch = requests.post(url=f'{URL}/pokemons/add_pokeball', headers=Header, json=body_catch)
if response_catch.status_code == 200:
   print(f"Error catching Pokemon: {response_catch.text}")
else:
   print("Pokemon caught successfully.")