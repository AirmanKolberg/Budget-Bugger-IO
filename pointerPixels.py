from Backend import system_commands
import pyautogui as pag

"""
Use this script to help determine (x, y)
coordinates on your specific monitor or
display screen.
"""


def show_pointer_pixels():
    try:
        while True:
            x, y = pag.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\n')


if __name__ == '__main__':

    system_commands.clear_screen()
    print('Press Ctrl-C to quit.\n')

    show_pointer_pixels()
