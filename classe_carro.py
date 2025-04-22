class Carro:
    def __it__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.combustivel = 0
        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        if self.combustivel > 0:
            self.ligado = True
            