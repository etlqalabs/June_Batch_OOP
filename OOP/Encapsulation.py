# parent class
class Bank:
    def __init__(self,owner,balance,pin):
        self.account_holder = owner
        self._account_balance = balance
        self.__account_pin = pin

    def print_account_holder_name(self):
        print("Account holder name is ",self.account_holder)

    def print_account_holder_balance(self):
        print("Account holder balance is ",self._account_balance)

    def print_account_holder_pin(self):
        print("Account holder pin is ",self.__account_pin)


# child class to Bank
class SavingsAccount(Bank):
    def __init__(self,owner,balance,pin,interest_rate):
        super().__init__(owner,balance,pin)
        self.savings_interest_rate = interest_rate

    def print_interest_rate(self):
        print("Interest of savings account is ",self.savings_interest_rate)

    def print_pin_inside_child_class(self):
        print(self.__pin_number)

class CallingClass:
# Create a object of savingsAccount
    savingAcount = SavingsAccount("Rakesh",6000,12345,10)
    #print(savingAcount.__account_pin)
    savingAcount.print_account_holder_pin()
    savingAcount.print_pin_inside_child_class()







'''
    # Accessing the value of variable using public methods
    print("Accessing the value of variable using public methods")
    bank = Bank("Hetu",5000,1234)
    bank.print_account_holder_name()
    bank.print_account_holder_balance()
    bank.print_account_holder_pin()

    # Accessing the value of variable directly
    print("Accessing the value of variable directly")
    print(bank.account_holder)
    print(bank._account_balance)
    #print(bank.__account_pin)
'''





