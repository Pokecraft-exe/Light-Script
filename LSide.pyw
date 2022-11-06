from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from sys import argv
from math import *

class debugWindow():
    def __init__(self, title, tofollow):
        self.w = Toplevel(root)
        self.w.title(title)
        self.l1 = Listbox(self.w)
        self.l1.pack(expand=True, fill='both', side = LEFT)
        self.l2 = Listbox(self.w)
        self.l2.pack(expand=True, fill='both', side = RIGHT)
        self.update(tofollow)


    def update(self, tofollow):
        i = 1
        for x in tofollow:
            self.l1.insert(i, x)
            self.l2.insert(i, tofollow[x])
            i + i + 1

        
class showinfo2():
    def __init__(self, root, message):
        self.w = Toplevel(root)
        self.w.title('info')
        Label(self.w, text=message).pack(expand=True, fill='y', side = TOP)
        Button(self.w, text="OK", command=self.clickedtrue).pack(expand=True, fill='y', side = BOTTOM)
        root.wait_window(self.w)

    
    def clickedtrue(self):
        self.w.destroy()
        

class askstring():
    def __new__(self, root, title, message) -> str:
        self.toreturn = ''
        self.w = Toplevel(root)
        self.w.title(title)
        self.clicked = False
        Label(self.w, text=message).pack(expand=True, fill='y', side = TOP)
        self.e = Entry(self.w)
        self.e.pack(expand=True, fill='y')
        self.e.focus()
        self.w.bind('<Return>', lambda evt: self.clickedtrue(self))
        Button(self.w, text="OK", command=lambda: self.clickedtrue(self)).pack(expand=True, fill='y', side = BOTTOM)
        root.wait_window(self.w)
        self.value = self.toreturn
        return self.toreturn

    
    def clickedtrue(self, event=None):
        self.clicked = True
        self.toreturn = self.e.get()
        self.w.destroy()

        
class LineNumbers(Text):
    def __init__(self, master, text_widget, **kwargs):
        super().__init__(master, **kwargs)
 
        self.text_widget = text_widget
        self.text_widget.bind('<KeyRelease>', self.on_key_release)
        self.text_widget.bind('<FocusIn>', self.on_key_release)
        self.text_widget.bind('<MouseWheel>', self.on_key_release)
 
        self.insert(1.0, '0')
        self.configure(state='disabled')
 
    def on_key_release(self, event=None):
        p, q = self.text_widget.index("@0,0").split('.')
        p = int(p)-1
        final_index = str(self.text_widget.index(END))
        num_of_lines = final_index.split('.')[0]
        line_numbers_string = "\n".join(str(p + no) for no in range(int(num_of_lines)))
        width = len(str(num_of_lines))
 
        self.configure(state='normal', width=width)
        self.delete(1.0, END)
        self.insert(1.0, line_numbers_string)
        self.configure(state='disabled')


root = Tk(className = " Light Script IDE - NewFile")
root['bg'] = 'black'
root.minsize(860, 450)
console = Toplevel(root)
console.title(" Light Script Result")

textc = Text(console, insertbackground="white", selectbackground="gray", background="black", foreground='white')
textc.pack(expand=True, fill='both')

frame = Frame(root)
frame.pack(pady=5, side=RIGHT, expand=True, fill='both')
frame.configure(background = 'black')

text = Text(frame, insertbackground="white", selectbackground="gray", background="black", foreground='white', undo=True)
text.pack(side=RIGHT, expand=True, fill='both')
ln = LineNumbers(frame, text, width=5, background="black", foreground='lime')
ln.pack(expand=True, fill=Y)
ln.on_key_release()

clicked = 0
file = "NewFile"
text_ = text.get("1.0", END)
tags = []

def cache(function):
    cache = {}

    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = function(*args, **kwargs)
        return cache[key]
    return wrapper

def printc(string):
    textc.insert(END, str(string) + '\n')
    textc.see("end")
    return


def inputc(string):
    answer = askstring(root, "input", string)
    return answer

    
def read(file):
    with open(file, 'r') as f:
        c = f.read()
    return c


def write(file, towrite):
    with open(file, 'w') as f:
        f.write(towrite)


