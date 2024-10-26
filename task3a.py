a = int(input('give me your 6-digit number: '))
if a // 10**5 > 0 and a // 10**5 <= 9:
    sum1 = (a // 10**3 % 10) + (a // 10**3 // 10 % 10) + (a // 10**3 // 10**2)
    sum2 = (a % 10**3 % 10) + (a % 10**3 // 10 % 10) + (a % 10**3 // 10**2)
    if sum1 == sum2:
        print('yes')
    else:
        print('no')
else:
    print('your number has more or less 6 digits. please retry')