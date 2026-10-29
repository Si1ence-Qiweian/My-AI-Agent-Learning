import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "ledger.json"

def add_expense(expenses, expense_id, category, amount, note = ""):
    expense = {
        "id": expense_id,
        "category": category,
        "amount": amount,
        "note": note, 
    }
    expenses.append(expense)
    return expense

def list_expenses(expenses):
    if not expenses:
        print("还没有账目")
        return

    print("\nID | 分类 | 金额 | 备注")
    print("-" * 40)
    for expense in ledger:
        print(
            f"{expense["id"]} | {expense["category"]} | "
            f"{expense["amount"]} | {expense["note"]}"
        )

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

def load_expenses(path=DATA_FILE):
    if not path.exists():
        return []

    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        print(f"警告：{path}不是合法的 JSON, 已按空账本启动。")
        return []
    except OSError as error:
        print(f"警告: 读取数据失败: {error}")
        return []

    if not isinstance(data, list):
        print(f"警告: 数据格式不是列表， 已按空账本启动。")
        return []

    return data

def save_expenses(expenses, path=DATA_FILE):
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(expenses, file, ensure_ascii=False, indent=2)

def next_expense_id(expenses):
    max_id = 0
    for expense in expenses:
        expense_id = expense.get("id", 0)
        if isinstance(expense_id, int) and expense_id > max_id:
            max_id = expense_id
    return max_id + 1

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

def main():
    expenses = load_expenses()
    next_id = next_expense_id(expenses)

    while True:
        print("\n===== 记账本 =====")
        print("1. 添加账目")
        print("2. 查看全部")
        print("3. 统计总额")
        print("4. 删除账目")
        print("5. 退出")

        choice = input("请选择 1-5: ").strip()

        if choice == "1":
            category = input("分类:").strip()
            amount = input_amount()
            note = input("备注(可为空): ").strip()

            add_expense(expenses, next_id, category, amount, note)
            save_expenses(expenses)
            print(f"已添加, ID = {next_id}")
            next_id += 1

        elif choice == "2":
            list_expenses(expenses)

        elif choice == "3":
            print(f"总支出: {total_expense(expenses): .2f} 元")

        elif choice == "4":
            expense_id = input_expense_id()
            if delete_expense(expenses, expense_id):
                save_expenses(expenses)
                print("已删除")
            else:
                print("没有找到这个ID")

        elif choice == "5":
            save_expenses(expenses)
            print("已保存,再见")
            break

        else:
            print("只能输入 1-5")

if __name__ == "__main__":
    main()

