import sys

from paquete.clientes import Cliente

print(sys.argv) #lista de argumentos al ejecutar el script; 0 es el propio script, a partir de 1 los que ingresemos

cliente1 = Cliente("Juan", "juan23@hotmail.com", 1234, "12345678")

print(cliente1)

cliente1.comprar("Play 5")

cliente1.comprar("Sandia")

cliente1.comprar("Fideos")

print(f"Hay {len(cliente1)} producto/s en el carro: {cliente1.carro}")

print(cliente1.__getitem__(1))

cliente1.__setitem__(2, "Arroz")

print(f"Se actualizo el carrito: {cliente1.carro}")