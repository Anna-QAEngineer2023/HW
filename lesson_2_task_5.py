def month_to_season(n):
    for i in range(1, 13):
        if i == 1 or i == 12 or i == 2:
            print("Зима")
        elif i == 3 or i == 4 or i == 5:
            print("Весна")
        elif i == 6 or i == 7 or i == 8:
            print("Лето")
        elif i == 9 or i == 10 or i == 11:
            print("Осень")
           
i = int(input(("Введите число = ")))
month_to_season(i)   
