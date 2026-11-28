# conditional statements : 
"""
if else  : 

syntax :
if condition :
    print() 
else :
    print()

"""
# ex :1 check for  eligible  for  voting  or  not. 

"""age =int(input("enter your age :"))  # 3

if age >=18 :  # 3 >=18 
    print("eligible for  voting")
else :
    print("not eligible for  voting")
"""    
# ex :2 ask user to enter the two number and check which  number is  big.  

"""
a=int(input("enter the first number :"))
b=int(input("enter the second number :"))

if a>b :
    print("a is big")
else :
    print("b is big")
"""

# ex :3 ask user to enter the number and check the number is  even or odd.

"""
num =int(input("enter the number :"))

if num % 2 ==0 :  # 34 / 2 == 0 
    print("even")
else :
    print("odd")
"""

# ex :4 ask user to enter the  year and check its leap  year or not . 
"""
year =int(input("enter the year :"))

if year % 4 == 0 :  # 34 / 2 == 0 
    print("leap yr")
else :
    print("not")
"""

# ex :5 ask user to enter the  number and check its which number is big
"""
nested if  : 

if  condition  : 
    print() 

elif condition : 
    print()

else :
    print()
"""

"""
a=int(input("enter the first number :"))
b=int(input("enter the second number :"))

if a>b :
    print("a is big")
elif b>a :
    print("b is big")
else :
    print("same")
"""

# ex :6 ask user to enter the temprature  the check  hot  cold  warm  . 

"""
temprature       condition
>40                hot
30-40              medium  hot 
20-30              medium cold 
10-20              cold 
<10                snow   

"""

"""tempature =int(input("enter the temprature :"))

if tempature >40 :
    print("hot")
elif tempature >=30 and tempature <=40 :
    print("medium hot") 
elif tempature >=20 and tempature <=30 :
    print("medium cold")
elif tempature >=10 and tempature <=20 :
    print("cold")
else :
    print("snow")
"""

#task  : 
"""
ask user to enter the three sunjects marks  : phy  che  maths

1. print  : total achieve marks  out of  100 : 
2. calculate  percentage  : 
                (total /300 )* 100  ----> phy : 90  che : 89  maths : 78 
on basic of  percentage  given grade : 

    percentage       grade
    >90                A+
    80-90              A
    70-80              B+
    60-70              B
    50-60              C+ 
    40-50              C
    <40                Fail
    

"""
 
"""
name =input("enter the name  : ")
surname =input("enter the surname :")
print("full name is  : ",name+surname)
print("full name is  : ",name,surname)
"""
"""
a=int(input("enter the first number :"))
b=int(input("enter the second number :"))
print(a+b)
"""

# data type change  : 

"""a=int(input("enter the first number :"))
b=int(input("enter the second number :"))
print("addition  : ",a+b)
print("convert addition in to int  : ",float(a+b))
"""

