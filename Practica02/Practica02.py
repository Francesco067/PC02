#problema 01
numeros_encontrados = []

for numero in range(1500, 2701):
    if numero % 7 == 0 and numero % 5 == 0:
        numeros_encontrados.append(numero)


print("Números divisibles por 7 y múltiplos de 5 en el rango de 1500 a 2700:")
print(numeros_encontrados)

#problema 02

n = 5

for i in range(n):
    print('* ' * (i + 1))

for i in range(n - 1):
    print('* ' * (n - i - 1))
    
#problema 03
numeros = []  
contador_pares = 0
contador_impares = 0

while True:
    opcion = input("Desea ingresar un número? (SI/NO): ")
    
    if opcion.upper() == "SI":
        numero = int(input("Ingrese el número: "))
        numeros.append(numero)
    elif opcion.upper() == "NO":
        break
    else:
        print("Opción no válida. Por favor, ingrese SI o NO.")

for num in numeros:
    if num % 2 == 0:  
        contador_pares += 1
    else:
        contador_impares += 1

print("Números ingresados:", numeros)
print("Cantidad de números pares:", contador_pares)
print("Cantidad de números impares:", contador_impares)

#problema 04

listado_alumnos = []


def ingresar_alumno():
    nombre = input("Ingrese el nombre del alumno: ")
    nota1 = float(input("Ingrese la primera calificación del alumno: "))
    nota2 = float(input("Ingrese la segunda calificación del alumno: "))
    nota3 = float(input("Ingrese la tercera calificación del alumno: "))
    alumno = {"Alumno": nombre, "Notas": [nota1, nota2, nota3]}
    listado_alumnos.append(alumno)

def mostrar_listado():
    print("Listado completo de alumnos:")
    for alumno in listado_alumnos:
        print(alumno)


n = int(input("Ingrese la cantidad de alumnos a registrar: "))
for _ in range(n):
    ingresar_alumno()


mostrar_listado()

#problema 05
numero=input("Dame el numero a examninar: ")
digito=input("Dame el digito a buscar en el numero: ")
def contar_digitos(numero, digito):
    
   
    cantidad = numero.count(str(digito))
    
    return cantidad


resultado = contar_digitos(numero, digito)
print(f"Cantidad de veces  de {digito} en el número {numero} es : {resultado}")

#problema 06
a, b = 0, 1

print(a)

while b <= 50:
    print(b)
    a, b = b, a + b

#problema 07
def es_primo(numero):
   
 
    for i in range(2, numero):
        if numero % i == 0:
            return False
    
  
    return True


numero = int(input("Ingrese un número para verificar si es primo: "))
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
    
#problema 08
def factorial(numero):
  
    if numero == 0:
        return 1
    
    resultado = 1
    
    for i in range(1, numero + 1):
        resultado *= i
    
    return resultado


numero = int(input("Ingrese un número para calcular su factorial: "))

resultado_factorial = factorial(numero)
print(f"El factorial de {numero} es: {resultado_factorial}")

#problema 09

def omitir_vocales(cadena):
   
   
    vocales = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
    
    cadena_resultante = ''
    
    for caracter in cadena:
    
        if caracter not in vocales:
            cadena_resultante += caracter
    
    return cadena_resultante

texto_original = input("Ingrese una cadena de texto: ")

texto_sin_vocales = omitir_vocales(texto_original)

print("Texto sin vocales:", texto_sin_vocales)

#problema 10