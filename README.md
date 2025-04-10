🚀 How to Run the App:
----------------------
1. Clone this repository
$ git clone https://github.com/Mothishmr/expense-tracker.git
$ cd expense-tracker

2. (Optional) Create a virtual environment
$ python -m venv venv
$ source venv/bin/activate        # For Linux/macOS
$ venv\\Scripts\\activate         # For Windows

3. Run the application

1. Install dependencies:
   pip install tk
$ python app.py

Once the GUI opens:
- Add expenses with date, amount, and category
- Set your monthly budget
- View report to compare budget vs spent
- Get an alert if you try to add an expense exceeding the budget (it won’t be added)


Expense Tracker App (Tkinter + SQLite)
======================================

💸 Description:
---------------
A simple personal expense tracker application built with Tkinter (Python GUI) and SQLite. It allows users to:
- Log daily expenses
- Set monthly budgets per category
- View alerts if the spending exceeds the budget
- View monthly reports comparing budget vs actual expenses

🗂️ Project Structure:
---------------------
expense-tracker/
│
├── app.py          # Main GUI application
├── db.py           # Handles database logic
├── util.py         # Utility functions like alerts and date handling
├── expenses.db     # SQLite database (auto-created on first run)
└── README.txt      # Setup and run instructions

✅ Requirements:
----------------
- Python 3.6 or higher

To check your Python version:
$ python --version

Make sure Tkinter is installed (usually comes pre-installed).
To check:
$ python -m tkinter

On Linux, if not installed:
$ sudo apt-get install python3-tk


🛠 Features:
------------
- Add and store expenses in local SQLite DB
- Set monthly budget per category
- Get alerts when budget is exceeded
- View budget vs expenses per category

📦 Future Ideas:
----------------
- Add charts (pie, bar) using matplotlib
- Export reports to Excel/PDF
- Add user login system
- Create a web version using Flask or Django

🤝 Contribution:
----------------
Feel free to fork the repo and contribute! Suggestions and issues are welcome.

📄 License:
-----------
MIT License
