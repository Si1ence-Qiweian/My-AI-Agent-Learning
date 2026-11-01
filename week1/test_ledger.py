from core import (
    add_expense,
    total_expense,
    delete_expense,
    next_expense_id
)

expenses = []

def test_total_expense_empty():
    assert total_expense(expenses) == 0.0

def test_add_expense():
    add_expense(expenses, 1, "餐饮", 15, "")
    assert expenses[0] == {"id": 1, "category": "餐饮", "amount": 15, "note": ""}
    
def test_total_expense():
    expenses = [
        {'amount': 14},
        {'amount': 20},
        {'amount': 10}
    ]
    assert total_expense(expenses) == 44.0

def test_delete_expense():
    expenses = [
        {
            'id': 1,
            'category': "餐饮",
            'amount': 25,
            'note': ""
        },
        {
            'id': 2,
            'category': "交通",
            'amount': 15,
            'note': ""
        }
    ]
    delete_expense(expenses, 1)
    assert expenses[0]["id"] == 2

def test_delete_expense_de():
    expenses = [
        {
            'id': 1,
            'category': "餐饮",
            'amount': 25,
            'note': ""
        },
        {
            'id': 2,
            'category': "交通",
            'amount': 15,
            'note': ""
        }
    ]
    result = delete_expense(expenses, 3)
    assert result == False

def test_next_expense_id():
    expenses = [
        {"id": 1, "category": "餐饮", "amount": 10.0, "note": ""},
        {"id": 3, "category": "交通", "amount": 5.0, "note": ""},
    ]

    assert next_expense_id(expenses) == 4

def test_delete_expense_updates_total():
    expenses = [
    {"id": 1, "category": "餐饮", "amount": 25, "note": ""},
    {"id": 2, "category": "交通", "amount": 15, "note": ""}
    ]
    delete_expense(expenses, 1)
    assert len(expenses) == 1
    assert expenses[0]["id"] == 2
    assert total_expense(expenses) == 15.0