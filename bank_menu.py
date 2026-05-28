from storage import save_data, load_data, load_history, save_history
from models import Bank
def bank_menu(user):
    try:
        print (f'Имя: {user['name']} | Баланс: {user['balance']}')
            
        while True:
            print('1. Проверить данные.')
            print('2. Снять деньги.')
            print('3. Пополнить баланс.')
            print('4. Перевести деньги.')
            print('5. Выйти')
            choice = int(input('Ваш выбор: '))
            
            if choice == 1:
                user_object = Bank(user['name'], user['last_name'], user['number'], user['login'], user['password'], user['balance'])
                user_object.get_info_bank_menu()
                continue
            
            if choice == 2:
                data = load_data()
                amount = int(input('Введите сумму, которую хотите снять: '))
                user_object = Bank(user['name'], user['last_name'], user['number'], user['login'], user['password'], user['balance'])
                user_object.withdraw(amount)
                for user in data:
                    user['balance'] = user_object.balance
                    save_data(data)
                
            if choice == 3:
                data = load_data()
                amount = int(input('Введите сумму, которую хотите положить на счет: '))
                user_object = Bank(user['name'], user['last_name'], user['number'], user['login'], user['password'], user['balance'])
                user_object.put_money(amount)
                for user in data:
                    user['balance'] = user_object.balance
                    save_data(data)
                    
            if choice == 4:
                name = input('Введите имя пользователя, которому хотите перевести деньги: ')
                number = int(input('Введите номер карты пользователя: '))
                amount = int(input('Введите сумму, которую хотите перевести: '))
                print(f'Перевод {name} | Номер карты: {number} | Сумма перевода: {amount}')
                right = input('Все верно? Да/Нет: ').lower()
                if right == 'да':
                    data = load_data()
                    user_object = Bank(user['name'], user['last_name'], user['number'], user['login'], user['password'], user['balance'])
                    user_object.withdraw(amount)
                    for user in data:
                        user['balance'] = user_object.balance
                        save_data(data)
                    history = load_history()
                    history_object = {
                        'name': name,
                        'number': number,
                        'amount': amount
                    }
                    history.append(history_object)
                    save_history(history)
                else:
                    print('Возврат.')

            if choice == 5:
                exit()
            
    except ValueError:
        print('Ошибка при вводе!')