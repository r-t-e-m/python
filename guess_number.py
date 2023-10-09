print('ЗАГАДАЙ ЧИСЛО')
f = int(input())
for el in range(1, 10):
    print()
print('УГАДАЙ ЧИСЛО')
a = 0
while 2 > 1:
    a = int(input())
    if a == f:
        print('УРА! ВЫ УГАДАЛИ. ЭТО ЧИСЛО', a)
        break
    elif a > f:
        print('ЧИСЛО МЕНЬШЕ')
    else:
        print('ЧИСЛО БОЛЬШЕ')