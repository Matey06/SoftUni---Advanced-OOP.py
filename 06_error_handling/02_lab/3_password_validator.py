class PasswordTooShortError(Exception):
    pass


class PasswordTooCommonError(Exception):
    pass


class PasswordNoSpecialCharactersError(Exception):
    pass


class PasswordContainsSpacesError(Exception):
    pass


def common_password_validator(pas, sp_chars):
    digits_only = pas.isdigit()
    letters_only = pas.isalpha()
    special_characters_only = all(ch in sp_chars for ch in pas)

    return digits_only or letters_only or special_characters_only


special_characters = ("@", "*", "&", "%")

while True:
    password = input()
    if password == "Done":
        break

    if len(password) < 8:
        raise PasswordTooShortError("Password must contain at least 8 characters")

    if common_password_validator(password, special_characters):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

    if not any(char in special_characters for char in password):
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")

    if " " in password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

    print("Password is valid")
