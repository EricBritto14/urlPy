class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        return url.strip()
    
    def valida_url(self):
        if self.url == "":
           raise ValueError("A URL está vazia") #Raise serve para tratamento de erros e retornar para o usuario um erro.
        
    def get_url_base(self):
        indice_interrogacao = self.url.find("?") #Metodo find para procurar algo especifico em uma string
        url_base = self.url[:indice_interrogacao] #Quando coloca assim, 0:2 significa do indice 0 ao 1, excluindo o 2. E quando deixa sem nada, por exemplo 0: ele começa do começo e vai até o fim                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        return url_base
 
    def get_url_parametros(self):
        indice_interrogacao = self.url.find("?") 
        url_parametros = self.url[indice_interrogacao +1:] #Nesta url, queremos pegar os parametros de pesquisa, entao pegamos o indice do ? que separa os parametros e a url, indice de interrogacao +1 para a interrogacao ficar de fora e : sem nada na frente para ir ate o fim da string
        return url_parametros
    
    def get_valor_parametro(self, nome_parametro):
        indice_parametro = self.get_url_parametros().find(nome_parametro) #Criando uma variável para buscar um novo parametro a partir do url_parametros que seria o indice pra frente do ?
        indice_valor = indice_parametro + len(nome_parametro) + 1 #Colocando o valor do indice 
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)

        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        
        return valor

extrator_url = ExtratorURL("bytebank.com/cambio?quantidade=100&moewdaOrigem=real&moedaDestino=dolar")
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)