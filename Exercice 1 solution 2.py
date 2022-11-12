if __name__ == '__main__':
    try:
        a = float(input("a: "))
        b = float(input("b: "))
        res = a/b
    except ValueError:
        print("Please entrer un chiffre") 
    except ZeroDivisionError:
        print("b ne doit pas être 0")
    else:
        print(res)