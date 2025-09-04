'''
#5 შექმენი ყველა 3-ელემენტიანი კომბინაცია სიიდან [1,2,3,4,5] (itertools-ის გამოყენებით)
'''

from itertools import combinations

nums = [1, 2, 3, 4, 5]

combos = list(combinations(nums, 3))
# list-ის ვარიანტი
print("ლისტის ვარინატი:\n", combos)
print("სულ რაოდენობა:", len(combos), "\n" * 2, "სხვა ვარიანტი")

# სხვა ვარიანტი
for p in combos:
    result = ""
    for x in p:
        result += str(x)
    print(result, end=' ')

print("\nსულ რაოდენობა:", len(combos))
