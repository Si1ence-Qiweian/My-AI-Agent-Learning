numbers = [12, 5, 89, 3, 45, 7]
result = sorted(
    numbers,
    key= lambda e: e,
    reverse= False
)
print(result)

words = ["python", "AI", "programming", "code", "agent"]
sort = sorted(
    words,
    key= len,
    reverse= False
)
print(sort)

expenses = [
    {"name": "早餐", "amount": 15},
    {"name": "午餐", "amount": 30},
    {"name": "晚餐", "amount": 25},
    {"name": "咖啡", "amount": 12}
]

result = sorted(
    expenses,
    key=lambda e: e["amount"],
    reverse=True
)

print(result)