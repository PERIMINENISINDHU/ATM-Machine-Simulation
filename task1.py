class ATM:
    def __init__(self, balance=1000, pin="1234"):
        self.balance = balance
        self.pin = pin
        self.transaction_history = []

    def check_balance(self):
        return f"Your current balance is ${self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
            return f"${amount} withdrawn successfully."

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount}")
        return f"${amount} deposited successfully."

    def change_pin(self, new_pin):
        self.pin = new_pin
        return "PIN changed successfully."

    def get_transaction_history(self):
        return self.transaction_history

def main():
    atm = ATM()  # Create an instance of the ATM class
    print("Welcome to the ATM Machine Simulation!")

    while True:
        print("\nOptions:")
        print("1. Check Balance")
        print("2. Withdraw Cash")
        print("3. Deposit Cash")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()  # Remove any surrounding whitespace

        if choice == '1': 
            print(atm.check_balance())
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            print(atm.withdraw(amount))
        elif choice == '3':
            amount = float(input("Enter amount to deposit: "))
            print(atm.deposit(amount))
        elif choice == '4':
            new_pin = input("Enter new PIN: ")
            print(atm.change_pin(new_pin))
        elif choice == '5':
            print("Transaction History:")
            for transaction in atm.get_transaction_history():
                print(transaction)
        elif choice == '6':
            print("Thank you for using the ATM Machine Simulation!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
