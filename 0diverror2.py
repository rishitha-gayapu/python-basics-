#like specialised doctors
#for those specific error only those exception
#blocks will get executed
a=10
try:
    b=int(input("enter the number:"))
    print("resourse open")
    print(a/b)
except ZeroDivisionError as e:
    print("please note,number cant be divided by zero")
except ValueError as e:
    print("Invalid input",e)
except Exception as e:#if not any above errors
    print("Other error",e)
finally:
    print("Resourse closed")
