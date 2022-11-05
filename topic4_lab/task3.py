def delete(list_, index=-1):
    list_copy = list_.copy()
    list_copy.pop(index)
    return list_copy


def delete2(list_, index=-1):
    list_copy = list_.copy()
    if index == -1:
        return list_copy[:index]
    else:
       return list_copy[:index] + list_copy[index + 1:]


# TODO реализовать функцию удаления элемента из списка по индексу


# print(delete([0, 0, 1, 2], index=0))  # [0, 1]
# print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
# print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]

print(delete2([0, 0, 1, 2], index=0))  # [0, 1]
print(delete2([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete2([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
