class BankAccountException(Exception):
    pass


class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    @property
    def account_number(self):
        pass

    @account_number.setter
    def account_number(self, _):
        raise BankAccountException("Account number cannot be changed")

    @account_number.deleter
    def account_number(self):
        if self.balance > 0:
            raise BankAccountException(
                "Account cannot be deleted with positive balance"
            )

        print("Account number deleted")

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):

        if new_balance < 0:
            raise BankAccountException("Balance cannot be a negative number")

        self._balance = new_balance

    def withdrawal(self, amount):
        self._audit_operation(amount, operation="withdrawal")
        self.balance -= amount

    def deposit(self, amount):
        self._audit_operation(amount, operation="deposit")
        self.balance += amount

    @staticmethod
    def _audit_operation(amount, operation):
        audit_ceil = 100_000

        if amount > audit_ceil:
            print(f"AUDIT - Amount {amount} above audit ceil for {operation} operation")

    def __str__(self):
        return f"{self.__class__.__name__}(account_number: {self._account_number}, balance: {self._balance})"


if __name__ == "__main__":
    account = BankAccount("112233", 1000)
    print(account)

    try:
        account.balance = -200
    except BankAccountException as e:
        print(e)

    try:
        account.account_number = "223344"
    except BankAccountException as e:
        print(e)

    account.deposit(1_000_000)
    print(account)

    try:
        del account.account_number
    except BankAccountException as e:
        print(e)

    account.withdrawal(1001000)
    print(account)

    del account.account_number
