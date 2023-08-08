from time import *                                     # '*' use this to directly acces all function of time
import random as r                                    # r as alias of random module

def mistake(partest,usertest):
    error=0                                            #define o as value 
    for i in range(len(partest)):
        try:                                            #it check the  counting of word
            if partest[i] != usertest[i]:
                error = error + 1
        except:
            error = error + 1
    return error       
    
def speed_time(time_s,time_e,userinput):
    time_delay=time_e - time_s
    time_R=round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)

while True:
    ck=input(" ready to test :yes / no  ")
    if ck== "yes":
        test=["tony i love you 3000",                          #we write string as list
            "steve we can do this all day",
            "thor God of thounder"]
        test1=r.choice(test)                                   # it take one string and store in test1
        print("********* Typing Speed **********")
        print(test1)
        print()                                                # to breack the line
        print()
        time_1 = time()
        testinput = input(" Enter: ")
        time_2 = time()

        print("Speed : ",speed_time(time_1,time_2,testinput),"w/sec")
        print("Error : ",mistake(test1,testinput))
    
    elif ck== "no":
        print("thank you ")
        break
    
    else:
        print(" wrong input ")
    








