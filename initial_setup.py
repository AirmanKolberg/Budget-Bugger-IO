from user_inputs import *
from system_commands import get_current_time_and_date


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
        add_another = input('Add another?\n').lower()
        adding_assets = verify_yes_or_no(add_another)

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

        add_another = input('Add another?\n').lower()
        adding_bills = verify_yes_or_no(add_another)

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

        add_another = input('Add another?\n').lower()
        adding_income = verify_yes_or_no(add_another)

    return incomes


def setup_savings_and_dailies(bills, incomes, assets):

    def get_sum_of_all_values(list_of_dicts):

        # The effect of everything combined, beginning of course at 0
        total_daily_effect = 0

        # Separate the list into single dicts
        for each_dict in list_of_dicts:

            # Get the key to access the value pairs
            for the_key in each_dict:

                # Returns the amount
                amount = each_dict[the_key][1]

                # Number of days between payments
                frequency = each_dict[the_key][0]

                # Add overall effect to running total
                daily_effect = (amount / frequency).__round__(2)
                total_daily_effect += daily_effect

        return total_daily_effect

    # Calculate daily budget
    daily_loss = get_sum_of_all_values(bills)
    daily_gain = get_sum_of_all_values(incomes)
    daily_budget = daily_gain - daily_loss

    savings_options = """Would you like savings based on a:
set         -    set rate, or manually choose the daily savings
percent     -    have it based on a percentage of your daily
"""

    option_set = False
    while not option_set:

        # Get the savings method from the user
        option_selected = input(savings_options).lower()

        if option_selected == 'set':

            daily_savings = (get_float_value_from_user('Enter daily savings: ')).__round__(2)
            true_daily = daily_budget - daily_savings
            option_set = True

        elif option_selected == 'percent':

            percentage = get_float_value_from_user('Enter percentage to save (ie 13.2 for 13.2%): ')

            # Convert to percentage
            percentage *= .01

            daily_savings = (daily_budget * percentage).__round__(2)
            true_daily = daily_budget - daily_savings
            option_set = True

        else:

            print(f"{option_selected} is neither 'set' nor 'percent', please try again.")

    date_now = get_current_time_and_date()
    current_savings_amount = 0

    # Calculate the total asset amount
    total_assets = 0
    for each_dict in assets:
        for each_key in each_dict:
            total_assets += each_dict[each_key]

    # Subtract one month of bills from current assets for starting budget
    current_budget_amount = (total_assets - (daily_loss * 30)).__round__(2)

    # {'Day Zero': [daily_addition_since_day_zero, current_savings_balance]}
    daily_framework = {
        'date': date_now,
        'daily_savings': daily_savings,
        'current_savings': current_savings_amount,
        'daily_budget': true_daily,
        'current_budget': current_budget_amount
    }

    return daily_framework


# This will be for testing/debugging purposes
def setup_all():

    assets = setup_assets()
    bills = setup_bills()
    incomes = setup_incomes()

    """
    ----------This returns the following dictionary:----------
    daily_framework = {
        'date': date_now,
        'daily_savings': daily_savings,
        'current_savings': current_savings_amount,
        'daily_budget': daily_non_savings,
        'current_budget': current_budget_amount
    }
    """
    daily_framework = setup_savings_and_dailies(bills, incomes, assets)

    budget_bugger_framework = {
        'assets': assets,
        'bills': bills,
        'incomes': incomes,
        'daily': daily_framework,
        'transactions': list(),
        'adjustments': list()
    }

    return budget_bugger_framework


if __name__ == '__main__':
    pass
