# Create Bank App with Transaction class
# Create Method withdraw_from_account(account : Account)  and deposit_to_account(account : Account)
# These methods will return the new balance after deposit/withdraw

from Accounts import(Account,SavingsAccount,CurrentAccount)

class Transaction:

    @staticmethod
    def deposit_to_account(account: Account, amount):
        return f'Balance after deposit : {account.deposit(amount)}'

    @staticmethod
    def withdraw_from_account(account : Account,amount):

        return f'Balance after withdraw : {account.withdraw(amount)}'



sap=SavingsAccount(101,'Pranita',80000,'personal')
sac=SavingsAccount(101,'Dhriti',180000,'corporate')
ca=CurrentAccount(101,'Ashish',280000)

print(sap)
Transaction.withdraw_from_account(sap,5000)
Transaction.deposit_to_account(sap,10000)
print('==================================')

print(sac)
Transaction.withdraw_from_account(sac,80000)
Transaction.deposit_to_account(sac,50000)
print('==================================')

print(ca)
Transaction.withdraw_from_account(ca,50000)
Transaction.deposit_to_account(ca,25000)
print('==================================')