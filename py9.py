'''
#9 იღბლიანი დაბადების დღე
მოთამაშემ უნდა შეიყვანოს დაბადების თარიღი და თამაში დაითვლის რამდენი დღეა დარჩენილი შემდეგ დაბადების დღემდე

birthday = date(2000, 12, 10)
'''


from datetime import date

# დღევანდელი თარიღის განსაზღვრა
today = date.today()

while True:
    # დაბადების თარიღის განსაზღვრა
    bday_input = input("შეიყვანეთ თქვენი დაბადების დღე და თვე ფორმატით DD-MM (მაგ: 25-10): ")

    parts = bday_input.split("-")
    # ფორმატის შემოწმება
    if len(parts) != 2:
        print("არასწორი ფორმატი. სცადეთ ისევ.\n")
        continue

    if not (parts[0].isdigit() and parts[1].isdigit()):
        print("უნდა მიუთითოთ მხოლოდ რიცხვები.\n")
        continue
    if int(parts[0])> 31 or int(parts[1])>12:
        print("არასწორი თარიღის ფორმატი, მოცემული არ შეიძლება თარიღი იყოს")
        continue

    # თვის და დღის განსაზღვრა
    month = int(parts[1])
    day = int(parts[0])

    # შემოწმება
    next_birthday = date(today.year, month, day)
    if next_birthday < today:
        next_birthday = date(today.year + 1, month, day)
    break

days_left = (next_birthday - today).days

if days_left == 0:
    print("გილოცავ დაბადების დღეს!")
else:
    print("შენი შემდეგი დაბადების დღემდე დარჩენილია -", days_left, "დღე")

