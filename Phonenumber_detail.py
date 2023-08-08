import  phonenumbers
from phonenumbers import timezone,geocoder,carrier                  #timezone =time,geocoder=sim ,carrier=sim related work

number=input("Enter your No with +__:")                              #to input number
phone=phonenumbers.parse(number)                                     #parase give  phonenumber detail
time=timezone.time_zones_for_number(phone)                       
car=carrier.name_for_number(phone,"en")                               #en give english name
reg=geocoder.description_for_number(phone,"en")                       #phone number deatail
print(phone)
print(time)
print(car)
print(reg)