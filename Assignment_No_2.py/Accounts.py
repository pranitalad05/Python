#Create an Account class Hierarchy
# Account with super class (acc_id, name, balance)
# methods - withdraw and deposit

from abc import ABC,abstractmethod

class MinBalanceError(Exception):
    pass

class InsufficientBalanceError(Exception):
    pass

class AccountTypeError(Exception):
    pass

class MoreMoneyError(Exception):
    pass


class Account(ABC):
    def __init__(self,accid,name,balance):
        self._accid=accid
        self._name=name
        self._balance=balance

    @abstractmethod
    def withdraw(self,amount):
        pass

    @abstractmethod
    def deposit(self,amount):
        pass

    def __str__(self):
        return f'Name:{self._name} || Old Balance:{self._balance}'



# =======================================================================================================


# Create SavingsAccount as subclass of account - additional field (type - personal/corporate etc)
# implement withdraw and deposit such that
# - maximum upto 1 lak can be deposited in an account at a time
# - Min balance 5000 must be maintained while withdrawal (if type = corporate you withdraw full amount = balance)


class SavingsAccount(Account):
    def __init__(self,accid,name,balance,type):
        super().__init__(accid,name,balance)
        self._type=type

    def withdraw(self,amount):
        if self._type.lower()=='personal':
            if self._balance-amount<5000:
                raise MinBalanceError('Cannot Withdraw : Account below min balance')
            else:
                self._balance=self._balance-amount
            return self._balance


        if self._type.lower() == 'corporate':
            if self._balance<amount:
                raise InsufficientBalanceError('Cannot Withdraw : Insufficient balance')
            else:
                self._balance = self._balance - amount
            return self._balance

        else:
            raise AccountTypeError('Entered Wrong Account Type!!!!')

    def deposit(self,amount):
        if amount>100000:
            raise MoreMoneyError('Cannot add more than 1 lakh in account')
        else:
            self._balance+=amount
        return self._balance



# =======================================================================================================


# Create CurrentAccount as subclass of account
# implement withdraw and deposit such that
# - maximum upto 2 lak can be deposited in an account at a time
# - Min balance 10000 must be maintained while withdrawal


class CurrentAccount(Account):
    def __init__(self,accid,name,balance):
        super().__init__(accid,name,balance)

    def withdraw(self,amount):
        if self._balance - amount < 10000:
            raise MinBalanceError('Cannot Withdraw : Account below min balance')
        else:
            self._balance = self._balance - amount
        return self._balance


    def deposit(self,amount):
        if amount > 200000:
            raise MoreMoneyError('Cannot add more than 1 lakh in account')
        else:
            self._balance += amount
        return self._balance


# =======================================================================================================

