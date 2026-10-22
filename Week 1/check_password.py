def check_password(pw):
    has_digit = False
    has_upper = False
    for ch in pw:
        if ch.isdigit():
            has_digit = True
        if ch.isupper():
            has_upper = True

    if len(pw) >= 12 and has_digit and has_upper:
        return "Strong"
    elif len(pw) >= 8:
        return "Medium"
    else:
        return "Weak"