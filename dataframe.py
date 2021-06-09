from datetime import datetime


# This is the framework for the .json file
framework = {
    'assets': float(),
    'bills': [{'bill name': [int(), float()]}],         # int = days between bills
    'income': [{'source': [int(), float()]}],           # float = bill amount
    'adjustments': [{float(): [datetime(), str()]}],    # str = note
                                                        # datetime = timestamp
    # 'daily shift' is the sum of all bills/income divided by 30.4
    'daily_shift': float(),
    'savings': float(),

    # The budget of the current day
    'day_budget': float()
}


if __name__ == '__main__':
    pass
