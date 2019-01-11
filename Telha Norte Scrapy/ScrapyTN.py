import requests, scrapy
from unicodedata import normalize
from informaçãoProduto import InfProduto

urlMain = 'https://www.telhanorte.com.br/buscapagina?fq=C:/20/&O=OrderByTopSaleDESC&PS=24&sl=36fe8748-a5ed-4b60-ab55-64a164e28165&cc=24&sm=0&PageNumber=1'

aux = 1
listaTitulos = []
listaId = []
listaPreco = []

while(aux > 0):
    resp = requests.get(urlMain.replace("PageNumber=1","PageNumber=" + str(aux)))
    if resp.text == "":
        break
    else:
        respScrapy = scrapy.selector
        respScrapy = respScrapy.Selector(resp)
        titulo = respScrapy.xpath('//div[@class="x-shelf__content"]//h2//text()').extract()
        idTitulo = respScrapy.xpath('//div[@class="x-shelf__details-content"]//@data-product-id').extract()
        precoTitulo = respScrapy.xpath('//span[@class="x-shelf__best-price x-shelf__best-price--footage"]//strong//text()').extract()
        listaTitulos.extend(titulo)
        listaId.extend(idTitulo)
        listaPreco.extend(precoTitulo)
        aux += 1

urlAux = 'https://www.telhanorte.com.br/'

listaAux = []
listaAux.extend(listaTitulos)


for i in range(len(listaAux)):
    listaAux[i] = normalize('NFKD', listaAux[i]).encode('ASCII','ignore').decode('ASCII')
    listaAux[i] = urlAux + listaAux[i].lower().replace(" ","-").replace(",","-") + "-" + str(listaId[i]) + "/p"
    main = InfProduto()
    main.Config(listaAux[i],listaId[i],listaTitulos[i])
    main.RunInfProduto()
main.FinalInfProduto()