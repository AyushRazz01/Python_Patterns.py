n = 5
for i in range(n):
    for j in range(n):
        if i==j or  i + j == 4:
         print('* ', end = ' ')
        else:
            print(' ', end=' ')
    print()
    
    
n = int(input("Enter NO,: "))
for i in range(n):
    for j in range(n):
        if i==j or i+j==(n-1):
            print('* ', end=' ')
        else:
            print(' ', end=' ')
    print()