from api import PetFriends
from settings import *
import os

pf = PetFriends()

def test_get_api_key_for_valid_user(email = valid_email, password = valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_all_pets_with_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert  status == 200
    assert len(result['pets']) > 0

def test_add_new_pets(name='Пуховой', animal_type='скот', age='5'):
    # Тестирование POST запроса, добавление питомца без фотографии

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pets_no_photo(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name

def test_api_update_set_photo( pet_photo = 'images/snake12.jpg'):
    # Тестирование PUT запроса, добавление фотографии питомца
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    print(my_pets)

    if len(my_pets['pets']) > 0 :
        status, result = pf.update_pet_set_photo(auth_key, my_pets['pets'][3]['id'],pet_photo)

    assert status == 200
    # assert result['name'] == name
    # assert result['pet_photo'] == pet_photo

def test_get_api_key_no_valid(email = false_email, password = false_password):
    # тест GET запрса с незарегистрированнным email и password
    status, result = pf.get_api_key(email, password)
    assert status != 200
    assert 'key' not in result

def test_get_api_key_empty_email(email = empty_email, password = valid_password):
    # тест GET запрса с пустой строкой email и валидным password
    status, result = pf.get_api_key(email, password)
    assert status != 200
    assert 'key' not in result

def test_get_api_key_empty_password(email = valid_email, password = empty_password):
    # тест GET запрса с валидным email и пустой строкой password
    status, result = pf.get_api_key(email, password)
    assert status != 200
    assert 'key' not in result

def test_get_api_key_empty(email=empty_email, password=empty_password):
    # тест GET запрса с пустой строкой email и пустой строкой password
    status, result = pf.get_api_key(email, password)
    assert status != 200
    assert 'key' not in result

def test_add_new_pets_name_null(name='', animal_type='скот', age='2', pet_photo = 'images/fuzz.jpg'):
    #Тест запроса POST на создание нового питомца без имени
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pets(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name

def test_add_new_pets_one_photo(name='', animal_type='', age='', pet_photo= 'images/fuzz.jpg'):
    #Тест запроса POST на создание нового питомца
    # без имени, без породы,без возраста, используюя только фотографию
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pets(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['pet_photo']

def test_add_new_pets_age_negative_number(name='Kitty', animal_type='скот', age=-2):
    #Тест запроса POST на создание нового питомца с отрицательным значение возраста

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pets_age_int(auth_key, name, animal_type,age)

    assert status == 200 , 'Баг: ввод отрицательного значения в поле возраст'
    assert result['name'] == name

def test_get_false_key(filter=''):
    # Тестирование GET запроса с передачей неверного auth_key
    status, auth_key = pf.get_api_key(false_email, false_password)
    assert auth_key
    assert  status == 403



