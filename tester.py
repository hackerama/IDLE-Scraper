#!/usr/bin/python

import urllib
from bs4 import BeautifulSoup 
import sys

resp = urllib.urlopen('http://www.portaldatransparencia.gov.br/servidores/Servidor-DetalhaServidor.asp?IdServidor=1000067')
html = resp.read()
bs = BeautifulSoup(html, 'lxml')
try:
    cat = bs.find_all(sys.argv[1], {sys.argv[2] : sys.argv[3]})
except: 
    cat = bs.find_all(sys.argv[1])

i = 0
for item in cat:
    print '[{}] {}'.format(i, item)
    i += 1



