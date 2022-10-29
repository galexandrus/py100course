money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

# month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение


def month_for_live(money_capital, salary, spend, increase, month=0):
    start_sum = money_capital
    while money_capital + salary - spend >= 0:
        if money_capital > start_sum * 20: # условие, чтобы избежать бесконечного цикла в случае ошибки
            break
        else:
            money_capital = money_capital + salary - spend
            spend = spend * (1 + increase)
            month += 1
    return month


month = month_for_live(money_capital, salary, spend, increase)

print(month)
