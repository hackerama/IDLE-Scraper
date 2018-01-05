#/usr/bin/python

from bs4 import BeautifulSoup
import urllib

idServ = '1527319'
resp = urllib.urlopen('http://www.portaltransparencia.gov.br/servidores/Servidor-DetalhaServidor.asp?IdServidor=' + idServ)
html = resp.read()
bs = BeautifulSoup(html, 'lxml')

print '\n[INICIANDO BUSCA POR SERVIDOR...]'
print '[+] HTML Status Code: {} '.format(resp.code)

print '\n[+] DADOS PESSOAIS'
nome = bs.find_all('td', {'class' : 'colunaValor'})
work =  nome[0].contents[0]
print 'Nome: {}'.format(work.strip())

cpf = bs.find_all('td', {'class' : 'colunaValor'})
work = cpf[1].contents[0]
print 'CPF: {}'.format(work.strip())

serv = bs.find_all('td', {'class' : 'colunaValor'})
work =  serv[2].contents[0]
print 'Servidor: {}'.format(work.strip())




mat  = bs.find_all('strong')
work =  mat[0].contents[0]
print 'Matricula: {}'.format(work.strip())

cargo = bs.find_all('strong')
work = cargo[1].contents[0]
print 'Cargo: {}'.format(work.strip())


print'\n[+] ORGAO ORIGEM - LOTACAO'

uorg = bs.find_all('strong')
work = uorg[7].contents[0]
print 'UORG: {}'.format(work.strip()) 

orgao = bs.find_all('strong')
work = orgao[8].contents[0]
print 'Orgao {}'.format(work.strip())

orgaoS = bs.find_all('strong')
work = orgaoS[9].contents[0]
print 'Orgao Superior: {}'.format(work.strip())

print '\n[+] LOCAL DE EXERCICIO'

uf = bs.find_all('strong')
work = uf[11].contents[0]
print 'UF: {}'.format(work.strip())

uorgEx = bs.find_all('strong')
work = uorgEx[12].contents[0]
print 'UORG: {}'.format(work.strip())

orgao = bs.find_all('strong')
work = orgao[13].contents[0]
print 'Orgao {}'.format(work.strip())

orgaoS = bs.find_all('strong')
work = orgaoS[14].contents[0]
print 'Orgao Superior: {}'.format(work.strip())

print '\n[+] OUTRAS INFORMACOES'

reg = bs.find_all('strong')
work = reg[15].contents[0]
print 'Regime Juridico: {}'.format(work.strip())

status = bs.find_all('strong')
work = status[16].contents[0]
print 'Situacao Vinculo {}'.format(work.strip())

jorn  = bs.find_all('strong')
work = jorn[18].contents[0]
print 'Jornada de Trabalho: {}'.format(work.strip()) 
