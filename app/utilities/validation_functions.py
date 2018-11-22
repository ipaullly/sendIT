import re

def check_for_space(input_data):
    output = input_data.strip(" ")
    return output

def check_email_format(input_email):
    match = re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]*\.*[com|org|edu]{3}$)", input_email)
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

def check_createparcel_keys(req_data, item, pickup, dest, pricing, user_id):
    if item == None:
        return False
    if pickup == None:
        return False
    if dest == None:
        return False
    if pricing == None:
        return False
    if user_id == None:
        return False