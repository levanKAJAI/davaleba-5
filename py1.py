'''
# 1 მოცემულია სიტყვა "ABCD".
დაბეჭდე ყველა შესაძლო ვარიანტი და **დაითვალე** რამდენია სულ რაოდენობრივად (უნდა დააბრუნო რიცხვი)

word = "ABCD"

'''

from itertools import permutations

word = "ABCD"

# ყველა ვარიანტი
perms = list(permutations(word))

# დაბეჭდვა
print("ჩამონათვალი:\n",perms, "\nუკეთესი ვერსია:")

for p in perms:
    print("".join(p), end=' ')
print("\nსულ რაოდენობა:", len(perms))