def search_one(string, char):
    isinstring = 0
    string = string+' '
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
    string = string+' '
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
    string = string+' '
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


def searchOuttaAll(string, pattern):
    isinstring = 0
    first = ""
    string = string+' '
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
        elif string[i] == "%":
            if isinstring == 1:
                if string[i] == first:
                    isinstring = 0
            else:
                isinstring = 1
                first = "%"
        elif string[i] == "$":
            if isinstring == 1:
                if string[i] == first:
                    isinstring = 0
            else:
                isinstring = 1
                first = "$"
        for j in range(M):
            if string[i + j] != pattern[j]:
                break;
            jj = j
        if jj == (M-1) and isinstring == 0:
            return i
    return -1


def getAllLines(string, iside = 0):
    args = [""]
    alist = 0
    isAltSix = 0
    for i in range(len(string)):
        if string[i] == '\n' and string[i-1] != '|':
            args.append("")
            alist = alist + 1
        elif string[i-1] == '|' and string[i] == '\n' and iside == 0:
            args[alist] = args[alist][:len(args[alist])-1]
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


@cache
def isvar(string):
    pos = []
    pos.append(search(string, '%')+1)
    if pos[0] != 0:
        string2 = string[pos[0]+1:]
        pos.append(search(string2, '%')+len(string)-len(string2))
        if pos[1] > pos[0]:
            return (1, pos)
        else:
            return (0, (0,0))
    else:
        return (0, (0,0))


@cache
def iscond(string):
    pos = []
    pos.append(search(string, '$')+1)
    if pos[0] != 0:
        string2 = string[pos[0]+1:]
        pos.append(search(string2, '$')+len(string)-len(string2))
        if pos[1] > pos[0]:
            return (1, pos)
        else:
            return (0, (0,0))
    else:
        return (0, (0,0))


@cache    
def isfunc(string):
    pos = []
    if search(string, '(') != -1:
        if search(string, ')') != -1:
            return 1
        else:
            return 0
    else:
        return 0


@cache
def isfloat(string):
    chars = "0123456789."
    if string != '':
        for i in range(len(string)):
            if not string[i] in chars:
                return 0
        return 1
    return 0
    

@cache
def isint(string):
    chars = "0123456789"
    if string != '':
        for i in range(len(string)):
            if not string[i] in chars:
                return 0
        return 1
    return 0


@cache
def isbin(string):
    chars = "0b1"
    if string != '':
        for i in range(len(string)):
            if not string[i] in chars:
                return 0
        return 1
    return 0


@cache
def ishex(string):
    chars = "0x123456789ABCDEF"
    if string != '':
        for i in range(len(string)):
            if not string[i] in chars:
                return 0
        return 1
    return 0
        

def replacevar(string, var):
    i, posi = isvar(string)
    while i == 1:
        toreplace = string[posi[0]-1:posi[1]+1]
        string = string.replace(toreplace, str(var[toreplace[1:-1]]))
        i, posi = isvar(string)
    return string


def ismath(string, var):
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
    pos = []
    pos.append(search(string, '[')+1)
    if pos[0] != 0:
        string2 = string[pos[0]+1:]
        pos.append(search(string2, ']')+len(string)-len(string2))
        if pos[1] > pos[0]:
            return (1, pos)
        else:
            return (0, (0,0))
    else:
        return (0, (0,0))


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


def index(script, end):
    for i in range(len(script)-1):
        if search(script[i], end) != -1:
            return i
    return -1


def getParametersF(function):
    parameters = []
    pos=1
    after = function[search(function, "(")+1:function.rfind(")")]
    afterr = after
    while pos:
        if search(after, ",") != -1:
            afterr = after[:search(after, ",")+1]
        else:
            afterr = after
        s = isvar(afterr)
        if s[0]:
            parameters.append(afterr[:s[1][1]+1])
        else:
            pos = 0
        if search(after, ",") == -1:
            after = after[:-1]
        else:
            after = after[search(after, ",")+1:]
    return parameters


@cache
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


