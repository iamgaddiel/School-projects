from random import choice


def generate_text(string_length):
    letters = '1234567890qwertyuiopasdfghjklzxcvbnm'
    string = ''
    count = 1
    while count <= string_length:
        string += choice(letters)
        count += 1
    return string
