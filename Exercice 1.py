if __name__ == '__main__':
    try:
        a = float(input("a: "))
        b = float(input("b: "))
        res = a/b
    except (ValueError, ZeroDivisionError):  #si le programme renvoie ValueError ou ZeroDivisionERROR,
        print("une valeur n'est pas correct")  #il affiche le print
    else: #sinon print le resultat
        print(res)