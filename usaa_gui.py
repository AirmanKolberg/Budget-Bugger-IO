import pyautogui as pag
from selenium import webdriver
from time import sleep
from system_commands import bash_command


def usaa_gui_login(username, password):

    login_data = [username, password]

    # Open the webdriver
    firefox = webdriver.Firefox()

    # Open USAA's website
    firefox.get('https://www.usaa.com/')
    input('testing...')

    # SETUP THE DOWNLOADS FOLDER FIRST TO AVOID HAVING TO MOVE

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

    # Relocate the downloaded file

    # FOR TESTING...
    input()

    # Close the webdriver
    firefox.close()


# TESTING...
from secrets import usaa_user, usaa_pass
usaa_gui_login(usaa_user, usaa_pass)
