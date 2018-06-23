import os
import time
import notify2
from playsound import playsound

ICON_PATH = "/home/anshuman/PycharmProjects/desktop_notifier/static/images/icon.png"
notify2.init("Pomodoro Notifier")

n = notify2.Notification(None, "Message", icon=ICON_PATH)
n.set_urgency(notify2.URGENCY_NORMAL)
n.set_timeout(10000)


def play_worksound() -> None:
    """
    Plays the sound alert for notifying begining of work time.

    Returns:
        None
    """
    directory_path_work = "static/audio/take_break.wav"
    playsound(os.path.join(os.getcwd(), directory_path_work))


def play_breaksound() -> None:
    """
    Plays the sound alert for notifying begining of break time.
    Returns:

    """

    directory_path_break = "static/audio/bring_back.wav"
    playsound(os.path.join(os.getcwd(), directory_path_break))


def initial_mesage_displayer() -> None:
    """
    Function to show initial message.
    Separating this as this needs to be shown only once.

    Returns:
        Now
    """
    # display the message
    summary = "Welcome to the notifier application!"
    message = "I will notify you to take a 10 minutes breaks after every hour. Ciao!"
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
