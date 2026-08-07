class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []

    def add_income(self, amount, description):
        self.incomes.append((amount,description))

    def add_expense(self, amount, description):
        self.expenses.append((amount, description))

    def total_income(self):
        return sum(income[0] for income in self.incomes)

    def total_expense(self):
        return sum(expense[0] for expense in self.expenses)

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        return f"Name: {self.firstname} {self.lastname}"