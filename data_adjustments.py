from Backend import system_commands
from user_inputs import get_float_value_from_user


# Add an adjustment or transaction (denoted as a string)
def add_adjustment_or_transaction(json_dict, new_data,
                                  adjustment_or_transaction):

    json_dict[adjustment_or_transaction].append(new_data)


def create_adjustment_or_transaction(adjustment_or_transaction):

    now = system_commands.get_current_time_and_date()

    # Get transaction/adjustment detail
    note = input('Note: ')

    amount = get_float_value_from_user(
        f'{adjustment_or_transaction.title()} amount: ')

    # Invert transactions, as they are to be subtracted
    if adjustment_or_transaction == 'transaction':
        amount *= -1

    # Format the new transaction/adjustment
    data = {amount: [now, note]}

    return data


if __name__ == '__main__':

    pass
