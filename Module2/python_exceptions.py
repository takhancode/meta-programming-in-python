try:
    num=int(input("EnteraNumber"))
    result=10/num
    print(result)
except ValueError:
    print("Invalid input.Please enter a number")
except ZeroDivisionError:
    print("CannotdividebyZero")


    # GenericExceptionHandler
try:
    num=int(input("EnteraNumber:"))
    print(10/num)
except Exception as e:
    print("An error occured",e)