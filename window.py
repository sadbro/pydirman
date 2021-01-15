from tkinter import *
import json
import random

class Host():

    def __init__(self, register_fp="register.json", matches_fp="matches.json"):
        self.file= register_fp
        self.match= matches_fp

    def start(self):

        def warning(s):
            host= Tk()
            host.title("WARNING!!")
            host.geometry("300x100")
            Label(host, text=s).pack()
            Button(host, text="Close", command=host.destroy, bd='2').pack(side='bottom')

        def CreateProfile():
            host= Tk()
            host.title('Enter your Details')
            host.geometry('300x100')

            name_str= Entry(host)
            desc_str= Entry(host)
            n= Label(host, text='Enter name:').grid(row=0, column=1)
            d= Label(host, text='Enter ID:').grid(row=1, column=1)

            def Submit():
                name= name_str.get()
                code= desc_str.get()

                with open(self.file) as f:
                    data= json.load(f)
                    dict= {"name":name, "ID":code}
                    data["players"].append(dict)

                with open(self.file, "w") as writer:
                    json.dump(data, writer)

                host.destroy()

            SubmitInput= Button(host, text='Submit', command=Submit)

            name_str.grid(row=0, column=2)
            desc_str.grid(row=1, column=2)
            SubmitInput.grid(row=3, column=2)

        def CreateGroupsOf2():
            with open(self.file) as f:
                data= json.load(f)
            names= []
            for player in data["players"]:
                names.append(player["name"])
            if len(names)%2==1:
                warning("Odd Number of participants detected->%d"%len(names))
            elif len(names)==0:
                warning("No participants found!!")
            else:
                random.shuffle(names)
                i= int(len(names)/2)
                G1= names[:i]
                G2= names[i:]
                #print(G1, G2)

            host= Tk()
            host.title("Groups Of 2")
            host.geometry("300x400")
            list1= "GROUP 1\n\n"
            list2= "GROUP 2\n\n"
            for i, j in zip(G1, G2):
                list1+= "NAME: {}\n".format(i)
                list2+= "NAME: {}\n".format(j)

            Label(host, text=list1).grid(row=0, column=0)
            Label(host, text=list2).grid(row=0, column=1)
            with open(self.match, "w") as f:
                data= {"matches":[G1, G2]}
                json.dump(data, f)

        def Display():
            host= Tk()
            host.title('Player List')
            host.geometry('250x450')

            list= ""
            with open(self.file) as f:
                data= json.load(f)
                for i, player in enumerate(data["players"]):
                    list+= "PLAYER {}\n  NAME: {}\n  ID: {}\n\n".format(i+1, player["name"], player["ID"])


            Label(host, text= list).pack()
            Button(host, text="Create Groups", command=CreateGroupsOf2).pack(side='top')
            Button(host, text="Back", command=host.destroy).pack(side='bottom')


        win= Tk()
        win.title('TestRun')
        win.geometry('200x100')

        Entree= Button(win, text='New Player', command=CreateProfile).pack()
        Display= Button(win, text='Player List', command=Display).pack()

        win.mainloop()
