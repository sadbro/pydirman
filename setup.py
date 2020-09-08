#!/bin/python

import sys
import os

require = ['termcolor', 'pip']
os_require = ['qterminal', 'gedit', 'gcc', 'g++']
PATH = os.path.realpath('.')
docs = sorted(os.listdir(PATH))

for package in require:
    if package in sys.modules:
        pass
    else:
        os.system('sudo apt install python3-{} >/dev/null 2>&1'.format(package))

for os_package in os_require:
    os.system('sudo apt install {} -i >/dev/null 2>&1'.format(os_package))

def fixer(cmd):
    os.system('sudo chmod 777 {}'.format(cmd))
    
for doc in docs:
    fixer(doc)

if 'pydirman' in os.listdir('/bin/'):
    pass
else:
    os.system('cp {}/{} /bin/'.format(PATH, 'pydirman'))
   
os.system('cp {}/pydirman.py /etc/'.format(PATH))
os.chdir('/bin/')
fixer('pydirman')
