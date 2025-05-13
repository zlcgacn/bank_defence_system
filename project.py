import sys


class Bank_defence:
    def __init__(self , name , defence=0):
        """
        Initialize user name and deposit amount
        """
        self.name_prop = name
        self.balance = defence

    def __str__(self):
        """
        Return user name and deposit amount
        """
        return f"User: {self.name_prop} , Defence: {self.balance}"
    
    
    def chooce_serve(self) -> str:
        """
        Choose to save money or withdraw money
        """
        serve = ""
        while True:
            serve = input("Choose your serve (save/withdraw):")
            if serve not in ["save" , "withdraw" , "s" , "w"]:
                print("Invalid choice, please enter 'save' or 'withdraw'.")
            else:
                break
        return serve
        
    
    def process_transaction(self , serve):
        """
        Process save money or withdraw money based on service selection.
        """
        message = ""
        if serve == "save" or serve == "s":
            message = self.save_money()
        elif serve == "withdraw" or serve == "w":
            message = self.withdraw_money()
        
        return message


    def save_money(self):
        """
        Save money
        """
        try:
            save_money_amount = int(input("Save your money:"))
            if save_money_amount < 0:
                return "Deposit amount cannot be negative."
            self.balance += save_money_amount
            return f"You have saved {save_money_amount} dollars. Current balance: {self.balance}"
        except ValueError:
            return "Please enter a valid numeric amount."


    def withdraw_money(self):
        """
        Withdraw money
        """
        try:
            withdraw_money_amount = int(input("Withdraw your money:"))
            if withdraw_money_amount < 0:
                return "Withdrawal amount cannot be negative."
            if withdraw_money_amount > self.balance:
                return f"Insufficient balance. Current balance: {self.balance}"
            self.balance -= withdraw_money_amount
            return f"You have withdrawn {withdraw_money_amount} dollars. Current balance: {self.balance}"
        except ValueError:
            return "Please enter a valid numeric amount."


def main():    
    user_input_name = ""
    while not user_input_name:
        user_input_name = input("Please enter your username: ").strip()
        if not user_input_name:
            print("Username cannot be empty, please re-enter.")
            
    bank_account = Bank_defence(name=user_input_name)
    print(f"Account '{bank_account.name_prop}' created successfully, initial balance: {bank_account.balance}")

    keep_running = True
    while keep_running:
        selected_service = bank_account.chooce_serve()
        transaction_message = bank_account.process_transaction(serve=selected_service)
        if transaction_message:
            print(transaction_message)
        print(bank_account)

        while True:
            continue_choice = input("Do you want to perform another operation? (yes/y/ye or no/n): ").strip().lower()
            if continue_choice in ['yes', 'y', 'ye']:
                break 
            elif continue_choice in ['no', 'n']:
                keep_running = False 
                break 
            else:
                print("Invalid input, please enter 'yes'/'y'/'ye' or 'no'/'n'.")
    
    print("Thank you for using our service!")

if __name__ == "__main__":
    main()
        
        
