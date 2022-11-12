a = int(input("Enter a positive number: "))
if a <= 0: #si une valeur n'est pas positive alors renvoie l'erreur suivante
    raise ValueError("It’s not a positive number")