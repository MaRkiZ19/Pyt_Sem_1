klass1= int(input('Введите количество учащихся 1ого мат.класса: '))
klass2= int(input('Введите количество учащихся 2ого мат.класса: '))
klass3= int(input('Введите количество учащихся 3ого мат.класса: '))
desk1=klass1//2
if klass1%2>0:
    desk1=desk1+1
desk2=klass2//2
if klass2%2>0:
    desk2=desk2+1
desk3=klass3//2
if klass3%2>0:
    desk3=desk3+1

sum_desk = desk1+desk2+desk3

print(sum_desk)