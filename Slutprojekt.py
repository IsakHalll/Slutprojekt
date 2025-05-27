import json
import os
import time


class BudgetManager:    # Klass för att hantera budgeten
    def __init__(self, filename="budget_data.json"):
        self.filename = filename # Filnamn där data ska sparas
        self.income = 0
        self.expenses = 0
        self.transactions = []
        self.load_data() # Ladda data från filen om den finns

  
    def load_data(self):   # Ladda data från JSON-filen
        try:
            with open(self.filename, "r") as file:
                data = json.load(file) # Hämta data från filen
                self.income = data.get("income", 0)
                self.expenses = data.get("expenses", 0)
                self.transactions = data.get("transactions", [])
        except FileNotFoundError: # Om filen inte finns
            pass

    
    def save_data(self):    # Spara data till JSON-filen
        data = {
            "income": self.income,
            "expenses": self.expenses,
            "transactions": self.transactions
        }
        with open(self.filename, "w") as file: # Skriv data till filen
            json.dump(data, file)

    
    def add_income(self, amount, description=""):   # Lägg till en inkomst
        self.income += amount
        self.transactions.append({"type": "income", "amount": amount, "description": description}) # Lägg till i listan
        self.save_data()    #  Spara data

    def add_expense(self, amount, description=""):   # Lägg till en utgift
        self.expenses += amount
        self.transactions.append({"type": "expense", "amount": amount, "description": description}) # Lägg till i listan
        self.save_data()    # Spara data

    def get_balance(self):  # Beräkna och returnera nuvarande balans
        return self.income - self.expenses
    
    def show_transactions(self):    # Visa alla transaktioner
        for transaction in self.transactions:
            print(f"{transaction['type']}: {transaction['amount']} - {transaction['description']}")


def main(): # Huvudfunktion
    manager = BudgetManager()

    while True: # Visa meny för användaren
        os.system('cls')
        print("\nBudgethanterare")
        print("1. Lägg till inkomst")
        print("2. Lägg till utgift")
        print("3. Visa balans")
        print("4. Visa transaktioner")
        print("5. Avsluta")
        choice = input("Välj ett alternativ: ")

        if choice == "1": # Lägg till inkomst
            try:
                amount = float(input("Ange belopp: "))
                description = input("Ange beskrivning: ")
                manager.add_income(amount, description)
            except:
                print("Fel: Ange ett giltigt tal för beloppet.")
                time.sleep(1)

        elif choice == "2": # Lägg till utgift
            try:
                amount = float(input("Ange belopp: "))
                description = input("Ange beskrivning: ")
                manager.add_expense(amount, description)
            except ValueError:
                print("Fel: Ange ett giltigt tal för beloppet.")
                time.sleep(1)
                
        elif choice == "3": # Visa saldo
            os.system('cls')
            print(f"Nuvarande balans: {manager.get_balance()}")
            input("Tryck på Enter för att fortsätta...")

        elif choice == "4": # Visa alla transaktioner
            os.system('cls')
            print("Transaktioner:")
            manager.show_transactions()
            input("Tryck på Enter för att fortsätta...")

            
        elif choice == "5": # Avsluta programmet
            break
        else: # Hantera ogiltigt val
            print("Ogiltigt val, försök igen.")

if __name__ == "__main__":
    main()