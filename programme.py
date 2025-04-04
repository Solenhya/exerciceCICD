
def addition(a:int,b:int)->int:
    try:
        a = int(a)
        b = int(b)
        return a+b
    except:
        return "Erreur"


def RunProgram():
    print("Bonjour dans ce simple programme d'addition")
    running = True
    a = input("Votre premier chiffre:")
    b = input("Votre deuxieme chiffre:")
    result = addition(a,b)
    if(result!="Erreur"):
        print(f"Le resultat de {a} + {b} est {result} merci d'avoir utiliser ce programme")
    else:
        print("Erreur")

if __name__=="__main__":
    RunProgram()