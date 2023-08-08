from plyer import notification                                           #player module for notification
import time                                                                # time module for notification one by one



if __name__ == '__main__':                                              #for seperate the code
    while True:                                                         #while loop for multiple time notification
        notification.notify(                                             #we create desktop notificatio with the help of notify
            title="***Take rest***",
            message="we need that",
            app_icon="C:/Users/DELL/Downloads/WhatsApp Image 2023-05-24 at 3.12.35 PM",                  #give the icon
            timeout=5)                                                       #timeout to give notification for 5 second
        time.sleep(20)                                                   
    
