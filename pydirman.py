#!/bin/python3

import os
import sys
from time import sleep
from termcolor import colored, cprint

global CUR_DIR, LS_DIR, CUR_PATH, CUR_FILE, SEARCH_DIR

if len(sys.argv) > 1:
    if sys.argv[1] == "--help" or sys.argv[1] == "-h":
        cprint("\nPython Directory Management", "red", attrs=['bold', 'underline'])
        cprint("Usage: pydirman [directory]", "blue", attrs=['bold'])
        cprint("if no arg is specified, current working directory will be specified by default.\n", "blue", attrs=['bold'])
        cprint("-h/--help flag for this help menu\n", "blue", attrs=['bold'])
        sys.exit()
    else:
        try:
            os.chdir(str(sys.argv[1]))
        except NotADirectoryError:
            cprint("\nEnter a Directory path only!!", "red", attrs=['bold'])
            sys.exit(1)

elif len(sys.argv):
    CUR_DIR = os.getcwd()

CUR_DIR = os.getcwd()
LS_DIR = sorted(os.listdir())
CUR_PATH = os.path.abspath(CUR_DIR)

def __display():

    CUR_DIR = os.getcwd()
    LS_DIR = sorted(os.listdir())
    CUR_PATH = os.path.abspath(CUR_DIR)

    print(colored("\nPYTHON DIRECTORY MANAGEMENT\n", "red", attrs=['underline', 'bold']))
    print(colored("Directory", "yellow") +" | "+ colored("File", "white"))
    print("=====================================================================")
    counter = 0
    for index,FI_FO in enumerate(LS_DIR):
        if os.path.isfile(FI_FO):
            print("[{}] ".format(index) + colored("{}".format(FI_FO), "white")) #color for file instance
            counter += 1
        elif os.path.isdir(FI_FO):
            print("[{}] ".format(index) + colored("{}/".format(FI_FO), "yellow")) #color for directory
            counter += 1

    print("=====================================================================")
    print("TOTAL FILES/DIRECTORIES: "+ colored("{}".format(counter), "red", attrs=['bold']))
    print("YOUR CURRENT LOCATION: "+ colored("{}".format(CUR_PATH), "red", attrs=['bold']))
    print("=====================================================================")
    print("[walker]  = "+ colored("[c]", 'red') +"hoose-" +colored("[p]", 'red') +"revious-"+ colored("[s]", 'red') +"earch")
    print("[utility] = "+ colored("[m]", 'red') +"odern-"+ colored("[t]", 'red') +"erminal-" +colored("[e]", 'red') +"xit")
    print("[writer]  = "+ colored("[n]", 'red') +"ewfile-" +colored("[d]", 'red') +"eletefile")


