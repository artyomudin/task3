import json

list_of_names = []
main_dict = {
    'name': 'first_name',
    'surname': 'last_name',
    'phone number': 'phone_number',
    'city': 'my_city',
    'state': 'my_state'
}


# просим от пользователя внести данные
def enter_data():
    print('please enter your data : ')
    for key, value in main_dict.items():
        main_dict[key] = input('insert your {} here:'.format(key))
    full_name = main_dict['name'] + '_' + main_dict['surname']
    main_dict.update({'full_name': full_name})
    print('your info is here: ')
    print(main_dict)
    print('\nyour information is here {}'.format(main_dict))
    print('your login here is \' {} \''.format(main_dict.get('full_name')))
enter_data()


# сохраняем информацию в формате json
with open('someinfo.json', 'w') as file_object:
    json.dump(main_dict, file_object)

# добавляем функцию поиска информации по имени

def name_search():

    with open('someinfo.json') as file_object:
        main_dict = json.load(file_object)


    while True:
        name = input('insert your name here or enter \'q\' if you want to quit: ')
        if name == main_dict['name']:
            print('your info: ')
            print(main_dict)
        else:
            name == 'q'
            break

name_search()

# добавляем функцию поиска по фамилии
def surname_search():
    with open('someinfo.json') as file_object:
        main_dict = json.load(file_object)

    while True:
        surname = input('insert your surname here or enter \'q\' if you want ot quit: ')
        if surname == main_dict['surname']:
            print('here is your info:')
            print(main_dict)
        elif surname == 'q':
            break

surname_search()

# добваляем функцию поиска по логину
def my_fullnamesearch():
    with open('someinfo.json') as file_object:
        main_dict = json.load(file_object)

    while True:
        f_name = input('insert your login here, please or enter \'q\' if you want ot quit: ')
        if f_name == main_dict['full_name']:
            print('here is your info:')
            print(main_dict)
        elif f_name == 'q':
            break

my_fullnamesearch()

# добавляем поиск по номеру телефона
def phone_search():
    with open('someinfo.json') as file_object:
        main_dict = json.load(file_object)

    while True:
        y_phone = input('enter your phone number here or enter \'q\' if you want ot quit: ')
        if y_phone == main_dict['phone number']:
            print('here is your info:')
            print(main_dict)
        elif y_phone == 'q':
            break

phone_search()

# ищем по городу или стране
def location_search():
    with open('someinfo.json') as file_object:
        main_dict = json.load(file_object)

    while True:
        location = input('insert your city or your country here or enter \'q\' if you want to quit: ')
        if location == main_dict['city'] or location == main_dict['state']:
            print('here is your info: ')
            print(main_dict)
        elif location == 'q':
            break

location_search()

# функция для удаления номера телефона
def number_destroy():
    with open('someinfo.json', 'w') as file_object:
        json.dump(main_dict, file_object)

    destroy = input('enter \'d\' if you want to clean your phone number')
    active = True
    while active:
        if destroy == 'd':
            main_dict['phone number'] = None
            active = False
            print(main_dict)
        else:
            print('did you want to insert \'d\'?')
            continue

number_destroy()

# функция для обновления номера телефона
def renew_phonenumber():
    with open('someinfo.json', 'w') as file_object:
        json.dump(main_dict, file_object)

    print('insert your new phone number here: ')
    new_number = input('new number: ')
    main_dict['phone number'] = new_number
    print('check, please, your information')
    print(main_dict)

renew_phonenumber()


