'''
#2 იპოვე მომდევნო კვირის პირველი სამშაბათი, საწყისი თარიღი არის დღევანდელი დღე (ხელით არ გაწეროთ თარიღი)
'''

from datetime import datetime, timedelta

# დღევანდელი თარიღი
today = datetime.today()

# პირობითი დღე
t_day = today
# სანამ სამშაბათი არ გახდება
while t_day.weekday() != 1:
    t_day += timedelta(days=1)

print("მომდევნო სამშაბათია:", t_day.date())