def __chdir(CUR_DIR):

    CUR_DIR = os.getcwd()
    LS_DIR = sorted(os.listdir())
    SEARCH_DIR = []
    for item in LS_DIR:
        SEARCH_DIR.append(str(item.lower()))
        
    __all__ = ['choose', 'exit', 'previous', 'search', 'terminal', 'newfile', 'deletefile', 'modern']

    com = str(input(colored("\npydirman", "blue", attrs=['underline']) +colored(">", "blue"))).strip()
    if com.lower() == "c":

        try: 
            ask = input("Enter your index: ")
            if ask.isdigit():
                ask = int(ask)

                try:
                    if os.path.isdir(str(LS_DIR[ask])):
                        os.chdir(str(LS_DIR[ask]))
                        __display()
                        __chdir(LS_DIR[ask])

                    elif os.path.isfile(str(LS_DIR[ask])):
                        porr = str(input(colored("THIS IS A FILE! [p]rint/[r]emain/[e]dit:", "white", attrs=['underline']) +" "))
                        CUR_FILE = str(LS_DIR[ask])

                        if porr.lower() == "p":
                            print(colored("\n" +"="*56 +"START"+ "="*56 +"\n", "red"))
                            os.system("cat " +CUR_FILE)
                            print(colored("\n" +"="*57 +"END"+ "="*57+ "\n", "red"))
                            stat = str(input("[c]ontinue/[e]xit: "))

                            if stat.lower() == "c":
                                __display()
                                __chdir(CUR_DIR)

                            elif stat.lower() == "e":
                                print(colored("See you soon!", "white"))
                                sys.exit(0)

                        elif porr.lower() == "r":
                            __display()
                            __chdir(os.getcwd())
                        
                        elif porr.lower() == "e":
                            os.system("sudo gedit {} >/dev/null 2>&1".format(CUR_FILE))
                            __chdir(os.getcwd())
                
                except IndexError:
                   print("oops, you entered a wrong number.")
                   __chdir(os.getcwd())
                    
            elif ask.isalpha():
                print("Please enter index of the file :[")
                print("[HINT] if you can't find the index then you can find it by typing [s] ;]")
                __chdir(os.getcwd())
  

        except PermissionError:
            cprint("\nThis directory is off limits!! Are you root?? I don't think so. BACK OFF!\n".upper(), "red", attrs=['bold'])
            sleep(2) 
            __chdir(os.getcwd())

    elif com.lower() == "e":
        print(colored("See you soon!\n", "white"))
        sys.exit(0)

    elif com.lower() == "p":
        os.chdir("..")
        if os.getcwd() == CUR_DIR:
            cprint("\nEnd of the line, buddy!", "blue", attrs=['bold'])
            __chdir(CUR_DIR)
        else:
            CUR_DIR = os.getcwd()
            __display()
            __chdir(CUR_DIR)

    elif com.lower() == "s":
        search = str(input("\nEnter your search: "))
        #cacheDir = []
        #for obj in LS_DIR:
        #    if search in obj:
        #        cacheDir.append(obj)
                
        search = search.lower()
        if search in SEARCH_DIR:
            print("File/Folder found. " +colored("\nindex: [{}]".format(SEARCH_DIR.index(search)), "red", attrs=['bold']))
            if os.path.isfile(search):
                cprint("is a [FILE]", "red", attrs=['bold'])
            elif os.path.isdir(search):
                cprint("is a [DIRECTORY]", "red", attrs=['bold'])
        #    print(cacheDir)
            
        #elif len(cacheDir) > 1:
        #    print("Multiple instances found! Showing all")
        #    for inst in cacheDir:
        #        print("[{}] {}".format(SEARCH_DIR.index(inst), inst))
                
        else:
            print("Sorry. your results returned no results. maybe you didn't enter the correct name.")
        __chdir(CUR_DIR)
        
    elif com.lower() == "t":
        termDir = os.getcwd()
        os.system("qterminal -d -w {} >/dev/null 2>&1".format(termDir))
        __chdir(os.getcwd())
        
    elif com.lower() == "n":
        filename = str(input("Enter file name [create]: "))
        os.system("sudo gedit {}".format(filename))
        __chdir(os.getcwd())
        
    elif com.lower() == "d":
        print("=====================================================================")
        counter = 0
        for index,FI_FO in enumerate(LS_DIR):
            if os.path.isfile(FI_FO):
                print("[{}] ".format(index) + colored("{}".format(FI_FO), "white")) #color for file instance
                counter += 1
            
            #elif os.path.isdir(FI_FO):
                #print("[{}] ".format(index) + colored("{}/".format(FI_FO), "yellow")) #color for directory
                #counter += 1
        print("=====================================================================")
        delfile = str(input("Enter file name [delete]: "))
        os.system("sudo rm {}".format(delfile))
        __chdir(os.getcwd())
        
    elif com.lower() == "m":
        print("=====================================================================")
        counter = 0
        for index,FI_FO in enumerate(sorted(os.listdir(os.getcwd()))):
            if os.path.isfile(FI_FO):
                print("[{}] ".format(index) + colored("{}".format(FI_FO), "white")) #color for file instance
                counter += 1
            elif os.path.isdir(FI_FO):
                print("[{}] ".format(index) + colored("{}/".format(FI_FO), "yellow")) #color for directory
                counter += 1
        print("=====================================================================")
        __chdir(os.getcwd())
        
    elif com.lower() in __all__:
        print("\nplease enter the the first letter [{}] only".format(com.lower()[0]))
        __chdir(os.getcwd())

    else:
       print("\nEnter a valid command!")
       __chdir(os.getcwd())
       
__display()
__chdir(CUR_DIR)
