#!/bin/python

import sys
import os
os.chdir('.')

require = ['termcolor', 'pip', 'cmake']
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

def fixer(cmd, ind):
    os.system('sudo chmod {} {}'.format(ind, cmd))
    
for doc in docs:
    fixer(doc, 777)

if 'pydirman' in os.listdir('/bin/'):
    pass
else:
    os.system('cp ./pydirman /bin/')
   
os.system('cp ./pydirman.py /etc/')
os.system('cp ./reader.out /bin/')
os.system('cp ./txted.py /etc/')
fixer('/bin/pydirman', 777)
fixer('/etc/pydirman.py', 777)
fixer('/bin/reader.out', 777)
fixer('/etc/txted.py', 777)
