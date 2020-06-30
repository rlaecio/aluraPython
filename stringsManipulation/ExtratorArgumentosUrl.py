class ExtratorArgumentosUrl:

    def __init__(self, url):
        self.url = url
        if self.urlEhValida(url):
            self.url = url.lower()
        else:
            raise LookupError('Url inválida!!!!')


    def __len__(self):
        return len(self.url)

    def __str__(self):
        moedaOrigem, moedaDestino = self.extraiArgumentos()
        representastring = "Valor: {} \nMoeda Origem: {} \nMoeda Destino: {} \n".format(self.extraiValor(), moedaOrigem, moedaDestino)
        return representastring

    def __eq__(self, other):
        return self.url == other.url




    @staticmethod
    def urlEhValida(url):
        if url and url.startswith("https://www.bytebank.com"):
            return True
        else:
            return False


    def extraiArgumentos(self):

        buscaMoedaOrigem  = "moedaorigem".lower()
        buscaMoedaDestino = "moedadestino".lower()

        indiceInicialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
        indiceFinalMoedaOrigem = self.url.find('&')
        moedaOrigem = self.url[indiceInicialMoedaOrigem : indiceFinalMoedaOrigem]

        if moedaOrigem == "moedadestino":
            self.trocaMoedaOrigem()
            indiceInicialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
            indiceFinalMoedaOrigem = self.url.find('&')
            moedaOrigem = self.url[indiceInicialMoedaOrigem: indiceFinalMoedaOrigem]

        indiceInicialMoedaDestino = self.encontraIndiceInicial(buscaMoedaDestino)
        indiceFinalMoedaDestino = self.url.find("&valor")
        moedaDestino = self.url[indiceInicialMoedaDestino:indiceFinalMoedaDestino]
        return moedaOrigem, moedaDestino

    def encontraIndiceInicial(self,moedaBuscada):
        return self.url.find(moedaBuscada) + len(moedaBuscada) + 1


    def trocaMoedaOrigem(self):
        self.url = self.url.replace("moedadestino", "real", 1)
        print(self.url)

    def extraiValor(self):
        buscaValor = "valor"
        indiceInicialValor = self.encontraIndiceInicial(buscaValor)
        valor = self.url[indiceInicialValor:]
        return valor


