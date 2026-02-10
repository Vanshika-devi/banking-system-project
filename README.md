# banking-system-project
Budget AppA Python-based personal finance tracker that manages multiple budget categories. It tracks deposits, withdrawals, and transfers while providing a visual bar chart of spending distributions.

Key FeaturesCategory Management: Create specific categories like "Food," "Entertainment," or "Business."Ledger Tracking: Every transaction is stored with an amount and a description.Balance Validation: The check_funds helper ensures you never withdraw more than you have available.Inter-Category Transfers: Easily move money between categories (e.g., moving $50 from "Business" to "Food").Formatted Output: A custom __str__ method prints a clean, aligned receipt for each category.Spending Visualization: Generate an ASCII bar chart showing the percentage of total spending per category.

Class Methods: CategoryMethodDescriptiondeposit(amount, desc)
Adds a positive amount to the ledger.withdraw(amount, desc)Adds a negative amount if funds are available. Returns True if successful.get_balance()Returns the current total remaining in the category.transfer(amount, cat)Withdraws from the current category and deposits into another.check_funds(amount)Returns True if the balance is greater than or equal to the amount.
## Spending Chart LogicThe create_apend_chart function provides a bird's-eye view of your expenses:
Calculates the total withdrawals (spending) across all categories.Determines what percentage of the total spending each category represents.Renders a vertical bar chart using "o" characters, rounded down to the nearest 10%.## Quick Start ExamplePython# Create a category
food = Category("Food")

# Add funds
food.deposit(1000, "Initial deposit")

# Record expenses
food.withdraw(10.15, "Groceries")
food.withdraw(15.89, "Restaurant")

# Transfer to another category
clothing = Category("Clothing")
food.transfer(50, clothing)

# Print the report
print(food)
Output Preview:Plaintext*************Food*************
initial deposit        1000.00
groceries              -10.15
restaurant             -15.89
Transfer to Clothing   -50.00
Total: 923.96
## Future EnhancementsData Persistence: Save ledgers to a .json or .csv file so data isn't lost when the script closes.Monthly Reset: Add functionality to clear ledgers at the start of a new month.Input Validation: Ensure amount is always a positive number.
