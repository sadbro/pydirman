#!/bin/python3

import sys
import os
os.chdir('.')

require = ['termcolor', 'pip']
os_require = ['nodejs', 'default-jdk']
PATH = os.path.realpath('.')
docs = sorted(os.listdir(PATH))

for package in require:
    if package in sys.modules:
        pass
    else:
        os.system('sudo apt install python3-{}'.format(package))

for os_package in os_require:
    os.system('sudo apt install {}'.format(os_package))

def fixer(cmd, ind):
    os.system('sudo chmod {} {}'.format(ind, cmd))

for doc in docs:
    fixer(doc, 777)

if 'pydirman' in os.listdir('/bin/'):
    pass
else:
    os.system('cp ./pydirman /bin/')

os.system('mkdir /etc/.pydirman')
os.system('cp ./pydirman.py /etc/')
os.system('cp ./reader.out /bin/')
os.system('cp ./commands.yaml /etc/.pydirman')
fixer('/bin/pydirman', 777)
fixer('/etc/pydirman.py', 777)
fixer('/bin/reader.out', 777)
