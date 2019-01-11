import requests, scrapy

def coletaDados(url):
    
    response = requests.get(url)
    sel = scrapy.selector
    select = sel.Selector(response)
    li = []
    try:
        tab = select.xpath('//tr//td//text()').extract()
    
        for i in range(0,len(tab)):
            tab[i] = tab[i].replace('\n','').replace('\t','').replace('  ','').replace(': R$','').strip().rstrip(":").lstrip(', ')
            if tab[i] == ' ':
                tab[i] = tab[i].replace(' ','')
            elif len(tab[i] ) != 0:
                li.append(tab[i])

        #Removendo lixo da lista e estrurando
        del(li[0:4])

        for x in range(0,2):
            del(li[-1])

        a = li.count('e a quantidade de')

        for b in range(0, a):
            b = li.index('e a quantidade de')
            del(li[b:b+4])

        for x in range(0,len(li)):
            if 'Fornecedor' in li[x]:
                li[x] = li[x].replace('. ','\n').replace(': ','\n').replace(', ','\n').replace('Melhor lance ','Melhor lance\n').replace('Fornecedor:','Fornecedor\n').replace('CNPJ/CPF:','CNPJ/CPF\n').split('\n')
            elif ',' in li[x]:
                if 'R$' not in li[x]:
                    aux = 'R$ ' + str(li[x])
                li[x] = aux
        return li
    except:
        pass