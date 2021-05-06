#Este metodo se encarga de calcular la parte entera del decimal ingresado para asi ser usado en el metodo decimalbinario.
def enteroBinario(numero):
    """    
    Documentation:
    *** Este método se encarga de calcular la parte entera del numero ingresado ***
    
    Variable(s)
    numero: Almacena la magnitud del número ingresado
    resultado: Almacena el resultado a la operación aplicada
    """  
    
    #Creamos las dos variables número que sirve para almacenar la magnitud del número ingresado
    #Y resultado para almacenar el resultado(número en binario)
    numero = abs(numero)
    resultado = ""

    #Verifica que el número sea mayor o igual a 1 y procedente al numero ingresado se le obtiene el modulo 2
    #Luego a la variable numero se le divide por 2 para asi saber si la variable es aun divisible por 2 y dado el caso en que 
    #Se cumpla vuelve hacer el proceso hasta que numero no sea mayor o igual a 1.
    while numero >= 1:
        resultado = str(int(numero%2))+resultado
        numero = int(numero/2)
    return resultado

    
def decimalABinario(numero):
    """
    Documentation:
    *** Este método se encarga de calcular la parte decimal del numero ingresado ***
    
    Variable(s)
    numero: Almacena el número ingresado
    decimal: Obtiene el valor absoluto de la parte decimal del numero ingresado
    resultado: Almacena el resultado a la operación aplicada
    """
    
    #Creamos las dos variables numero que sirve para almacenar la parte decimal del numero ingresado
    #Y resultado para almacenar el resultado de la parte decimal en binario 
    decimal = abs(numero-int(numero))
    resultado = ""

    #Verifica que el numero sea diferente a 0 y procedente al numero decimal ingresado se le multiplica x 2
    #Despues se va almacenando el resultado en la variable resultado y ya luego volvemos a obtener la parte decimal 
    #restandole la parte entera
    while decimal != 0:
        decimal = decimal*2
        resultado = resultado + str(int(decimal))
        decimal = decimal - int(decimal)

    return resultado




def decimalBinario(numero, formato):
    """
    Documentation:
    *** Este método se encarga de unir los dos metodos anteriores enteroBinario y decimalABinario, y luego
    aplicarle el formato IEEE 754 de 32 bits o el formato IEEE 754 de 64 bits segun lo que elija el usuario ***
    
    Variable(s)
    numero: Almacena el número ingresado
    entera: Obtiene el resultado enteroBinario (la parte entera del numero ingresado)
    decimal: Obtiene el resultado metodo decimalABinario (la parte decimal del numero ingresado)
    resultado: Almacena el resultado de la operacion aplicada
    exponente: Almacena el exponente con el cual se hara uso en las operaciones
    mantisa: Almacena la mantisa para asi ser usada al obtener los formatos
    
    """

    #Primero recibimos el numero y el formato que se desea obtener 
    #Luego se crean dos variables que llamaran los metodos anteriores
    
    #Esta variable llama al metodo que obtiene la parte entera en binario
    entera = enteroBinario(numero)
    #Esta variable llama al metodo que obtiene la parte decimal a  binario
    decimal =  decimalABinario(numero)
    resultado = ""
    
    #Esta variable calcula el tamaño de la parte entera para obtener el exponente
    exponente = len(entera)

    #En este for se recorre el vector de la parte entera y convierte el exponente
    for i in entera:
        exponente = exponente-1

        if i =="1":
            break
            
    #En este if se obtiene el signo haciendo una verificacion de igualdad
    if str(numero).find("-") == 0:
        resultado = "1"+ resultado
    else:
        resultado = "0"+ resultado

    #Esta variable almacena la mantisa 
    mantisa = entera[1:len(entera)] + decimal 

    #En este if se verifica que formato fue ingresado 
    if formato == "32":
        exponente = exponente + 127 
        exponente = enteroBinario(exponente)

        resultado = resultado + exponente + mantisa

        #En este if se hace la operacion para obtener el formato de 32 bits
        if(len(resultado)<32):
            resultado = resultado + "0"*(32-len(resultado))

    elif formato == "64":
        exponente = exponente + 1023
        exponente = enteroBinario(exponente)
        resultado = resultado + exponente + mantisa

        #En este if se hace la operacion para obtener el formato de 64 bits
        if(len(resultado)<64):
            resultado = resultado + "0"*(64-len(resultado))

    return resultado




