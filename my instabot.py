from instabot import Bot                                                    #import instabot 
bot=Bot()                                                                   #bot as varible
#ID=input("enter your id")
#Password=input("Enter your password")
bot.login(username="harsh.dethe",password="")                   
#bot.follow("kapilsharma")
#bot.upload_photo("C:/Users/DELL/OneDrive/Pictures/FB_IMG_15829035157093160.jpg",caption="my Gabbar")
#bot.unfollow("kapilsharma")
bot.send_message("hii",["Yash Dethe","samantha"])
follwers=bot.get_user_followers("harsh.dethe")
