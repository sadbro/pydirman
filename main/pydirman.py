#!/bin/python3



        #######    ##       ##   ##########     ########   #######    ##        ###         ###         ###     ##
        ##    ##    ##     ##    ##      ###       ##      ##    ##   ####     ####        ## ##        ####    ##
        ##    ##     ##  ##      ##       ##       ##      ##    ##   ## ##   ## ##       ##   ##       ## ##   ##
        #######        ##        ##       ##       ##      #######    ##   ###   ##      ##     ##      ##  ##  ##
        ##             ##        ##       ##       ##      ## ##      ##         ##     ###########     ##   ## ##
        ##             ##        ##      ###       ##      ##  ##     ##         ##    ##         ##    ##    ####
        ##             ##        ##########     ########   ##   ###   ##         ##   ##           ##   ##     ###



import os
import sys
import socket
from time import sleep
from termcolor import colored, cprint

global CUR_DIR, LS_DIR, CUR_PATH, CUR_FILE, SEARCH_DIR, SYS_DIR, TempC, TempCpp, COL
TempC = "#include <stdio.h>\n\nint main(){\n\n    return 0;\n}"
TempCpp = "#include <iostream>\n\nusing namespace std;\nint main(){\n\n    return 0;\n}"
COL, LINE = os.get_terminal_size()

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
            NDIR= sys.argv[1]
            #os.system("mkdir {} && pydirman {}".format(NDIR, NDIR))
            cprint("Directory does not exist!!\n", "red", attrs=['bold'])
            sys.exit(0)

elif len(sys.argv):
    CUR_DIR = os.getcwd()

CUR_DIR = os.getcwd()
LS_DIR = sorted(os.listdir())
CUR_PATH = os.path.abspath(CUR_DIR)

def test(file):
    __file = file.split(".")
    filename, file_type = __file
    command = str(input("Enter command [exit|test|nano] "))
    if command.lower() == "t":
        print("-"*COL)

        if file_type == 'py':
            os.system("python3 {}".format(file))

        elif file_type == 'c':
            os.system("gcc {} -o {}.out && ./{}.out".format(file, filename, filename))

        elif file_type == 'cpp':
            os.system("g++ {} -o {}.out && ./{}.out".format(file, filename, filename))

        elif file_type == 'js':
            os.system("node {}".format(file))

        elif file_type == 'java':
            os.system("javac {} && java {}".format(file, filename))

        elif file_type == 'out':
            os.system("./{}".format(file))

        elif file_type == 'class':
            os.system("java {}".format(filename))

        print("-"*COL)
        test(file)

    elif command.lower() == "n":
        os.system("sudo nano {}".format(file))
        test(file)

    elif command.lower() == "e":
        __display()
        __chdir(os.getcwd())

def __display():

    global COL

    IP_ADDRESS= socket.gethostbyname(socket.gethostname())
    CUR_DIR = os.getcwd()
    LS_DIR = sorted(os.listdir())
    CUR_PATH = os.path.abspath(CUR_DIR)

    print(colored("\nPYTHON DIRECTORY MANAGEMENT\n", "red", attrs=['underline', 'bold']))
    print(colored("Directory", "yellow") +" | "+ colored("File", "white"))
    print("="*COL)
    counter = 0
    for index,FI_FO in enumerate(LS_DIR):
        if os.path.isfile(FI_FO):
            print("[{}] ".format(index) + colored("{}".format(FI_FO), "white")) #color for file instance
            counter += 1
        elif os.path.isdir(FI_FO):
            print("[{}] ".format(index) + colored("{}/".format(FI_FO), "yellow")) #color for directory
            counter += 1

    print("="*COL)
    print("TOTAL FILES/DIRECTORIES: "+ colored("{}".format(counter), "red", attrs=['bold']))
    print("YOUR CURRENT LOCATION: "+ colored("{}".format(CUR_PATH), "red", attrs=['bold']))
    print("="*COL)
    print("[help] = "+ colored("[?]", 'red'))

