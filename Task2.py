import json
from datetime import datetime

class Transaction:
    def __init__(self, type, category, amount, date):
        self.type = type
        self.category = category
        self.amount = amount
        self.date = date

    def __str__(self):
        return f"{self.date} - {self.type}: {self.category} (${self.amount})"

class BudgetTracker:
    def __init__(self):
        self.transactions = []

    def add_expense(self, category, amount, date):
        transaction = Transaction("Expense", category, amount, date)
        self.transactions.append(transaction)

    def add_income(self, category, amount, date):
        transaction = Transaction("Income", category, amount, date)
        self.transactions.append(transaction)

    def calculate_budget(self):
        income = sum(transaction.amount for transaction in self.transactions if transaction.type == "Income")
        expenses = sum(transaction.amount for transaction in self.transactions if transaction.type == "Expense")
        return income - expenses

    def analyze_expenses(self):
        expense_categories = {}
        for transaction in self.transactions:
            if transaction.type == "Expense":
                if transaction.category in expense_categories:
                    expense_categories[transaction.category] += transaction.amount
                else:
                    expense_categories[transaction.category] = transaction.amount
        return expense_categories

    def save_transactions(self, filename):
        with open(filename, 'w') as f:
            json.dump([vars(transaction) for transaction in self.transactions], f)

    def load_transactions(self, filename):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.transactions = [Transaction(**transaction) for transaction in data]
        except FileNotFoundError:
            pass

def main():
    budget_tracker = BudgetTracker()
    budget_tracker.load_transactions("transactions.json")

    while True:
        print("\n1. Add Expense")
        print("2. Add Income")
        print("3. View Budget")
        print("4. Analyze Expenses")
        print("5. Save and Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            budget_tracker.add_expense(category, amount, date)
        elif choice == '2':
            category = input("Enter income category: ")
            amount = float(input("Enter income amount: "))
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            budget_tracker.add_income(category, amount, date)
        elif choice == '3':
            remaining_budget = budget_tracker.calculate_budget()
            print(f"Remaining Budget: ${remaining_budget}")
        elif choice == '4':
            expense_categories = budget_tracker.analyze_expenses()
            for category, amount in expense_categories.items():
                print(f"{category}: ${amount}")
        elif choice == '5':
            budget_tracker.save_transactions("transactions.json")
            print("Transactions saved. Quitting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