@cache
def scankeyType(after):
    if searchOuttaAll(after, "int") != -1:
        return "int"
    elif searchOuttaAll(after, "str") != -1:
        return "str"
    elif searchOuttaAll(after, "float") != -1:
        return "float"
    elif searchOuttaAll(after, "bin") != -1:
        return "bin"
    elif searchOuttaAll(after, "hex") != -1:
        return "hex"
    elif searchOuttaAll(after, "global") != -1:
        return "global"
    elif searchOuttaAll(after, "raw") != -1:
        return "raw"
    return -1


@cache
def scanOperatorEqual(after):
    if search(after, "**=") != -1:
        return "**="
    elif search(after, "*=") != -1:
        return "*="
    elif search(after, "+=") != -1:
        return "+="
    elif search(after, "-=") != -1:
        return "-="
    elif search(after, "/=") != -1:
        return "/="
    elif search(after, "%=") != -1 and isvar(after) == -1:
        return "%="
    elif search(after, "^=") != -1:
        return "^="
    elif search(after, "->") != -1:
        return "->"
    elif search(after, "=") != -1:
        return "="
    return -1


@cache
def scanOperator(after):
    if search(after, "**") != -1:
        return "**"
    elif search(after, "*") != -1:
        return "*"
    elif search(after, "+") != -1:
        return "+"
    elif search(after, "-") != -1:
        return "-"
    elif search(after, "/") != -1:
        return "/"
    elif search(after, "^") != -1:
        return "^"
    elif search(after, "%") != -1 and isvar(after) == -1:
        return "%"
    return -1


