def get_all_sub_str(string, length):
    return [string[i:i+length] for i in range(len(string) - length + 1)]


def get_all_indexes(string, char):
    return set([i for i in range(len(string)) if string[i] == char])


def get_palindrom_dict(string):
    final_dict = {}
    for i in range(1, len(string) + 1):
        palindroms = [sub_str for sub_str in get_all_sub_str(string, i) if sub_str == sub_str[::-1]]
        if palindroms:
            final_dict[i] = palindroms
    return final_dict


def check_match(string):
    first_str = string[::2]
    second_str = string[1::2]
    if len(first_str) != len(second_str):
        return False

    for i in range(len(first_str)):
        if not get_all_indexes(first_str, first_str[i]).issubset(get_all_indexes(second_str, second_str[i])):
            return False

    return True
