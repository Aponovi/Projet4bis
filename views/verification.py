from datetime import datetime


def field_string(wording_input, max_len=100, isalpha=False, isalnum=False):
    value = input(wording_input)
    while not check_string(value, max_len=max_len, isalpha=isalpha, isalnum=isalnum):
        print("Saisie incorrecte.")
        value = input(wording_input)
    return value


def check_string(value_input, max_len=100, isalpha=False, isalnum=False):
    if value_input.strip() == '':
        return False
    if len(value_input) > max_len:
        return False
    if isalpha:
        if not value_input.replace('-', '').replace(' ', '').isalpha():
            return False
    if isalnum:
        if not value_input.replace('-', '').replace(' ', '').replace('.', '').isalnum():
            return False

    return True


def field_date(date_input):
    value = input(date_input)
    date_formatter = "%d/%m/%Y"
    while not check_date(value, date_formatter):
        print("Saisie incorrecte.")
        value = input(date_input)
    return datetime.strptime(value, date_formatter)


def check_date(date_input, date_formatter):
    try:
        datetime.strptime(date_input, date_formatter)
    except ValueError:
        return False
    return True


def check_gender(wording_input):
    value = input(wording_input)
    while value.lower() not in ('f', 'm'):
        print("Saisie incorrecte.")
        value = input(wording_input)
    return value


def field_int(number_input, max_len=9999):
    value = input(number_input)
    while not check_int(value, max_len=max_len):
        print("Saisie incorrecte.")
        value = input(number_input)
    return int(value)


def check_int(value_input, max_len=9999):
    if value_input.strip() == '':
        return False
    if value_input.isdigit():
        if int(value_input) > max_len:
            return False
        else:
            return True
    else:
        return False
