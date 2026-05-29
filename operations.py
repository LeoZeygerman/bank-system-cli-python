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