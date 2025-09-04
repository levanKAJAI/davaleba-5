'''
#3 დაადგინე, არის თუ არა შეყვანილი წელი ნაკიანი, მომხმარებელს შემოჰყავს მხოლოდ წელი და ვეუბნებით არის თუ არა ნაკიანი

import calendar
myinput = ...
'''

import calendar

print("წელი არის თუა არა ნაკიანი ")

while True:
    year = input("შეიყვანე წელი: ")

    # რიცხვია თუ არა
    if year.isdigit():
        year = int(year)
        if calendar.isleap(year):
            print(f"{year} ნაკიანი წელია")
            break
        else:
            print(f"{year} ნაკიანი არ არის")
            break
    else:
        print("შეიყვანე მხოლოდ რიცხვი (წელი)!")
