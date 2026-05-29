from storage import save_data, load_data, load_history, save_history
from models import Bank
from operations import withdraw_money, put_on, withdraw_money
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
                withdraw_money(user)
                
            if choice == 3:
                put_on(user)
                    
            if choice == 4:
                withdraw_money(user)

            if choice == 5:
                exit()
            
    except ValueError:
        print('Ошибка при вводе!')