#variables d'input

firstNumber = input("Entrez le premier nombre: ")
secondNumber = input("Entrez le second nombre: ")
operator = input(
	"+ pour la somme"+ "\n" +
	"- pour la soustraction"+ "\n" +
	"* pour la multiplication"+ "\n" +
	"/ pour la division"+ "\n" +
 "Entrez l'opération à effectuer: ")

#conditions de sortie

#on veut un chiffre dans le premier input et dans le second input
if (type(firstNumber) != int) & (type(secondNumber) != int):
    if(operator == "+"):
        print(float(firstNumber) + float(secondNumber))
    elif(operator == "-"):
        print(float(firstNumber) - float(secondNumber))
    elif(operator == "*"):
        print(float(firstNumber) * float(secondNumber))
    elif(operator == "/"):
#prévoir la division par zéro si l'utilisateur est malicieux
        if(secondNumber == 0):
            print("Il est impossible de diviser par zéro, enfin!")
        else:
            print(float(firstNumber) / float(secondNumber))
    else:
        print("L'opérateur n'est pas valide, veuillez relancer le programme!")
else:
    print("Veuillez entrer un nombre valide")