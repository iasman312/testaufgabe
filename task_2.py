def calculate_char_of_name(string):
    char_list = string.lower()
    number_list = []
    for character in char_list:
        number = ord(character) - 96
        number_list.append(number)
    return sum(number_list)


print(calculate_char_of_name("Asman"))


