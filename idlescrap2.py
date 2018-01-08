#!/usr/bin/python
#!-*- coding:utf-8 -*-

import csv
import urllib
from bs4 import BeautifulSoup

def stripWork(fetch, x, y):
#    try:    
        if fetch[x].contents == []:
            return servFeat.append('(vazio)')

        else:
            work = fetch[x].contents[y]
            servFeat.append(work.strip().encode('utf-8'))
#    except:
#        servFeat.append('(nao informado)')

def parseCivil():
    
    global servFeat

    srch1 = bs.find_all('td', {'class' : 'colunaValor'})
    stripWork(srch1, 0, 0) #nome
    stripWork(srch1, 1, 0) #cpf
    stripWork(srch1, 2, 0) #servidor
    
    srch2 = bs.find_all('strong')
    stripWork(srch2, 0, 0) #matricula
    stripWork(srch2, 1, 0) #cargo
    stripWork(srch2, 7, 0) # o. origem - uorg 
    stripWork(srch2, 8, 0) # o. origem - orgao
    stripWork(srch2, 9, 0) # o.orgiem - orgao superior
    stripWork(srch2, 11, 0) # l. ex - uf
    stripWork(srch2, 12, 0) # l. ex - uorg
    stripWork(srch2, 13, 0) # l. ex - orgao
    stripWork(srch2, 14, 0) # l. ex - orgao superior
    stripWork(srch2, 15, 0) # regime
    stripWork(srch2, 16, 0) # status
    stripWork(srch2, 18, 0) # jornada

    srch3 = bs2.find_all('td', {'class' : 'colunaValor'})
    srch4 = bs2.find_all('td', {'colspan' : '3'})
    try:  
        d = srch4[9].contents[0].split(' ')
        e = srch4[5].contents[0].split(' ')
        f = srch4[7].contents[0].split(' ')
        
        if d[0] == 'Demais': 
            stripWork(srch3, 7, 0) # remuneracao basica 
            stripWork(srch3, 21, 0) # remuneracao basica 

        elif e[1] == 'eventual':
            stripWork(srch3, 7, 0) # remuneracao basica 
            stripWork(srch3, 18, 0) # rem. total apos deducoes
        
        elif f[0] == 'Demais':
            stripWork(srch3, 7, 0) # remuneracao basica 
            stripWork(srch3, 16, 0) # rem. total apos deducoes
        
        else:
            stripWork(srch3, 7, 0) # remuneracao basica 
            stripWork(srch3, 13, 0) # rem. total apos deducoes
  
    except:
        try:    
            stripWork(srch3, 7, 0) # remuneracao basica 
            stripWork(srch3, 13, 0) # rem. total apos deducoes
        except:
            servFeat.append('(nao informado)')
            servFeat.append('(nao informado)')
    
    return servFeat


def parseConf():
    global servFeat
    
    srch1 = bs.find_all('td', {'class' : 'colunaValor'})
    stripWork(srch1, 0, 0) #nome
    stripWork(srch1, 1, 0) #cpf
    stripWork(srch1, 2, 0) #servidor
    
    srch2 = bs.find_all('strong')
    stripWork(srch2, 26, 0) #matricula
    stripWork(srch2, 27, 0) #cargo
    stripWork(srch2, 33, 0) # o. origem - uorg 
    stripWork(srch2, 34, 0) # o. origem - orgao
    stripWork(srch2, 35, 0) # o.orgiem - orgao superior
    
    stripWork(srch2, 37, 0) # l. ex - uf
    stripWork(srch2, 38, 0) # l. ex - uorg
    stripWork(srch2, 39, 0) # l. ex - orgao
    stripWork(srch2, 40, 0) # l. ex - orgao superior
    
    stripWork(srch2, 41, 0) # regime
    stripWork(srch2, 42, 0) # status
    stripWork(srch2, 44, 0) # jornada
    srch3 = bs2.find_all('td', {'class' : 'colunaValor'})
    stripWork(srch3, 7, 0) # remuneracao basica 
    stripWork(srch3, 18, 0) # rem. total apos deducoes
    
    return servFeat



