#!/usr/bin/python

import urllib
from bs4 import BeautifulSoup 
import sys
id = sys.argv[1]
resp = urllib.urlopen('http://www.portaldatransparencia.gov.br/servidores/Servidor-DetalhaServidor.asp?IdServidor='+id)
html = resp.read()
bs = BeautifulSoup(html, 'lxml')
try:
    cat = bs.find_all(sys.argv[2], {sys.argv[3] : sys.argv[4]})
except: 
    cat = bs.find_all(sys.argv[2])

i = 0
for item in cat:
    print '[{}] {}'.format(i, item)
    i += 1



