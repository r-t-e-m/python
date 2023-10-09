a = 1
b = 1000
c = 10
f = 0

while f < a or f > b:
    print('Загадай число от', a, 'до', b)
    f = int(input())    

l = a
r = b

while c > 0:
    g = round((l + r) / 2)
    print('Я думаю, это число', g)
    
    if g == f:
        print('УРА! Я угадал. Это число', g)
        break
    elif g > f:
        print('ЧИСЛО МЕНЬШЕ')
        r = g
    else:
        print('ЧИСЛО БОЛЬШЕ')
        l = g
    
    c = c - 1
    print('Осталось попыток:', c)
    
    if c == 0:
        print('Я не смог угадать число :(')