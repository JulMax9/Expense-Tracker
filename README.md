# Expense-Tracker
 A console-based expense tracker built in Python to practice core programming concepts. Users can add expenses, view records, calculate totals, analyze spending by category, identify the highest expense, and persist data using JSON. Built incrementally as a learning project.

## Features

- **Add Expenses**: Record expenses with amount, category, and date
- **View Expenses**: Display all recorded expenses in a formatted list
- **Total Expenses**: Calculate the sum of all expenses
- **Highest Expense**: Find and display the largest single expense
- **Category Breakdown**: Analyze spending by category
- **Data Persistence**: Automatically saves and loads data using JSON

## What I Learned

### Core Python Concepts
- Working with lists and dictionaries
- List comprehension and enumeration
- Error handling with try/except blocks
- Input validation
- Function organization

### Data Management
- JSON file handling (saving and loading structured data)
- Data aggregation and analysis
- Working with complex data structures

### Problem-Solving Skills
- Debugging JSON decode errors
- Implementing data validation
- Structuring a multi-feature application

## How to Run
```bash
python3 expensetracker.py
```

## Requirements

- Python 3.x
- No external libraries required (uses built-in `json` module)

## Usage

1. Run the program
2. Choose from the menu:
   - `1` - Add a new expense
   - `2` - View all expenses
   - `3` - See total spending
   - `4` - Find highest expense
   - `5` - View spending by category
   - `6` - Save and quit

3. Data is automatically saved when you quit and loaded when you restart

## Project Structure
```
expense-tracker/
├── expensetracker.py    # Main application
└── expensetracker.json  # Data storage (created automatically)
```

## Example
```
1. Add expenses:
2. View expenses:
3. Total expense:
4. Highest expense:
5. Category breakdown:
6. Quit:

make a choice: 1
Enter an amount: 50
Enter the category: Food
Enter the date: 2025-01-27
```

## Future Improvements

- Date range filtering
- Budget limits with warnings
- Export to CSV
- Data visualization
- Monthly/weekly summaries

## Skills Demonstrated

- Python fundamentals
- File I/O operations
- JSON data handling
- Error handling
- User input validation
- Data analysis and aggregation

---

**Built as part of my Python learning journey** 🚀
