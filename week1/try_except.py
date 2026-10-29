def input_int():
    while True:
        value = input("请输入人数:").strip()
        try:
            num = int(value)
        except:
            print("请输入整数, 如1, 4等")
            continue

        if num < 0:
            print("人数至少大于0")
            continue

        return num

input_int()