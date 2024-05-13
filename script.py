"""
#defino el diccionario para los usuarios
usuarios = {}

#funciones para registrarse, recuperar la información y loguearse
def registro ():
  user = input("Ingrese el nombre de usuario: ")
  while user == "":
    user = input("Ingrese el nombre de usuario: ")
  while user in usuarios:
    user = input("El usuario ya está registrado. Crea uno nuevo: ")
  password = input("Ingrese la contraseña: ")
  while password == "":
    password = input("Ingrese la contraseña: ")
  usuarios[user] = password
  print("Usuario creado!")

def leer_usuarios ():
  if len(usuarios) != 0:
    print(usuarios)
  else:
    print("No hay usuarios registrados!")

def login():
  user = input("Ingrese el usuario: ")
  if user in usuarios:
    password = input("Ingrese la contraseña: ")
    if password == usuarios[user]:
      print("Bienvenido!")
    else:
      print("La contraseña es incorrecta. Vuelve a intentarlo")
  else:
    print("El usuario ingresado no existe!")

# Y la interacción principal
def menu():
  opcion = ""
  while opcion != "4":
    opcion = input("Ingresa una opción: \n\t1-Crear usuario \n\t2-Leer registro de usuarios \n\t3-Ingresar \n\t4-Finalizar\n")
    if opcion == "1":
      registro()
    if opcion == "2":
      leer_usuarios()
    if opcion == "3":
      login()
    if opcion == "4":
      print("Hasta la próxima!")

menu()
"""

import sys

from paquete.clientes import Cliente

print(sys.argv) #lista de argumentos al ejecutar el script; 0 es el propio script, a partir de 1 los que ingresemos

cliente1 = Cliente("Juan", "asjdjas@hjotmail.com", 1234, "12345678")

print(cliente1)

cliente1.comprar("Play 5")

cliente1.comprar("Sandia")

cliente1.comprar("Fideos")

print(f"Hay {len(cliente1)} producto/s en el carro: {cliente1.carro}")

print(cliente1.__getitem__(1))

cliente1.__setitem__(2, "Arroz")

print(f"Se actualizo el carrito: {cliente1.carro}")