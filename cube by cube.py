def cube(number):
    return number*number*number
def div(number):
    if number %3==0:
        return cube(number)
    else:
        return False
print(div(18))    
print(div(4))    