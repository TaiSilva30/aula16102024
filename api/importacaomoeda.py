import http.client
import json

def verificarCotacaoEmReais():
    precoDollar, precoEuro, precoBitCoin = buscarPrecoDasMoedas()

    print(f"Preco do BitCoin: {formatar_valor(float(precoBitCoin))}")
    print(f"Preco do Dolar: {formatar_valor(float(precoDollar))}")
    print(f"Preco do Euro: {formatar_valor(float(precoEuro))}")

    return

def formatar_valor(valor):
    return f"R$ {valor: ,.2f}".replace(',', 'X').replace('.',',').replace('X', '.')

def buscarPrecoDasMoedas():
    awesomeapi = http.client.HTTPSConnection ("economia.awesomeapi.com.br")
    awesomeapi.request("GET", "/json/last/USD-BRL,EUR-BRL,BTC-BRL")
    response =awesomeapi.getresponse()
    data = response.read()
    cotacoes = json.loads(data)
    return cotacoes['USDBRL']['bid'], cotacoes['EURBRL']['bid'], cotacoes['BTCBRL']['bid']

verificarCotacaoEmReais()