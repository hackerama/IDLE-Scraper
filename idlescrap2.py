#!/usr/bin/python
import csv
import urllib
from bs4 import BeautifulSoup

def stripWork(fetch, x, y):

    if fetch[x].contents == []:
       return servFeat.append('NULL')

    else:
        work = fetch[x].contents[y]
        servFeat.append(work.strip())


def parseCivil():
    
    global servFeat

    nome = bs.find_all('td', {'class' : 'colunaValor'})
    stripWork(nome, 0, 0)

    cpf = bs.find_all('td', {'class' : 'colunaValor'})
    stripWork(cpf, 1, 0)

    serv = bs.find_all('td', {'class' : 'colunaValor'})
    stripWork(serv, 2, 0)
    
    mat = bs.find_all('strong')
    stripWork(mat, 0, 0)

    cargo = bs.find_all('strong')
    stripWork(cargo, 1, 0)
    
    #orgao origem - lotacao

    uorg = bs.find_all('strong')
    stripWork(uorg, 7, 0)

    orgao = bs.find_all('strong')
    stripWork(orgao, 8, 0)

    orgaoS = bs.find_all('strong')
    stripWork(orgaoS, 9, 0)

    #local de exercicio
    
    uf = bs.find_all('strong')
    stripWork(uf, 11, 0)

    uorgx = bs.find_all('strong')
    stripWork(uorgx, 12, 0)

    orgaox = bs.find_all('strong')
    stripWork(orgaox, 13, 0)


    orgaoSx = bs.find_all('strong')
    stripWork(orgaoSx, 14, 0)
    
    # outras informacoes

    reg = bs.find_all('strong')
    stripWork(reg, 15, 0)
    
    status = bs.find_all('strong')
    stripWork(status, 16, 0)


    jorn = bs.find_all('strong')
    stripWork(jorn, 18, 0)

    return servFeat


c = csv.writer(open("servcivil.csv", "ab"))
c.writerow([
    "Nome","CPF","Servidor","Matricula","Cargo","O. Origem - UORG",
    "O. Origem - Orgao", "O. Origem - Orgao Superior", 
    "Local de Exercicio - UF", "Local de Exercicio - UORG", 
    "Local de Exercicio - Orgao","Local de Exercicio - Orgao Superior",
    "Regime Juridico", "Situacao Vinculo", "Jornada de Trabalho"
    ])


for idServ in range(1000002, 1000020):
    servFeat = []
    idServ = str(idServ)
    print idServ
    resp = urllib.urlopen('http://www.portaltransparencia.gov.br/servidores/Servidor-DetalhaServidor.asp?IdServidor=' + idServ)
    resp2 = urllib.urlopen('http://www.portaltransparencia.gov.br/servidores/Servidor-DetalhaRemuneracao.asp?Op=1&IdServidor=' + idServ + '&bInformacaoFinanceira=True')
    if resp.code == 200:
        html = resp.read()
        bs = BeautifulSoup(html, 'lxml')
        print idServ, resp.code
        serv = bs.find_all('td', {'class': 'colunaValor'})
        work = serv[2].contents[0]
        if work.strip() == 'Civil':
            parseCivil()
            try:
                c.writerow(servFeat)
            except UnicodeEncodeError:
                c.writerow("ERROR")  #gambiarra
                continue
            print work.strip()
    
    else:
        pass
