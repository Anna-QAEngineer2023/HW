def bank(x, y):
    money = x
    for i in range(y):
        money = money * 1.1
    print(money)
bank(1000, 5)

