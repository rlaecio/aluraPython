from ExtratorArgumentosUrl import ExtratorArgumentosUrl


url = "https://www.bytebank.com/cambio?moedaorigem=Real&moedadestino=dolar&valor=1500"

argumentoUrl = ExtratorArgumentosUrl(url)
moedaOrigem, moedaDestino = argumentoUrl.extraiArgumentos()
valor = argumentoUrl.extraiValor()
print(moedaDestino, moedaOrigem, valor)



