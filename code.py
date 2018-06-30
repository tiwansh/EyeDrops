import os
import time
import notify2
import requests
import json
import setup
from typing import List

# from setup import personal_list_map, access_token, client_id

# Creating the path for the icon
ICON_PATH = "{}/static/images/icon.png".format(os.getcwd())
print(ICON_PATH)

# Initializing the notification
notify2.init("Pomodoro Notifier")
n = notify2.Notification(None, "Message", icon=ICON_PATH)
n.set_urgency(notify2.URGENCY_CRITICAL)
# Time for which the notif will be displayed in milliseconds
n.set_timeout(10000)


def get_all_tasks_of_specific_list(id: int) -> List:
    """
    Gets the list of tasks from WUNDERLIST according to input param

    Args:
        id: The id of the list that we want to extract tasks from

    Returns:
        List of tasks in the specified list(using id)
    """
    headers = {'X-Access-Token': setup.access_token, 'X-Client-ID': setup.client_id, 'Content-Type': 'application/json'}
    response = requests.get('https://a.wunderlist.com/api/v1/tasks', headers=headers, params={'list_id': id})
    data = json.loads(response.content)

    list_of_tasks = []
    for i in range(len(data)):
        list_of_tasks.append(data[i]['title'])

    return list_of_tasks


def play_worksound() -> None:
    """
    Plays the sound alert for notifying begining of work time.

    Returns:
        None
    """
    directory_path_work = "static/audio/take_break.wav"
    os.system("aplay {}/{}".format(os.getcwd(), directory_path_work))


def play_breaksound() -> None:
    """
    Plays the sound alert for notifying begining of break time.
    Returns:

    """

    directory_path_break = "static/audio/bring_back.wav"
    os.system("aplay {}/{}".format(os.getcwd(), directory_path_break))


def initial_mesage_displayer() -> None:
    """
    Function to show initial message.
    Separating this as this needs to be shown only once.

    Returns:
        Now
    """
    # wait for 20 seconds after bootup and then display notif
    time.sleep(20)
    # display the message
    summary = "Welcome to the notifier application!"
    message = "I will notify you to take a 10 minutes breaks after every hour. Ciao!"
    display_list = get_all_tasks_of_specific_list(setup.personal_list_map.groceries)
    for task in display_list:
        message += '\n' + task
    n.update(summary, message)
    n.show()
    play_worksound()
    # sleep for an hour
    time.sleep(3600)


def generic_message_displayer() -> None:
    """
    Function to give a generic message. This is different since it also adds 10 minutes of break
    to the sleep time

    Returns:
        None
    """
    # display the message
    summary = "You have been working for the past hour."
    message = "Please consider taking a break!"
    n.update(summary, message)
    n.show()
    play_breaksound()
    # sleep for the break time
    time.sleep(600)
    # display the message after break
    n.update("Enjoyed the break ?", "Let's get back on!")
    n.show()
    play_worksound()
    # again sleep for another hour
    time.sleep(3600)


initial_mesage_displayer()
for i in range(1, 100000):
    generic_message_displayer()
