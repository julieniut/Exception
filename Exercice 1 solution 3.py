if __name__ == '__main__':
    try:
        a = float(input("a: "))
        b = float(input("b: "))
        res = a/b
    except ValueError as err:
        print(f"Please enter a float: {err}")
    except ZeroDivisionError as err:
        print(f"b should not be 0: {err}")
    else:
        print(res)