class ls():
    def __init__(self, script):
        self.script = []
        self.functions = {}
        self.label = {}
        self.condition = {}
        self.var = {}
        self.default_function = {}
        self.current_function = ""
        # defining default functions
        self.default_function[""] = -1
        self.default_function["print(%any%)"] = 0
        self.default_function["os.file.write(%file%, %string%)"] = 1
        self.default_function["os.file.read(%file%)"] = 2
        self.default_function["write(%file%, %string%)"] = 1
        self.default_function["read(%file%)"] = 2
        self.default_function["input(%string%)"] = 3
        self.default_function["return(%any%)"] = 4
        self.default_function["len(%list%)"] = 5
        self.default_function["goto(%name%)"] = 6
        self.default_function["label(%name%)"] = 7
        self.default_function["sin(%float%)"] = 8
        self.default_function["cos(%float%)"] = 9
        self.default_function["tan(%float%)"] = 10
        self.default_function["lstype(%any%)"] = 11
        self.default_function["type(%any%)"] = 12
        self.default_function["free(%any%)"] = 13
        # defining default vars
        self.var["pi"] = pi
        for i in getAllLines(script):
            if search(i, '#') != -1:
                self.script.append(i[:search(i, '#')])
            else:
                comma = search(i, ';')
                if comma != -1:
                    self.script.append(i[:comma])
                    self.script.append(i[comma+1:])
                else:
                    self.script.append(i)


    def parse(self, script):
        for l in range(len(self.script)-1):
            subscript = self.script[l]
            if search(subscript, "def") != -1 and search(subscript, ":") != -1:
                self.functions[subscript[4:search(subscript, ':')]] = l


    def typescan(self, after, line, function = "", test = 0):
        after = notab(str(after))
        if test == 0:
            if islist(after)[0] and (isvar(after)[1][0] > islist(after)[1][0] or isvar(after)[0] == 0):
                return self.getlist(after, line, function)
            elif isfunc(after):
                return self.exec(after, line, function)
            elif isstring(after)[0]:
                s = isstring(after)
                return after[s[1][0]:s[1][1]]
            elif isint(after):
                return int(after)
            elif isfloat(after):
                return float(after)
            elif isbin(after):
                return bin(after)
            elif ishex(after):
                return hex(after)
            elif ismath(after, self.var) and scanOperator(after) != -1:
                return eval(replacevar(after, self.var))
            elif isvar(after)[0]:
                s = isvar(after)
                if after[s[1][0]:s[1][1]] in self.var:
                    if isvar(after)[1][0] < islist(after)[1][0]:
                        index = getlist(after, self.var)[0]
                        return self.var[after[s[1][0]:s[1][1]]][index]
                    return self.var[after[s[1][0]:s[1][1]]]
                else:
                    if function+'.'+after[s[1][0]:s[1][1]] in self.var:
                        if isvar(after)[1][0] < islist(after)[1][0]:
                            index = getlist(after, self.var)[0]
                            return self.var[function+'.'+after[s[1][0]:s[1][1]]][index]
                        return self.var[function+'.'+after[s[1][0]:s[1][1]]]
                    else:
                        printc(f"Error at line {line}, variable `{str(function)+'.'+after[s[1][0]:s[1][1]]}' referenced before assignent.")
                        printc("Prehaps you have forgot `raw' or `global' ?")
                        return -1
                return 0
            return -1
        else:
            if islist(after)[0] and (isvar(after)[1][0] > islist(after)[1][0] or isvar(after)[0] == 0):
                return "list"
            elif isfunc(after):
                return "function"
            elif isstring(after)[0]:
                return "string"
            elif isint(after):
                return "int"
            elif isfloat(after):
                return "float"
            elif isbin(after):
                return "bin"
            elif ishex(after):
                return "hex"
            elif ismath(after, self.var) and scanOperator(after) != -1:
                return "float"
            elif isvar(after)[0]:
                return "var"
            return -1


    def tokeytype(self, keytype, after, line, function):
        if keytype == -1:
            return self.typescan(after, line, function)
        elif keytype == "int":
            return int(self.typescan(after, line, function))
        elif keytype == "str":
            return str(self.typescan(after, line, function))
        elif keytype == "float":
            return float(self.typescan(after, line, function))
        elif keytype == "bin":
            return bin(self.typescan(after, line, function))
        elif keytype == "hex":
            return hex(self.typescan(after, line, function))
        else:
            return self.typescan(after, line, function)
        
            
    def scanVarI(self, l, line, function):
        pos = isvar(l)
        tosearch = scanOperatorEqual(l)
        posint = search(l, tosearch)
        after = l[posint+len(tosearch):]
        posi = pos[1]
        keytype = scankeyType(l)
        ll = l
        if tosearch == "->":
            self.scanPointI(l, line, function)
            return
        if keytype == "global":
            l = l[posi[0]:posi[1]]
        else:
            l = function+'.'+l[posi[0]:posi[1]]
        if posint > islist(ll)[1][0] and islist(ll)[0] != 0:
            index = self.getlist(ll, line, function)[0]
            if tosearch == "**=":
                self.var[l][index] = self.var[l][index] ** self.tokeytype(keytype, after, line, function)
            elif tosearch == "*=":
                self.var[l][index] = self.var[l][index] * self.tokeytype(keytype, after, line, function)
            elif tosearch == "+=":
                self.var[l][index] = self.var[l][index] + self.tokeytype(keytype, after, line, function)
            elif tosearch == "-=":
                self.var[l][index] = self.var[l][index] - self.tokeytype(keytype, after, line, function)
            elif tosearch == "/=":
                self.var[l][index] = self.var[l][index] / self.tokeytype(keytype, after, line, function)
            elif tosearch == "%=":
                self.var[l][index] = self.var[l][index] % self.tokeytype(keytype, after, line, function)
            elif tosearch == "^=":
                self.var[l][index] = self.tokeytype(keytype, after, line, function) ^ self.tokeytype(keytype, after, line, function)
            elif tosearch == "=":
                self.var[l][index] = self.tokeytype(keytype, after, line, function)
        else:
            if tosearch == "**=":
                self.var[l] = self.var[l] ** self.tokeytype(keytype, after, line, function)
            elif tosearch == "*=":
                self.var[l] = self.var[l] * self.tokeytype(keytype, after, line, function)
            elif tosearch == "+=":
                self.var[l] = self.var[l] + self.tokeytype(keytype, after, line, function)
            elif tosearch == "-=":
                self.var[l] = self.var[l] - self.tokeytype(keytype, after, line, function)
            elif tosearch == "/=":
                self.var[l] = self.var[l] / self.tokeytype(keytype, after, line, function)
            elif tosearch == "%=":
                self.var[l] = self.var[l] % self.tokeytype(keytype, after, line, function)
            elif tosearch == "^=":
                self.var[l] = self.var[l] ^ self.tokeytype(keytype, after, line, function)
            elif tosearch == "=":
                self.var[l] = self.tokeytype(keytype, after, line, function)


    def getParameters(self, function, lastf, line):
        parameters = []
        pos=1
        l = function
        after = l[search(l, "(")+1:l.rfind(")")]
        if l.rfind(')') == -1:
            after+=')'
        afterr = after
        lf = (lastf[:lastf.find('(')] if lastf.find('(') != -1 else lastf)
        while pos:
            if search(after, ",") != -1:
                afterr = after[:search(after, ",")+1]
            else:
                afterr = after
                
            if self.typescan(afterr, line, test = 1) != -1:
                parameters.append(self.tokeytype(-1, afterr, line, lf))
            else:
                pos = 0
                
            if search(after, ",") == -1:
                after = after[:-1]
            else:
                after = after[search(after, ",")+1:]
        return parameters


    def getlist(self, string, line, function):
        parameters = []
        pos=1
        l = string
        after = l[search(l, "[")+1:l.rfind("]")]
        afterr = after
        while pos:
            if search(after, ",") != -1:
                afterr = after[:search(after, ",")]
            else:
                afterr = after
            if self.typescan(afterr, line, test = 1) != -1:
                parameters.append(self.tokeytype(-1, afterr, line, function))
            else:
                pos = 0
                
            if search(after, ",") == -1:
                after = after[:-1]
            else:
                after = after[search(after, ",")+1:]
        return parameters
    

    # dictionnary are not yet used
    """def getdict(self, string, line):
        parameters = []
        pos=1
        l = string
        after = l[search(l, "[")+1:l.rfind("]")]
        afterr = after
        while pos:
            if search(after, ",") != -1:
                afterr = after[:search(after, ",")+1]
            else:
                afterr = after
                
            if self.typescan(afterr, line) != -1:
                parameters.append(self.tokeytype(-1, afterr, line))
            else:
                pos = 0
                
            if search(after, ",") == -1:
                after = after[:-1]
            else:
                after = after[search(after, ",")+1:]
        return parameters"""


    def scanCondI(self, l):
        pos = iscond(l)
        after = l[search(l, "=")+1:]
        posi = pos[1]
        self.condition[l[posi[0]:posi[1]]] = notab(after)


    def scanPointI(self, l, line, function):
        before = l[:search(l, "->")]
        after = notab(l[searchend(l, "->"):])
        pos = isvar(after)[1]
        after = after[pos[0]:pos[1]]
        if self.typescan(before, line, test = 1) == "var":
            self.var[after] = '&'+before
        else:
            self.scanVarI(self.var[after]+'='+before, line, function)
        return

            
    def condI(self, l, line, function):
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
            after = self.tokeytype(-1, c[search(c, "=")+1:], line, function)
            before = self.tokeytype(-1, c[:search(c, "=")], line, function)
            if search(c, "==") != -1:
                if before == after:
                    if iselse == 0:
                        return self.exec_(f, line, [], function, one=l)
                else:
                    if iselse == 1:
                        return self.exec_(f, line, [], function, one=l)
            elif search(c, ">") != -1:
                if before > after:
                    if iselse == 0:
                        return self.exec_(f, line, [], function, one=l)
                else:
                    if iselse == 1:
                        return self.exec_(f, line, [], function, one=l)
            elif search(c, "<") != -1:
                if before < after:
                    if iselse == 0:
                        return self.exec_(f, line, [], function, one=l)
                else:
                    if iselse == 1:
                        return self.exec_(f, line, [], function, one=l)
            elif search(c, "!=") != -1:
                if before != after:
                    if iselse == 0:
                        return self.exec_(f, line, [], function, one=l)
                else:
                    if iselse == 1:
                        return self.exec_(f, line, [], function, one=l)
            elif search(c, "<=") != -1:
                if before <= after:
                    if iselse == 0:
                        return self.exec_(f, line, [], function, one=l)
                else:
                    if iselse == 1:
                        return self.exec_(f, line, [], function, one=l)
            elif search(c, ">=") != -1:
                if before >= after:
                    if iselse == 0:
                        return self.exec_(f, line, [], function, one=l)
                else:
                    if iselse == 1:
                        return self.exec_(f, line, [], function, one=l)
            

    def exec_(self, i, line, parameters, function, end = "end def", one = 0):
        toreturn = None
        if one == 0:
            j=0
            func = self.functions[i]
            line = func
            script = self.script[func:]
            parametersF = getParametersF(script[0])
            script = script[1:index(script, end)]
            if not '%...args%' in parametersF:
                if len(parameters) > len(parametersF):
                    printc(f"Error: too many parameters for function `{function}', at line {line}")
            else:
                print("param", parameters, i)
                parametersPP = parameters[:len(parametersF)+1]
                print("paramP", parametersPP, i)
                parametersP = parameters[len(parametersPP):]
                print("paramPP", parametersP, i)
                parameters = parametersPP
                parameters.append(parametersP)
                print("param", parameters, i)
            if len(parameters) < len(parametersF):
                printc(f"Error: not enough parameters for function `{function}', at line {line}")
                return None
            for i in range(len(parametersF)):
                keyT = scankeyType(parametersF[i])
                if keyT == "global":
                    self.scanVarI("{} = {}".format(parametersF[i], parameters[i]), line, function[:function.find('(')])
                else:
                    self.scanVarI("{} = {}".format(function[:function.find('(')]+'.'+parametersF[i], parameters[i]), line, function[:function.find('(')])
            while j != len(script):
                line2 = line + j
                i = script[j]
                if iscond(i)[0] == 0 and isvar(i) != -1 and scanOperatorEqual(i) != -1:
                    self.scanVarI(i, line2, function[:function.find('(')])
                elif iscond(i)[0] == 1 and scanCondType(i) != -1:
                    self.scanCondI(i)
                elif iscond(i)[0] == 1:
                    toreturn = self.condI(i, line2, function[:function.find('(')])
                else:
                    toreturn = self.exec(i, line2, function)
                if type(toreturn) == type([1, 1]):
                    if toreturn[0] == "__Python__.__ls__.__sys__.__goto__":
                        j = toreturn[1]-line
                        toreturn = None
                else:
                    j += 1
            return toreturn
        else:
            line2 = line
            lf = (function[:function.find('(')] if function.find("(") != -1 else function)
            if iscond(i)[0] == 0 and isvar(i) != -1 and scanOperatorEqual(i) != -1:
                self.scanVarI(i, line, lf)
            elif iscond(i)[0] == 1 and scanCondType(i) != -1:
                self.scanCondI(i)
            elif iscond(i)[0] == 1:
                toreturn = self.condI(i, line2, lf)
            else:
                toreturn = self.exec(i, line2, function)
        return toreturn


    def exec_one_by_one(self, i, line, parameters, function, end = "end def", one = 0):
        toreturn = None
        if one == 0:
            j=0
            func = self.functions[i]
            line = func
            script = self.script[func:]
            parametersF = getParametersF(script[0])
            script = script[1:index(script, end)]
            if len(parameters) > len(parametersF):
                printc(f"Error: too many parameters for function `{function}', at line {line}")
            if len(parameters) < len(parametersF):
                printc(f"Error: not enough parameters for function `{function}', at line {line}")
                return None
            for i in range(len(parametersF)):
                self.var[parametersF[i]] = parameters[i]
            while j != len(script):
                line2 = line + j
                showinfo2(root, 'Go to next line: {}'.format(line2))
                i = script[j]
                if iscond(i)[0] == 0 and isvar(i) != -1 and scanOperatorEqual(i) != -1:
                    self.scanVarI(i, line2)
                elif iscond(i)[0] == 1 and scanCondType(i) != -1:
                    self.scanCondI(i)
                elif iscond(i)[0] == 1:
                    toreturn = self.condI(i, line2, function[:function.find('(')])
                else:
                    toreturn = self.exec(i, line2, function[:function.find('(')])
                if type(toreturn) == type([1, 1]):
                    if toreturn[0] == "__Python__.__ls__.__sys__.__goto__":
                        j = toreturn[1]-line
                        toreturn = None
                else:
                    j += 1
            return toreturn
        else:
            line2 = line
            if iscond(i)[0] == 0 and isvar(i) != -1 and scanOperatorEqual(i) != -1:
                self.scanVarI(i)
            elif iscond(i)[0] == 1 and scanCondType(i) != -1:
                self.scanCondI(i)
            elif iscond(i)[0] == 1:
                toreturn = self.condI(i, line2, function[:function.find('(')])
            else:
                toreturn = self.exec(i, line2, function[:function.find('(')], 1)
        return toreturn
            
              
    def exec(self, function, line, lastF = "", obo = 0):
        func = ""
        function = notab(function)
        toreturn = None
        parameters = self.getParameters(function, lastF, line)
        for i in self.functions:
            nf = i[:search(i, "(")]+'()'
            tcf = function[:search(function, "(")]+'()'
            if nf == tcf:
                func = i
                if obo == 0:
                    toreturn = self.exec_(i, line, parameters, function)
                else:
                    toreturn = self.exec_one_by_one(i, line, parameters, function)
                break
        for i in self.default_function:
            nf = i[:search(i, "(")+1]+i[-1:]
            tcf = function[:search(function, "(")+1]+function[-1:]
            if nf == tcf:
                parametersF = getParametersF(i)
                if len(parameters) < len(parametersF):
                    printc(f"Error: not enough parameters for function `{function}', at line {line}")
                    return None
                func = i
                func = self.default_function[func]
                if func == 0:
                    printc(parameters[0])
                elif func == 1:
                    write(parameters[0], parameters[1])
                elif func == 2:
                    toreturn = read(parameters[0])
                elif func == 3:
                    toreturn = inputc(parameters[0])
                elif func == 4:
                    toreturn = parameters[0]
                elif func == 5:
                    try:
                        toreturn = len(parameters[0])
                    except:
                        printc(f"Error at line {line}, can't perform `len()'")
                elif func == 6:
                    toreturn = ["__Python__.__ls__.__sys__.__goto__", self.label[parameters[0]]]
                elif func == 7:
                    self.label[parameters[0]] = line+1
                elif func == 8:
                    toreturn = sin(parameters[0])
                elif func == 9:
                    toreturn = cos(parameters[0])
                elif func == 10:
                    toreturn = tan(parameters[0])
                elif func == 11:
                    toreturn = type(parameters[0])
                elif func == 12:
                    toreturn = self.typescan(parameters[0], line, test = 1)
                    if (toreturn == "var"):
                        toreturn = self.typescan(str(typescan(parameters[0], line)), line, test = 1)
                    break
                elif func == 13:
                    fpar = getParametersF(function)[0]
                    after = isvar(fpar)
                    try:
                        if isvar(after)[1][0] < islist(after)[1][0]:
                            index = getlist(after, self.var)[0]
                            s = isvar(after)
                            self.var[fpar[after[1][0]:after[1][1]]].pop(index)
                        s = isvar(after)
                        self.var[fpar[after[1][0]:after[1][1]]].pop()
                    except:
                        try:
                            if isvar(after)[1][0] < islist(after)[1][0]:
                                index = getlist(after, self.var)[0]
                                s = isvar(after)
                                self.var[lastF[:lastF.find('(')]+'.'+fpar[after[1][0]:after[1][1]]].pop(index)
                            s = isvar(after)
                            self.var[lastF[:lastF.find('(')]+'.'+fpar[after[1][0]:after[1][1]]].pop()
                        except:
                            printc(f"Error at line {line}, variable `{lastF[:lastF.find('(')]+'.'+fpar[after[1][0]:after[1][1]]}' referenced before assignent.")
                            printc("Prehaps you have forgot `raw' or `global' ?")
                            return -1
                    
                elif func == 14:
                    # list()
                    return [0 for i in range(parameters[0])]
        if func == "":
            printc(f"Error, function not found `{function}' at line {line}")
            return None
        return toreturn


