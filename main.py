from storage import save_data, load_data
from models import Bank
from bank_menu import bank_menu

while True:
    try:
        data = load_data()
        if len(data) == 0:
            print('Регистрация')
            name = input('Введите имя: ')
            last_name = input('Введите фамилию: ')
            number = int(input('Введите номер телефона: '))
            login = input('Введите ваш логин: ')
            password = input('Введите пароль: ')
            balance = 0
            user = {
                'name': name,
                'last_name': last_name,
                'number': number,
                'login': login,
                'password': password,
                'balance': balance
            }
            data.append(user)
            save_data(data)
            user_object = Bank(name, last_name, number, login, password, balance)
            user_object.get_info()
            print('Регистрация прошла успешно, вход...')
            bank_menu()
            break
        
        else:
            while True:
                print('Войти')
                login = input('Введите логин: ')
                password = input('Введите пароль: ')
                data = load_data()
                for user in data:
                    if login == user['login'] and password == user['password']:
                        print('Вы успешно вошли.')
                        bank_menu() 
                        break
                    else:
                        print(f'Ошибка! Проверьте логин или пароль.')
                break
    except ValueError:
        print('Ошибка!')