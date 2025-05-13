import pytest
from unittest.mock import patch

try:
    from project import Bank_defence
except ImportError:
    print("Warning: project.py not found.")
    pytest.skip("project.py not found", allow_module_level=True)

def test_initialization_and_str():
    account = Bank_defence(name="TestUser", defence=100)
    assert account.name_prop == "TestUser"
    assert account.balance == 100
    assert str(account) == "User: TestUser , Defence: 100"

    account_default_balance = Bank_defence(name="DefaultUser")
    assert account_default_balance.name_prop == "DefaultUser"
    assert account_default_balance.balance == 0
    assert str(account_default_balance) == "User: DefaultUser , Defence: 0"

@patch('builtins.input', return_value='50')
def test_save_money_valid(mock_input):
    account = Bank_defence(name="TestSave", defence=100)
    message = account.save_money()
    assert account.balance == 150
    assert message == "You have saved 50 dollars. Current balance: 150"

@patch('builtins.input', return_value='-50')
def test_save_money_negative(mock_input):
    account = Bank_defence(name="TestSaveNeg", defence=100)
    message = account.save_money()
    assert account.balance == 100
    assert message == "Deposit amount cannot be negative."

@patch('builtins.input', return_value='abc')
def test_save_money_invalid_input(mock_input):
    account = Bank_defence(name="TestSaveInvalid", defence=100)
    message = account.save_money()
    assert account.balance == 100
    assert message == "Please enter a valid numeric amount."

@patch('builtins.input', return_value='50')
def test_withdraw_money_valid(mock_input):
    account = Bank_defence(name="TestWithdraw", defence=100)
    message = account.withdraw_money()
    assert account.balance == 50
    assert message == "You have withdrawn 50 dollars. Current balance: 50"

@patch('builtins.input', return_value='-50')
def test_withdraw_money_negative(mock_input):
    account = Bank_defence(name="TestWithdrawNeg", defence=100)
    message = account.withdraw_money()
    assert account.balance == 100
    assert message == "Withdrawal amount cannot be negative."

@patch('builtins.input', return_value='150')
def test_withdraw_money_insufficient_funds(mock_input):
    account = Bank_defence(name="TestWithdrawInsuff", defence=100)
    message = account.withdraw_money()
    assert account.balance == 100
    assert message == "Insufficient balance. Current balance: 100"

@patch('builtins.input', return_value='xyz')
def test_withdraw_money_invalid_input(mock_input):
    account = Bank_defence(name="TestWithdrawInvalid", defence=100)
    message = account.withdraw_money()
    assert account.balance == 100
    assert message == "Please enter a valid numeric amount."

@patch('builtins.input', return_value='100')
def test_process_transaction_save(mock_amount_input):
    account = Bank_defence(name="ProcSave", defence=0)
    message = account.process_transaction("save")
    assert account.balance == 100
    assert message == "You have saved 100 dollars. Current balance: 100"
    
    account_s = Bank_defence(name="ProcSaveS", defence=0)
    message_s = account_s.process_transaction("s")
    assert account_s.balance == 100
    assert message_s == "You have saved 100 dollars. Current balance: 100"

@patch('builtins.input', return_value='50')
def test_process_transaction_withdraw(mock_amount_input):
    account = Bank_defence(name="ProcWithdraw", defence=100)
    message = account.process_transaction("withdraw")
    assert account.balance == 50
    assert message == "You have withdrawn 50 dollars. Current balance: 50"

    account_w = Bank_defence(name="ProcWithdrawW", defence=100)
    message_w = account_w.process_transaction("w")
    assert account_w.balance == 50
    assert message_w == "You have withdrawn 50 dollars. Current balance: 50"

@patch('builtins.input', side_effect=['invalid_choice', 'save'])
def test_chooce_serve_invalid_then_valid(mock_input):
    account = Bank_defence(name="TestServe")
    with patch('builtins.print') as mock_print:
        choice = account.chooce_serve()
        assert choice == "save"
        mock_print.assert_any_call("Invalid choice, please enter 'save' or 'withdraw'.")

@patch('builtins.input', return_value='withdraw')
def test_chooce_serve_valid_withdraw(mock_input):
    account = Bank_defence(name="TestServeW")
    choice = account.chooce_serve()
    assert choice == "withdraw"

@patch('builtins.input', return_value='s')
def test_chooce_serve_valid_s(mock_input):
    account = Bank_defence(name="TestServeS")
    choice = account.chooce_serve()
    assert choice == "s" 