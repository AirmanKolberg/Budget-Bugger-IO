import pyautogui as pag
from selenium import webdriver
from time import sleep
import pandas as pd
from secrets import usaa_csv_location
from system_commands import bash_command


def usaa_gui_login(username, password):

    login_data = [username, password]

    # Open the webdriver
    firefox = webdriver.Firefox()

    # Open USAA's website
    firefox.get('https://www.usaa.com/')
    sleep(5)

    # Open FireFox Preferences
    pag.hotkey('command', ',')
    sleep(2)

    # Begin writing "downloads" in the search field
    pag.write('dow', interval=0.08)
    sleep(0.3)

    # Click 'Choose' for new download location
    pag.click(x=855, y=737)
    sleep(1.5)

    # Click the search field
    pag.click(x=961, y=174)
    sleep(0.2)

    """
    The location of the downloaded .csv file will
    absolutely change before deploying the app next
    week, please take note of this...
    """

    # Go through all directories/subdirectories
    for location in usaa_csv_location:
        x = usaa_csv_location[location][0]
        y = usaa_csv_location[location][1]

        pag.write(location, interval=0.08)
        sleep(0.1)

        # Enter directory listed as first search result
        pag.doubleClick(x=x, y=y)
        sleep(0.2)

    # Click "Open" to select location
    pag.click(x=1020, y=516)
    sleep(0.2)

    # Close the Preferences tab and continue
    pag.hotkey('command', 'w')
    sleep(0.2)

    # Click the button allowing you to navigate to login site
    firefox.find_element_by_class_name('profileWidget-buttonLeft').click()
    sleep(5)

    # Input username/password and press 'Return' (Mac OS X and 11)
    for i in login_data:
        pag.write(i, interval=0.08)
        pag.press('return')
        sleep(5)

    """
    The PyAutoGUI coordinates are set for a 15" 2015 MacBook Pro
    
    coordinate = {'what it does': [x_coor, y_coor, sleep_duration]}
    """
    pag_steps = [
        {'send_verification': [925, 451, 10]},
        {'click_text_notification': [1204, 98, 5]}
    ]

    sleep(2)    # For good measure

    def go_through_pag_steps(pag_steps):

        for each_step in pag_steps:
            for key in each_step:

                # Extract steps from data
                x = each_step[key][0]
                y = each_step[key][1]
                sleep_dur = each_step[key][2]

                # Execute each step
                pag.click(x=x, y=y)
                sleep(sleep_dur)

    # Go through the first set of steps
    go_through_pag_steps(pag_steps)

    # Highlight code
    pag.doubleClick(x=321, y=527)
    sleep(1)

    # Copy code
    pag.hotkey('command', 'c')

    # Paste it in and login
    pag.click(x=890, y=526)
    sleep(0.2)
    pag.hotkey('command', 'v')
    sleep(0.1)
    pag.press('return')
    sleep(0.5)

    # Switch back to Messages
    pag.click(x=579, y=871)
    sleep(0.2)

    # Delete message
    pag.rightClick(x=48, y=610)
    sleep(0.3)
    pag.click(x=80, y=644)
    sleep(1.2)
    pag.click(x=363, y=749)
    sleep(1)

    # Quit Messages
    pag.hotkey('command', 'q')
    sleep(3)

    pag_steps = [
        {'access_account': [316, 619, 5]},
        {'select_i_want_to': [515, 631, 1]},
        {'click_export': [308, 704, 1.5]},
        {'click_export_again': [840, 619, 5]},
        {'click_save_file': [485, 485, 1]},
        {'click_okay': [770, 573, 5]}
    ]

    # Go through second set of PyAutoGUI steps
    go_through_pag_steps(pag_steps)

    # Give it some time to download
    sleep(5)

    # Close the webdriver
    firefox.close()


# Returns dict():  {float(amount): 'description'}  with last 10 values
# Standard USAA filename: bk_download.csv
def get_last_ten_transactions_usaa(csv_file):
    py_csv = pd.read_csv(csv_file)

    # Grab last 10 transactions and descriptions from .csv
    amounts = py_csv.iloc[0:10, -1]
    descriptions = py_csv.iloc[0:10, -3]

    # Setup lists for final framework
    last_ten_transactions = list()
    last_ten_descriptions = list()

    # Add all necessary data to the lists
    for charge in amounts:
        last_ten_transactions.append(charge)

    for description in descriptions:

        # Remove excess spaces, *s and ~s
        description = description.replace('  ', '')
        description = description.replace('*', '')
        description = description.replace('~', '')

        last_ten_descriptions.append(description)

    # Initialise the empty framework.  {float(amount): 'description'}
    framework = dict()

    # Add all data to the framework
    for i in range(len(last_ten_descriptions)):
        framework[last_ten_transactions[i]] = last_ten_descriptions[i]

    # Remove file to avoid future duplicates
    bash_command(f'rm {csv_file}')

    return framework


if __name__ == '__main__':
    
    pass
