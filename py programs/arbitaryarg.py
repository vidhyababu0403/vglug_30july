def number(*args):
    "its prints the number sequence"
    for i in args:
        print(i)
number(1,2,3,4,"hi",5,"hello")
print(number.__doc__)
