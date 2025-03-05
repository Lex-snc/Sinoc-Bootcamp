class BankingSystem:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited: ${amount}. New balance: ${self.balance}.')

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds!')
        else:
            self.balance -= amount
            print(f'Withdrew: ${amount}. New balance: ${self.balance}.')

    def check_balance(self):
        print(f'Current balance: ${self.balance}.')


def main():
    bank = BankingSystem()
    while True:
        print('\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit')
        choice = input('Choose an option: ')
        if choice == '1':
            amount = float(input('Enter amount to deposit: '))
            bank.deposit(amount)
        elif choice == '2':
            amount = float(input('Enter amount to withdraw: '))
            bank.withdraw(amount)
        elif choice == '3':
            bank.check_balance()
        elif choice == '4':
            print('Exiting...')
            break
        else:
            print('Invalid choice!')

if __name__ == '__main__':
    main()
