
def check_username():
    u_name = input('Enter your Username: ')
    if not u_name.isalnum():
        print('Invalid Username')
        return check_username()
    return u_name


def check_password():
    pwd = input('Enter your password: ')

    if len(pwd) < 8:
        print('Password length should be at least 8')
        return check_password()
    else:
        upper_count = 0
        lower_count = 0
        special_c = 0
        for c in pwd:
            if c.isupper():
                upper_count += 1
            if c.islower():
                lower_count += 1
            if c in ['@', '#', '$', '%', '*']:
                special_c += 1
        if not upper_count or not lower_count or not special_c:
            print('Invalid Password!')
            return check_password()
    return pwd


def check_password2(pwd):
    is_valid = True

    if len(pwd) < 8:
        print('Password length should be at least 8')
        is_valid = False

    if not any(c.islower() for c in pwd):
        print('Password should have at least one lowercase letter!')
        is_valid = False

    if not any(c.isupper() for c in pwd):
        print('Password should have at least one uppercase letter!')
        is_valid = False

    if not any(c in ['@', '#', '$', '%', '*'] for c in pwd):
        print('Password should have at least one of the symbols @#$%*')
        is_valid = False
    return is_valid


username = check_username()
while True:
    password = input('Enter your password: ')
    if check_password2(password):
        print('Welcome to Smartlarn!')
        break
    else:
        print('Invalid password! Try again ...')


