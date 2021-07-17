from initial_setup import setup_all
from json_tools import dict_to_json


if __name__ == '__main__':

    user_id = 'test123'

    # Get the backend data collected for the app
    bug_framework = setup_all()

    # Save dictionary to JSON
    dict_to_json(bug_framework, f'{user_id}BugReport.json')
