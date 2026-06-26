import sqlite3
def connect():
    con = sqlite3.connect("expense.db")
    cursor = con.cursor()
    return con,cursor

def create_table():
    con,cursor = connect()  
    cursor.execute('''CREATE TABLE IF NOT EXISTS expense (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        amount REAL NOT NULL,
                        category TEXT,
                        date DATE NOT NULL
                    )''')
    con.commit()
    con.close()
def add_expenses(name,amount,category,date):
    con,cursor = connect()
    cursor.execute("INSERT INTO expense (name, amount, category, date) VALUES (?, ?, ?, ?)", (name, amount, category, date))
    con.commit()
    con.close()
    print(f"\nExpense {name} of {amount} added successfully\n")

def view_all_expenses():
    con,cursor = connect()
    cursor.execute("SELECT * FROM expense ORDER BY date DESC")
    rows = cursor.fetchall()
    con.close()
    if not rows:
        print("\n No expenses found\n")
        return
    print("\n"+"-"*50)
    print(f"{'Id':<5}{'Name ':<20}{'Amount':<10.2f}{'Category':<15}{'Date'}")
    print("_"*50)
    for row in rows:
        print(f"{row[0]:<5}{row[1]:<15}{row[2]:<10.2f}{row[3]:<12}{row[4]}")
    print("_"*50)
def view_by_category(category):
    con,cursor = connect()
    cursor.execute("SELECT * FROM expense WHERE category = ? ORDER BY date DESC",(category,))
    rows = cursor.fetchall()
    con.close()
    if not rows:
        print(f"\n No expenses found for category '{category}'\n")
        return
    print(f"\n Expenses in category '{category}':")
    print("_"*50)
    print(f"{'Id':<5}{'Name ':<20}{'Amount':<10.2f}{'Category':<15}{'Date'}")
    for row in rows:
        print(f"{row[0]:<5}{row[1]:<15}{row[2]:<10.2f}{row[3]:<12}{row[4]}")
    print("_"*50 +"\n")
def total_spending():
    con,cursor = connect()
    cursor.execute("SELECT SUM(Amount) FROM expense")
    Total = cursor.fetchone()[0]
    con.close()
    
    if Total is None:
        print("\n No expense Yet.\n")
    else:
        print(f"\n Total Spending : ₹{Total:.2f}\n")
def delete_expense(expense_ID):
    con,cursor = connect()
    cursor.execute("DELETE FROM expense WHERE id = ?",(expense_ID))
    if cursor.rowcount==0:
        print(f"\n No expense found {expense_ID}\n")
    else:
        print(f"\n Expense with Id {expense_ID} deleted\n")
    con.commit()
    con.close()
 
def show_menu():
    print("╔══════════════════════════════╗")
    print("║         Expense Tracker      ║")
    print("╠══════════════════════════════╣")
    print("║  1. Add Expense              ║")
    print("║  2. View All Expenses        ║")
    print("║  3. View by Category         ║")
    print("║  4. Total Spending           ║")
    print("║  5. Delete Expense           ║")
    print("║  6. Exit                     ║")
    print("╚══════════════════════════════╝")
def main():
    create_table()
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()
        print(f"Your choice is: {choice}")
        if choice =="1":
            name = input("Enter your name: ").strip()
            amount = float(input("Amount : "))
            category =input("Category : ").strip()
            date = input("Date(YYYY-MM-DD) : ").strip()
            add_expenses(name,amount,category,date)
        elif choice =="2":
            view_all_expenses()
        elif choice =="3":
            category = input("Enter category to filter: ").strip()
            view_by_category(category)
        elif choice =="4":
            total_spending()
        elif choice =="5":
            view_all_expenses()
            expense_ID= int(input("Enter ID to delete: "))
            delete_expense(expense_ID)
        elif choice =="6":
            print("\nGoodBuy! keep tracking your expenses.\n")
            break
        else:
            print("\nInvalid choice!\n")
if __name__ =="__main__":
    main()
