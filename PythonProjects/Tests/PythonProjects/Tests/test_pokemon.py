import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
Token = '4f10a21aafec52bad2dbcb07be66f9b1'
Header = {'Content-Type' : 'application/json','trainer_token':Token}
Trainer_id = '35804'
Trainer_name = 'Don'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {('id','35804')})
    assert response.status_code == 200
     
@pytest.mark.parametrize('key,value',[('id', Trainer_id),('name', Trainer_name)])
def test_parametrize(key, value):
    response_parametrize = requests.get(url=f'{URL}/trainers', headers=Header, params={'trainer_id':Trainer_id})
    assert response.status_code == 200, f"Ошибка статуса: {response.status_code}"
    trainer_data = response.json()['data'][0]
    assert response_parametrize.json()["data"][0][key] == value
    assert trainer_data[key] == value, f"Значение '{key}' не соответствует ожидаемому значению '{value}', получено: {trainer_data[key]}"   
   
    

