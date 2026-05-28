class Bank:
    def __init__ (self, name, last_name, number, login, password, balance):
        self.name = name
        self.last_name = last_name
        self.number = number
        self.login = login
        self.password = password
        self.balance = balance
        
    def get_info(self):
        print(f'Имя: {self.name} | Фамилия: {self.last_name} | Номер телефона: {self.number} | Логин: {self.login} | Пароль: {self.password}')
    
    def get_info_bank_menu(self):
        print(f'Имя: {self.name} | Фамилия: {self.last_name} | Баланс: {self.balance}')
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f'Операция успешна! Баланс: {self.balance}')
        else:
            print(f'Недостаточно средств.')
            
    def put_money(self, amount):
        self.balance += amount
        print(f'Операция успешна! Баланс: {self.balance}')