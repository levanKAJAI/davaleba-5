'''
#8 ორი მოთამაშე იწყებს "გარბენს". უნდა შეამოწმო რომელი დაასრულებს ნაკლებ დროში

player1 = start + timedelta(seconds=random.randint(5,20))
player2 = start + timedelta(seconds=random.randint(5,20))
'''

from datetime import datetime, timedelta
import random

# დროის ათვლის დაწყება
start = datetime.now()

# თითო მოთამაშის დასრულების დრო (5–დან 20 წამამდე)
player1_finish = start + timedelta(seconds=random.randint(5, 20))
player2_finish = start + timedelta(seconds=random.randint(5, 20))

# დასრულების დროების დაბეჭდვა
print("Player 1 დასრულების დრო:", player1_finish.time())
print("Player 2 დასრულების დრო:", player2_finish.time())

# ვინ მოიგო
print("\n" + "*" * 42)
if player1_finish < player2_finish:
    print("Player 1 მოიგო!")
elif player2_finish < player1_finish:
    print("Player 2 მოიგო!")
else:
    print("ფრე! ორივემ ერთდროულად დაასრულა.")
