def add_expense(expenses, expense_id, category, amount, note = ""):
    expense = {
        "id": expense_id,
        "category": category,
        "amount": amount,
        "note": note, 
    }
    expenses.append(expense)
    return expense

def total_expense(expenses):
    total = 0.0
    for expense in expenses:
        total += expense["amount"]
    return total

def delete_expense(expenses, expense_id):
    for expense in expenses:
        if expense["id"] == expense_id:
            expenses.remove(expense)
            return True
    return False

def next_expense_id(expenses):
    max_id = 0
    for expense in expenses:
        expense_id = expense.get("id", 0)
        if isinstance(expense_id, int) and expense_id > max_id:
            max_id = expense_id
    return max_id + 1

def list_expenses(expenses):
    if not expenses:
        print("还没有账目")
        return

    print("\nID | 分类 | 金额 | 备注")
    print("-" * 40)
    for expense in expenses:
        print(
            f"{expense["id"]} | {expense["category"]} | "
            f"{expense["amount"]} | {expense["note"]}"
        )

def input_amount():
    while True:
        text = input("金额:").strip()
        try:
            amount = float(text)
        except ValueError:
            print("请输入数字, 例如 25.5")
            continue

        if amount <= 0:
            print("金额必须大于0")
            continue

        return amount

def input_expense_id():
    while True:
        text = input("要删除的ID:").strip()
        try:
            return int(text)
        except ValueError:
            print("请输入整数ID")