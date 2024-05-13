class Cliente:

    # atributo de clase, compartido por todas las instancias
    # categoria = "cliente premium"

    #Constructor
    def __init__(self, nombre, email, password, dni):
        self.nombre = nombre
        self.email = email
        self.password = password
        self.dni = dni
        self.carro = []
    
    def comprar(self, articulo):
        self.carro.append(articulo)
        print(f"{self.nombre} compro {articulo}")

    def __str__(self):
        return f"Nuevo cliente {self.nombre} con usuario {self.email}"
    
    def __len__(self):
        return len(self.carro)
    
    def __getitem__(self, pos):
        return self.carro[pos]
    
    def __setitem__(self, pos, articulo_nuevo):
        self.carro[pos] = articulo_nuevo