n = 5
for i in range(n, 0, -1):
    print(' ' * (n - i) * 2, end=' ')  
    for j in range(i):
       print('x', end=' ')
    print() 
