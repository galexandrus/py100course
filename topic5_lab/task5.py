import random
import string


def get_random_password(n=8) -> str:
    upper_list = [sign for sign in string.ascii_uppercase]
    lower_list = [sign for sign in string.ascii_lowercase]
    digit_list = [str(i) for i in range(10)]
    alphabet = upper_list + lower_list + digit_list
    common_list = random.sample(alphabet, n)
    password = ""
    for sign in common_list:
        password += sign
    return password


print(get_random_password())
