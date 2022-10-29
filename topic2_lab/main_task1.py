list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]
# TODO найти сумму, количество и среднее арифметическое уникальных чисел

set_ = set(list_)
# print(set_)
sum_ = sum(set_)
print(sum_)
count = len(set_)
print(count)
average = sum_ / count
print(round(average, 5))
