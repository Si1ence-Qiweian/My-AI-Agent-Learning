from ledger import add_expense, total_expense, delete_expense, next_expense_id


def test_empty_total():
    """空账本总额应为 0.0"""
    assert total_expense([]) == 0.0


def test_delete_missing_id():
    """删除不存在的 ID 应返回 False，且不改变原列表"""
    ledger = [
        {"id": 1, "category": "餐饮", "amount": 10.0, "note": ""}
    ]

    result = delete_expense(ledger, 999)

    assert result is False
    assert len(ledger) == 1
    assert ledger[0]["id"] == 1


def test_next_id_after_delete():
    """删除最大 ID 后，新 ID 仍应是 max + 1"""
    ledger = [
        {"id": 1, "category": "餐饮", "amount": 10.0, "note": ""},
        {"id": 3, "category": "交通", "amount": 5.0, "note": ""},
    ]

    assert next_expense_id(ledger) == 4


def test_add_expense_sanity():
    """正常添加一笔账，检查字段是否写入"""
    ledger = []

    add_expense(ledger, 1, "餐饮", 25.5, "午饭")

    assert len(ledger) == 1
    assert ledger[0]["category"] == "餐饮"
    assert ledger[0]["amount"] == 25.5


def main():
    test_empty_total()
    test_delete_missing_id()
    test_next_id_after_delete()
    test_add_expense_sanity()
    print("全部测试通过")


if __name__ == "__main__":
    main()