class Account:
    def __init__(self, owner, balance=0, min_balance=50):
        self.owner = owner
        self.balance = balance
        self.min_balance = min_balance
        self.loan_balance = 0
        self.deposits = []
        self.withdrawals = []
        self.loans = []
        self.repaid = []
        self.interests = []
        self.transfers = {} 
        self.is_frozen = False
    def deposit(self, amount):
        if self.is_frozen:
            print("Account is frozen: can't deposit")
            return
        if amount > 0:
            self.balance += amount
            self.deposits.append(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive")
    def withdraw(self, amount):
        if self.is_frozen:
            print("Account is frozen: can't withdraw")
            return
        if amount <= 0:
            print("Withdrawal amount must be positive")
            return
        if self.balance - amount < self.min_balance:
            print("Withdrawal would violate minimum balance requirement")
        elif amount <= self.balance:
            self.balance -= amount
            self.withdrawals.append(f"Withdrawn: {amount}")
        else:
            print("Insufficient funds")
    def transfer(self, amount, recipient):
        if self.is_frozen:
            print("Account is frozen: can't transfer")
            return
        if amount <= 0:
            print("Transfer amount must be positive")
            return
        if self.balance - amount < self.min_balance:
            print("Transfer would violate minimum balance requirement")
        elif amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            transfer_detail = f"Transferred: {amount} to {recipient.owner}"
            if recipient.owner in self.transfers:
                self.transfers[recipient.owner].append(transfer_detail)
            else:
                self.transfers[recipient.owner] = [transfer_detail]
            recipient.deposits.append(f"Received: {amount} from {self.owner}")
        else:
            print("Insufficient funds")
    def get_loan(self, amount):
        if self.is_frozen:
            print("Account is frozen: can't get loan")
            return
        if amount > 0:
            self.loan_balance += amount
            self.balance += amount
            self.loans.append(f"Loan received: {amount}")
        else:
            print("Loan amount must be positive")
    def repay_loan(self, amount):
        if self.is_frozen:
            print("Account is frozen: can't repay loan")
            return
        if amount <= 0:
            print("Repayment amount must be positive")
            return
        if amount <= self.balance and amount <= self.loan_balance:
            self.balance -= amount
            self.loan_balance -= amount
            self.repaid.append(f"Loan repaid: {amount}")
        else:
            print("Insufficient funds or loan balance to repay")
    def view_account_details(self):
        return f"Owner: {self.owner}, Balance: {self.balance}, Loan Balance: {self.loan_balance}, Minimum Balance: {self.min_balance}"
    def change_account_owner(self, new_owner):
        if new_owner:
            self.owner = new_owner
        else:
            print("New owner name cannot be empty")
    def get_statement(self):
        print(f"Account Statement for {self.owner}:")
        print("Deposits:")
        for deposit in self.deposits:
            print(f"  {deposit}")
        print("Withdrawals:")
        for withdrawal in self.withdrawals:
            print(f"  {withdrawal}")
        print("Transfers:")
        for recipient, transfers in self.transfers.items():
            print(f"  To {recipient}:")
            for transfer in transfers:
                print(f"    {transfer}")
        print("Loans:")
        for loan in self.loans:
            print(f"  {loan}")
        print("Loan Repayments:")
        for repayment in self.repaid:
            print(f"  {repayment}")
        print("Interest Applied:")
        for interest in self.interests:
            print(f"  {interest}")
        print(f"Current Balance: {self.balance}, Loan Balance: {self.loan_balance}")
    def apply_interest(self):
        if not self.is_frozen:
            interest = self.balance * 0.05
            self.balance += interest
            self.interests.append(f"Interest applied: {interest}")
        else:
            print("Account is frozen: can't apply interest")
    def freeze_account(self):
        self.is_frozen = True
    def unfreeze_account(self):
        self.is_frozen = False
    def set_minimum_balance(self, amount):
        if amount >= 0:
            self.min_balance = amount
        else:
            print("Minimum balance cannot be negative")
    def close_account(self):
        if self.loan_balance > 0:
            print("Cannot close account with outstanding loan balance")
            return
        self.balance = 0
        self.loan_balance = 0
        self.is_frozen = True
        print("Account closed")













