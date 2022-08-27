from sys import argv

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
                index = getlist(after)
                s = isvar(after)
                parameters.append(var[after[s[1][0]:s[1][1]]][index])
            else:
                s = isvar(after)
                parameters.append(var[after[s[1][0]:s[1][1]]])
        elif isvar(after)[0]:
            pos = 1
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
        self.default_function["input(%string%)"] = 3
        self.default_function["return(%to_return%)"] = 4
        self.default_function["free(%variable%)"] = 5
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
                index = getlist(after)
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
                print("Error: too many parameters for function `{}', at line {}".format(function, line))
            if len(parameters) < len(parametersF):
                print("Error: not enough parameters for function `{}', at line {}".format(function, line))
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
                    print(parameters[0])
                elif func == 1:
                    write(parameters[0], parameters[1])
                elif func == 2:
                    toreturn = read(parameters[0])
                elif func == 3:
                    toreturn = input(parameters[0])
                elif func == 4:
                    toreturn = parameters[0]
                elif func == 5:
                    f = 1
                elif func == 6:
                    toreturn = ["__Python__.__ls__.__sys__.__goto__", self.label[parameters[0]]]
                elif func == 7:
                    self.label[parameters[0]] = line+1
                break
        if func == "":
            print("Error, function not found `{}' at line {}".format(function, line))
            return None
        return toreturn


def main():
    reader = ls(read(argv[1]))
    reader.parse(read(argv[1]))
    reader.var["__Python__.__LS__.__sys__.__argv__"] = argv
    reader.exec("start(%__Python__.__LS__.__sys__.__argv__%)", 0)
    

main()
