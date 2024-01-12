url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"
url = ""

url = url.strip()



#Parte que separa a base e os parametros
indice_interrogacao = url.find("?") #Metodo find para procurar algo especifico em uma string
url_base = url[:indice_interrogacao] #Quando coloca assim, 0:2 significa do indice 0 ao 1, excluindo o 2. E quando deixa sem nada, por exemplo 0: ele começa do começo e vai até o fim
url_parametros = url[indice_interrogacao +1:] #Nesta url, queremos pegar os parametros de pesquisa, entao pegamos o indice do ? que separa os parametros e a url, indice de interrogacao +1 para a interrogacao ficar de fora e : sem nada na frente para ir ate o fim da string
#print(url_parametros)

#Busca o valor de um parametro
parametro_busca = 'moedaOrigem' #Este codigo funcionou com o moedaOrigem no parametro, assim mostrando o "real" apenas no final, agora faremos com o moedaDestino
indice_parametro = url_parametros.find(parametro_busca) #Criando uma variável para buscar um novo parametro a partir do url_parametros que seria o indice pra frente do ?
indice_valor = indice_parametro + len(parametro_busca) + 1 #Colocando o valor do indice 
valor = url_parametros[indice_valor:]
#print(valor)

#Busca o valor de um parametro
#Código para funcionar quando o parametro não estiver apenas no final da url
parametro_busca = 'moedaDestino' 
indice_parametro = url_parametros.find(parametro_busca) #Criando uma variável para buscar um novo parametro a partir do url_parametros que seria o indice pra frente do ?
indice_valor = indice_parametro + len(parametro_busca) + 1 #Colocando o valor do indice 
indice_e_comercial = url_parametros.find('&', indice_valor) #Deste jeito usando o find, estou dizendo para ele procurar um & depois do indice_valor, se não tiver retorna -1 e se tiver retorna outro valor
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor= url_parametros[indice_valor:indice_e_comercial] #Para que se haver algum & comercial depois do indice_valor, ele parar de imprimir antes do & comercial para não pegar outros parametros
print(valor)
 