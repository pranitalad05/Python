# Create user with user interface that gives 2 menu options
# 1. Deposit
# 2. Withdraw
# Both options will ask user to enter money to withdraw/deposit
# Display a statement with each transaction and final balance after user exits from the menu
# Identify possible Exceptions and implement them


from Python.Assignments.Assignment_No_2.Transactions import Transaction
from Python.Assignments.Assignment_No_2.Accounts import SavingsAccount, CurrentAccount

if __name__=='__main__':
    statement=[]
    print('-------- Choose Account Type --------')
    print('1) Personal Savings')
    print('2) Corporate Savings')
    print('3) Current')

    ch = int(input('Enter Choice : '))

    if ch == 1:
        acc = SavingsAccount(101, 'Pranita', 80000, 'personal')
    elif ch == 2:
        acc = SavingsAccount(101, 'Dhriti', 180000, 'corporate')
    elif ch == 3:
        acc = CurrentAccount(101, 'Ashish', 280000)
    else:
        print('Invalid Account Type!!!!')
        exit()

    print('----------------------')
    print(acc)

    print('-------- Bank Menu --------')
    print('1) Deposit')
    print('2) Withdraw')
    print('3) Exit')
    while True:
        try:
            choice = int(input('Enter Choice : '))

            if choice==1:
                amt = int(input('Enter amount to deposit : '))
                bal = Transaction.deposit_to_account(acc,amt)
                msg=f'Deposited amount : {amt} | {bal}'
                # print(msg)
                statement.append(msg)

            elif choice == 2:
                amt = int(input('Enter amount to withdraw : '))
                bal = Transaction.withdraw_from_account(acc, amt)
                msg = f'Withdraw amount : {amt} | Balance : {bal}'
                # print(msg)
                statement.append(msg)

            elif choice==3:
                break

            else:
                print('Invalid Choice!!!')

        except Exception as e:
            print(e)


    print('>>>> Transactional Statements <<<<')
    for message in statement:
        print(message)



