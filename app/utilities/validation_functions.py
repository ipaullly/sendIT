import re

def check_for_space(varib):
    output = varib.strip(" ")
    if output:
        return True
    else:
        return False

def check_email_format(varib):
    match = re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]*\.*[com|org|edu]{3}$)",varib)
    if match:
        return True
    else:
        return False

def check_password_strength(password):
    leng_regex = re.compile(r'.{8,}')
    leng = True if leng_regex.search(password) != None else False

    capital_regex = re.compile(r'[A-Z]')
    uppercase = True if capital_regex.search(password) != None else False
    return(leng and uppercase == True)