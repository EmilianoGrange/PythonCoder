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