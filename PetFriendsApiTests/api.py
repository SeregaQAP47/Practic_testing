import requests
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder
import os

class PetFriends:
    def __init__(self):
        self.base_url = "https://petfriends1.herokuapp.com/"

    def get_api_key(self, email:str, password:str) -> json:
        '''Метод выполняет GET запрос к API сервера и возвращает статус запроса и результат в формате Json
         с уникальным ключом пользователя, найденного по указанным email и паролю'''

        headers = {
            'email' : email,
            'password' : password
        }
        res = requests.get(self.base_url + 'api/key', headers = headers)

        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def get_list_of_pets(self, auth_key : json, filter : str = "") -> json:
        '''Метод выполняет GET запрос к API сервера и возвращает статус запроса и результат в формате Json
        (список питомцев), используя уникальный ключ пользователя и фильтр '''

        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}
        res = requests.get(self.base_url + 'api/pets', headers = headers, params = filter)

        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def add_new_pets(self, auth_key:json , name:str, animal_type:str, age:str, pet_photo:str) -> json:
        '''Метод выполняет POST запрос к API сервера и добавляет нового питомца, возврвщает статус запроса и
        результат в формате Json'''

        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })

        headers = {'auth_key': auth_key['key'],
                   'Content-Type': data.content_type
                   }

        res = requests.post(self.base_url + 'api/pets', headers = headers, data = data)

        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result

    def delete_pet(self, auth_key: json, pet_id: str) -> json:
        """Метод отправляет на сервер запрос на удаление питомца по указанному ID и возвращает
        статус запроса и результат в формате JSON с текстом уведомления о успешном удалении.
        На сегодняшний день тут есть баг - в result приходит пустая строка, но status при этом = 200"""

        headers = {'auth_key': auth_key['key']}

        res = requests.delete(self.base_url + 'api/pets/' + pet_id, headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def update_pet_info(self, auth_key: json, pet_id: str, name: str,
                        animal_type: str, age: int) -> json:
        """Метод отправляет запрос на сервер о обновлении данных питомуа по указанному ID и
        возвращает статус запроса и result в формате JSON с обновлённыи данными питомца"""

        headers = {'auth_key': auth_key['key']}
        data = {
            'name': name,
            'age': age,
            'animal_type': animal_type
        }

        res = requests.put(self.base_url + 'api/pets/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def add_new_pets_no_photo(self, auth_key:json , name:str, animal_type:str, age:str) -> json:
        '''Метод выполняет POST запрос к API сервера и добавляет нового питомца без фотографии,
         возврвщает статус запроса и
        результат в формате Json'''

        data = {
                'name': name,
                'age': age,
                'animal_type': animal_type
            }

        headers = {'auth_key': auth_key['key'] }

        res = requests.post(self.base_url + 'api/create_pet_simple', headers = headers, data = data)

        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result

    def update_pet_set_photo(self, auth_key: json,pet_id: str, pet_photo: str) -> json:
        '''Метод выполняет POST запрос к API сервера и добавляет фото питомца , возврвщает статус запроса и
        результат в формате Json'''

        data = MultipartEncoder(
            fields={
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })

        headers = {'auth_key': auth_key['key'],
                   'Content-Type': data.content_type
                   }

        res = requests.post(self.base_url + 'api/pets/set_photo/'+ pet_id, headers=headers, data=data)

        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result

    def add_new_pets_age_int(self, auth_key:json, name:str, animal_type:str, age:int) -> json:
        '''Метод выполняет POST запрос к API сервера и добавляет нового питомца без фотографии,
        с числовым значением возраста, возврвщает статус запроса и
        результат в формате Json'''

        data = {
                'name': name,
                'age': age,
                'animal_type': animal_type
            }

        headers = {'auth_key': auth_key['key'] }

        res = requests.post(self.base_url + 'api/create_pet_simple', headers = headers, data = data)

        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result