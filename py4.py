'''
#4 დაითვალე რამდენი კვირაა დარჩენილი ახალ წლამდე, საწყისი თარიღი არის დღევანდელი დღე (ხელით არ გაწეროთ თარიღი)
'''

from datetime import datetime

today = datetime.today()
new_year = datetime(today.year + 1, 1, 1)

weeks = (new_year - today).days // 7
print(f"ახალ წლამდე დარჩენილია {weeks} კვირა")
