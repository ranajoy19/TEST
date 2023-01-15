from random import choice
from this import d
def generate_code():
    """
    Generate 6 Digit verification code Prevent cracking
    :return:
    """
    seeds = "1234567890abcdefghijklmnopqrstuvwxyz"
    random_str = []

    for i in range(6):
        random_str.append(choice(seeds))
    return "".join(random_str)


print(generate_code())        