from storage import save_data, load_data
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
                    
            if choice == 5:
                exit()
            
    except ValueError:
        print('Ошибка при вводе!')