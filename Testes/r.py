import requests, xlrd, scrapy
from s import coletaDados

def xls_parser(arquivo):
    tabela = xlrd.open_workbook(arquivo).sheet_by_index(0)
    qtd_linhas = tabela.nrows
    linhas = []
    for i in range(1, qtd_linhas):
        linhas.append(
            {
                'prgcod': str(tabela.row(i)[0].value).replace('.0',''),
                'co_no_uasg': str(tabela.row(i)[1].value).replace('.0',''),
            }
        )
    return linhas


if __name__ == "__main__":
    arquivo = '/Users/JOSÉVICTORTEIXEIRADA/Documents/Projetos/DevTeste/Testes/Pregao_UASG.xls'
    ld = xls_parser(arquivo)
    url = 'http://comprasnet.gov.br/livre/pregao/termojulg.asp?prgcod=342018&Acao=A&co_no_uasg=70027'
    for i in range(0,len(ld)):
        aux = url.replace('prgcod=342018', 'prgcod='+ld[i]['prgcod']).replace('co_no_uasg=70027', 'co_no_uasg='+ld[i]['co_no_uasg'])
        print(aux)
        print(coletaDados(aux))
