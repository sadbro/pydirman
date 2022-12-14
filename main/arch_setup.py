#!/usr/bin/env python3

import subprocess as sp
from subprocess import getoutput
import sys
import os
from termcolor import colored
os.chdir('.')

require = ['termcolor', 'pip']
PATH = os.path.realpath('.')
# GET OS VERSION
os_details = sp.getoutput("cat /etc/[A-Za-z]*[_-][rv]e[lr]*")
if 'arch' in os_details.lower():
    OS_VERSION = 'arch'
    os_require = ['nodejs', 'jdk-openjdk']
elif 'debian' in os_details.lower():
    OS_VERSION = 'debian'
    os_require = ['nodejs', 'default-jdk']
else:
    print(colored("Unsupported GNU/Linux Distro", "red", attrs=['underlined', 'bold']))
    sys.exit(-1)

for package in require:
    if package in sys.modules:
        pass
    else:
        if OS_VERSION == 'arch':
            os.system('sudo pacman -S python-{} --noconfirm'.format(package))
        elif OS_VERSION == 'debian':
            os.system('sudo apt install python3-{}'.format(package))

# CHECK IF THE USER HAS THE OS_REQUIRE PACKAGES ALREADY INSTALLED ON THEIR SYSTEM
# Working for ARCH ONLY, 
if OS_VERSION == 'arch':
    print(colored('SEARCHING FOR PACKAGES...', 'yellow'))
    for package in os_require:
        result = sp.getoutput('pacman -Qe {}'.format(package))

    # PACKAGE MENU
    for i in range(len(os_require)):
        print(colored('[{}]: {}'.format(i, os_require[i]), "yellow"))
    req_packages = input(colored(f"\nEnter the index of the packages you want to install\ne.g. 0 1 2\n", "red", attrs=['bold']))

    print("Installing {} packages".format(len(req_packages)))
    for index in req_packages.strip().split():
        os.system('sudo pacman -S {} --noconfirm'.format(os_require[int(index)]))

elif OS_VERSION == 'debian':
    for os_package in os_require:
        os.system('sudo apt install {}'.format(os_package))

def fixer(cmd, ind):
    '''sets the file permission for cmd file to ind'''
    os.system('sudo chmod {} {}'.format(ind, cmd))

#docs = sorted(os.listdir(PATH))
#for doc in docs:
#    fixer(doc, 777)

if 'pydirman' in os.listdir('/bin/'):
    pass
else:
    os.system('cp ./pydirman /bin/')
   
os.system('cp ./pydirman /bin/')
os.system('cp ./reader.out /bin/')
os.system('cp ./.pydirman.commands /etc/')
fixer('/bin/pydirman', 777)
#fixer('/etc/pydirman.py', 777)
fixer('/bin/reader.out', 777)