def binarioDecimal(numero):
    """
    Documentation: 
    *** Este método sirve para convertir de binario a Decimal ***
    
    Variable(s)    
    t: Tamaño de la cadena de numeros ingresados
    numero: Almacena el número ingresado
    resultado: Almacena el resultado de operacion aplicada
        
    """    
    #Tamaño de la cadena sacando el número que corresponde al signo
    t = len(numero.split(".")[0])-1 
    #resultado del número binario convertido a decimal
    resultado = 0 
    
    #Parte entera 
    for i in numero.split(".")[0]:        
        resultado =  int(i)*(2**t)+resultado
        t = t-1
        
    #Si el numero tiene decimal    
    if len(numero.split(".")) != 1 :
        for i in numero.split(".")[1]:
            resultado =  int(i)*(2**t)+resultado
            t = t-1
    return resultado




def binarioEntero(numero, formato):
    """
    Documentation: 
    *** Este método se encarga de quitar los formatos de los numeros binarios 
    haciendo uso del metodo binarioDecimal***
    
    Variable(s)    
    numero: Almacena el número ingresado
    signo: Almacena el signo obtenido del numero ingresado a convertir 
    formato: Almacena el formato del numero binario ingresado (formato de 32 o 64)
    resultado: Almacena el resultado de la operacion aplicada
    exponente: Almacena el exponente con el cual se hara uso en las operaciones
    mantisa: Almacena la mantisa para asi ser usada en los formatos
    resultado2: Es el resultado multiplicado por el signo obtenido
    """
   
    resultado = ""
    #Se verifica  cual es el digito del numero ingresado
    #Ya que el primer numero es el signo entonces si es igual a 1 el signo es negativo en caso contrario es positivo
    if numero[0] == "1" :
        signo = -1
    else:
        signo = 1

    #Se quita el formato de 32 
    if (formato == "32"):
        #Pasamos el exponenteonente a decimal
        exponente = binarioDecimal(numero[1:9])
        exponente = exponente - 127

        #Mantisa
        mantisa = numero[9:31]
        
    #Se quita el formato de 64
    elif formato == "64" :
        #Pasamos el exponenteonente a decimal
        exponente = binarioDecimal(numero[1:12])
        exponente = exponente - 1023

        #Mantisa
        mantisa = numero[12:61]

    mantisa = float("1." + mantisa)
    resultado = str(mantisa*(10**exponente))

    resultado2 = binarioDecimal(resultado)*signo
    
    return resultado2



def letras(numero):
    """
    Documentation:
    *** Este metodo se encarga de convertir los numeros mayores a 9 en formato hexadecimal ***
    
    Variable(s)
    numero: Almacena el número ingresado
    letra: Almacena la letra correspondiente al numero ingresado
    
    """
    letra = ""

    if numero == 15:
        letra = "F"

    elif numero == 14:
        letra = "E"

    elif numero == 13:
        letra = "D"

    elif numero == 12:
        letra = "C"

    elif numero == 11:
        letra = "B"

    elif numero == 10:
        letra = "A"

    return letra




def aHexadecimal(numero):
    
    """
     Documentation:
    *** Este metodo se encarga de convertir los numeros de decimal a hexadecimal ***
    
    Variable(s)
    numero: Almacena el número ingresado    
    resultado: Almacena el resultado de operacion aplicada
    mod: Almacena el modulo del numero ingresado
    """   

    resultado = ""
    
    while numero/16 > 0 :
        
        mod = int(numero%16)
        
        if mod >= 10: 
            mod = letras(mod)
        
        resultado = str(mod) + resultado 
        numero = int(numero/16)
        
    return resultado



def letrasHexadecimal(letra):
    """
    Documentation:
    *** Este metodo se encarga de convertir las letras ingresadas en formato hexadecimal a numeros mayores a 9  ***
    
    Variable(s)
    numero: Almacena el número correspondiente a la letra ingresada
    letra: Almacena la letra ingresada
    
    """

    if letra == "F":
        numero = 15

    elif letra == "E":
         numero= 14

    elif letra == "D":
        numero = 13

    elif letra == "C":
        numero = 12

    elif letra == "B":
        numero = 11

    elif letra == "A":
        numero = 10

    return numero




