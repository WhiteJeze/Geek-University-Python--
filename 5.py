revenue = float(input("Введите выручку фирмы: "))
cost = float(input("Введите издержки фирмы: "))
if revenue > cost:
    print("Фирма работает с прибылью. Рентабельность выручки составила ", revenue / cost)
    workers = int(input("Введите количество сотрудников фирмы: "))
    print("Прибыль в расчете на одного сторудника сотавила ", revenue / workers)
elif revenue == cost:
    print("Фирма работает в ноль.")
else:
    print("Фирма работает в убыток.")