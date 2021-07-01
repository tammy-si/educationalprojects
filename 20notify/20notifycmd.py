# notification thing for the 20 minute rule
# but this one is the one that opens the command prompt and shows the time
# other one (20notify.pyw) just runs in the background and doesn't print out time


from plyer import notification
# import time module so we could use the sleep function
import time

t = 20 * 60

def countdown(currenttime):
    # while there is still time left, update the countdown timer every second
    while currenttime > 0: 
        # use divmod to help format the timer; take the current time divide it by sixty
        mins, secs =  divmod(currenttime, 60)
        timer = "{:02d}:{:02d}".format(mins,secs)
        print(timer, end="\r")
        time.sleep(1)
        currenttime -= 1
    mins, secs =  divmod(currenttime, 60)
    print("{:02d}:{:02d}".format(mins,secs), end="\r")

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