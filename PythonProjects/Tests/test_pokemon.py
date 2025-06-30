import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
Token = '4f10a21aafec52bad2dbcb07be66f9b1'
Header = {'Content-Type' : 'application/json','trainer_token':Token }
Trainer_id = '35804'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {('id','35804')})
    assert response.status_code == 200
     
@pytest.mark.parametrize('key,value',[('id','35804')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url=f'{URL}/trainers', params={'trainer_id':Trainer_id})
    response_name = requests.get(url=f'{URL}/trainers', params={('trainer_id',Trainer_id),('id','35804'),('name','Don'),})
    assert response_parametrize.json()["data"][0][key] == value
    assert response_name.json()["data"][0][key] == value
   
   
    

