from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from sys import argv

global file
global text_
text_ = ""
file = "NewFile"
root = Tk(className = " Light Script IDE - NewFile")
console = Tk(className = " Light Script Result")
textc = Text(console, insertbackground="white", selectbackground="gray", background="black", foreground='white')
root['bg'] = 'black'
frame = Frame(root)
frame.pack(pady=5, expand=True, fill='both')
frame.configure(background = 'black')
text = Text(frame, insertbackground="white", selectbackground="gray", background="black", foreground='white', undo=True)
text.pack(expand=True, fill='both')
textc.pack(expand=True, fill='both')
text_ = text.get("1.0", END)
tags = []
menubar = Menu(root)


def printc(string):
    textc.insert(END, str(string) + '\n')
    return

    
def read(file):
    with open(file, 'r') as f:
        c = f.read()
    return c

def write(file, towrite):
    with open(file, 'w') as f:
        f.write(towrite)


def search_one(string, char):
    isinstring = 0
    first = ""
    N = len(string)
    for i in range(N):
        if string[i] == '"':
            if isinstring == 1:
                if string[i] == first:
                    isinstring = 0
            else:
                isinstring = 1
                first = '"'
        elif string[i] == "'":
            if isinstring == 1:
                if string[i] == first:
                    isinstring = 0
            else:
                isinstring = 1
                first = "'"
        if string[i] == char and isinstring == 0:
            return i
    return -1


def search(string, pattern):
    isinstring = 0
    first = ""
    M = len(pattern)
    N = len(string)
    if len(pattern) == 1:
        return search_one(string, pattern)
    for i in range(N-M):
        jj = 0
        if string[i] == '"':
            if isinstring == 1:
                if string[i] == first:
                    isinstring = 0
            else:
                isinstring = 1
                first = '"'
        elif string[i] == "'":
            if isinstring == 1:
                if string[i] == first:
                    isinstring = 0
            else:
                isinstring = 1
                first = "'"
        for j in range(M):
            if string[i + j] != pattern[j]:
                break;
            jj = j
        if jj == (M-1) and isinstring == 0:
            return i
    return -1


def searchend(string, pattern):
    isinstring = 0
    first = ""
    M = len(pattern)
    N = len(string)
    if len(pattern) == 1:
        return search_one(string, pattern)
    for i in range(N-M):
        jj = 0
        if string[i] == '"':
            if isinstring == 1:
                if string[i] == first:
                    isinstring = 0
            else:
                isinstring = 1
                first = '"'
        elif string[i] == "'":
            if isinstring == 1:
                if string[i] == first:
                    isinstring = 0
            else:
                isinstring = 1
                first = "'"
        for j in range(M):
            if string[i + j] != pattern[j]:
                break;
            jj = j
        if jj == (M-1) and isinstring == 0:
            return i+M
    return -1


def lastline(string, sub):
    args = [""]
    alist = 0
    for i in range(len(string)):
        if string[i] == '\n':
            args.append("")
            alist = alist + 1
        else:
            args[alist] = args[alist] + string[i]
    for i in range(len(args)-1):
        if search(args[i], sub) != -1:
            return i


def getline(string, line):
    args = [""]
    alist = 0
    for i in range(len(string)):
        if string[i] == '\n':
            args.append("")
            alist = alist + 1
        else:
            args[alist] = args[alist] + string[i]
    return args[line]


def getAllLines(string):
    args = [""]
    alist = 0
    for i in range(len(string)):
        if string[i] == '\n':
            args.append("")
            alist = alist + 1
        else:
            args[alist] = args[alist] + string[i]
    return args
    

def isstring(string):
    pos = []
    tosearch = '"'
    
    if string.find('"') < string.find("'"):
        tosearch = "'"
        
    if string.find(tosearch) != -1:
        pos.append(string.find(tosearch)+1)
        string2 = string[string.find(tosearch)+1:]
        if string2.find(tosearch) != -1:
            pos.append(string2.find(tosearch)+(len(string)-len(string2)))
            return (1, pos)
        else:
            return (0, (0,0))
    else:
        return (0, (0,0))


