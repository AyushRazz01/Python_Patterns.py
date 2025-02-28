#Start
print("Hello world")
print("My name is Ayush Raj")
print("My name is ayush ", "Age is 20 ")
print(20)
print("35")
print(20 + 35)
print("20 + 35")

name=("ghosu")
age=(19)
price=(150)

#differnce "name" , name, type
#"2" = string    , 2 =int
print("name: ", name)
print(age) 
print(price)
print(type(name))
print(type("name"))
print(type(age))
print(type(price))

age=(15)
old=False               
hi=True
a=None
print(type(age))
print(type(old))
print(type(hi))
print(type(a))

#sum, diff
a=5
b=6
sum=a+b
diff=(a-b)
print(sum)
print(diff)


#Expression execution
          ## Sting and numeric = X times string
A,B=2,3
Txt="@"
print(2*Txt*3)


         ## String and string = add()*str
A,B="2", 3
Txt="@"
print((A+Txt)*B)


         ## Numericvalue can operatera together with all arithmatic operator = bodmas
A,B=2,3
C=4
print(A+B*C)         


         ##A rithmartic expressions with integers and float = float   (int + float = float)
A,B =10,5.0
C=A*B
print(C)


         ## Division operator with two integers = float
A,B=1,2
C=A/B
print(C)

 
        ## Integers division(floor) with float and int = float = closes value
A,B=1.5,3
C=A//B
print(C//A/B)


#input
name=input("name: ")
print(name)

age=int(input("age: "))
print(type(age))

price=float(input("price: "))
print(price)

print("My name is", name, "and I am", age, "years old" )

#Conditions (if-elif-else)
"""if(age>=18):
    print("Vote")
 elif(age<17):
    print("underage")
else:
    print("not eligible") """

#Single line Comment 
food = input("food :")
eat = "yes" if food=="cake" else "no"
print(eat)

food = input("food: ")
print("Sweet") if food=="cake" or "jalebi" else print("not sweet")

age=int(input("age: "))
vote=("yes", "No") [age>=18]
print(vote)

sal=float(input("salary: "))
tax=sal*(0.1,0.2) [sal<=50000]
print(tax)


#Traffic lights
light=input("light color: ")
if (light=="red"):
    print("stop")
elif(light=="yellow"):
    print("wait/lool")
elif(light=="green"):
    print("go")
else:
    print("light is damaged or broken")


   #Marks
marks=input("marks")
if(marks>=90):
    print("A")
elif(marks>=80 and marks<90):
    print("B")
elif(marks>=70 and marks<80):
    print("C")
else:
    print("D")


        #Practise Time 
"""A=5 , G=M
A=2, G=F

A=int(input("A :"))
G=intput("M/F: ")
if((A==1 or A== 2) and  G=="M"):
    print("fee is 100")
elif(A==3 or A==4 pr G=="F"):
    print("fee is 200")
elif(A==5 or G==M):
    print("Fee is 300")
else:
    print("no") """



#Calculate S.I.
P=float(input("p: "))
R=float(input("R: "))
T=float(input("T: "))
SI=(P*R*T)/100
print(SI)

#arithmatic operators
a=5
b=2
print(a+b) #sum
print(a-b)#diff
print(a*b)#multiply
print(a/b)#divide
print(a%b)#remainder

#relational operator
a=50
b=20
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)
print(a>b)
print(a<b)

#assignment operaator
a=10
a+=5
print("a: ", a)
a-=5
print("a: ", a)
a*=5
print("a: ", a)
a/=5
print("a: ", a)
a%=5
print("a: ", a)
a**=5
print("a: ", a)


"""#logical operator
a=10
b=5
          #_not_operator
print(not(a>b))
print(not(a<b))

#and_operator
print(a>b) and (b<a)      
print(a>b) and (b>a)
print(a<b) and (b>a)
print(a<b) and (b<a)

#or_operator
print(a>b) or (a>b)
print(a>b) or (a<b)
print(a<b) or (a<b)
print(a<b) or (a>b)"""


