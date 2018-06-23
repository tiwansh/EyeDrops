import time
import notify2

ICON_PATH = "/home/anshuman/PycharmProjects/desktop_notifier/icon.png"
notify2.init("Pomodoro Notifier")

n = notify2.Notification(None, "Message", icon=ICON_PATH)
n.set_urgency(notify2.URGENCY_NORMAL)
n.set_timeout(10000)


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
    # sleep for the break time
    time.sleep(600)
    # display the message after break
    n.update("Enjoyed the break ?", "Let's get back on!")
    n.show()
    # again sleep for another hour
    time.sleep(3600)

initial_mesage_displayer()
for i in range(1, 100000):
    generic_message_displayer()