def isvar(string):
    pos = []
    if search(string, '%') != -1:
        pos.append(search(string, '%')+1)
        string2 = string[search(string, '%')+1:]
        if search(string2, '%') != -1:
            pos.append(search(string2, '%')+len(string)-len(string2))
            return (1, pos)
        else:
            return (0, (0,0))
    else:
        return (0, (0,0))


def iscond(string):
    pos = []
    if search(string, '$') != -1:
        pos.append(search(string, '$')+1)
        string2 = string[search(string, '$')+1:]
        if search(string2, '$') != -1:
            pos.append(search(string2, '$')+len(string)-len(string2))
            return (1, pos)
        else:
            return (0, (0,0))
    else:
        return (0, (0,0))

    
def isfunc(string):
    pos = []
    if search(string, '(') != -1:
        if search(string, ')') != -1:
            return 1
        else:
            return 0
    else:
        return 0


def isfloat(string):
    try:
        s = float(string)
        return 1
    except:
        return 0
    

def isint(string):
    try:
        s = int(string)
        return 1
    except:
        return 0
        

def replacevar(string, var):
    i, posi = isvar(string)
    while i == 1:
        toreplace = string[posi[0]-1:posi[1]+1]
        string = string.replace(toreplace, str(var[toreplace[1:-1]]))
        i, posi = isvar(string)
    return string


def ismath(string, var):
    if scanOperator != -1:
        try:
            s = eval(replacevar(string, var))
            return 1
        except:
            return 0


def findchar(lists, char):
  find=0
  for i in range(len(lists)-1):
    if lists[i] == char:
      find=find+1
  return find


def islist(string):
    pos = 0
    if search(string, ']') != -1:
        pos = search(string, ']')
        string = string[search(string, '[')+1:]
        if search(string, ']') != -1:
            return (1, (pos, search(string, ']')))
        else:
            return (0, (0, 0))
    else:
        return (0, (0, 0))


def notab(string):
    isinstring = 0
    first = ""
    nstr = ""
    for i in range(len(string)):
        if string[i] == " ":
            if isinstring == 1:
                nstr = nstr + string[i]
        elif string[i] == '"':
            if isinstring == 1:
                if string[i] == first:
                    isinstring = 0
            else:
                isinstring = 1
                first = '"'
            nstr = nstr + string[i]
        elif string[i] == "'":
            if isinstring == 1:
                if string[i] == first:
                    isinstring = 0
            else:
                isinstring = 1
                first = "'"
            nstr = nstr + string[i]
        else:
            nstr = nstr + string[i]
            
    return nstr


def getlist(string, var):
    pos = []
    passed = 0
    string = string[search(string, '[')+1:]
    for i in range(findchar(string, ',')+1):
        s = search(string, ',')
        if s == -1:
            if passed >= 1:
                return pos
            else:
                passed += 1
        if isfunc(string[:s].replace(' ', '')):
            f = 1
            passstr = string
            passed = 0
        elif isstring(string[:s])[0]:
            f = isstring(string[:s])
            pos.append(string[f[1][0]:f[1][1]])
            string = string[search(string, ',')+1:]
            passstr = string
            passed = 0
        elif ismath(string[:s], var):
            pos.append(eval(replacevar(string[:s], var)))
            string = string[search(string, ',')+1:]
            passstr = string
            passed = 0
        elif isvar(string[:s])[0]:
            f = isvar(string[:s])
            pos.append(var[string[f[1][0]:f[1][1]]])
            string = string[search(string, ',')+1:]
            passstr = string
            passed = 0
        elif isint(string[:s]):
            pos.append(int(string[:s]))
            string = string[search(string, ',')+1:]
            passstr = string
            passed = 0
        elif isfloat(string[:s]):
            pos.append(float(string[:s]))
            string = string[search(string, ',')+1:]
            passstr = string
            passed = 0
        else:
            l = getlist(string[:search(string, ']')+1], var)
            pos.append(l)
            passstr = string[search(string, ',')+1:]
            for j in range(len(pos[len(pos)-1])):
                string = string[search(string, ',')+1:]
    return pos


def getParametersF(function):
    parameters = []
    after = function[search(function, "(")+1:-2]
    pos = 1
    while pos:
        if isvar(after)[0]:
            pos = 1
            s = isvar(after)
            parameters.append(after[s[1][0]:s[1][1]])
            if search(after, ",") == -1:
                after = after[:-1]
            after = after[search(after, ",")+1:]
        else:
            pos = 0
    return parameters


