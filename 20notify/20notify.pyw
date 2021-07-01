# notification thing for the 20 minute rule
# version just runs in the background without command prompt

from plyer import notification
# import time module so we could use the sleep function
import time

t = 20 * 60

def countdown(currenttime):
    # while there is still time left, update the countdown timer every second
    while currenttime > 0: 
        time.sleep(1)
        currenttime -= 1
        
    # send the notification
    notification.notify(
        title = "Look away from the screen >:(",
        message = "Stare at something 20 feet away for 20 seconds",
        app_name = "20Notify",
        app_icon = "Custom-Icon-Design-Pretty-Office-8-Eye.ico",
        timeout = 20,
    )

while True:
    countdown(t)
    time.sleep(20)