def parseMil():

    global servFeat

    srch1 = bs.find_all('td', {'class' : 'colunaValor'})
    stripWork(srch1, 0, 0)  #nome
    stripWork(srch1, 1, 0)  #cpf
    stripWork(srch1, 2, 0)  #servidor

    srch2 = bs.find_all('strong')
    stripWork(srch2, 0, 0)  #matricula
    stripWork(srch2, 1, 0)  #posto 
    stripWork(srch2, 2, 0)  #orgao
    stripWork(srch2, 3, 0)  #o.superior
    stripWork(srch2, 4, 0)  #regime
    stripWork(srch2, 5, 0)  #status
    stripWork(srch2, 7, 0)  #jornada

    srch3 = bs2.find_all('td', {'class' : 'colunaValor'})
    stripWork(srch3, 7, 0) # remuneracao basica 
    stripWork(srch3, 15, 0) # rem. total apos deducoes
    
    return servFeat

def parseContra():
    global servFeat
    srch1 = bs.find_all('td', {'class' : 'colunaValor'})
    stripWork(srch1, 0, 0)  #nome
    stripWork(srch1, 1, 0)  #cpf
    stripWork(srch1, 2, 0)  #servidor
    
    srch2 = bs.find_all('strong')
    stripWork(srch2, 0, 0) #matricula
    stripWork(srch2, 2, 0) # o. origem - uorg 
    stripWork(srch2, 3, 0) # o. origem - orgao
    stripWork(srch2, 4, 0) # o.orgiem - orgao superior
    
    servFeat.append("(nao informado)") 
    servFeat.append("(nao informado)")
    servFeat.append("(nao informado)") 
    servFeat.append("(nao informado)")
    
    stripWork(srch2, 5, 0) # regime
    stripWork(srch2, 6, 0) # status
    stripWork(srch2, 8, 0) # jornada
    
    srch3 = bs2.find_all('td', {'class' : 'colunaValor'})
    try:
        stripWork(srch3, 7, 0) # remuneracao basica 
        stripWork(srch3, 18, 0) # rem. total apos deducoes
    except:
        servFeat.append('(nao informado)')
        servFeat.append('(nao informado)')

    return servFeat

c = csv.writer(open("servcivil.csv", "ab"))
cm = csv.writer(open("servMilitar.csv", "ab"))
c.writerow([
    "idServ","Nome","CPF","Servidor","Matricula","Cargo",
    "O. Origem - UORG","O. Origem - Orgao", "O. Origem - Orgao Superior", 
    "Local de Exercicio - UF", "Local de Exercicio - UORG", 
    "Local de Exercicio - Orgao","Local de Exercicio - Orgao Superior",
    "Regime Juridico", "Situacao Vinculo", "Jornada de Trabalhoi",
    "Remuneracao Basica", "Rem. Total Apos Reducoes"
    ])

cm.writerow([
   "idServ","Nome","CPF","Servidor","Matricula","Posto - Graduacao",
   "Orgao","Orgao Superior","Regime Juridico","Situacao Vinculo",
   "Jornada de Trabalho"
    ])

for idServ in range(1000000, 1000070):
    servFeat = []
    idServ = str(idServ)
    servFeat = [idServ]
    #print idServ
    resp = urllib.urlopen('http://www.portaltransparencia.gov.br/servidores/Servidor-DetalhaServidor.asp?IdServidor=' + idServ)
    resp2 = urllib.urlopen('http://www.portaltransparencia.gov.br/servidores/Servidor-DetalhaRemuneracao.asp?Op=1&IdServidor=' + idServ + '&bInformacaoFinanceira=True')
    if resp.code == 200:
        html = resp.read()
        html2 = resp2.read()
        bs = BeautifulSoup(html, 'lxml')
        bs2 = BeautifulSoup(html2, 'lxml')
        serv = bs.find_all('td', {'class': 'colunaValor'})
        cargo = bs.find_all('strong')
        work = serv[2].contents[0].strip()
        name =  serv[0].contents[0].strip() 
        print '[+] GOT - idServ: {} | {} | {}'.format(idServ, name, work)
        
        if work == 'Civil':

            if cargo[1].contents == []:
                try:
                    parseConf()
                except:
                    parseContra()
            else:
                parseCivil()

            c.writerow(servFeat)
           # print work.strip()
        
        else: 
            parseMil()
            cm.writerow(servFeat)

    else:
        pass
