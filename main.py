class User:
    account_count = 0
    accounts = []

    def __init__(self, name, email, address, account_type):
        User.account_count += 1
        self.account_number = User.account_count
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.loan_limit = 2
        self.loan_taken = 0
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
        else:
            print("Withdrawal amount exceeded")

    def check_balance(self):
        return self.balance

    def check_history(self):
        return self.transaction_history

    def take_loan(self, amount):
        if self.loan_limit > 0 and amount > 0:
            self.loan_taken += amount
            self.balance += amount
            self.loan_limit -= 1
            self.transaction_history.append(f"Took a loan of ${amount}")
        else:
            print("Loan limit exceeded or invalid loan request")

    def transfer(self, receiver, amount):
        if receiver:
            if self.balance >= amount:
                self.balance -= amount
                receiver.balance += amount
                self.transaction_history.append(f"Transferred ${amount} to account {receiver.account_number}")
            else:
                print("Not enough balance for the transfer")
        else:
            print("Account does not exist")

    def get_loan_limit(self):
        return self.loan_limit

    def bankrupt(self):
        if self.balance < 0:
            return True
        return False

class Admin:
    def __init__(self):
        self.users = []

    def create_account(self, name, email, address, account_type):
        user = User(name, email, address, account_type)
        self.users.append(user)
        return user

    def delete_account(self, account_number):
        for user in self.users:
            if user.account_number == account_number:
                self.users.remove(user)
                return True
        return False

    def list_accounts(self):
        return self.users

    def total_balance(self):
        total_balance = 0
        for user in self.users:
            total_balance += user.check_balance()
        return total_balance

    def total_loan_amount(self):
        total_loan = 0
        for user in self.users:
            total_loan += user.loan_taken
        return total_loan

    def toggle_loan_feature(self, status):
        User.loan_limit = 2 * status

def main():
    admin = Admin()

    user1 = admin.create_account("Kodom Ali", "kodomali@gmail.com", "Address1", "10000")
    user2 = admin.create_account("Sami", "sami@gmail.com", "Address2", "18000")

    user1.deposit(1000)
    user2.deposit(2000)

    user1.transfer(user2, 500)
    user1.transfer(user2, 1000)

    user1.take_loan(1500)
    user1.take_loan(5000)

    admin.toggle_loan_feature(True)

    user1.take_loan(2000)
    user2.withdraw(3000)

    for user in admin.list_accounts():
        print(f"Account {user.account_number}: {user.name}, Balance: ${user.check_balance()}, Loan Taken: ${user.loan_taken}")

    print(f"Total Bank Balance: ${admin.total_balance()}")
    print(f"Total Loan Amount: ${admin.total_loan_amount()}")
    print(f"Loan Feature Status: {User.loan_limit} loans allowed")

    if user1.bankrupt():
        print("User1's account is bankrupt")
    if user2.bankrupt():
        print("User2's account is bankrupt")

if __name__ == '__main__':
    main()
