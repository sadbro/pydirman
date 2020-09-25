#!/bin/python3

import os
import sys
from time import sleep
from termcolor import colored, cprint

global CUR_DIR, LS_DIR, CUR_PATH, CUR_FILE, SEARCH_DIR, SYS_DIR

SYS_DIR = []
for directory in os.listdir("/"):
    SYS_DIR.append(directory)

if len(sys.argv) > 1:
    if sys.argv[1] == "--help" or sys.argv[1] == "-h":
        cprint("\nPython Directory Management", "red", attrs=['bold', 'underline'])
        cprint("Usage: pydirman [directory]", "blue", attrs=['bold'])
        cprint("if no arg is specified, current working directory will be specified by default.\n", "blue", attrs=['bold'])
        cprint("-h/--help flag for this help menu\n", "blue", attrs=['bold'])
        sys.exit()
    else:
        try:
            os.chdir(sys.argv[1])
        except NotADirectoryError:
            cprint("\nEnter a Directory path only!!", "red", attrs=['bold'])
            sys.exit(1)
        except FileNotFoundError:
            cprint("Directory does not exist!!\n", "red", attrs=['bold'])
            sys.exit(1)
            
elif len(sys.argv):
    CUR_DIR = os.getcwd()

CUR_DIR = os.getcwd()
LS_DIR = sorted(os.listdir())
CUR_PATH = os.path.abspath(CUR_DIR)

def test(file):
    __file = file.split(".")
    file_type = __file[1]
    command = str(input("Enter command [exit|test|gedit] "))
    if command.lower() == "t":
        print("--------------------------------------------------------------------")
        if file_type == 'py':
            os.system("python3 {}".format(file))
        elif file_type == 'c' or file_type == 'cpp':
            os.system("g++ {} -o {}.out && ./{}.out".format(file, __file[0], __file[0]))
        print("--------------------------------------------------------------------")
        if file_type == 'out':
            print("Binary File detected.\n")
        test(file)

    elif command.lower() == "g":
        os.system("sudo gedit {} >/dev/null 2>&1".format(file))
        test(file)

    elif command.lower() == "e":
        os.system("clear")
        __display()
        __chdir(os.getcwd())

def __display():

    CUR_DIR = os.getcwd()
    LS_DIR = sorted(os.listdir())
    CUR_PATH = os.path.abspath(CUR_DIR)

    print(colored("\nPYTHON DIRECTORY MANAGEMENT\n", "red", attrs=['underline', 'bold']))
    print(colored("Directory", "yellow") +" | "+ colored("File", "white"))
    print("============================================================================")
    counter = 0
    for index,FI_FO in enumerate(LS_DIR):
        if os.path.isfile(FI_FO):
            print("[{}] ".format(index) + colored("{}".format(FI_FO), "white")) #color for file instance
            counter += 1
        elif os.path.isdir(FI_FO):
            print("[{}] ".format(index) + colored("{}/".format(FI_FO), "yellow")) #color for directory
            counter += 1

    print("============================================================================")
    print("TOTAL FILES/DIRECTORIES: "+ colored("{}".format(counter), "red", attrs=['bold']))
    print("YOUR CURRENT LOCATION: "+ colored("{}".format(CUR_PATH), "red", attrs=['bold']))
    print("============================================================================")
    print("[help] = "+ colored("[?]", 'red'))

