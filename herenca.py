class Alimentos:
    def __init__(self, nome, origem, sabor, nutriente, caloria):
        self.nome = nome
        self.origem = origem
        self.sabor = sabor
        self.nutriente = nutriente
        self.caloria = caloria


class Ovo(Alimentos):
    def __init__(self, nome, origem, sabor, nutriente, caloria, tipo, modo):
        super().__init__(nome, origem, sabor, nutriente, caloria)
        self.tipo = tipo
        self.modo = modo

    def comer(self):
        cardapio = ["Omelete", "Ovo cozido", "Ovo de codorna", "Ovo frito", "Ovo mexido"]
        for i in range(len(cardapio)):
            print(f"{i + 1} - {cardapio[i]}")
        while True:
            self.modo = int(input("Digite qual tipo de ovo você deseja comer: "))

            if self.modo == 0:
                print("Não tem esse item no cardápio!")

            elif self.modo in range(len(cardapio) + 1):
                print(f"Voce escolheu {cardapio[self.modo - 1]}")
                break

            else:
                print("Não tem esse item no cardápio!")

    def tipoOvo(self):
        while True:
            self.tipo = int(input("Digite '1 - Granja ' ou '2- Ovo Caipira'"))


ovo = Ovo("Caio", "Awsfd", "ofaw", "oejfop", "oas9", "pfjA)W", "OJDBA")

Ovo.comer(ovo)
