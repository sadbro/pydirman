#!/bin/python3

import sys
import os
os.chdir('.')

require = ['termcolor', 'pip']
#os_require = ['nodejs npm', 'jdk-openjdk']
PATH = os.path.realpath('.')
docs = sorted(os.listdir(PATH))

for package in require:
    if package in sys.modules:
        pass
    else:
        os.system('sudo pacman -S python-{} --noconfirm'.format(package))

#for os_package in os_require:
#    os.system('sudo pacman -S {}'.format(os_package))

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
os.system('cp ./.pydirman.commands /etc/')
fixer('/bin/pydirman', 777)
fixer('/etc/pydirman.py', 777)
fixer('/bin/reader.out', 777)