global reader
reader = ls("")

def openFile(e = None):
    global file
    file = askopenfilename(title="Open",filetypes=[('Light Script files','.ls'),('all files','.*')])
    with open(file, 'r') as f:
        text_ = text.get("1.0", END)
        text.insert("1.0", f.read())
    root.title(' Light Script IDE - ' + file)
    return 0


def saveFile(e = None):
    global file
    root.title(' Light Script IDE - ' + file)
    if file == "NewFile":
        f = asksaveasfile(initialfile = file, defaultextension=".ls",filetypes=[("All Files","*.*"),("Light Script","*.ls")])
        f.write(text.get("1.0", END))
    else:
        with open(file, 'w') as f:
            f.write(text.get("1.0", END))
    return 0


def run(e = None):
    global reader
    printc('')
    printc('----- {} -----'.format(file))
    reader = ls(read(file))
    reader.parse(read(file))
    reader.var["noargs"] = [file]
    reader.exec("start(%noargs%)", 0, "file")


def run_lbl():
    global reader
    printc('')
    printc('----Debug line by line ----')
    printc('----- {} -----'.format(file))
    reader = ls(read(file))
    reader.parse(read(file))
    reader.var["noargs"] = [file]
    reader.exec("start(%noargs%)", 0, 1)


def runcustom():
    global reader
    args = askstring(root, 'Run Custom', 'Arguments:')
    printc('')
    printc('----- {} -----'.format(file))
    reader = ls(read(file))
    reader.parse(read(file))
    reader.var["__Python__.__LS__.__sys__.__argv__"] = [file, args]
    reader.exec("start(%__Python__.__LS__.__sys__.__argv__%)", 0)


