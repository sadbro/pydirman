#!/bin/python

import sys
import os

require = ['termcolor', 'pip']
PATH = os.path.realpath('.')
docs = sorted(os.listdir(PATH))

for package in require:
    if package in sys.modules:
        pass
    else:
        os.system('sudo apt install python3-{}'.format(package))

def fixer(cmd):
    os.system('sudo chmod 777 {}'.format(cmd))
    
for doc in docs:
    fixer(doc)

if 'pydirman' in os.listdir('/bin/'):
    pass
else:
    os.system('cp {}/{} /bin/'.format(PATH, 'pydirman'))
   
os.chdir('/bin/')
fixer('pydirman')
