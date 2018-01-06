#!/usr/bin/python
import csv
import urllib
from bs4 import BeautifulSoup

def worko(fetch, x, y):

    if fetch[x].contents == []:
       return servFeat.append('NULL')

    else:
        work = fetch[x].contents[y]
        servFeat.append(work.strip())


def parseCivil():
    
    global servFeat

    nome = bs.find_all('td', {'class' : 'colunaValor'})
    work =  nome[0].contents[0]
    servFeat.append(work.strip())

    cpf = bs.find_all('td', {'class' : 'colunaValor'})
    work = cpf[1].contents[0]
    servFeat.append(work.strip())

    serv = bs.find_all('td', {'class' : 'colunaValor'})
    work = serv[2].contents[0]
    servFeat.append(work.strip())
    
    mat = bs.find_all('strong')
    work = mat[0].contents[0]
    servFeat.append(work.strip())

    cargo = bs.find_all('strong')
    work = cargo[1].contents[0]
    servFeat.append(work.strip())
    
    #orgao origem - lotacao

    uorg = bs.find_all('strong')
    work = uorg[7].contents[0]
    servFeat.append(work.strip())

    orgao = bs.find_all('strong')
    work = orgao[8].contents[0]
    servFeat.append(work.strip())

    orgaoS = bs.find_all('strong')
    work = orgaoS[9].contents[0]
    servFeat.append(work.strip())

    #local de exercicio
    
    uf = bs.find_all('strong')
    worko(uf, 11, 0)


    uorg = bs.find_all('strong')
    if uorg[12].contents == []:
        servFeat.append('null')
    else:    
        work = uorg[12].contents[0]
        servFeat.append(work.strip())

    orgao = bs.find_all('strong')
    work = orgao[13].contents[0]
    servFeat.append(work.strip())

    orgaoS = bs.find_all('strong')
    work = orgaoS[14].contents[0]
    servFeat.append(work.strip())
    
    # outras informacoes

    reg = bs.find_all('strong')
    work = reg[15].contents[0]
    servFeat.append(work.strip())
    
    status = bs.find_all('strong')
    work = status[16].contents[0]
    servFeat.append(work.strip())

    jorn = bs.find_all('strong')
    work = jorn[18].contents[0]
    servFeat.append(work.strip())

    return servFeat


c = csv.writer(open("servcivil.csv", "ab"))
c.writerow(["Nome","CPF","Servidor","Matricula","Cargo",
    "O. Origem - UORG","O. Origem - Orgao", "O. Origem - Orgao Superior", 
    "Local de Exercicio - UF", "Local de Exercicio - UORG", 
    "Local de Exercicio - Orgao","Local de Exercicio - Orgao Superior",
    "Regime Juridico", "Situacao Vinculo", "Jornada de Trabalho"
    ])


for idServ in range(1000002, 1000010):
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
            c.writerow(servFeat)
            print work.strip()
    
    else:
        pass
