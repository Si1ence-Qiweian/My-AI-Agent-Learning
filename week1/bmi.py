def calculate_bmi(weight_kg: float, height_m: float) -> float:
    return weight_kg / (height_m ** 2)
def bmi_category(bmi: float) -> str:
    if bmi < 18.5:
        return "偏瘦"
    elif bmi < 23.9:
        return "正常"
    elif bmi < 27.9:
        return "偏胖"
    else:
        return "肥胖"
def main():
    weight = float(input("体重(kg):"))
    height = float(input("身高(m):"))
    bmi = calculate_bmi(weight, height)
    print(f"BMI: {bmi: .2f}")
    print(f"分类: {bmi_category(bmi)}")
if __name__ == "__main__":
    main()