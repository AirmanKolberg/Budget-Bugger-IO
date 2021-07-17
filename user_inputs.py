# Use this to verify yes or no questions
def verify_yes_or_no(response):

    if response == 'yes' or response == 'y':
        
        return True

    elif response == 'no' or response == 'n':

        return False

    else:
        response = input("Try again, simple 'yes', 'y', 'no', or 'n': ")
        verify_yes_or_no(response)


# Use this for any user input that must be a number
def get_float_value_from_user(message_prompt):

    try:

        value = float(input(message_prompt))

    except ValueError:

        print('Please try again, numbers only...')
        value = get_float_value_from_user(message_prompt)

    return value


# Use this for any user input that must be an integer
def get_int_value_from_user(message_prompt):

    try:

        value = int(input(message_prompt))

    except ValueError:
        
        print('Please try again, integers only...')
        value = get_int_value_from_user(message_prompt)

    return value


if __name__ == '__main__':

    pass
