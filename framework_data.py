def create_new_framework(assets, bills, incomes, adjustments,
                         transactions, daily_shift, savings,
                         day_budget):

    framework = {
        'assets': assets,
        'bills': bills,
        'incomes': incomes,
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


# The data_point should either be 'adjustments' or 'transactions'
def get_total_adjustments_or_transactions(dictionary, data_point):

    total_amount = 0
    for adjustments in dictionary[data_point]:
        for transaction in adjustments:
            total_amount += transaction

    return total_amount


if __name__ == '__main__':
    pass
