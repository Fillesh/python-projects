import random,string,os

nums = []
letters = []
twodigit = []
threedigit = []
fourdigit = []

os.system("cls")
print("Preparing The Script...")
for lel in range(0,(len(string.digits))):
    nums.append(string.digits[lel])

for lel in range(0,(len(string.ascii_letters))):
    letters.append(string.ascii_letters[lel])

for ph1 in range(0, (len(nums))):
    for ph2 in range(0, (len(letters))):
        twodigit.append((nums[ph1] + letters[ph2]))

for ph1 in range(0, (len(letters))):
    for ph2 in range(0, (len(nums))):
        twodigit.append((letters[ph1] + nums[ph2]))

for ph1 in range(0, (len(letters))):
    for ph2 in range(0, len(letters)):
        twodigit.append((letters[ph1] + letters[ph2]))

for ph1 in range(0, (len(nums))):
    for ph2 in range(0, len(nums)):
        twodigit.append((nums[ph1] + nums[ph2]))

for ph1 in range(0, (len(twodigit))):
    for ph2 in range(0, (len(nums))):
        threedigit.append((twodigit[ph1] + nums[ph2]))
    for ph3 in range(0, (len(letters))):
        threedigit.append((twodigit[ph1] + letters[ph3]))

for ph1 in range(0, (len(twodigit))):
    for ph2 in range(0, (len(nums))):
        threedigit.append((nums[ph2] + twodigit[ph1]))
    for ph3 in range(0, (len(letters))):
        threedigit.append((twodigit[ph1] + letters[ph3]))

for ph1 in range(0, (len(twodigit))):
    for ph2 in range(0, (len(nums))):
        threedigit.append((nums[ph2] + twodigit[ph1]))
    for ph3 in range(0, (len(letters))):
        threedigit.append((letters[ph3] + twodigit[ph1]))

for ph1 in range(0, (len(twodigit))):
    for ph2 in range(0, (len(nums))):
        threedigit.append((twodigit[ph1] + nums[ph2]))
    for ph3 in range(0, (len(letters))):
        threedigit.append((letters[ph3] + twodigit[ph1]))

for ph1 in range(0, (len(threedigit))):
    for ph2 in range(0, (len(nums))):
        fourdigit.append((threedigit[ph1] + nums[ph2]))
    for ph3 in range(0, (len(letters))):
        fourdigit.append((threedigit[ph1] + letters[ph3]))

for ph1 in range(0, (len(threedigit))):
    for ph2 in range(0, (len(nums))):
        fourdigit.append((nums[ph2] + threedigit[ph1]))
    for ph3 in range(0, (len(letters))):
        fourdigit.append((threedigit[ph1] + letters[ph3]))

for ph1 in range(0, (len(threedigit))):
    for ph2 in range(0, (len(nums))):
        fourdigit.append((nums[ph2] + threedigit[ph1]))
    for ph3 in range(0, (len(letters))):
        fourdigit.append((letters[ph3] + threedigit[ph1]))

for ph1 in range(0, (len(threedigit))):
    for ph2 in range(0, (len(nums))):
        fourdigit.append((threedigit[ph1] + nums[ph2]))
    for ph3 in range(0, (len(letters))):
        fourdigit.append((letters[ph3] + threedigit[ph1]))

set(twodigit)
set(threedigit)
set(fourdigit)
print(f"\nLenght of the two digits : {len(twodigit)}")
print(f"Lenght of the three digits : {len(threedigit)}")
print(f"Lenght of the four digits : {len(fourdigit)}")
sifre = input("\nPass? : ")
countd = 1
if len(sifre) == 4:
    for check in range(0, (len(fourdigit))):
        if sifre == fourdigit[check]:
            print(f"Found your password in {countd} attempts.\n")
            break
        else:
            countd = countd+1
elif len(sifre) == 3:
    for check in range(0, (len(threedigit))):
        if sifre == threedigit[check]:
            print(f"Found your password in {countd} attempts.\n")
            break
        else:
            countd = countd+1
elif len(sifre) == 2:
    for check in range(0, (len(twodigit))):
        if sifre == twodigit[check]:
            print(f"Found your password in {countd} attempts.\n")
            break
        else:
            countd = countd+1