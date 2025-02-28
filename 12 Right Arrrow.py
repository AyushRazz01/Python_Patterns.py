n=3
for i in range(1, n+1):
    print('* ' * i)#top half
for i in range(n-1,0,-1):#bottom half
    print('* ' * i)    
   
print("Another answer is: ")

n = 5
for i in range(n):
    if i <=n // 2:
        print('* ' * (i + 1))
    else:
        print('* ' * (n - i))
        
    