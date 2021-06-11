# Use this to verify yes or no questions
def verify_yes_or_no(response):
    if response == 'yes' or response == 'y':
        return True
    elif response == 'no' or response == 'n':
        return False
    else:
        response = input("Try again, simple 'yes', 'y', 'no', or 'n': ")
        verify_yes_or_no(response)


if __name__ == '__main__':
    pass
