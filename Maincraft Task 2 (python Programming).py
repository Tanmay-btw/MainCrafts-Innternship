import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"
HEADERS = ["Date", "Description", "Category", "Amount"]

# ──────────────────────────────────────────────
# File helpers
# ──────────────────────────────────────────────

def initialize_file():
    """Create the CSV file with headers if it doesn't exist."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as f:
            csv.writer(f).writerow(HEADERS)


def read_expenses():
    """Return all expense rows as a list of dicts."""
    with open(FILE_NAME, "r", newline="") as f:
        return list(csv.DictReader(f))

# ──────────────────────────────────────────────
# Core features
# ──────────────────────────────────────────────

def add_expense():
    """Prompt the user and save a new expense."""
    print("\n── Add Expense ──")
    desc = input("Description : ").strip()
    if not desc:
        print("❌ Description cannot be empty.")
        return

    category = input("Category (e.g. Food, Travel, Bills) : ").strip() or "General"

    try:
        amount = float(input("Amount (₹)  : "))
        if amount <= 0:
            raise ValueError
    except ValueError:
        print("❌ Please enter a valid positive number for amount.")
        return

    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, "a", newline="") as f:
        csv.writer(f).writerow([date, desc, category, f"{amount:.2f}"])

    print(f"✅ Expense '{desc}' of ₹{amount:.2f} added successfully!")


def view_expenses():
    """Display all saved expenses in a formatted table."""
    print("\n── All Expenses ──")
    expenses = read_expenses()

    if not expenses:
        print("No expenses recorded yet.")
        return

    # Column widths
    print(f"\n{'#':<4} {'Date':<12} {'Description':<20} {'Category':<15} {'Amount':>10}")
    print("─" * 65)

    for i, row in enumerate(expenses, 1):
        print(f"{i:<4} {row['Date']:<12} {row['Description']:<20} {row['Category']:<15} ₹{float(row['Amount']):>9.2f}")

    print("─" * 65)


def view_total():
    """Calculate and display the total amount spent."""
    expenses = read_expenses()
    if not expenses:
        print("\nNo expenses to total.")
        return

    total = sum(float(row["Amount"]) for row in expenses)
    print(f"\n💰 Total Expenses: ₹{total:.2f}  ({len(expenses)} item(s))")


def view_by_category():
    """Show spending grouped by category."""
    expenses = read_expenses()
    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    summary = {}
    for row in expenses:
        cat = row["Category"]
        summary[cat] = summary.get(cat, 0) + float(row["Amount"])

    print("\n── Spending by Category ──")
    print(f"{'Category':<20} {'Amount':>10}")
    print("─" * 32)
    for cat, total in sorted(summary.items(), key=lambda x: -x[1]):
        print(f"{cat:<20} ₹{total:>9.2f}")
    print("─" * 32)
    print(f"{'TOTAL':<20} ₹{sum(summary.values()):>9.2f}")


def delete_expense():
    """Delete a specific expense by its number."""
    view_expenses()
    expenses = read_expenses()
    if not expenses:
        return

    try:
        idx = int(input("\nEnter the # of the expense to delete (0 to cancel): "))
        if idx == 0:
            return
        if not (1 <= idx <= len(expenses)):
            raise ValueError
    except ValueError:
        print("❌ Invalid choice.")
        return

    removed = expenses.pop(idx - 1)

    # Rewrite file
    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS)
        writer.writeheader()
        writer.writerows(expenses)

    print(f"🗑️  Deleted: '{removed['Description']}' (₹{removed['Amount']})")

# ──────────────────────────────────────────────
# Menu
# ──────────────────────────────────────────────

def show_menu():
    print("\n╔══════════════════════════════╗")
    print("║      💸 EXPENSE TRACKER      ║")
    print("╠══════════════════════════════╣")
    print("║  1. Add Expense              ║")
    print("║  2. View All Expenses        ║")
    print("║  3. View Total Spent         ║")
    print("║  4. View by Category         ║")
    print("║  5. Delete an Expense        ║")
    print("║  6. Exit                     ║")
    print("╚══════════════════════════════╝")


def main():
    initialize_file()
    print("\nWelcome to your Expense Tracker!")

    actions = {
        "1": add_expense,
        "2": view_expenses,
        "3": view_total,
        "4": view_by_category,
        "5": delete_expense,
    }

    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "6":
            print("\nGoodbye! Keep tracking those expenses 👋\n")
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("❌ Invalid option. Please choose between 1 and 6.")


if __name__ == "__main__":
    main()
