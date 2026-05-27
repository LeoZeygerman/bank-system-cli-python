from storage import save_data, load_data
from models import Bank
def bank_menu():
    while True:
        data = load_data()
        for user in data:
            print (f'Имя: {user['name']} | Баланс: {user['balance']}')
        break