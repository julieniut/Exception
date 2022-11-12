if __name__ == '__main__':
    try:
        file = open('file.txt', 'r')
        lines = file.readlines()
        # fermez le fichier après avoir lu les lignes
        file.close()
        print(lines)

    except FileNotFoundError as err:
        print(f"Vérifier le chemin d'acces: {err}")
    except FileExistsError as err:
        print(f" {err}")
    except UnicodeDecodeError as err:
        print(f"Caractère non gérer par le codec: {err}")
    except PermissionError as err:
        print(f"Permission non attribuer: {err}")