n = 3 
for i in range(1, n + 1):
    print('  ' * (n - i) + '* ' * i)

# Bottom half
for i in range(n - 1, 0, -1):
    print('  ' * (n - i) + '* ' * i)
 
 
 
print("Another answer is: ") 
 
n = 5
for i in range(n):
    if i <=n//2:
        print('  ' *(n//2 - i) + '* ' * (i+1))
    else:
        print('  ' *(i - n//2)  + '* '*(n-i))
 