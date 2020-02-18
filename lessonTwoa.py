points = float(input('enter points; '))
if points <= 50:
    print('u do not qualify')
elif 50 < points <= 500:
    print('50gb free data')
elif 500 > points <= 1000:
    print('free smart phone')
elif 1000 > points <= 2000:
    print('free macBook')
    if points < 1500:
        print('macBookPro')
    else:
        pass
else:
    print('continue playing')


