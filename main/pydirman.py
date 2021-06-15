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
import readline
import subprocess as sp
from time import sleep
from termcolor import colored, cprint

global CUR_DIR, LS_DIR, CUR_PATH, CUR_FILE, SEARCH_DIR, SYS_DIR, TempC, TempCpp, COL, browser
app_path= "/usr/share/applications/defaults.list"
browser_prefix="application/xhtml+xml"
TempC = "#include <stdio.h>\n\nint main(){\n\n    return 0;\n}"
TempCpp = "#include <iostream>\n\nusing namespace std;\nint main(){\n\n    return 0;\n}"
COL, LINE = os.get_terminal_size()

with open(app_path, "r") as file:
    data= file.readlines()

for d in data:
    if d.startswith(browser_prefix):
        browser= d.split("=")[1].split(".")[:-1][0]

def green(text):

    return colored(text, "green")

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
            sys.exit(0)

elif len(sys.argv) == 1:
    CUR_DIR = os.getcwd()

CUR_DIR = os.getcwd()
LS_DIR = sorted(os.listdir())
CUR_PATH = os.path.abspath(CUR_DIR)

def convert_bytes(size):
    for ext in ['bytes', 'KB', 'MB', 'GB']:
        if size < 1024:
            return "{} {}".format(round(size, 2), ext)
        else:
            size/= 1024

def __hex(fp):
    with open(fp, "rb") as file:
        content= file.read()

    hexd= content.hex(sep= ' ')
    print("\n"+ colored(hexd, "blue") +"\n")

def test(file):

    global COL, browser
    __file = file.split(".")
    try:
        filename, file_type = __file
    except:
        filename= __file[0]

    command = str(input("Enter command [exit|test|nano|clear|hex] "))
    if command.startswith("t"):
        args_list= command.split(" ")[1:]
        args= ""
        for arg in args_list:
            args+= arg+" "

        print("-"*COL)

        if file_type == 'py':
            os.system("python3 {} {}".format(file, args).rstrip())

        elif file_type == 'c':
            os.system("gcc {} -o {}.out && ./{}.out {}".format(file, filename, filename, args).rstrip())

        elif file_type == 'cpp':
            os.system("g++ {} -o {}.out && ./{}.out {}".format(file, filename, filename, args).rstrip())

        elif file_type == 'asm':
            os.system("sudo nasm -f elf64 {} && sudo ld -o {}.out {}.o && sudo ./{}.out".format(file, filename, filename, filename))

        elif file_type == 'js':
            os.system("node {} {}".format(file, args).rstrip())

        elif file_type == 'java':
            os.system("javac {} && java {} {}".format(file, filename, args).strip())

        elif file_type == 'out':
            os.system("./{} {}".format(file, args).rstrip())

        elif file_type == 'class':
            os.system("java {} {}".format(filename, args).rstrip())

        elif file_type == 'html':
            os.system("{} {}".format(browser, file))

        print("-"*COL)
        test(file)

    elif command.lower() == "n":
        os.system("sudo nano {}".format(file))
        test(file)

    elif command.lower() == "c":
        COL= os.get_terminal_size()[0]
        os.system("clear")
        print("FILE -> {}\n".format(file))
        test(file)

    elif command.lower() == "h":
        __hex(file)
        test(file)

    elif command.lower() == "e":
        os.system("clear")
        __display()
        __chdir(os.getcwd())

    else:
        print("please enter a valid command")
        test(file)