def hexadecimalDecimal(numero):
    """
    Documentation:
    ***Este metodo se encarga de convertir los numeros de Hexadecimal a Decimal ***
    
    Variable(s)    
    resultado: Almacena el resultado de la operacion aplicada
    exponente: Almacena el exponente con el cual se hara uso en las operaciones 
    
    """
    #recibe el número hexa convertir    
    resultado = 0
    exponente = len(numero)-1

    for i in numero:
        
        #Cuando lee una letra le asigna su valor en decimal
        if i.isalpha() :
            i = letrasHexadecimal(i)
            
        #convertimos a decimal multiplicando x16 elevado a la posicion del dato y x el valor del dato 
        resultado = resultado + pow(16,exponente)*int(i)
        #restamos uno al exponente porque cambia de dato
        exponente = exponente - 1
        
    return resultado




def binario_decimal_sinFormato(numero):  
    """
    Documentation:
    ***Este metodo se encarga de convertir los numeros de binario sin formato a Decimal ***
    
    Variable(s)
    t: Almacena el tamaño del numero
    resultado: Almacena el resultado a la operacion aplicada
    numero: Almacena el número ingresado 
    
    """
    t = len(numero)-1    
    resultado = 0
    for i in numero:
        numero = int(i)
        resultado = resultado + numero*(pow(2,t))
        t = t-1

    return resultado
  
    
    
    
def binarioHexadecimal(numero):
    """
    Documentation:
    *** Este método se encarga de convertir de binario a decimal y luego Decimal a Hexadecimal ***
    
    Variable(s)
    Adec: Almacena el resultado del metodo binario_decimal_sinFormato  
    resultado: Almacena el resultado del metodo aHexadecimal
    
    """
    
    Adec = binario_decimal_sinFormato(numero)    
       
    resultado = aHexadecimal(float(Adec))
    
    #Convierte de binario formato 32 a decimal
    #Adec = binarioEntero(numero, "32")    
    
    return(resultado)



    
def hexadecimalBinario(numero):  
    """
    Documentatio:
    *** Método que convierte Hexadecimal a Decimal y luego de Decimal a Binario ***
    
    Variable(s)
    Adec: Almacena el resultado del metodo hexadecimalDecimal (el numero en decimal)
    resultado: Almacena el numero de los metodos enteroBinario y decimalABinario (el numero en binario)
    """
    
    #Convierte de hexadecimal a decimal
    Adec = hexadecimalDecimal(numero)     
   
    #Convierte de decimal a binario(sin formato)      
    #Concatena la parte entera y la parte decimal separados por un punto
    resultado = str(enteroBinario(Adec)) + "." + str(decimalABinario(Adec))
       
    # Convertir de decimal a binario 32 bits
    #resultado = (decimalBinario(float(Adec), "32"))
        
    return(resultado)



 
def opciones (): 
    
    """
    Documentation:
    *** #Este metodo se encarga de mostrar todas las opciones que se brindan al usuario ***
    
    Variable(s)
    numero: Almacena el número ingresado 
    opcion: Almacena la opcion elegida
    """
    print(" ")
    print("\nPrograma para convertir entre sistemas numéricos\n")   
    print("¡NOTA: INGRESA SOLO MAYÚSCULAS!") 
    print("Elija una de las opciones")  
    print("1. Decimal a IEEE754 de 32 bits")
    print("2. IEEE754 de 32 bits a decimal")
    print("3. Decimal a IEEE 754 de 64 bits")
    print("4. IEEE 754 de 32 bits a Decimal")
    print("5. Decimal a Hexadecimal")
    print("6. Hexadecimal a Decimal")
    print("7. Binario a Hexadecimal")
    print("8. Hexadecimal a Binario")
    
    opcion = str(input("\nIngresa la opción que deseas ejecutar: "))   
    
    if int(opcion) > 8:
        print("No existe ninguna opción con este numeral intenta nuevamente")
    else:
        print("Escriba el numero a convertir")
    
    
    numero = input()   
    

    if opcion == "1":
        print(decimalBinario(float(numero), "32"))
    
    if opcion == "2":
        print(binarioEntero(numero, "32"))

    if opcion == "3":
        print(decimalBinario(float(numero), "64"))

    if opcion == "4":
        print(binarioEntero(numero, "64"))

    if opcion == "5":
        print(aHexadecimal(float(numero)))
    
    if opcion == "6":
        print(hexadecimalDecimal(numero))
            
    if opcion == "7":
        print(binarioHexadecimal(numero))
        
    if opcion == "8":
        print(hexadecimalBinario(numero))
        
    
    opciones()
opciones()