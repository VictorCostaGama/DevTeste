# -*- coding: utf-8 -*-
from selenium import webdriver

class InfProduto(object):
    def Config(self,url,ind,titulo):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = url
        self.verificationErrors = []
        self.accept_next_alert = True
        self.id = ind
        self.nome = titulo
        self.lista = []
        self.dic = []

    def RunInfProduto(self):
        driver = self.driver
        driver.get(self.base_url)
        material = driver.find_element_by_class_name('x-description__container')
        self.lista.append(material.text)
        self.lista = self.lista[0].split('\n')
        lg = {}
        l1 = {}
        l2 = {}

        lista = self.lista

        for i in range(0,len(lista)):
            if i < lista.index('Dimensões'):
                if i == 0:
                    aux = lista[i]
                else:
                    if i == 1:
                        lg[lista[i]] = ''
                        a = lista[i]
                    else:
                        if lg[a] == '':
                            lg[a] = lista[i]
                        else:
                            lg[lista[i]] = ''
                            a = lista[i]
            else:
                if i == lista.index('Dimensões'):
                    iaux = lista[i]
                    c = i+1
                else:
                    if i == c:
                        l1[lista[i]] = ''
                        b = lista[i]
                    else:
                        if l1[b] == '':
                            l1[b] = lista[i]
                        else:
                            l1[lista[i]] = ''
                            b = lista[i]

        l2[aux] = lg
        l2[iaux] = l1

        print(l2)
        print('\n\n')
                
    def FinalInfProduto(self):
        self.driver.quit()