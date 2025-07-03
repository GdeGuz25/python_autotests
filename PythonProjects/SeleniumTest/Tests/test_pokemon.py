import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '4f10a21aafec52bad2dbcb07be66f9b1'
HEADER = {'Content-type':'application/json','trainer_token':TOKEN}
TRAINER_ID = '35804'
TRAINER_NAME = 'Don'

def test_status_code():
    response = requests.get(url=f'{URL}/trainers', params= {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url=f'{URL}/trainers',headers=HEADER, params = {'trainer_id': TRAINER_ID})
    assert response_get.json()['data'][0]["name"] == 'Don'

@pytest.mark.parametrize('key, value', [('name', TRAINER_NAME),('trainer_id', TRAINER_ID), ('id', TRAINER_ID)])
def test_parametrize(key, value):
   response_parametrize = requests.get(url=f'{URL}/trainers', headers = HEADER, params= {'trainer_id': TRAINER_ID})
   assert response_parametrize.json()['data'][0][key] == value