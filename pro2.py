class category:
    def __init__(self,name):
        self.name=name
        self.ledger=[]
    def deposit(self,amount,description=""):
        self.ledger.append({"amount":amount,"description":description})
    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)
    def withdraw(self,amount,description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount":-amount,"description":description})
            return True
        else:
            return False
    def check_funds(self,amount):
        if self.get_balance()>=amount:
            return True
        else:
            return False
    def transfer(self,amount,cat):
        if self.check_funds(amount):
            self.withdraw(amount,f"Transfer to {cat.name}")
            cat.deposit(amount,f"Transfer from {self.name}")
            return True
        else:
            return False
    def  __str__(self):
        display=self.name.center(30,'*')+'\n'
        for item in self.ledger:
            short_desc = item["description"][:23]
            format_amount=f"{item['amount']:.2f}"[:7]
            display+=f"{short_desc:<23}{format_amount:<7}\n"
        display += f"Total: {self.get_balance()}"
        return display

def create_apend_chart(categories):
    spent_list = []
    for cat in categories:
        spent = 0
        for balue in cat.ledger:
            if balue['amount'] < 0:
                spent += abs(balue['amount'])
        spent_list.append(spent)
    
    total_spent = sum(spent_list)
    percents = [(s / total_spent * 100) // 10 * 10 for s in spent_list]
 
    res = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        res += f"{str(i).rjust(3)}| "
        for p in percents:
            res += "o  " if p >= i else "   "
        res += "\n"

    res += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    

    names = [cat.name for cat in categories]
    max_len = max(len(n) for n in names)
    names = [n.ljust(max_len) for n in names]
    
    for i in range(max_len):
        res += "     "
        for name in names:
            res += name[i] + "  "
        if i < max_len - 1:
            res += "\n"
            
    return res

# 1. SETUP THE OBJECTS
food = category("Food")
entertainment = category("Entertainment")
business = category("Business")

# 2. PERFORM TRANSACTIONS
food.deposit(900, "initial deposit")
food.withdraw(45.67, "groceries")
food.withdraw(15.00, "restaurant and more food")

entertainment.deposit(900, "initial deposit")
entertainment.withdraw(33.40, "movies")

business.deposit(900, "initial deposit")
business.withdraw(10.99, "office supplies")

# 3. PRINT THE LEDGERS (Testing your __str__ method)
print(food)
print(entertainment)
print(business)

# 4. CALL THE CHART FUNCTION
# We pass the objects inside a list
categories_list = [food, entertainment, business]
print(create_apend_chart(categories_list))