def getParameters(function, var):
    parameters = []
    pos=1
    l = function
    after = l[search(l, "(")+1:-1]
    while pos:
        if islist(after)[0] and (isvar(after)[1][0] > islist(after)[1][0] or isvar(after)[0] == 0):
            pos = 1
            parameters.append(getlist(after, var))
        elif isstring(after)[0]:
            pos = 1
            s = isstring(after)
            parameters.append(after[s[1][0]:s[1][1]])
        elif isfunc(after):
            pos = 1
        elif ismath(after, var):
            pos = 1
            parameters.append(eval(replacevar(after, var)))
        elif isvar(after)[0]:
            if isvar(after)[1][0] < islist(after)[1][0]:
                index = getlist(after, var)
                s = isvar(after)
                parameters.append(var[after[s[1][0]:s[1][1]]][index])
            else:
                s = isvar(after)
                parameters.append(var[after[s[1][0]:s[1][1]]])
        elif isint(after):
            pos = 1
            parameters.append(int(after))
        elif isfloat(after):
            pos = 1
            parameters.append(float(after))
        else:
            pos = 0
        if search(after, ",") == -1:
            after = after[:-1]
        after = after[search(after, ",")+1:]
    return parameters


def scanCondType(after):
    if search(after, "==") != -1:
        return "=="
    elif search(after, ">") != -1:
        return ">="
    elif search(after, "<") != -1:
        return "<"
    elif search(after, "!=") != -1:
        return "!="
    elif search(after, "<=") != -1:
        return "<="
    elif search(after, ">=") != -1:
        return ">="
    return -1


def scanOperator(after):
    if search(after, "**") != -1:
        return "**"
    elif search(after, "*") != -1:
        return "*"
    elif search(after, "+") != -1:
        return "+"
    elif search(after, "-") != -1:
        return "-"
    elif search(after, "//") != -1:
        return "="
    elif search(after, "/") != -1:
        return "/"
    elif search(after, "%") != -1 and isvar(after) == -1:
        return "%"
    elif search(after, "=") != -1:
        return "="
    return -1