def __chdir(CUR_DIR):

    CUR_DIR = os.getcwd()
    LS_DIR = sorted(os.listdir())
    SEARCH_DIR = []
    for item in LS_DIR:
        SEARCH_DIR.append(str(item.lower()))
    SOURCE_FILE_PATH = "/etc/pydirman.py"
        
    __all__ = [
    '?', 'help', 'editsource',
    'goto', 'previous', 'search',
    'update', 'terminal', 'exit', 'clear',
    'newfile', 'deletefile',
    'makedir', 'removedir',
    'build', 'execute', 'test'
    ]

    try:
        com = str(input(colored("\npydirman", "blue", attrs=['underline']) +colored(">", "blue"))).strip()
        if com.lower() == "g":

            try: 
                ask = input("Enter your index: ")
                if ask.isdigit():
                    ask = int(ask)

                    try:
                        if os.path.isdir(str(LS_DIR[ask])):
                            os.system("clear")
                            os.chdir(str(LS_DIR[ask]))
                            __display()
                            __chdir(LS_DIR[ask])

                        elif os.path.isfile(str(LS_DIR[ask])):
                            rp = colored('[p]', 'red')
                            rc = colored('[c]', 'red')
                            re = colored('[e]', 'red')
                            porr = str(input(colored("FILE=[{}]\n".format(str(LS_DIR[ask])), "white")+"{}rint/{}ancel/{}dit: ".format(rp, rc, re)))
                            CUR_FILE = str(LS_DIR[ask])

                            if porr.lower() == "p":
                                print(colored("\n" +"="*56 +"START"+ "="*56 +"\n", "red"))
                                os.system("reader.out {}".format(CUR_FILE))
                                print(colored("\n" +"="*57 +"END"+ "="*57+ "\n", "red"))
                                stat = str(input("[c]ontinue/[e]xit: "))

                                if stat.lower() == "c":
                                    __display()
                                    __chdir(CUR_DIR)

                                elif stat.lower() == "e":
                                    print(colored("See you soon!", "white"))
                                    sys.exit(0)
                                
                                else:
                                    print("Enter a valid command!")
                                    __chdir(os.getcwd())

                            elif porr.lower() == "c":
                                __chdir(os.getcwd())
                        
                            elif porr.lower() == "e":
                                os.system("sudo gedit {} >/dev/null 2>&1".format(CUR_FILE))
                                __chdir(os.getcwd())
                            
                            else:
                                print("Enter a valid command")
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

        elif com.lower() == "ed":
            os.system("sudo gedit {} >/dev/null 2>&1".format(SOURCE_FILE_PATH))
            __chdir(os.getcwd())

        elif com.lower() == "c":
            os.system("clear && pydirman {}".format(CUR_DIR))

        elif com.lower() == "test":
            CUR_DIR = os.getcwd()
            LS_DIR = sorted(os.listdir())
            file_index = int(input("Enter File index: "))
            file = LS_DIR[file_index]
            if os.path.isfile(file):
                os.system("clear")
                print("FILE -> {}\n".format(file))
                test(file)

            elif os.path.isdir(file):
                print("Enter index of files only !!")
            __chdir(CUR_DIR)

        elif com.lower() == "b":
            print("========================================================================")
            counter = 0
            for index,FI_FO in enumerate(LS_DIR):
                if os.path.isfile(FI_FO):
                    print("[{}] ".format(index) + colored("{}".format(FI_FO), "white")) #color for file instance
                    counter += 1
            
                #elif os.path.isdir(FI_FO):
                    #print("[{}] ".format(index) + colored("{}/".format(FI_FO), "yellow")) #color for directory
                    #counter += 1
            print("========================================================================")
            try:
                buildindex = int(input("Enter file index [build]: "))
                buildfile = LS_DIR[buildindex]
                build_dict = buildfile.split(".")
                buildname = str(build_dict[0])
                buildtype = str(build_dict[1])
                if buildtype == 'c':
                    os.system("gcc {} -o {}.out".format(buildfile, buildname))
                elif buildtype == 'cpp':
                    os.system("g++ {} -o {}.out".format(buildfile, buildname))
            except KeyboardInterrupt:
                print("File not built")
            except ValueError:
                print("Enter Correctly")
            except IndexError:
                print("Enter Correctly")
            
            __chdir(os.getcwd())

        elif com.lower() == "x":
            print("========================================================================")
            counter = 0
            for index,FI_FO in enumerate(LS_DIR):
                if os.path.isfile(FI_FO):
                    print("[{}] ".format(index) + colored("{}".format(FI_FO), "white")) #color for file instance
                    counter += 1
            
                #elif os.path.isdir(FI_FO):
                    #print("[{}] ".format(index) + colored("{}/".format(FI_FO), "yellow")) #color for directory
                    #counter += 1
            print("========================================================================")
            try:
                exeindex = int(input("Enter file index [execute]: "))
                exefile = LS_DIR[exeindex]
                exe_dict = exefile.split('.')
                exetype = str(exe_dict[1])
                if exetype == "out":
                    print("---------------------------------C{}--------------------------------")
                    os.system("./{}".format(exefile))
                elif exetype == "py":
                    print("--------------------------------PYTHON------------------------------")
                    os.system("python3 {}".format(exefile))
                print("\n--------------------------------------------------------------------")

            except KeyboardInterrupt:
                print("File not executed")
            except ValueError:
                print("Enter Correctly\n")
            except IndexError:
                print("Enter Correctly\n")
                
            __chdir(os.getcwd())

        elif (com.lower() == "?")or(com.lower() == "h"):
            print("\n[help]    = "+ colored("[?/h]", 'red') +"elp-"+ colored("[ed]", 'red') +"itsource")
            print("[walker]  = "+ colored("[g]", 'red') +"oto-" +colored("[p]", 'red') +"revious-"+ colored("[s]", 'red') +"earch")
            print("[utility] = "+ colored("[c]", 'red') +"lear-"+ colored("[t]", 'red') +"erminal-" +colored("[e]", 'red') +"xit-" +colored("[c]", 'red') +"lear")
            print("[writer]  = "+ colored("[n]", 'red') +"ewfile-" +colored("[d]", 'red') +"eletefile")
            print("[folder]  = "+ colored("[m]", 'red') +"akedir-" +colored("[r]", 'red') +"emovedir")
            print("[builder] = "+ colored("[b]", 'red') +"uild-e" +colored("[x]", 'red') +"ecute")
            __chdir(CUR_DIR)

        elif com.lower() == "p":
            os.system("clear")
            os.chdir("..")
            if os.getcwd() == CUR_DIR:
                cprint("\nEnd of the line, buddy!", "blue", attrs=['bold'])
                __chdir(CUR_DIR)
            else:
                CUR_DIR = os.getcwd()
                __display()
                __chdir(CUR_DIR)

        elif com.lower() == "s":
            search = str(input("\nEnter your search: ")).strip()
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
            os.system("qterminal -w {} >/dev/null 2>&1".format(termDir))
            __chdir(os.getcwd())
        
        elif com.lower() == "n":
            try:
                #filename = str(input("Enter file name [create]: "))
                #os.system("sudo gedit {} >/dev/null 2>&1".format(filename))
                #os.system("sudo chmod 777 {}".format(filename))
                os.system("sudo python3 /etc/txted.py >/dev/null 2>&1")
            except KeyboardInterrupt:
                print("File not created")
            
            __chdir(os.getcwd())
        
        elif com.lower() == "d":
            print("============================================================================================================================")
            counter = 0
            for index,FI_FO in enumerate(LS_DIR):
                if os.path.isfile(FI_FO):
                    print("[{}] ".format(index) + colored("{}".format(FI_FO), "white")) #color for file instance
                    counter += 1

                #elif os.path.isdir(FI_FO):
                    #print("[{}] ".format(index) + colored("{}/".format(FI_FO), "yellow")) #color for directory
                    #counter += 1
            print("============================================================================================================================")
            try:
                delfileindex = int(input("Enter file index [delete]: "))
                delfile = LS_DIR[delfileindex]
                os.system("sudo rm {}".format(delfile))
            except KeyboardInterrupt:
                print("File not deleted")
            except ValueError:
                print("Enter Correctly")
            except IndexError:
                print("Enter Correctly")
         
            __chdir(os.getcwd())

        elif com.lower() == "m":
            try:
                dirname_mk = str(input("Enter Directory name: "))
                os.system("mkdir {}".format(dirname_mk))
            except KeyboardInterrupt:
                print("Directory not created!")
            
            __chdir(os.getcwd)

        elif com.lower() == "r":
            print("============================================================================================================================")
            counter = 0
            for index,FI_FO in enumerate(LS_DIR):
                #if os.path.isfile(FI_FO):
                    #print("[{}] ".format(index) + colored("{}".format(FI_FO), "white")) #color for file instance
                    #counter += 1

                if os.path.isdir(FI_FO):
                    print("[{}] ".format(index) + colored("{}/".format(FI_FO), "yellow")) #color for directory
                    counter += 1
            print("============================================================================================================================")
            try:
                dirname_rm = str(input("Enter directory name: ")).strip()
                if dirname_rm in SYS_DIR:
                    print("You just tried to delete a system file!!")
                os.system("rmdir {}".format(dirname_rm))
            except KeyboardInterrupt:
                print("Directory not deleted")
            except ValueError:
                print("Enter Correctly")
            except IndexError:
                print("Enter Correctly")
            
            __chdir(os.getcwd())
        
        elif com.lower() in __all__:
            print("\nplease enter the the first letter [{}] only".format(com.lower()[0]))
            __chdir(os.getcwd())

        else:
           print("\nEnter a valid command!")
           __chdir(os.getcwd())

    except KeyboardInterrupt:
        print("\nKeyboard interrupt detected..Press e for exit")
        __chdir(os.getcwd)

__display()
__chdir(CUR_DIR)
