# =============================
# db.py - Handles all database-related operations
# =============================
# - Initializes the SQLite database with two tables:
#     1. expenses: stores individual expense entries
#     2. budgets: stores category-wise budgets for each month
# - Provides functions to:
#     - add an expense (with budget limit check)
#     - set/update a budget
#     - get total spent for a month
#     - get category-wise budget vs spending report

import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("expenses.db")
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS budgets (
            category TEXT,
            month TEXT NOT NULL,
            budget REAL NOT NULL,
            PRIMARY KEY (category, month)
        )
    ''')

    conn.commit()
    conn.close()

def add_expense(amount, category, date):
    conn = sqlite3.connect("expenses.db")
    c = conn.cursor()
    c.execute("INSERT INTO expenses (amount, category, date) VALUES (?, ?, ?)", (amount, category, date))
    conn.commit()
    conn.close()

def set_budget(category, month, budget):
    conn = sqlite3.connect("expenses.db")
    c = conn.cursor()
    c.execute("REPLACE INTO budgets (category, month, budget) VALUES (?, ?, ?)", (category, month, budget))
    conn.commit()
    conn.close()

def get_total_spent(month):
    conn = sqlite3.connect("expenses.db")
    c = conn.cursor()
    c.execute("SELECT SUM(amount) FROM expenses WHERE strftime('%Y-%m', date) = ?", (month,))
    result = c.fetchone()[0]
    conn.close()
    return result or 0

def get_budget_report(month):
    conn = sqlite3.connect("expenses.db")
    c = conn.cursor()
    c.execute('''
        SELECT b.category, b.budget,
               IFNULL(SUM(e.amount), 0) AS spent
        FROM budgets b
        LEFT JOIN expenses e ON b.category = e.category AND strftime('%Y-%m', e.date) = ?
        WHERE b.month = ?
        GROUP BY b.category
    ''', (month, month))
    result = c.fetchall()
    conn.close()
    return result
