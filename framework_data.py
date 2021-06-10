"""
# This is the framework for the .json file
framework = {
    'assets': float(),
    'bills': [{'bill name': [int(), float()]}],         # int = days between bills
    'income': [{'source': [int(), float()]}],           # float = bill amount
    'adjustments': [{float(): [datetime, str()]}],      # str = note
                                                        # datetime = timestamp
    'transactions': [{float(): [datetime, str()]}]
    # 'daily shift' is the sum of all bills/income divided by 30.4
    'daily_shift': float(),
    'savings': float(),

    # The budget of the current day
    'day_budget': float()
}
"""


def create_new_framework(assets, bills, incomes, adjustments,
                         transactions, daily_shift, savings,
                         day_budget):

    framework = {
        'assets': assets,
        'bills': bills,
        'income': incomes,
        'adjustments': adjustments,
        'transactions': transactions,
        'daily_shift': daily_shift,
        'savings': savings,
        'day_budget': day_budget
    }
    return framework


# The data_point should either be 'bills' or 'income'
def get_total_bills_or_income(dictionary, data_point):
    total_bills = 0

    for sections in dictionary[data_point]:
        for section_name in sections:
            total_bills += sections[section_name][1]

    return total_bills


def get_total_adjustments(dictionary):

    total_adjustments = 0
    for adjustments in dictionary['adjustments']:
        for adjustment in adjustments:
            total_adjustments += adjustment

    return total_adjustments


if __name__ == '__main__':
    pass
