class Atleta:

    def __init__(self, nombre, apellido, altura, peso, telefono):
       self.nombre = nombre
       self.apellido = apellido
       self.altura = altura
       self.peso = peso
       self.telefono = telefono
   
    def get_imc(self):
        return self.peso / self.altura ** 2

atleta_1 = Atleta("Leo", "Messi", 1.7, 80, 12345)

atleta_1.altura = 1.2

print(atleta_1.get_imc())