class ls():
    def __init__(self, script):
        self.script = []
        self.functions = {}
        self.label = {}
        self.default_function = {}
        self.default_function[""] = -1
        self.default_function["print(%string%)"] = 0
        self.default_function["os.file.write(%file%, %string%)"] = 1
        self.default_function["os.file.read(%file%)"] = 2
        self.default_function["write(%file%, %string%)"] = 1
        self.default_function["read(%file%)"] = 2
        self.default_function["input(%string%)"] = 3
        self.default_function["return(%to_return%)"] = 4
        self.default_function["len(%list%)"] = 5
        self.default_function["goto(%name%)"] = 6
        self.default_function["label(%name%)"] = 7
        self.condition = {}
        self.var = {}
        for i in getAllLines(script):
            if search(i, '#') != -1:
                if i[:search(i, '#')] != '\n':
                    self.script.append(i[:search(i, '#')])
            else:
                if i != '\n':
                    self.script.append(i)            


    def parse(self, script):
        for l in range(len(self.script)-1):
            subscript = self.script[l]
            if search(subscript, "def") != -1 and search(subscript, ":") != -1:
                self.functions[subscript[4:search(subscript, ':')]] = l


    def typescan(self, after):
        if islist(after)[0] and (isvar(after)[1][0] > islist(after)[1][0] or isvar(after)[0] == 0):
                return getlist(after, self.var)
        elif isfunc(after):
            return self.exec(after, 0)
        elif isstring(after)[0]:
            s = isstring(after)
            return after[s[1][0]:s[1][1]]
        elif ismath(after, self.var):
            return eval(replacevar(after, self.var))
        elif isvar(after)[0]:
            if isvar(after)[1][0] < islist(after)[1][0]:
                index = getlist(after, self.var)[0]
                s = isvar(after)
                return self.var[after[s[1][0]:s[1][1]]][index]
            s = isvar(after)
            return self.var[after[s[1][0]:s[1][1]]]
        elif isint(after):
            return int(after)
        elif isfloat(after):
            return float(after)

            
    def scanVarI(self, l):
        pos = isvar(l)
        after = l[search(l, "=")+1:]
        posi = pos[1]
        if search(l, "=") > islist(l)[1][0] and islist(l)[0] != 0:
                index = getlist(l, self.var)[0][0]
                self.var[l[posi[0]:posi[1]]][index] = self.typescan(after)
        else:
            self.var[l[posi[0]:posi[1]]] = self.typescan(after)

                
    def scanCondI(self, l):
        pos = iscond(l)
        after = l[search(l, "=")+1:]
        posi = pos[1]
        self.condition[l[posi[0]:posi[1]]] = notab(after)

            
    def condI(self, l, line):
        pos = iscond(l)
        iselse = 0
        if pos[0]:
            posi = pos[1]
            f = notab(l[posi[1]+1:])
            if search(l, '!') == posi[0]:
                iselse = 1
                c = self.condition[l[posi[0]+1:posi[1]]]
            else:
                c = self.condition[l[posi[0]:posi[1]]]
            after = self.typescan(c[search(c, "=")+1:])
            before = self.typescan(c[:search(c, "=")])
            if search(c, "==") != -1:
                if before == after:
                    if iselse == 0:
                        return self.exec_(f, line, [], f, one=l)
                else:
                    if iselse == 1:
                        return self.exec_(f, line, [], f, one=l)
            elif search(c, ">") != -1:
                if before > after:
                    if iselse == 0:
                        return self.exec_(f, line, [], f, one=l)
                else:
                    if iselse == 1:
                        return self.exec_(f, line, [], f, one=l)
            elif search(c, "<") != -1:
                if before < after:
                    if iselse == 0:
                        return self.exec_(f, line, [], f, one=l)
                else:
                    if iselse == 1:
                        return self.exec_(f, line, [], f, one=l)
            elif search(c, "!=") != -1:
                if before != after:
                    if iselse == 0:
                        return self.exec_(f, line, [], f, one=l)
                else:
                    if iselse == 1:
                        return self.exec_(f, line, [], f, one=l)
            elif search(c, "<=") != -1:
                if before <= after:
                    if iselse == 0:
                        return self.exec_(f, line, [], f, one=l)
                else:
                    if iselse == 1:
                        return self.exec_(f, line, [], f, one=l)
            elif search(c, ">=") != -1:
                if before >= after:
                    if iselse == 0:
                        return self.exec_(f, line, [], f, one=l)
                else:
                    if iselse == 1:
                        return self.exec_(f, line, [], f, one=l)
            

    def exec_(self, i, line, parameters, function, end = "end def", one = 0):
        toreturn = None
        if one == 0:
            j=0
            func = self.functions[i]
            line = func
            script = self.script[func:]
            parametersF = getParametersF(script[0])
            script = script[1:script.index(end)]
            if len(parameters) > len(parametersF):
                printc("Error: too many parameters for function `{}', at line {}".format(function, line))
            if len(parameters) < len(parametersF):
                printc("Error: not enough parameters for function `{}', at line {}".format(function, line))
                return None
            for i in range(len(parametersF)):
                self.var[parametersF[i]] = parameters[i]
            while j != len(script):
                line2 = line + j
                i = script[j]
                if iscond(i)[0] == 0 and isvar(i) != -1 and scanOperator(i) != -1:
                    self.scanVarI(i)
                elif iscond(i)[0] == 1 and scanCondType(i) != -1:
                    self.scanCondI(i)
                elif iscond(i)[0] == 1:
                    toreturn = self.condI(i, line2)
                else:
                    toreturn = self.exec(i, line2)
                if type(toreturn) == type([1, 1]):
                    if toreturn[0] == "__Python__.__ls__.__sys__.__goto__":
                        j = toreturn[1]-line
                        toreturn = None
                else:
                    j += 1
            return toreturn
        else:
            line2 = line
            if iscond(i)[0] == 0 and isvar(i) != -1 and scanOperator(i) != -1:
                self.scanVarI(i)
            elif iscond(i)[0] == 1 and scanCondType(i) != -1:
                self.scanCondI(i)
            elif iscond(i)[0] == 1:
                toreturn = self.condI(i, line2)
            else:
                toreturn = self.exec(i, line2)
        return toreturn
            
            

    def exec(self, function, line):
        func = ""
        function = notab(function)
        toreturn = None
        parameters = getParameters(function, self.var)
        for i in self.functions:
            nf = i[:search(i, "(")+1]+i[-1:]
            tcf = function[:search(function, "(")+1]+function[-1:]
            if nf == tcf:
                func = i
                toreturn = self.exec_(i, line, parameters, function)
                break
        for i in self.default_function:
            nf = i[:search(i, "(")+1]+i[-1:]
            tcf = function[:search(function, "(")+1]+function[-1:]
            if nf == tcf:
                func = i
                func = self.default_function[func]
                if func == 0:
                    printc(parameters[0])
                elif func == 1:
                    write(parameters[0], parameters[1])
                elif func == 2:
                    toreturn = read(parameters[0])
                elif func == 3:
                    toreturn = input(parameters[0])
                elif func == 4:
                    toreturn = parameters[0]
                elif func == 5:
                    toreturn = len(parameters[0])
                elif func == 6:
                    toreturn = ["__Python__.__ls__.__sys__.__goto__", self.label[parameters[0]]]
                elif func == 7:
                    self.label[parameters[0]] = line+1
                break
        if func == "":
            printc("Error, function not found `{}' at line {}".format(function, line))
            return None
        return toreturn


