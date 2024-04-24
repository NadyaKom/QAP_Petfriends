from api import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password
import os

pf = PetFriends()

def test_get_api_key_for_invalid_email_invalid_password(email=invalid_email, password=invalid_password):
    """Проверяем возможность входа при неверном логине и пароле """

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(invalid_email, invalid_password)

    assert status == 400
    assert status == 400
      

def test_get_api_key_for_invalid_email_valid_password(email=invalid_email, password=valid_password):
     """Проверяем возможность входа при неверном логине и верном пароле """

     # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(invalid_email, valid_password)

     assert status == 400
     assert status == 400
     

def test_get_api_key_for_invalid_email_valid_password(email=valid_email, password=invalid_password):
    """Проверяем возможность входа при верном логине и неверном пароле """
   
    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, invalid_password)

    assert status == 400
    assert status == 400

def test_get_api_key_for_invalid_user(email=valid_email, password=valid_password):
    """Проверяем возможность входа при верном логине и верном пароле """

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    
    assert status == 200
    assert 'key' in result

def test_add_new_pet_with_invalid_data_invalid_age(name='Персик', animal_type='кот',
                                     age='65948776554'):
    """Проверяем добавление питомца с  некорректными данными слишком большим числом в возрасте"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    
    

def test_add_new_pet_with_invalid_data_invalid_animal_type(name='Персик', animal_type='1568792855',
                                     age='4'):
    """Проверяем добавление питомца с  некорректными данными - некоректными данными в animal_type """
   
    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age)
    
    assert status == 200
    assert result['name'] == name
                                    
def test_add_new_pet_with_incomplete_data(name='Персик', animal_type=' ',
                                     age=' '):
    """Проверяем что можно добавить питомца с неполными данными"""
   
    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_get_my_pets_with_valid_key(my_pets):
    """ Проверяем что запрос моих питомцев возвращает только список моих питомцев"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_my_pets(auth_key, my_pets)

    assert status == 200
    assert len(result['pets']) == my_pets

def test_delete_pet_by_id(pet_id='f70212c3-4ced-4fa7-b4a5-17041a6f8454'):
    """ Проверяем удаление питомца по id""" 
   
    pet_id = 'f3043661-b5a7-41b2-be7c-39e1e3141290'
    status, _ = pf.delete_pet(auth_key, pet_id)

    #запрашиваем список своих питомцев
    _, my_pets = pf.get_list_my_pets(auth_key, "my_pets")

    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()

def test_delete_pet_by_invalid_id(pet_id='f70212c3-4ced-4fa7-b4a5-17041a6f')
   """ Проверяем удаление питомца по  неверному id""" 
   
    pet_id = 'ff70212c3-4ced-4fa7-b4a5-17041a6f'
    status, _ = pf.delete_pet(auth_key, pet_id)

    #запрашиваем список своих питомцев
    _, my_pets = pf.get_list_my_pets(auth_key, "my_pets")

    # Проверяем что статус ответа равен 400 и в списке питомцев нет такого  id  питомца
    assert status == 400
    assert pet_id not in my_pets.values()
