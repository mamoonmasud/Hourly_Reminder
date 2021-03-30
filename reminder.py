import time
from plyer import notification
#The following application sends a reminder every hour to take a break, and after 5 mins of that to end the break.
work_time = 55 #Enter total time you want to work before a break, in mins
break_time = 5 #Enter total time you want to take a break for, in mins

work_time = work_time*60
break_time= break_time*60

if __name__ == "__main__":
    while True:
    	time.sleep(work_time)
        
        notification.notify(
            title = "REMINDER!!!",
            message = "It has been an hour! Time for a break",
            timeout = 10,
            app_icon= 'logo_m.ico'
        )
        time.sleep(break_time)
        notification.notify(
            title = "REMINDER!!!",
            message = "Let's get back to work! Break is Over",
            timeout = 10,
            app_icon= 'logo_m.ico'
        )
        