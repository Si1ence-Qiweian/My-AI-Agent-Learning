def add_expense(ledger, expense_id, category, amount, note = ""):
    expense = {
        "id": expense_id,
        "category": category,
        "amount": amount,
        "note": note, 
    }
    ledger.append(expense)
    return expense

def list_expenses(ledger):
    if not ledger:
        print("还没有账目")
        return

    print("\nID | 分类 | 金额 | 备注")
    print("-" * 40)
    for expense in ledger:
        print(
            f"{expense["id"]} | {expense["category"]} | "
            f"{expense["amount"]} | {expense["note"]}"
        )

def total_expense(ledger):
    total = 0.0
    for expense in ledger:
        total += expense["amount"]
    return total

def delete_expense(ledger, expense_id):
    for expense in ledger:
        if expense["id"] == expense_id:
            ledger.remove(expense)
            return True
    return False

def main():
    ledger = []
    next_id = 1

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
            amount = float(input("金额: "))
            note = input("备注(可为空): ").strip()

            add_expense(ledger, next_id, category, amount, note)
            print(f"已添加, ID = {next_id}")
            next_id += 1

        elif choice == "2":
            list_expenses(ledger)

        elif choice == "3":
            print(f"总支出: {total_expense(ledger): .2f} 元")

        elif choice == "4":
            expense_id = int(input("要删除的ID: "))
            if delete_expense(ledger, expense_id):
                print("已删除")
            else:
                print("没有找到这个ID")

        elif choice == "5":
            print("再见")

        else:
            print("只能输入 1-5")

if __name__ == "__main__":
    main()

