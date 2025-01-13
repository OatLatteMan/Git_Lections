class BankAccount:
    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.number = number
        self.balance = balance


my_account = BankAccount('Suche Ganbaatar', 1, 100_000)


# -----------------------------------------------------------------


class BankAccount2:
    def __init__(self, owner, number, balance=0, owner_address='', owner_birth_date=None, owner_id=None):
        self.owner = owner
        self.owner_address_city = owner_address
        self.owner_address_street = owner_address
        self.owner_address_number = owner_address
        self.owner_birth_date = owner_birth_date
        self.owner_id = owner_id
        self.number = number
        self.balance = balance


my_account = BankAccount('Suche Ganbaatar', 1, 100_000)

# -----------------------------------------------------------------

class Address:
    def __init__(self, street, street_number, city):
        self.street = street
        self.street_number = street_number
        self.city = city

    def __str__(self):
        return f'{self.street} {self.street_number}, {self.city}'


class Person:
    def __init__(self, first_name, last_name, address: Address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

        self.accounts = set() # seznam bank. učtu

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class BankAccount3:
    def __init__(self, owner: Person, number: int, balance=0):
        self.owner = owner
        self.number = number
        self.balance = balance

        self.owner.accounts.add(self)

    def __str__(self):
        return f'Bank Account {self.number} from {self.owner}'

my_address = Address('Dolní', '176', 'Praha')
print(my_address)


my_self = Person('Suche', 'Ganbaatar', my_address)
my_account = BankAccount3(my_self, 1, 1000000)
my_account2 = BankAccount3(my_self, 2)

print(my_account2)

for account in my_self.accounts:
    print(account.balance, account.number, '<<<<<<')

print(my_account.balance)
print(my_account2.balance)
print(my_account.number)
print(my_account.owner.first_name)
print(my_account.owner.address.street)
print(my_account.owner.address)