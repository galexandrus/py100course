list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
# print(list_numbers)

# TODO Оформить решение

max_num_i = 0
max_num = list_numbers[max_num_i]
last_num_i = len(list_numbers) - 1
last_num = list_numbers[last_num_i]

# print(max_num, last_num)

for i, num in enumerate(list_numbers):
    if num > max_num:
        max_num = num
        max_num_i = i

list_numbers[max_num_i] = last_num
list_numbers[last_num_i] = max_num

print(list_numbers)
