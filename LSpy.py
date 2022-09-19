from sys import argv
from math import *

def printc(string):
    print(string)
    

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
    chars = "0123456789."
    if string != '':
        for i in range(len(string)):
            if not string[i] in chars:
                return 0
        return 1
    return 0
    

def isint(string):
    chars = "0123456789"
    if string != '':
        for i in range(len(string)):
            if not string[i] in chars:
                return 0
        return 1
    return 0


def isbin(string):
    chars = "0b1"
    if string != '':
        for i in range(len(string)):
            if not string[i] in chars:
                return 0
        return 1
    return 0


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
            parameters.append(afterr[s[1][0]:s[1][1]])
        else:
            pos = 0
        if search(after, ",") == -1:
            after = after[:-1]
        else:
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
    return -1


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
        # defining default vars
        self.var["pi"] = pi
        skip = 0
        for i in getAllLines(script):
            if skip != 1:
                if search(i, '#') != -1:
                    self.script.append(i[:search(i, '#')])
                else:
                    comma = search(i, ';')
                    if comma != -1:
                        self.script.append(i[:comma])
                        self.script.append(i[comma+1:])
                    else:
                        self.script.append(i)
            else:
                skip = 0


    def parse(self, script):
        for l in range(len(self.script)-1):
            subscript = self.script[l]
            if search(subscript, "def") != -1 and search(subscript, ":") != -1:
                self.functions[subscript[4:search(subscript, ':')]] = l


    def typescan(self, after, line, test = 0):
        after = notab(after)
        if test == 0:
            if islist(after)[0] and (isvar(after)[1][0] > islist(after)[1][0] or isvar(after)[0] == 0):
                return self.getlist(after, line)
            elif isfunc(after):
                return self.exec(after, line)
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
                if isvar(after)[1][0] < islist(after)[1][0]:
                    index = getlist(after, self.var)[0]
                    s = isvar(after)
                    return self.var[after[s[1][0]:s[1][1]]][index]
                s = isvar(after)
                return self.var[after[s[1][0]:s[1][1]]]
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


    def tokeytype(self, keytype, after, line):
        if keytype == -1:
            return self.typescan(after, line)
        elif keytype == "int":
            return int(self.typescan(after, line))
        elif keytype == "str":
            return str(self.typescan(after, line))
        elif keytype == "float":
            return float(self.typescan(after, line))
        elif keytype == "bin":
            return bin(self.typescan(after, line))
        elif keytype == "hex":
            return hex(self.typescan(after, line))
        else:
            return self.typescan(after, line)
        
            
    def scanVarI(self, l, line):
        pos = isvar(l)
        tosearch = scanOperatorEqual(l)
        posint = search(l, tosearch)
        after = l[posint+len(tosearch):]
        posi = pos[1]
        keytype = scankeyType(l)
        if tosearch == "->":
            self.scanPointI(l, line)
        if posint > islist(l)[1][0] and islist(l)[0] != 0:
            index = self.getlist(l, line)[0]
            if tosearch == "**=":
                self.var[l[posi[0]:posi[1]]][index] = self.var[l[posi[0]:posi[1]]][index] ** self.tokeytype(keytype, after, line)
            elif tosearch == "*=":
                self.var[l[posi[0]:posi[1]]][index] = self.var[l[posi[0]:posi[1]]][index] * self.tokeytype(keytype, after, line)
            elif tosearch == "+=":
                self.var[l[posi[0]:posi[1]]][index] = self.var[l[posi[0]:posi[1]]][index] + self.tokeytype(keytype, after, line)
            elif tosearch == "-=":
                self.var[l[posi[0]:posi[1]]][index] = self.var[l[posi[0]:posi[1]]][index] - self.tokeytype(keytype, after, line)
            elif tosearch == "/=":
                self.var[l[posi[0]:posi[1]]][index] = self.var[l[posi[0]:posi[1]]][index] / self.tokeytype(keytype, after, line)
            elif tosearch == "%=":
                self.var[l[posi[0]:posi[1]]][index] = self.var[l[posi[0]:posi[1]]][index] % self.tokeytype(keytype, after, line)
            elif tosearch == "^=":
                self.var[l[posi[0]:posi[1]]][index] = self.tokeytype(keytype, after, line) ^ semf.tokeytype(keytype, after, line)
            elif tosearch == "=":
                self.var[l[posi[0]:posi[1]]][index] = self.tokeytype(keytype, after, line)
        else:
            if tosearch == "**=":
                self.var[l[posi[0]:posi[1]]] = self.var[l[posi[0]:posi[1]]] ** self.tokeytype(keytype, after, line)
            elif tosearch == "*=":
                self.var[l[posi[0]:posi[1]]] = self.var[l[posi[0]:posi[1]]] * self.tokeytype(keytype, after, line)
            elif tosearch == "+=":
                self.var[l[posi[0]:posi[1]]] = self.var[l[posi[0]:posi[1]]] + self.tokeytype(keytype, after, line)
            elif tosearch == "-=":
                self.var[l[posi[0]:posi[1]]] = self.var[l[posi[0]:posi[1]]] - self.tokeytype(keytype, after, line)
            elif tosearch == "/=":
                self.var[l[posi[0]:posi[1]]] = self.var[l[posi[0]:posi[1]]] / self.tokeytype(keytype, after, line)
            elif tosearch == "%=":
                self.var[l[posi[0]:posi[1]]] = self.var[l[posi[0]:posi[1]]] % self.tokeytype(keytype, after, line)
            elif tosearch == "^=":
                self.var[l[posi[0]:posi[1]]] = self.var[l[posi[0]:posi[1]]] ^ self.tokeytype(keytype, after, line)
            elif tosearch == "=":
                self.var[l[posi[0]:posi[1]]] = self.tokeytype(keytype, after, line)


    def getParameters(self, function, line):
        parameters = []
        pos=1
        l = function
        after = l[search(l, "(")+1:l.rfind(")")]
        if l.rfind(')') == -1:
            after+=')'
        afterr = after
        while pos:
            if search(after, ",") != -1:
                afterr = after[:search(after, ",")+1]
            else:
                afterr = after
                
            if self.typescan(afterr, line, 1) != -1:
                parameters.append(self.tokeytype(-1, afterr, line))
            else:
                pos = 0
                
            if search(after, ",") == -1:
                after = after[:-1]
            else:
                after = after[search(after, ",")+1:]
        return parameters


    def getlist(self, string, line):
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
        return parameters


    def scanCondI(self, l):
        pos = iscond(l)
        after = l[search(l, "=")+1:]
        posi = pos[1]
        self.condition[l[posi[0]:posi[1]]] = notab(after)


    def scanPointI(self, l, line):
        before = l[:search(l, "->")]
        after = notab(l[searchend(l, "->"):])
        pos = isvar(after)[1]
        after = after[pos[0]:pos[1]]
        if self.typescan(before, line, 1) == "var":
            self.var[after] = '&'+before
        else:
            self.scanVarI(self.var[after]+'='+before, line)
        return

            
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
            after = self.tokeytype(-1, c[search(c, "=")+1:], line)
            before = self.tokeytype(-1, c[:search(c, "=")], line)
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
            script = script[1:index(script, end)]
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
                if iscond(i)[0] == 0 and isvar(i) != -1 and scanOperatorEqual(i) != -1:
                    self.scanVarI(i, line2)
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
            if iscond(i)[0] == 0 and isvar(i) != -1 and scanOperatorEqual(i) != -1:
                self.scanVarI(i, line)
            elif iscond(i)[0] == 1 and scanCondType(i) != -1:
                self.scanCondI(i)
            elif iscond(i)[0] == 1:
                toreturn = self.condI(i, line2)
            else:
                toreturn = self.exec(i, line2)
        return toreturn
    
              
    def exec(self, function, line, obo = 0):
        func = ""
        function = notab(function)
        toreturn = None
        parameters = self.getParameters(function, line)
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
                    printc("Error: not enough parameters for function `{}', at line {}".format(function, line+1))
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
                    toreturn = len(parameters[0])
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
                    toreturn = type(parameters[0])
                    break
        if func == "":
            printc("Error, function not found `{}' at line {}".format(function, line))
            return None
        return toreturn
    

def main():
    if (len(argv) != 0):
        reader = ls(read(argv[1]))
        reader.parse(read(argv[1]))
        reader.var["__Python__.__LS__.__sys__.__argv__"] = argv
        reader.exec("start(%__Python__.__LS__.__sys__.__argv__%)", 0)
    else:
        print("Specify a file to read")
    

main()