def __display():

    global COL

    COL= os.get_terminal_size()[0]
    TAB= round((0.6*COL))
    CUR_DIR = os.getcwd()
    LS_DIR = sorted(os.listdir())
    CUR_PATH = os.path.abspath(CUR_DIR)

    print(colored("\nPYTHON DIRECTORY MANAGEMENT\n", "red", attrs=['underline', 'bold']))
    gi= green(" | ")
    print(colored("Directory", "yellow") + gi + colored("File", "white") + gi + colored("Misc", "red") + gi + colored("Size", "blue"))
    print(green("="*COL))
    fc = 0
    dc = 0
    misc= 0
    counter = 0
    total_size = 0
    for index,FI_FO in enumerate(LS_DIR):
        gin= green("[{}] ".format(index))
        counter += 1
        if os.path.isfile(FI_FO):
            fc += 1
            name_length= len(str(counter))+ 3+ len(FI_FO)
            GAP= TAB-name_length
            file_size= convert_bytes(os.path.getsize(FI_FO))
            total_size+= os.path.getsize(FI_FO)
            print(gin + colored("{}".format(str(FI_FO)), "white") + colored("-"*GAP +"{}".format(file_size), "blue"))

        elif os.path.isdir(FI_FO):
            dc += 1
            print(gin + colored("{}/".format(str(FI_FO)), "yellow"))

        else:
            print(gin + colored("{}".format(str(FI_FO)), "red"))
            misc += 1

    print(green("="*COL))
    fcounter = colored("{}".format(fc), "white", attrs=['bold'])
    dcounter = colored("{}".format(dc), "yellow", attrs=['bold'])
    c = colored("{}".format(counter), "green", attrs=['bold'])
    m = colored("{}".format(misc), "red", attrs=['bold'])
    print("TOTAL FILES/DIRECTORIES: {} ({}/{}/{})".format(c, fcounter, dcounter, m))
    print("YOUR CURRENT LOCATION: "+ colored("{}".format(CUR_PATH), "green", attrs=['bold']))
    print("TOTAL SIZE HERE(files): "+ colored("{}".format(convert_bytes(total_size)), "green", attrs=['bold']))
    print(green("="*COL))
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
        if com.startswith("g"): #  GOTO COMMAND

            try:
                if len(os.listdir(os.getcwd()))==1:
                    ask= "0"
                else:
                    if len(com.strip())==1:
                        print("I need a index here to work!")
                        __chdir(CUR_DIR)
                    else:
                        ask= com.split(" ")[1]

                if ask.isdigit():
                    ask= eval(ask)

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
                            porr = str(input(colored("FILE=[{}]\n".format(str(LS_DIR[ask])), "white")+"{}rint/{}ancel/{}xit: ".format(rp,rc,re)))
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

                else:
                    print("wait what?, what is this: {}".format(" ".join(com.split(" ")[1:])))
                    __chdir(os.getcwd())

            except PermissionError:
                cprint("\nThis directory is off limits!! Are you root?? I don't think so. BACK OFF!\n".upper(), "red", attrs=['bold'])
                sleep(2)
                __chdir(os.getcwd())

        elif com.lower() == "e": #  EXIT COMMAND
            print(colored("See you soon!\n", "white"))
            sys.exit(0)

        elif com.lower() == "console": #  PYTHON CONSOLE
            os.system("clear")
            sp.run("python3")
            __display()
            __chdir(CUR_DIR)

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
            os.system("clear")
            __display()
            __chdir(CUR_DIR)

        elif com.startswith("test"): #  CODE-TESTING COMMAND
            CUR_DIR = os.getcwd()
            LS_DIR = sorted(os.listdir())

            if len(com) == 4:
                print("I am hungry! Feed me indices.\n")
                __chdir(CUR_DIR)
            else:
                try:
                    file_index = int(com[5:])
                    file = LS_DIR[file_index]

                    if os.path.isfile(file):
                        os.system("clear")
                        print("FILE -> {}\n".format(file))
                        test(file)

                    elif os.path.isdir(file):
                        print("Enter index of files only !!")
                        __chdir(CUR_DIR)

                except IndexError:
                    print("Index {} not found".format(file_index))
                    __chdir(CUR_DIR)

                except ValueError:
                    print("Please enter a index!!")
                    __chdir(CUR_DIR)

        elif (com.lower() == "?")or(com.lower() == "h"): #  HELP COMMAND
            print("\n[help]      = "+ colored("[?/h]", 'red') +"elp-"+ colored("[ed]", 'red') +"itsource")
            print("[walker]    = "+ colored("[g]", 'red') +"oto-" +colored("[p]", 'red') +"revious-"+ colored("[s]", 'red') +"earch")
            print("[utility]   = "+ colored("[c]", 'red') +"lear-"+ colored("[t]", 'red') +"erminal-" +colored("[e]", 'red')+ "xit-" +colored("[c]", 'red') +"lear")
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

        elif com.startswith("s "): #  SEARCH COMMAND
            args= com.split()
            search = args[1]
            try:
                con= args[2]
            except:
                con= "-a"
            objects= []
            for object in LS_DIR:
                if search in object:
                    if con == "-a":
                        objects.append((object, LS_DIR.index(object)))
                    elif con == "-f":
                        if os.path.isfile(object):
                            objects.append((object, LS_DIR.index(object)))
                    elif con == "-d":
                        if os.path.isdir(object):
                            objects.append((object, LS_DIR.index(object)))
                    else:
                        print("Wrong argument: `{}`".format(con))
                        print("\n[-a] for all(by default).\n[-f] for files only.\n[-d] for directory only.\n")
                        break

            if len(objects) > 0:
                print("-"*COL)
                print(colored(f"OBJECTS SEARCHED: {len(LS_DIR)}, OBJECTS FOUND: {len(objects)}", "red", attrs=["bold"]))
                print("-"*COL)

                for object in objects:
                    if os.path.isfile(object[0]):
                        print("[{}] ".format(object[1]) + colored("{}".format(object[0]), "white"))
                    elif os.path.isdir(object[0]):
                        print("[{}] ".format(object[1]) + colored("{}/".format(object[0]), "yellow"))
                print("-"*COL)

            else:
                print("`{}` not found!!!".format(args[:]))
            __chdir(CUR_DIR)

        elif com.startswith("t "): #  TERMINAL COMMAND
            cmd= com[2:]
            cmd_args= cmd.split(" ")
            print("-"*COL + "\nExecuting [{}]...\n".format(colored(cmd, "green")) + "-"*COL)
            os.system(cmd)
            print("-"*COL)
            __chdir(CUR_DIR)

        elif com.lower() == "n": #  NEW-FILE COMMAND
            try:
                filename = str(input("Enter file name [create]: "))
                os.system("touch {}".format(filename))
                file_name ,file_ext = filename.split('.')
                TempJava= "public class "+ file_name +" {\n\n    public static void main(String[] args){\n\n\n    }\n\n}\n"
                ns= "__"+ file_name.upper() +"_H"
                TempHPP= "#ifndef {}\n#define {}\n\n\n".format(ns, ns) + "class "+ file_name +" {\n\n};\n\n#endif"

                if file_ext == 'c':
                    os.system('echo "{}" > {}'.format(TempC, filename))

                elif file_ext == 'cpp':
                    os.system('echo "{}" > {}'.format(TempCpp, filename))

                elif file_ext == 'java':
                    os.system('echo "{}" > {}'.format(TempJava, filename))

                elif file_ext == 'hpp':
                    os.system('echo "{}" > {}'.format(TempHPP, filename))

                os.system("sudo chmod 777 {}".format(filename))

            except:
                print("File not created")

            os.system("clear")
            __display()
            __chdir(CUR_DIR)

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

        elif com.startswith("m "): #  NEW-DIRECTORY COMMAND
            try:
                dirname_mk = com.split(" ")[1]
                os.system("mkdir {}".format(dirname_mk))
            except KeyboardInterrupt:
                print("Directory not created!")

            os.system("clear")
            __display()
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
                    print("You just tried to delete a system folder!!")
                    __chdir(os.getcwd())
                os.system("rmdir {}".format(dirname_rm))
            except KeyboardInterrupt:
                print("Directory not deleted")
            except ValueError:
                print("Enter Correctly")
            except IndexError:
                print("Enter Correctly")

            os.system("clear")
            __display()
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
