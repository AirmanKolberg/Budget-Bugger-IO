from user_inputs import verify_yes_or_no


def setup_assets():

    adding_assets = True
    assets = list()

    while adding_assets:
        name = input('Account name: ')
        balance = input(f'{name} balance: ')

        # Create the dictionary and add it to the list to be returned
        new_asset = {name: balance}
        assets.append(new_asset)

        # Verify if user wishes to add another
        adding_assets = verify_yes_or_no(input('Add another?\n'))

    return assets


if __name__ == '__main__':
    pass
