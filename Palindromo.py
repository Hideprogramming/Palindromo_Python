def palindromo(palabra):

    #Para borrar los espacios
    palabra = palabra.replace(" ", "")

    #Para que los caracteres sean minusculas
    palabra = palabra.lower()

    #Para invertir la palabra
    palabra_invertida = palabra[::-1]

    #Verificar si es o no es palindromo
    if palabra == palabra_invertida:
        return True
    else:
        return False

#Funcion principal:
def main():

    #Entrada de la palabra por teclado
    palabra = input("Ingrese una palabra: ")

    #Capturar la palabra
    es_palindromo = palindromo(palabra)

    #Validar Si es o No palindromo
    if es_palindromo:
        print("La palabra ingresada es Palindromo")
    else:
        print("La palabra ingresada NO es Palindromo")

#Entry point: inicio de la aplicacion:
if __name__ == '__main__':
    main()#Se ejecuta la funcion principal.
