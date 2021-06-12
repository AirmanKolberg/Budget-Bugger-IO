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

        # NOTE: Add functionality for "monthly", "weekly", etc.
        frequency = get_int_value_from_user('Day between bills: ')

        amount = get_float_value_from_user(f'{name} amount: ')

        new_bill = {name: [frequency, amount]}
        bills.append(new_bill)

        adding_bills = verify_yes_or_no('Add another?\n')

    return bills


def setup_incomes():

    adding_income = True
    incomes = list()

    while adding_income:
        name = input('Income source: ')

        # NOTE: Add functionality for "monthly", "weekly", etc.
        frequency = get_int_value_from_user('Day between pay: ')

        amount = get_float_value_from_user(f'{name} amount: ')

        new_income = {name: [frequency, amount]}
        incomes.append(new_income)

        adding_income = verify_yes_or_no('Add another?\n')

    return incomes


# This will be for testing/debugging purposes
def setup_all():

    assets = setup_assets()
    bills = setup_bills()
    incomes = setup_incomes()

    """
    Theoretically, at startup, there should be no
    need to make adjustments or transactions, so
    these can be skipped, or just created as an
    empty list just waiting to be appended.  :)
    """

    # NOTE:  Next- determine savings


if __name__ == '__main__':
    pass