def openFile():
    global file
    file = askopenfilename(title="Open",filetypes=[('Light Script files','.ls'),('all files','.*')])
    with open(file, 'r') as f:
        text_ = text.get("1.0", END)
        text.insert("1.0", f.read())
    root.title(' Light Script IDE - ' + file)
    return 0


def saveFile():
    global file
    root.title(' Light Script IDE - ' + file)
    if file == "NewFile":
        f = asksaveasfile(initialfile = file, defaultextension=".ls",filetypes=[("All Files","*.*"),("Light Script","*.ls")])
        f.write(text.get("1.0", END))
    else:
        with open(file, 'w') as f:
            f.write(text.get("1.0", END))
    return 0


def run():
    printc('')
    printc('----- {} -----'.format(file))
    reader = ls(read(file))
    reader.parse(read(file))
    reader.var["noargs"] = [file]
    reader.exec("start(%noargs%)", 0)
    console.mainloop()


def runcustom():
    args = askquestion(title='Arguments', message='Arguments:')
    system('LSpy "'+file+'"'+args)
    return


menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Open", command=openFile)
menu1.add_command(label="Save", command=saveFile)
menu1.add_separator()
menu1.add_command(label="Exit", command=exit)
menubar.add_cascade(label="File", menu=menu1)
menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Run", command=run)
menu2.add_command(label="Run Custom...", command=runcustom)
menubar.add_cascade(label="Run", menu=menu2)

root.config(menu=menubar)


def scanKeyWord(after):
    if search(after, "=") != -1:
        return [search(after, "="), searchend(after, "=")]
    elif search(after, ">") != -1:
        return [search(after, ">"), searchend(after, ">")]
    elif search(after, "<") != -1:
        return [search(after, "<"), searchend(after, "<")]
    elif search(after, "!") != -1:
        return [search(after, "!"), searchend(after, "!")]
    elif search(after, "*") != -1:
        return [search(after, "*"), searchend(after, "*")]
    elif search(after, "+") != -1:
        return [search(after, "="), searchend(after, "=")]
    elif search(after, "-") != -1:
        return [search(after, "-"), searchend(after, "-")]
    elif search(after, "/") != -1:
        return [search(after, "/"), searchend(after, "/")]
    elif search(after, "%") != -1 and isvar(after) == -1:
        return [search(after, "%"), searchend(after, "%")]
    elif search(after, "=") != -1:
        return [search(after, "="), searchend(after, "=")]
    elif search(after, "end") != -1:
        return [search(after, "end"), searchend(after, "end")]
    elif search(after, "def") != -1:
        return [search(after, "def"), searchend(after, "def")]
    elif search(after, ",") != -1:
        return [search(after, ","), searchend(after, ",")]
    elif search(after, "0") != -1:
        return [search(after, "0"), searchend(after, "0")]
    elif search(after, "1") != -1:
        return [search(after, "1"), searchend(after, "1")]
    elif search(after, "2") != -1:
        return [search(after, "2"), searchend(after, "2")]
    elif search(after, "3") != -1:
        return [search(after, "3"), searchend(after, "3")]
    elif search(after, "4") != -1:
        return [search(after, "4"), searchend(after, "4")]
    elif search(after, "5") != -1:
        return [search(after, "5"), searchend(after, "5")]
    elif search(after, "6") != -1:
        return [search(after, "6"), searchend(after, "6")]
    elif search(after, "7") != -1:
        return [search(after, "7"), searchend(after, "7")]
    elif search(after, "8") != -1:
        return [search(after, "8"), searchend(after, "8")]
    elif search(after, "9") != -1:
        return [search(after, "9"), searchend(after, "9")]
    elif search(after, ":") != -1:
        return [search(after, ":"), searchend(after, ":")]
    return [-1, -1]

    
