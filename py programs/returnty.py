num=int(input("enter a value:"))
def oddeven(num) -> str:
    if(num%2==0):
        return "even"
    else:
        return "odd"
print(oddeven(num))