from .storage import load_expenses, save_expenses
from .core import (
next_expense_id, 
add_expense, 
delete_expense, 
total_expense,
input_amount,
input_expense_id,
list_expenses
)

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