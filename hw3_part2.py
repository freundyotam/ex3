def get_all_sub_str(string, length):
    return [string[i:i+length] for i in range(len(string) - length + 1)]


def get_palindrom_dict(string):
    final_dict = {}
    for i in range(1, len(string) + 1):
        palindroms = [sub_str for sub_str in get_all_sub_str(string, i) if sub_str == sub_str[::-1]]
        if palindroms:
            final_dict[i] = palindroms
    return final_dict
