class Cachorro:
    def __init__(self, nome, raca, comida, acordado, feliz):
        self.nome = nome
        self.raca = raca  # Corrigido de 'raça' para 'raca' (nome de variável não pode ter acento)
        self.comida = comida
        self.acordado = acordado
        self.feliz = feliz
        self.energia = 100  # Inicializa a energia com 100 pontos

    def comer(self, quantidade):
        self.comida -= quantidade
        self.feliz = True
        print(f"{self.nome} comida restante: {self.comida}")

    def dormir(self):
        self.acordado = False
        self.energia = 100  # Restaura a energia para 100 quando o cachorro dorme
        print(f"{self.nome} está dormindo e recuperou a energia.")

    def acordar(self):
        self.acordado = True
        print(f"{self.nome} está acordado")

    def latir(self):
        if self.acordado:
            print(f"{self.nome} latiu: AU AU!")
        else:
            print(f"{self.nome} está dormindo")

    def brincar(self):
        if self.energia >= 20:  # Verifica se a energia é suficiente para brincar
            self.energia -= 20  # Reduz 20 pontos de energia ao brincar
            self.feliz = True
            print(f"{self.nome} está brincando! Energia restante: {self.energia}")
        else:
            print(f"{self.nome} não tem energia suficiente para brincar. Energia atual: {self.energia}")

# Criando instâncias de cachorro
cachorro1 = Cachorro("Humpty Dumpty", "bulldog francês", 8, True, True)
cachorro2 = Cachorro("Costelinha", "dachshund", 3, False, False)

# Interagindo com os cachorros
cachorro1.comer(2)
cachorro1.dormir()
cachorro2.acordar()
cachorro2.brincar()  # Vai brincar e gastar energia
cachorro2.latir()  # Deve latir se estiver acordado
cachorro2.brincar()  # Se a energia for suficiente, vai brincar, senão avisa que não tem energia
