from os import system
from datetime import datetime


# Runs any given shell command
def bash_command(user_in):

    _ = system(user_in)


def clear_screen():

    bash_command('clear')


def get_current_time_and_date():
    
    moment_in_time = datetime.now()

    # Date Format:  MM/DD/YY
    # Time Format: HH:MM:SS
    date_today = moment_in_time.strftime('%m/%d/%Y')
    time_now = moment_in_time.strftime('%H:%M:%S')

    return f'{date_today} @ {time_now}'


if __name__ == '__main__':

    pass
