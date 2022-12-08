def roman_to_int(roman_string):
    """Converts a roman numeral to an integer."""
    if (not isinstance(roman_string, str) or roman_string is None):
        return (0)

    num = 0
    length = len(roman_string)
    roman_dict = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }

    for i in range(length):
        if roman_dict.get(roman_string[i]) is None:
            return (0)
        if (i < length - 1 and
                roman_dict[roman_string[i]] < roman_dict[roman_string[i + 1]]):
            num -= roman_dict[roman_string[i]]
        else:
            num += roman_dict[roman_string[i]]

    return (num)
