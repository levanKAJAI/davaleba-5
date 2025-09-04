'''
#6 მიიღე ყველა კომბინაცია "XYZ"-ის სიმბოლოებით სიგრძე 1-დან 3-მდე
მაგალითი: X, Y, Z, XY, XZ, YZ, XYZ უნდა მივიღოთ მსგავსი შედეგი.
'''

from itertools import combinations

sia = "XYZ"

# ლისტის შემოტანა
bolo_sia = []

for x in range(1, len(sia) + 1):
    for comb in combinations(sia, x):
        bolo_sia.append("".join(comb))

# შედეგის გამოტანა
print(", ".join(bolo_sia))
