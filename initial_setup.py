from user_inputs import *


def setup_assets():

    adding_assets = True
    assets = list()

    while adding_assets:
        name = input('Account name: ')
        balance = get_float_value_from_user(f'{name} balance: ')

        # Create the dictionary and add it to the list to be returned
        new_asset = {name: balance}
        assets.append(new_asset)

        # Verify if user wishes to add another
        adding_assets = verify_yes_or_no('Add another?\n')

    return assets


def setup_bills():

    adding_bills = True
    bills = list()

    while adding_bills:
        name = input('Bill name: ')
        frequency = get_int_value_from_user('Day between bills: ')


if __name__ == '__main__':
    pass
