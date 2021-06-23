import hashlib


def verify_password(plain_password, correct_pass_hash):

    user_in_converted = bytes(plain_password, 'utf-8')
    user_in_hash = hashlib.sha256(user_in_converted).hexdigest()

    if user_in_hash == correct_pass_hash:
        return True
    return False


def create_new_password(plain_password):

    converted_password = bytes(plain_password, 'utf-8')
    password_hash = hashlib.sha256(converted_password).hexdigest()

    return password_hash
