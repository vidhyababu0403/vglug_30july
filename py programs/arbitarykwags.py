def number(**kwargs):
    "its prints the number sequence with keys and values"
    for key,value in kwargs.items():
        print(key,value)
number(nmae="vidhya.B",age=21,rollno=201021132)
print(number.__doc__)
