def clean_text(text):
    text = text.replace(r'\r\n', '')
    text = text.replace('"html": "": "', '')
    text = text.replace('"}', '')
    text = text.replace('"', '')
    text = text.replace('{', '')
    text = text.replace('}', '')
    text = text.replace('html: ', '')
    return text

def check_even_number(number):
    if (number % 2 == 0):
        return 1
    else:
        return 0

def check_odd_number(number):
    if (number % 2 != 0):
        return 1
    else:
        return 0

def check_prime_number(number):
    div_count = 0
    for x in range(1, number + 1):
        if number % x == 0:
            div_count += 1
    if div_count == 2:
        return 1
    else:
        return 0

def checks(number):
    dict_response = {}

    dict_response['number'] = number
    dict_response['even_number'] = check_even_number(number)
    dict_response['odd_number'] = check_odd_number(number)
    dict_response['prime_number'] = check_prime_number(number)
    return dict_response
