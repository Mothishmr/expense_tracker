# =============================
# app.py - Main GUI Application
# =============================
# - Provides a tkinter-based user interface
# - Lets users:
#     - Add expense logs 
#     - Set category-wise budgets for any month
#     - Shows alerts when spending exceeds budget
# - Internally connects to db.py for all data operations
# - Uses utils.py to check and alert if budget exceeded


import tkinter as tk
from tkinter import ttk, messagebox
from db import init_db, add_expense, set_budget, get_total_spent, get_budget_report
from utils import check_budget_alert
from datetime import datetime

init_db()

root = tk.Tk()
root.title("Expense Tracker")
root.geometry("600x600")
root.resizable(False, False)

# Categories
categories = ["Food", "Transport", "Entertainment", "Utilities", "Other"]

# -------------- Frames ----------------
notebook = ttk.Notebook(root)
notebook.pack(expand=1, fill="both")

expense_frame = ttk.Frame(notebook)
budget_frame = ttk.Frame(notebook)
report_frame = ttk.Frame(notebook)

notebook.add(expense_frame, text="Add Expense")
notebook.add(budget_frame, text="Set Budget")
notebook.add(report_frame, text="Reports")

# ---------------- Expense Tab ----------------
tk.Label(expense_frame, text="Category:").pack()
expense_category = tk.StringVar()
expense_menu = ttk.Combobox(expense_frame, textvariable=expense_category, values=categories, state="readonly")
expense_menu.pack()

tk.Label(expense_frame, text="Month (YYYY-MM):").pack()
expense_month_entry = tk.Entry(expense_frame)
expense_month_entry.insert(0, datetime.now().strftime("%Y-%m"))
expense_month_entry.pack()

tk.Label(expense_frame, text="Amount:").pack()
expense_amount_entry = tk.Entry(expense_frame)
expense_amount_entry.pack()

def save_expense():
    try:
        category = expense_category.get()
        month = expense_month_entry.get()
        amount = float(expense_amount_entry.get())

        if not category or not month:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        date = f"{month}-01"  # Use 1st of the month for consistency
        add_expense(amount, category, date)
        check_budget_alert(month)

        # Reset form
        expense_category.set("")
        expense_month_entry.delete(0, tk.END)
        expense_month_entry.insert(0, datetime.now().strftime("%Y-%m"))
        expense_amount_entry.delete(0, tk.END)

        messagebox.showinfo("Saved", "Expense added successfully!")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid amount.")

tk.Button(expense_frame, text="Save Expense", command=save_expense).pack(pady=10)

# ---------------- Budget Tab ----------------
tk.Label(budget_frame, text="Category:").pack()
budget_category = tk.StringVar()
budget_menu = ttk.Combobox(budget_frame, textvariable=budget_category, values=categories, state="readonly")
budget_menu.pack()

tk.Label(budget_frame, text="Month (YYYY-MM):").pack()
month_entry = tk.Entry(budget_frame)
month_entry.insert(0, datetime.now().strftime("%Y-%m"))
month_entry.pack()

tk.Label(budget_frame, text="Budget Amount:").pack()
budget_amount = tk.Entry(budget_frame)
budget_amount.pack()

def save_budget():
    try:
        category = budget_category.get()
        month = month_entry.get()
        amount = float(budget_amount.get())

        if not category or not month:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        set_budget(category, month, amount)
        messagebox.showinfo("Saved", "Budget set successfully!")

        # Reset form
        budget_category.set("")
        month_entry.delete(0, tk.END)
        month_entry.insert(0, datetime.now().strftime("%Y-%m"))
        budget_amount.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid amount.")

tk.Button(budget_frame, text="Set Budget", command=save_budget).pack(pady=10)

# ---------------- Reports Tab ----------------
tk.Label(report_frame, text="Enter Month (YYYY-MM):").pack()
report_month_entry = tk.Entry(report_frame)
report_month_entry.insert(0, datetime.now().strftime("%Y-%m"))
report_month_entry.pack()

output_text = tk.Text(report_frame, height=20, width=70)
output_text.pack()

def show_reports():
    month = report_month_entry.get()
    total = get_total_spent(month)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, f"Total Spent in {month}: ₹{total}\n\n")
    output_text.insert(tk.END, "Category-wise Spending vs Budget:\n")
    output_text.insert(tk.END, "-"*50 + "\n")
    report = get_budget_report(month)
    for cat, budget, spent in report:
        output_text.insert(tk.END, f"{cat:15} - Budget: ₹{budget:<8} | Spent: ₹{spent}\n")

tk.Button(report_frame, text="Generate Report", command=show_reports).pack(pady=10)

root.mainloop()
