import http.client
import json

class EnderecoApiService:

    def consultarEnderecoIbge(self, cep=None):
        apiViaCep = http.client.HTTPSConnection("viacep.com.br")

        while True:
            cep = input("digite o cep para consultar o endereco: ")

            apiViaCep.request("GET", f"/ws/{cep}/json/")

            response = apiViaCep.getresponse()

            data = response.read().decode("utf-8")
            endereco = json.loads(data)


            print(endereco)

servico = EnderecoApiService()
servico.consultarEnderecoIbge()