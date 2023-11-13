# CRIAÇÃO DA CLASSE PAI
class Alimentos:
    def __init__(self, nome, origem, sabor, nutriente, caloria):
        self.nome = nome
        self.origem = origem
        self.sabor = sabor
        self.nutriente = nutriente
        self.caloria = caloria


# CRIAÇÃO DA CLASSE FILHA
class Ovo(Alimentos):
    def __init__(self, nome, origem, sabor, nutriente, caloria, tipo, estado, temperos, acompanhamento):
        super().__init__(nome, origem, sabor, nutriente, caloria)
        self.tipo = tipo
        self.estado = estado
        self.temperos = temperos
        self.acompanhamento = acompanhamento

    print("\nBEM-VINDO A0 RESTAURANTE MURIEGGS!")

# FUNÇÃO COMER O OVO ESCOLHIDO

    def comer(self):
        cardapio = ["Omelete", "Ovo cozido", "Ovo de codorna", "Ovo frito", "Ovo mexido"]
        for i in range(len(cardapio)):
            print(f"{i + 1} - {cardapio[i]}")
        while True:
            opt = int(input("\nDigite qual tipo de ovo você deseja comer: "))

            if opt == 0:
                print("\nValor Inválido!\n")

            elif opt in range(len(cardapio) + 1):
                print(f"\nVocê escolheu comer um {cardapio[opt - 1]}\n")
                self.nome = cardapio[opt - 1]
                break
            else:
                print("\nValor Inválido!\n")

# FUNÇÃO TEMPERAR O OVO

    def temperar(self):
        temperos = ["sal", "azeite", "alho", "cebola"]
        for t in range(len(temperos)):
            print(f"{t + 1} - {temperos[t]}")
        while True:
            escolhaTempero = int(input(f"\nDigite qual tempero você deseja adicionar no {self.nome}: "))

            if escolhaTempero == 0:
                print("\nValor Inválido!\n")

            elif escolhaTempero in range(len(temperos) + 1):
                self.temperos = temperos[escolhaTempero - 1]
                print(f"\nO {self.nome} será temperado com {self.temperos}")
                break
            else:
                print("\nValor Inválido!\n")

# FUNÇÃO PARA ESCOLHER O PRATO PRINCIPAL QUE IRÁ COMER COM OVO

    def escolherPrato(self):
        pratos = ["Tapioca", "Pão", "Arroz e Feijão"]
        while True:
            opcao = input(f"\nVocê deseja adicionar algum prato principal para comer com o {self.nome}?: ")
            if opcao == "sim":
                for a in range(len(pratos)):
                    print(f"{a + 1} - {pratos[a]}")
                escolhaPrato = int(input(f"\nDigite qual acompanhamento você deseja adicionar com o {self.nome}: "))

                if escolhaPrato == 0:
                    print("\nValor Inválido!\n")

                elif escolhaPrato in range(len(pratos) + 1):
                    self.acompanhamento = pratos[escolhaPrato - 1]
                    print(
                        f"\nSeu prato está pronto!\n{self.acompanhamento} com {self.nome} temperado com {self.temperos}")
                    break
                else:
                    print("\nValor Inválido\n")
            elif opcao == "não":
                print(f"\nSeu prato está pronto!\nDelicioso {self.nome} temperado com {self.temperos}")
                break
            else:
                print("\nValor Inválido! Digite 'sim' ou 'não' para escolher acompanhamento")


# CRIAÇÃO DO OBJETO

ovo = Ovo("", "", "", "", "", "", "", "", "")

# CHAMAR A FUNÇÃO PARA EXIBIR OS RESULTADOS

Ovo.comer(ovo)
Ovo.temperar(ovo)
Ovo.escolherPrato(ovo)