def __chdir(CUR_DIR):

    global TempC, TempCpp, COL
    CUR_DIR = os.getcwd()
    LS_DIR = sorted(os.listdir())
    SEARCH_DIR = []
    for item in LS_DIR:
        SEARCH_DIR.append(str(item.lower()))
    SOURCE_FILE_PATH = os.path.abspath(sys.argv[0])

    __all__ = [
    '?', 'help', 'editsource', 'usb', 'open'
    'goto', 'previous', 'search',
    'update', 'terminal', 'exit', 'clear',
    'newfile', 'deletefile', 'searchfile',
    'makedir', 'removedir', 'test'
    ]

    try:
        com = str(input(colored("\npydirman", "blue", attrs=['underline']) +colored(">", "blue"))).strip()
        if com.lower() == "g": #  GOTO COMMAND

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
                            porr = str(input(colored("FILE=[{}]\n".format(str(LS_DIR[ask])), "white")+"{}rint/{}ancel/{}dit: ".format(rp,rc,re)))
                            CUR_FILE = str(LS_DIR[ask])

                            if porr.lower() == "p":
                                print(colored("\n" +"="*((COL-5)//2) +"START"+ "="*((COL-5)//2) +"\n", "red"))
                                os.system("reader.out {}".format(CUR_FILE))
                                print(colored("\n" +"="*((COL-3)//2) +"END"+ "="*((COL-3)//2)+ "\n", "red"))
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
                                os.system("sudo nano {}".format(CUR_FILE))
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

        elif com.lower() == "e": #  EXIT COMMAND
            print(colored("See you soon!\n", "white"))
            sys.exit(0)

        elif com.lower() == "o": #  OPEN-IN-GUI COMMAND
            os.system("nautilus {}".format(CUR_DIR))
            __chdir(CUR_DIR)

        elif com.lower() == "u": #  USB COMMAND
            try:
                CUR_DIR= "/media/{}".format(os.environ["SUDO_USER"])
            except KeyError:
                CUR_DIR= "/media/{}".format(os.environ["USER"])

            os.system("clear")
            os.chdir(CUR_DIR)
            __display()
            __chdir(CUR_DIR)

        elif com.lower() == "ed":
            os.system("sudo nano {} ".format(SOURCE_FILE_PATH))
            __chdir(os.getcwd())

        elif com.lower() == "c": #  CLEAR/REFRESH COMMAND
            os.system("clear && cd {}".format(CUR_DIR))
            __display()
            __chdir(CUR_DIR)

        elif com.lower() == "test": #  CODE-TESTING COMMAND
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

        elif com.startswith("s "): #  SEARCH EXTENSION COMMAND
            ext= com[2:]
            files= []
            total_files_folders= len(os.listdir(os.getcwd()))
            print("-"*COL)
            for file in os.listdir(os.getcwd()):
                if file.endswith(ext):
                    files.append(file)
            print(colored(f"OBJECTS SEARCHED: {total_files_folders}, OBJECTS FOUND: {len(files)}", "red", attrs=["bold"]))
            print("-"*COL)
            for file in files:
                print(f"{file}")
            print("-"*COL)
            __chdir(os.getcwd())

        elif (com.lower() == "?")or(com.lower() == "h"): #  HELP COMMAND
            print("\n[help]      = "+ colored("[?/h]", 'red') +"elp-"+ colored("[ed]", 'red') +"itsource")
            print("[walker]    = "+ colored("[g]", 'red') +"oto-" +colored("[p]", 'red') +"revious-"+ colored("[s]", 'red') +"earch")
            print("[utility]   = "+ colored("[c]", 'red') +"lear-"+ colored("[t]", 'red') +"erminal-" +colored("[e]", 'red') +"xit-" +colored("[c]", 'red') +"lear")
            print("[writer]    = "+ colored("[n]", 'red') +"ewfile-" +colored("[d]", 'red') +"eletefile")
            print("[folder]    = "+ colored("[m]", 'red') +"akedir-" +colored("[r]", 'red') +"emovedir")
            print("[misc]      = "+ colored("[u]", 'red') +"sb-"+ colored("[o]", 'red') +"pen")
            __chdir(CUR_DIR)

        elif com.lower() == "p": #  PREVIOUS COMMAND
            os.system("clear")
            os.chdir("..")
            if os.getcwd() == CUR_DIR:
                cprint("\nEnd of the line, buddy!", "blue", attrs=['bold'])
                __chdir(CUR_DIR)
            else:
                CUR_DIR = os.getcwd()
                __display()
                __chdir(CUR_DIR)

        elif com.lower() == "s": #  SEARCH COMMAND
            search = str(input("\nEnter your search: ")).strip()
            search = search.lower()
            if search in SEARCH_DIR:
                print("File/Folder found. " +colored("\nindex: [{}]".format(SEARCH_DIR.index(search)), "red", attrs=['bold']))
                if os.path.isfile(search):
                    cprint("is a [FILE]", "red", attrs=['bold'])
                elif os.path.isdir(search):
                    cprint("is a [DIRECTORY]", "red", attrs=['bold'])

            else:
                print("Sorry. your results returned no results. maybe you didn't enter the correct name.")
            __chdir(CUR_DIR)

        elif com.startswith("t"): #  TERMINAL COMMAND
            cmd= com[2:]
            print("-"*COL + "\nExecuting [{}]...\n".format(colored(cmd, "green")) + "-"*COL)
            os.system(cmd)
            print("-"*COL)
            __chdir(os.getcwd())

        elif com.lower() == "n": #  NEW-FILE COMMAND
            try:
                filename = str(input("Enter file name [create]: "))
                os.system("touch {}".format(filename))
                file_name ,file_ext = filename.split('.')
                TempJava= "public class "+ file_name +" {\n\n    public static void main(String[] args){\n\n\n    }\n\n}\n"

                if file_ext == 'c':
                    os.system('echo "{}" > {}'.format(TempC, filename))

                elif file_ext == 'cpp':
                    os.system('echo "{}" > {}'.format(TempCpp, filename))

                elif file_ext == 'java':
                    os.system('echo "{}" > {}'.format(TempJava, filename))

                os.system("sudo nano {}".format(filename))
                os.system("sudo chmod 777 {}".format(filename))

            except:
                print("File not created")

            os.system("clear && pydirman {}".format(CUR_DIR))

        elif com.lower() == "d": #  DELETE-FILE COMMAND
            print("="*COL)
            counter = 0
            for index,FI_FO in enumerate(LS_DIR):
                if os.path.isfile(FI_FO):
                    print("[{}] ".format(index) + colored("{}".format(FI_FO), "white")) #color for file instance
                    counter += 1

            print("="*COL)
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

        elif com.lower() == "m": #  NEW-DIRECTORY COMMAND
            try:
                dirname_mk = str(input("Enter Directory name: "))
                os.system("mkdir {}".format(dirname_mk))
            except KeyboardInterrupt:
                print("Directory not created!")

            __chdir(os.getcwd)

        elif com.lower() == "r": #  DELETE-DIRECTORY COMMAND
            print("="*COL)
            counter = 0
            for index,FI_FO in enumerate(LS_DIR):

                if os.path.isdir(FI_FO):
                    print("[{}] ".format(index) + colored("{}/".format(FI_FO), "yellow")) #color for directory
                    counter += 1
            print("="*COL)
            try:
                dirname_rm = str(input("Enter directory name: ")).strip()
                if dirname_rm in SYS_DIR:
                    print("You just tried to delete a system file!!")
                    __chdir(os.getcwd())
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
