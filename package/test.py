from module1 import Account, AccountControl
from module2 import FinancialServices
from pack2module1 import Authorize 
from pack2module2 import CustomerService 

def test_account():
    print("\nTesting Account")
    test = Account("1234", 1000, "password123")
    test.add_transaction(200, "deposit")
    print(f"New balance after deposit: {test.balance}")
    test.add_transaction(100, "withdrawal")
    print(f"New balance after withdrawal: {test.balance}")

def test_account_control():
    print("\nTesting AccountControl...")
    test = AccountControl()
    test_1 = Account("1234", 1500, "password1234")
    test.add_account(test_1)
    print(f"Balance for account 002: {test.check_balance('002')}")

def test_financial_services():
    print("\nTesting FinancialServices...")
    fs = FinancialServices()
    ac = Account("123", 1000, "password12345")
    fs.account_control.add_account(ac)
    fs.account_control.execute_transaction("003", 300, "deposit")
    print(f"New balance after deposit: {fs.account_control.check_balance('123')}")
    fs.account_control.execute_transaction("003", 150, "withdrawal")
    print(f"New balance after withdrawal: {fs.account_control.check_balance('123')}")
    
def test_authorize():
    print("\nTesting Authorize")
    ac = AccountControl()
    auth = Authorize("3333", "password123456", ac)
    auth.add_user("user1", "pass1")
    result = auth.login("user1", "pass1")
    print("Login successful?" if result else "Login failed")

def test_customer_service():
    print("\nTesting CustomerService")
    cs = CustomerService()
    cs.save_message()
    cs.customer_service()


def main():
    test_account()
    test_account_control()
    test_financial_services()
    test_authorize()
    test_customer_service()

if __name__ == "__main__":
    main()