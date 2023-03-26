from random import randint


class Roleta:
    def __init__(self, tipo, qtdCasas, qtdZeros):
        self.tipo = tipo
        self.qtdCasas = qtdCasas
        self.qtdZeros = qtdZeros

    def getTipo(self):
        return Roleta.tipo

    def setTipo(self, tipo):
        self.tipo = tipo

    def getQtdCasas(self):
        return Roleta.qtdCasas

    def setQtdCasas(self, qtdCasas):
        self.qtdCasas = qtdCasas

    def getQtdZeros(self):
        return Roleta.qtdZeros

    def setQtdCasas(self, qtdZeros):
        self.qtdZeros = qtdZeros


class RoletaAmericana(Roleta):

    def __init__(self, tipo, qtdCasas, qtdZeros):
        super().__init__(tipo, qtdCasas, qtdZeros)
        self.tipo = "Americana"
        self.qtdCasas = 38
        self.qtdZeros = 2

    def gerarNumero(self, casa):
        numerosA = [0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                    27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
        return numerosA[casa]

    def gerarCor(self, casa):
        coresA = [0, 0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1,
                  2, 1, 2, 1, ]
        if coresA[casa] == 0:
            cor = "Verde"
        elif coresA[casa] == 1:
            cor = "Vermelho"
        elif coresA[casa] == 2:
            cor = "Preto"
        return cor


class RoletaEuropeia(Roleta):

    def __init__(self, tipo, qtdCasas, qtdZeros):
        super().__init__(tipo, qtdCasas, qtdZeros)
        self.tipo = "Européia"
        self.qtdCasas = 37
        self.qtdZeros = 1

    def gerarNumero(self, casa):
        numerosE = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                    27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
        return numerosE[casa]

    def gerarCor(self, casa):
        coresE = [0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2,
                  1, 2, 1, ]
        if coresE[casa] == 0:
            cor = "Verde"
        elif coresE[casa] == 1:
            cor = "Vermelho"
        elif coresE[casa] == 2:
            cor = "Preto"
        return cor


class RoletaFrancesa(Roleta):

    def __init__(self, tipo, qtdCasas, qtdZeros):
        super().__init__(tipo, qtdCasas, qtdZeros)
        self.tipo = "Francesa"
        self.qtdCasas = 37
        self.qtdZeros = 1

    def gerarNumero(self, casa):
        numerosf = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                    27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
        return numerosf[casa]

    def gerarCor(self, casa):
        coresf = [0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2,
                  1, 2, 1, ]

        if coresf[casa] == 0:
            cor = "Verde"
        elif coresf[casa] == 1:
            cor = "Vermelho"
        elif coresf[casa] == 2:
            cor = "Preto"
        return cor


class Banca:
    def __init__(self):
        self.budget = 1000

    def getBudget(self):
        return Banca.budget

    def setBudget(self, budget):
        self.budget = budget

    def alterarBudget(self, budget):
        self.budget += budget


class Jogador:
    def __init__(self, nome, saldo, aposta, dinheiroapostado, opcaoj, rodadasSemJogar):
        self.nome = nome
        self.saldo = saldo
        self.aposta = aposta
        self.dinheiroapostado = dinheiroapostado
        self.opcaoj = opcaoj
        self.rodadasSemJogar = rodadasSemJogar

    def getNome(self):
        return Jogador.nome

    def setNome(self, nome):
        self.nome = nome

    def getSaldo(self):
        return Jogador.saldo

    def setSaldo(self, saldo):
        self.saldo = saldo

    def alterarSaldo(self, saldo):
        self.saldo += saldo

    def setAposta(self, aposta):
        self.aposta = aposta

    def getAposta(self):
        return Jogador.aposta

    def setDinheiroApostado(self, dinheiroapostado):
        self.dinheiroapostado = dinheiroapostado

    def getDinheiroApostado(self):
        return Jogador.dinheiroapostado


class Main:
    print("Escolha o tipo da roleta : ")
    print("1 - Roleta Americana")
    print("2 - Roleta Européia")
    print("3 - Roleta Francesa")

    tipoRoleta = input("Digite o número correspondente : ")
    print()
    qtdJogadores = int(input("Número de jogadores : "))
    jogadores = []
    banca = Banca()
    resultado = 0
    casa = 0

    for i in range(qtdJogadores):
        print()
        print("Digite os dados do Jogador " + str(i + 1) + " :")
        nome = input("Nome : ")
        saldo = int(100)
        jogador = Jogador(nome, saldo, 0, 0, 1, 0)
        jogadores.append(jogador)
        print("Jogador Adicionado!")
        print("Você possui 100 fichas")

    while banca.budget != 0:
        print()
        print("Façam suas apostas!")

        for i in range(qtdJogadores):
            print("Jogador " + jogadores[(i)].nome + " :")
            print("Você deseja apostar?")
            opcaoj = (int(input("Digite 1 para Sim ou 2 para Não :")))
            jogadores[i].opcaoj = opcaoj
            jogadores[i].rodadasSemJogar += 1
            if jogadores[i].opcaoj == 1:
                print()
                print("Escolha um número de 1 a 36")
                jogadores[i].setAposta(int(input("Aposta : ")))
                print("Quanto você gostaria de apostar ?")
                jogadores[i].setDinheiroApostado(int(input("$$ : ")))
                print("Obrigado por sua aposta! ")
            elif jogadores[i].opcaoj == 2:
                print()
                print("Você esta a " + str(jogadores[i].rodadasSemJogar) + " rodadas sem jogar")

        if int(tipoRoleta) == 1:
            roletaAmericana = RoletaAmericana("Americana", 38, 2)
            print()
            print("O resultado da roleta foi : ")
            casa = randint(0, 37)
            resultado = roletaAmericana.gerarNumero(casa)
            print(str(roletaAmericana.gerarNumero(casa)))
            print(str(roletaAmericana.gerarCor(casa)))
        elif int(tipoRoleta) == 2:
            roletaEuropeia = RoletaEuropeia("Européia", 37, 1)
            print()
            print("O resultado da roleta foi : ")
            casa = randint(0, 36)
            resultado = roletaEuropeia.gerarNumero(casa)
            print(str(roletaEuropeia.gerarNumero(casa)))
            print(str(roletaEuropeia.gerarCor(casa)))
        elif int(tipoRoleta) == 3:
            roletaFrancesa = RoletaFrancesa("Francesa", 27, 1)
            print()
            print("O resultado da roleta foi : ")
            casa = randint(0, 36)
            resultado = roletaFrancesa.gerarNumero(casa)
            print(str(roletaFrancesa.gerarNumero(casa)))
            print(str(roletaFrancesa.gerarCor(casa)))
            if int(resultado) == 0:
                for i in range(qtdJogadores):
                    if jogadores[i].opcaoj == 1:
                        print()
                        print("Jogador" + jogadores[i].nome + ", o resultado foi 0 ou 00, o que você deseja ?")
                        print("1 - Pegar metade do dinheiro apostado de volta")
                        print("2 - Tentar novamente")
                        opcaof = int(input("Digite a sua opção : "))
                        if opcaof == 1:
                            jogadores[i].saldo = int(jogadores[i].saldo) + (
                                    jogadores[i].dinheiroapostado / 2)
                            print()
                            print("Metade do seu dinheiro apostado foi devolvido")
                        if opcaof == 2:
                            print()
                            print("O resultado da roleta foi : ")
                            casa = randint(0, roletaFrancesa.qtdCasas())
                            resultado = roletaFrancesa.gerarNumero(casa)
                            print(str(roletaFrancesa.gerarNumero(casa)))
                            print(str(roletaFrancesa.gerarCor(casa)))
                            if jogadores[i].getAposta == resultado:
                                print()
                                print("O jogador " + jogadores[i].nome + " ganhou " + str(
                                    jogadores[i].dinheiroapostado * 35))

                                banca.alterarBudget(- (jogadores[i].dinheiroapostado * 35))
                            else:
                                print()
                                print("O jogador " + jogadores[i].nome + " perdeu " + str(jogadores[i].dinheiroapostado))
                                jogadores[i].saldo = int(jogadores[i].saldo) - jogadores[i].dinheiroapostado
                                banca.alterarBudget(jogadores[i].dinheiroapostado)

        for i in range(qtdJogadores):
            if jogadores[i].opcaoj == 1:
                if jogadores[i].getAposta == resultado:
                    print()
                    print("O jogador " + jogadores[i].nome + " ganhou " + str(jogadores[i].dinheiroapostado * 35))

                    banca.alterarBudget(- (jogadores[i].dinheiroapostado * 35))
                else:
                    print()
                    print("O jogador " + jogadores[i].nome + " perdeu " + str(jogadores[i].dinheiroapostado))
                    jogadores[i].saldo = int(jogadores[i].saldo) - jogadores[i].dinheiroapostado
                    banca.alterarBudget(jogadores[i].dinheiroapostado)

        for i in range(qtdJogadores):
            if jogadores[i].saldo == 0 or jogadores[i].rodadasSemJogar == 4:
                del (jogadores[i])
                print()
                print("O jogador " + jogadores[i].nome + " foi eliminado")

        print()
        print("Saldo")
        print("Banca : " + str(banca.budget))
        for i in range(qtdJogadores):
            print("Jogador " + jogadores[i].nome + " :" + str(jogadores[i].saldo))

    if banca.budget == 0:
        print()
        print("A banca quebrou!")
        print("O jogo acabou")