def execc_():
    j=0
    line = 1
    script = getAllLines(text.get("1.0", END))
    for tag in text.tag_names():
        text.tag_remove(tag, "1.0", END)
    tags = []
    r = 0
    jj = 0
    while j != len(script):
        line2 = line + j
        i = script[j]
        iii = len(i)
        comment = search(i, "#")
        while jj != iii:
            key = scanKeyWord(i)
            if key[0] != -1:
                tags.append(str(line2)+'.'+str(r+key[0]))
                text.tag_add(tags[-1], str(line2)+'.'+str(r+key[0]), str(line2)+'.'+str(r+key[1]+1))
                text.tag_config(tags[-1], foreground="violet")
                index = key[1]+1
                i = i[index:]
                r = r + key[1]+1
                iii = len(i)
            else: 
                jj = iii
        i = script[j]
        r = 0
        iii = len(i)
        jj = 0
        while jj != iii:
            var = isvar(i)
            if var[0]:
                tags.append(str(line2)+'.'+str(r+var[1][0]))
                text.tag_add(tags[-1], str(line2)+'.'+str(r+var[1][0]-1), str(line2)+'.'+str(var[1][1]+1))
                text.tag_config(tags[-1], foreground="cyan")
                i = i[var[1][1]:]
                r = r + 1
                iii = len(i)
            else:
                jj = iii
        i = script[j]
        r = 0
        iii = len(i)
        jj = 0
        while jj != iii:
            cond = iscond(i)
            if cond[0]:
                tags.append(str(line2)+'.'+str(r+cond[1][0]))
                text.tag_add(tags[-1], str(line2)+'.'+str(r+cond[1][0]-1), str(line2)+'.'+str(r+cond[1][1]+1))
                text.tag_config(tags[-1], foreground="orange")
                i = i[1:]
                r = r + 1
                iii = len(i)
            else:
                jj = iii
        i = script[j]
        r = 0
        iii = len(i)
        jj = 0
        while jj != iii:
            string = isstring(i)
            if string[0]:
                tags.append(str(line2)+'.'+str(r+string[1][0]))
                text.tag_add(tags[-1], str(line2)+'.'+str(r+string[1][0]-1), str(line2)+'.'+str(string[1][1]+1))
                text.tag_config(tags[-1], foreground="green")
                i = i[1:]
                r = r + 1
                iii = len(i)
            else:
                jj = iii
        i = script[j]
        r = 0
        iii = len(i)
        jj = 0
        if comment != -1:
            tags.append(str(line2)+'.'+str(comment))
            text.tag_add(tags[-1], str(line2)+'.'+str(comment), str(line2)+'.'+str(len(i)))
            text.tag_config(tags[-1], foreground="red")
        j += 1
    return 0


def check():
    global text_
    if (text.get("1.0", END) != text_):
        root.title(' Light Script IDE - *' + file)
        text_ = text.get("1.0", END)
        execc_()
    root.after(500, check)
  
root.after(500, check)
if len(argv) == 2:
    try:
        file = argv[2]
        with open(file, 'r') as f:
            text_ = text.get("1.0", END)
            text.insert("1.0", f.read())
        root.title(' Light Script IDE - ' + file)
    except:
        printc("Argument must be a path to a file")
else:
    if len(argv) > 2:
        printc("LSide only take 1 argument")
        
root.mainloop()
