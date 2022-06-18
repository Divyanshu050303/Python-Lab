
class myError(Exception):
    pass


def factorial():
    n = int(input("enter a number"))
    try:
        if n<0:
            raise myError('Negative Number')
        else:
            print(" factorial of the number")
            fct = 1
            for i in range(1, n + 1):
                fct = fct * i
            print(fct)
    except myError as error:
        print(error)


factorial()