#type_conversion
name=input("enter name: ") #_type_conversion(automatic)
age=int(input("enter age: "))#_type_casting(manual)
marks=float(input("enter marks:"))#_type_casting(manual)

print("welcome", name)
print("age", age)
print("marks", marks)

a=int(input("first number: "))
b=int(input("second number: "))
sum=(a+b)
print(sum)

#_area_perimeter_of_square
side=int(input("side: "))
area=side*side
print("area",area)
print("perimeter:",4*side )

side=float(input("enter side: "))
print("area=",side**2)
print("perimeter:",4*side )


#_area_perimneter_of_rectangle
l=int(input("length: "))
b=int(input("bredth: "))
print("area: ", l*b)
print("perimeter: ", 2*(l+b))

#_avg_value
a=float(input("decimal no.1 "))
b=float(input("decimal no.2: "))
print("avg:" (a+b)/2)

#true_false
a=int(input("number 1: "))
b=int(input("numbers 2: "))
print("True") if a>=b else print("False")
#print(a>b)

                #_String
str1="Ayush"
str2="Raj"
final_str=str1+str2 
print(final_str)
print(len(final_str))
final_str=str1+ " "+str2
print(final_str)
print(len(final_str))

         #_Slicing
str="Apna College"  
print(str[1:4])       
print(str[5:12])
print(str[5:])
print(str[5:len(str)])

#_neative slicing
str="Ayush"
print(str[-3:-1])

          #_EVEN-ODD_number
num=int(input("enter_number: "))
if (num % 2==0):
    print("even")  

else: 
    print("odd")

    #largest-number
a=int(input("enter_number1: "))
b=int(input("enter_number:2 "))
c=int(input("enter_number:3 "))
if (a>=b) and(a>=c):
    print(a)
elif(b>=c):
    
    print(b)
else:
    print(c)   


a=int(input("enter num1: "))
b=int(input("enter num2: "))
c=int(input("enter num3: "))
d=int(input("enter num4: "))
if (a>=b)and(a>=c)and(a>=d):
    print(a)
elif(b>=c)and(b>=d):
    print(b)
elif(c>=d):
    print(c)
else:
    print(d)    
        
        #Multiple_of_7 or not
num=int(input("enter_number: "))
if (num % 7==0):
    print("yes, Multiple of 7")
else:
    print("no, not a multiple of 7")     
num=int(input("enter number: "))
if(num % 7==0):
    print("Yes baby")
else:
    print("No babes")



         #___Lists (immutable)
student=["karan", 95.4, 17, "Delhi"]
print(student)
      #_modified changable
student=["karan", 95.4, 17, "Delhi"]
student[0]="raj"
print(student)
          #slicing_in_lists
marks=[87,64,33,95,76]

print(marks[1:4])
print(marks[:4])
print(marks[1:])
print(marks[-3:-1])      


              #Tuples(immutable)
tup=(87,64,33,95,76)     #tup[0],tup[1]...
tup[0]=43                #NOT allowed in python

tup1=()
tup2=(1,)
tup3=(1,2,3)
  

          #_Practise____
movies = []
movies.append(input("Enter 1st movie:"))
movies.append(input("Enter 2nd movie:"))
movies.append(input("Enter 3rd movie:"))

print(movies)


user=("Enter nammes of 3 favourite movies: ")          
print(user)
a=input("Movie 1:")
b=input("Movie 2: ")
c=input("movie3: ")
list=[a,b,c]
print(list)


ist=["c","d","a","a","b","b","a"]
list.sort()
print(list)

#____set  (union)
set1={1,2,3,4}
set2={3,4,5,6,7}
print(set1.union(set2))
#(intersection)
set1={1,2,3,4,5,6,7,8,9}
set2={2,3,4,6,8}
print(set1(intersection(set2)))