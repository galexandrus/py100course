import random

def get_unique_list_numbers() -> list[int]:
    min_val = -10
    max_val = 10
    amount = 15
    nums = []
    for i in range(amount):
        num = random.randint(min_val, max_val)
        if num not in nums:
            nums.append(num)
        else:
            i -= 1
    return nums


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
