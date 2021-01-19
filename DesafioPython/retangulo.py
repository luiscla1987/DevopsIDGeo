class Retangulo(object):

    def __init__(self, base, altura, inicialX, inicialY):
        self._base = base
        self._altura = altura
        self._pontoA = [inicialX, inicialY]

    def getAltura(self):
        return self._altura

    def setAltura(self, valor):
        self._altura = valor

    def getBase(self):
        return self._base

    def setBase(self, valor):
        self._base = valor

    def getPontoInical(self):
        return self._pontoA

    def setPontoInicial(self, inicialX, inicialY):
        self._pontoA = [inicialX, inicialY]

    def _calcular_area(self):
        if(self._base != self._altura):
            return self._base * self._altura
        return 'Os valores informados formam um Quadrado'

    def _calcular_perimetro(self):
        return 2 * (self._base + self._altura)

    def _showInicialPoints(self):
        print(f"InicialPoints: [{self._pontoA[0]},{self._pontoA[1]}]")

    def _definirPontos(self):
        pontos = [self.getPontoInical()]
        pontos.append([(pontos[0][1] + self._base), pontos[0][0]])
        pontos.append([pontos[1][0], pontos[1][1] - self._altura])
        pontos.append([pontos[0][1], pontos[0][0] - self._altura])
        return pontos

    def _showInfos(self):
        print(f"Base: {self._base}")
        print(f"Altura: {self._altura}")
        print(f"Pontos Inciais: {self.getPontoInical()}")
        print(f"Pontos Vértices: {self._definirPontos()}")
        print(f"Perímetro: {self._calcular_perimetro()}")
        print(f"Área: {self._calcular_area()}²")


if __name__ == '__main__':
    ret = Retangulo(5, 3, 0, 0)
    ret._showInfos()
