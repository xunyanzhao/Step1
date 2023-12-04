Class Account
To create a bank account with some attributes 

Attributes
account_id: account id.
balance:  current balance of the account.
transaction_history: A list of all transactions by time.
password: The password for the account.

Methods

__init__(self, account_number, initial_balance, password)
Initializes a new account.

add_transaction(self, amount, transaction_type)
Records a new transaction.


update_balance(self, amount, transaction_type)

This method will upadate the account balance after transaction.


Class AccountControl

Manages banking accounts 

Attributes
account: A dictionary storing all accounts, key is account id.

Methods
__init__(self)
Initializes the AccountControl 
 
add_account(self, account)
Adds a new account to the our banking system.

check_balance(self, account_id)
check the balance based ob the account_id.


print_transaction_history(self, transactions)
print the transaction history in a good format

view_transaction_history(self, start_date=None, end_date=None)
retrun the transaction history for a user input date range.


execute_transaction(self, account_id, amount, transaction_type)
identify a transaction on a based account_id and transaction_type .


Class FinancialServices

financial services like fund transfer, deposit, and withdrawal.

Attributes
account_control: An instance of AccountControl.

Methods
__init__(self)
Initializes the FinancialServices instance.

fund_transfer(self, first_account_id, sec_account_id, amount)
Transfers funds between your accout or other's account.


deposit(self, user_id, amount)
Deposits money into an account.


withdrawal(self, user_id, amount)
Withdraws money from an account.

