def factorial(n):
    if n==0 or n==1 :
        return 1
    else:
        return n * factorial(n-1)
num =int(input("Enter a number"))    
if num <0:
    print("Factoral of negetive numbers do not exsist")
else:
    print("the factoral of",num,"is",factorial(num))    