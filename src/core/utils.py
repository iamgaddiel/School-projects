from random import choice

def generate_license_number(no_of_char: str) -> str:
    char = '1234567890QWERTYUIOPASDFGHJKLZXCVBNM'
    license, counter = '', 0
    while counter < no_of_char:
        license += choice(char)
    return license

