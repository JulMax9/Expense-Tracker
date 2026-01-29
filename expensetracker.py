import json

expense = []

def load_from_file():
    try:
        with open("expensetracker.json", "r") as f:
            global expense
            expense = json.load(f)
        print(f"loaded {len(expense)} expenses")
    except FileNotFoundError:
        print("No saved file found, starting fresh")

def add_expense():
    while True:
        try:
            amount = float(input("Enter an amount: "))
            if amount > 0:
                break
            else:
                print("Enter a positive number")
        except ValueError:
            print("Oops, enter a positive integer.")
            
    category = input("Enter the category: ")
    date = input("Enter the date: ")

    expense.append({
                
        "amount": amount,
        "category": category,
        "date": date
                
    })

    print(expense)

def view_expense():
    if len(expense) == 0:
        print("The expense list is still empty")
    else:
        for index, exp in enumerate(expense, start=1):
            print(f"{index}. {exp['amount']}, {exp['category']}, {exp['date']}")

def total_expense():
    total = 0
    if len(expense) == 0:
        print("Expense List is empty")
    else:
        for exp in expense:
            total += exp["amount"]
    print(f"The total Amount for all expenses {total}")
    

def highest_expense():
    if len(expense) == 0:
        print("expense list is empty")
        return

    max_expense = expense[0]
        
    for exp in expense:
        if exp["amount"] > max_expense["amount"]:
            max_expense = exp
    print(f"Highest :₩{max_expense['amount']} - {max_expense['category']}")

def category_breakdown():
    total_category = {} # for addition money(amount) per category

    for exp in expense:
        cat = exp["category"]
        amt = exp["amount"]

        if cat in total_category:
            total_category[cat] += amt
        else:
            total_category[cat] = amt

    print("\nCategory Breakdown: ")
    for category, total in total_category.items():
        print(f" - {category}: ₩{total}")

def save_to_file():
    with open("expensetracker.json", "w") as f:
        json.dump(expense, f, indent=2)
    print("Expenses added")
    
load_from_file()

while True:
    options = ["Add expenses:", "View expenses:","Total expense:", "Highest expense:", "Category breakdown:", "Quit:"]
    for index, opt in enumerate(options, start=1):
        print(f"{index}. {opt}")

    try:
        choice = int(input("make a choice: "))
        if choice == 1:
            add_expense()
        elif choice == 2:
            view_expense()
        elif choice == 3:
            total_expense()
        elif choice == 4:
            highest_expense()
        elif choice == 5:
            category_breakdown()
        elif choice == 6:
            save_to_file()
            print("Done using the expense tracker, see you next time!")
            break
        else:
            print("Wrong Input")
    except ValueError:
        print("Enter a valid choice")

    
    

    
        
    
    
