
def oddeven(num):
    '''this function return the string odd or eve'''
    if(num%2==0):
        return "even"
    else:
        return "odd"
print(oddeven(23))
print(oddeven.__doc__)