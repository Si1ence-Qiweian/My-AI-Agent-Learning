import json
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

def load_expenses(path=BASE_DIR/"data"/"ledger.json"):
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

def save_expenses(expenses, path=BASE_DIR/"data"/"ledger.json"):
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(expenses, file, ensure_ascii=False, indent=2)