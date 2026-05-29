from storage import save_data, load_data, load_history, save_history
from models import Bank

def withdraw_money(user):
    data = load_data()
    amount = int(input('Введите сумму, которую хотите снять: '))
    user_object = Bank(user['name'], user['last_name'], user['number'], user['login'], user['password'], user['balance'])
    user_object.withdraw(amount)
    for item in data:
        if item['login'] == user['login']:      #item because user in main bank_menu function
            item['balance'] = user_object.balance      #user who in account
            user['balance'] = user_object.balance
    save_data(data)
    
def put_on(user):
    data = load_data()
    amount = int(input('Введите сумму, которую хотите положить на счет: '))
    user_object = Bank(user['name'], user['last_name'], user['number'], user['login'], user['password'], user['balance'])
    user_object.put_money(amount)
    for item in data:
        if item['login'] == user['login']:
            item['balance'] = user_object.balance
            user['balance'] = user_object.balance
    save_data(data)
    
def withdraw_money(user): 
    name = input('Введите имя пользователя, которому хотите перевести деньги: ')
    number = int(input('Введите номер карты пользователя: '))
    amount = int(input('Введите сумму, которую хотите перевести: '))
    print(f'Перевод {name} | Номер карты: {number} | Сумма перевода: {amount}')
    right = input('Все верно? Да/Нет: ').lower()
    if right == 'да':
        data = load_data()
        user_object = Bank(user['name'], user['last_name'], user['number'], user['login'], user['password'], user['balance'])
        user_object.withdraw(amount)
        for item in data:
            if item['login'] == user['login']:
                item['balance'] = user_object.balance
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