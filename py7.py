'''
#7 თამაში უკუსვლაზე
კომპიუტერი ირჩევს შემთხვევითობის პრინციპით რიცხვს 1-20 მდე, მოთამაშეს აქვს მხოლოდ 5 წამი რიცხვის გამოსაცნობად,
თუ 5 წამში სწორ რიცხვს ვერ შეიყვანს, თამაში სრულდება და გამოდის ტექსტი "დრო ამოიწურა, თქვენ დამარცხდით".

from datetime import datetime, timedelta
import time, random
'''

from datetime import datetime, timedelta
import random

# რიცხვის გენერირება
secret = random.randint(1, 20)

# დაწყება
print("თამაში დაიწყო!\nშემთხვევითი რიცხვი 1–დან 20-მდე.")
print("გაქვს 5 წამი მოსაფიქრებლად და შეგიძლია რამდენჯერმე სცადო.\n")

# დროის გამოთვლა (საწყისი/ბოლო)
start = datetime.now()
end = start + timedelta(seconds=5)

# წყვეტის წერტილი
won = False

while datetime.now() < end:
    # რიცხვის შემოტანა
    guess = input("შეიყვანე შენი ვარაუდი: ").strip()

    # შემოწმება რომ რიცხვია
    if not guess.isdigit():
        print("გთხოვ დაიწერე მხოლოდ რიცხვი!")
        continue

    guess = int(guess)

    # დიაპაზონში თუ ჯდება
    if guess < 1 or guess > 20:
        print(f"{guess} რიცხვი არ ჯდება დიაპაზონში (1–დან 20-მდე)!")
        continue

    # შემოწმება
    if guess == secret:
        print("გილოცავ! სწორად გამოიცანი:", secret)
        won = True
        break
    else:
        print("არასწორია, სცადე ისევ. დარჩა დრო:", round((end - datetime.now()).total_seconds(), 1), "წმ.")

# დროის ამოწურვის დროს
if not won:
    print("\n" * 2 + "*" * 35 + "\nდრო ამოიწურა, თქვენ დამარცხდით.\nსწორი რიცხვი იყო:", secret)
