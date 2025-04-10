# =============================
# util.py - Helper utilities for alerts
# =============================
# - Provides function to:
#     - check if any category has exceeded its monthly budget
#     - show alert messages using tkinter messagebox if exceeded

from tkinter import messagebox
from db import get_budget_report

def check_budget_alert(month):
    report = get_budget_report(month)
    for category, budget, spent in report:
        if spent > budget:
            messagebox.showwarning("Budget Exceeded", f"You've exceeded the budget for {category}!")
