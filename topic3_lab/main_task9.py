salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

# need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение


def money_for_10_months(salary, spend, months, increase):
    capital = 0
    for mon in range(months):
        capital = capital + salary - spend
        spend = spend * (1 + increase)
    return capital * (-1)


need_money = money_for_10_months(salary, spend, months, increase)

print(round(need_money))
