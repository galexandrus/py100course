def get_count_char(str_):
    str_low = str_.lower()
    sign_dict = {}
    for sign in str_low:
        if sign.isalpha():
            if sign_dict.get(sign) is None:
                sign_dict[sign] = 1
            else:
                sign_dict[sign] = sign_dict.get(sign) + 1
        else:
            continue
    return sign_dict


# TODO посчитать количество каждой буквы в строке в аргументе str_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))