def seevar():
    w = debugWindow('Variables', reader.var)
    return


def seecond():
    w = debugWindow('Conditions', reader.condition)
    return


def seefunc():
    w = debugWindow('Functions', reader.functions)
    return


def scanKeyWord(after):
    if search(after, "**=") != -1:
        return [search(after, "**="), searchend(after, "**=")]
    elif search(after, "*=") != -1:
        return [search(after, "*="), searchend(after, "*=")]
    elif search(after, "+=") != -1:
        return [search(after, "+="), searchend(after, "+=")]
    elif search(after, "-=") != -1:
        return [search(after, "-="), searchend(after, "-=")]
    elif search(after, "/=") != -1:
        return [search(after, "/="), searchend(after, "/=")]
    elif search(after, "%=") != -1 and isvar(after) == -1:
        return [search(after, "%="), searchend(after, "%=")]
    elif search(after, "=") != -1:
        return [search(after, "="), searchend(after, "=")]
    elif search(after, ">") != -1:
        return [search(after, ">"), searchend(after, ">")]
    elif search(after, "<") != -1:
        return [search(after, "<"), searchend(after, "<")]
    elif search(after, ">=") != -1:
        return [search(after, ">="), searchend(after, ">=")]
    elif search(after, "<=") != -1:
        return [search(after, "<="), searchend(after, "<=")]
    elif search(after, "==") != -1:
        return [search(after, "=="), searchend(after, "==")]
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
    elif search(after, "int ") != -1:
        return [search(after, "int "), searchend(after, "int ")]
    elif search(after, "str ") != -1:
        return [search(after, "str "), searchend(after, "str ")]
    elif search(after, "float ") != -1:
        return [search(after, "float "), searchend(after, "float ")]
    elif search(after, "bin ") != -1:
        return [search(after, "bin "), searchend(after, "bin ")]
    elif search(after, "hex ") != -1:
        return [search(after, "hex "), searchend(after, "hex ")]
    elif search(after, "global ") != -1:
        return [search(after, "global "), searchend(after, "global ")]
    elif search(after, "raw ") != -1:
        return [search(after, "raw "), searchend(after, "raw ")]
    return [-1, -1]

    
def execc_():
    j=0
    line = 1
    script = getAllLines(text.get("1.0", END), 1)
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


menubar = Menu(root)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Open     ctrl+o", command=openFile)
root.bind_all('<Control-o>', openFile)
menu1.add_command(label="Save      ctrl+s", command=saveFile)
root.bind_all('<Control-s>', saveFile)
menu1.add_separator()
menu1.add_command(label="Exit        ctrl+/", command=exit)
root.bind_all('<Control-slash>', exit)
menubar.add_cascade(label="File", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Run         F5", command=run)
root.bind_all('<F5>', run)
menu2.add_command(label="Run Custom...", command=runcustom)
menu2.add_command(label="Run Line by Line", command=run_lbl)
menubar.add_cascade(label="Run", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="Variables", command=seevar)
menu3.add_command(label="Conditions", command=seecond)
menu3.add_command(label="Functions", command=seefunc)
menubar.add_cascade(label="Debug", menu=menu3)

root.config(menu=menubar)

root.mainloop()
