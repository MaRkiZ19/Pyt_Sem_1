year=int(input('введите год: '))
if year%4==0 and year%100>0:
    print('Yes')
# elif year%100>0:
#     print('Yes')
elif year%400==0:
    print('Yes')
else:
    print('No')
