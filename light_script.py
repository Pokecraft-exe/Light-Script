from sys import argv

def read(file):
    with open(file, 'r') as f:
        c = f.read()
    return c

def write(file, towrite):
    with open(file, 'w') as f:
        f.write(towrite)

"""
steps:
parse
execute
for
if
else
elif
while
math var
"""

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
        if args[i].find(sub) != -1:
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
    if string.find('%') != -1:
        pos.append(string.find('%')+1)
        string2 = string[string.find('%')+1:]
        if string2.find('%') != -1:
            pos.append(string2.find('%')+len(string)-len(string2))
            return (1, pos)
        else:
            return (0, (0,0))
    else:
        return (0, (0,0))

def isfunc(string):
    pos = []
    if string.find('(') != -1:
        if string.find(')') != -1:
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
        

def ismath(string):
    try:
        s = eval(string)
        return 1
    except:
        return 0


def findchar(lists, char):
  find=0
  for i in range(len(lists)-1):
    if lists[(i)] == char:
      find=find+1
  return find


def islist(string):
    if string.find('[') != -1:
        string = string[string.find('[')+1:]
        if string.find(']') != -1:
            return 1
        else:
            return 0
    else:
        return 0


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
    string = string[string.find('[')+1:]
    for i in range(findchar(string, ',')+1):
        s = string.find(',')
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
            string = string[string.find(',')+1:]
            passstr = string
            passed = 0
        elif isvar(string[:s].replace(' ', ''))[0]:
            f = isvar(string[:s])
            pos.append(var[string[s[1][0]:s[1][1]]])
            string = string[string.find(',')+1:]
            passstr = string
            passed = 0
        elif ismath(string[:s].replace(' ', '')):
            pos.append(eval(string[:s].replace(' ', '')))
            string = string[string.find(',')+1:]
            passstr = string
            passed = 0
        elif isint(string[:s].replace(' ', '')):
            pos.append(int(string[:s].replace(' ', '')))
            string = string[string.find(',')+1:]
            passstr = string
            passed = 0
        elif isfloat(string[:s].replace(' ', '')):
            pos.append(float(string[:s].replace(' ', '')))
            string = string[string.find(',')+1:]
            passstr = string
            passed = 0
        else:
            l = getlist(string[:string.find(']')+1], var)
            pos.append(l)
            passstr = string[string.find(',')+1:]
            for j in range(len(pos[len(pos)-1])):
                string = string[string.find(',')+1:]
    return pos


def getParametersF(function):
    parameters = []
    after = function[function.find("(")+1:-2]
    pos = 1
    while pos:
        if isvar(after)[0]:
            pos = 1
            s = isvar(after)
            parameters.append(after[s[1][0]:s[1][1]])
            if after.find(",") == -1:
                after = after[:-1]
            after = after[after.find(",")+1:]
        else:
            pos = 0
    return parameters


def getParameters(function, var):
    parameters = []
    pos=1
    l = function
    after = l[l.find("(")+1:-1]
    while pos:
        if islist(after):
            pos = 1
            parameters.append(getlist(after, var))
        elif isstring(after)[0]:
            pos = 1
            s = isstring(after)
            parameters.append(after[s[1][0]:s[1][1]])
        elif isfunc(after):
            pos = 1
        elif isvar(after)[0]:
            pos = 1
            s = isvar(after)
            parameters.append(var[after[s[1][0]:s[1][1]]])
        elif ismath(after):
            pos = 1
            parameters.append(eval(after))
        elif isint(after):
            pos = 1
            parameters.append(int(after))
        elif isfloat(after):
            pos = 1
            parameters.append(float(after))
        else:
            pos = 0
        if after.find(",") == -1:
            after = after[:-1]
        after = after[after.find(",")+1:]
    return parameters


class ls():
    def __init__(self, script):
        self.script = []
        self.functions = {}
        self.default_function = {}
        self.default_function[""] = -1
        self.default_function["print(%string%)"] = 0
        self.default_function["os.file.write(%file%, %string%)"] = 1
        self.default_function["os.file.read(%file%)"] = 2
        self.default_function["input(%string%)"] = 3
        self.default_function["return(%to_return%)"] = 4
        self.default_function["if(%compare1%, %mode%, %compare2%)"] = 4
        self.default_function["for(%number%)"] = 5
        self.var = {}
        for i in getAllLines(script):
            if i.find('#') != -1:
                if i[:i.find('#')] != '\n':
                    self.script.append(i[:i.find('#')])
            else:
                if i != '\n':
                    self.script.append(i)
            


    def parse(self, script):
        for l in range(len(self.script)-1):
            subscript = self.script[l]
            if subscript.find("def") != -1 and subscript.find(":") != -1:
                self.functions[subscript[4:subscript.find(':')]] = l


    def scanVarI(self, l):
        pos = isvar(l)
        if pos[0] and l.find("=") != -1:
            after = l[l.find("=")+1:]
            posi = pos[1]
            if islist(after): #no lists into lists into lists ex [[0, 3, [5, 6]], 0, 3]
                self.var[l[posi[0]:posi[1]]] = getlist(after, self.var)
            elif isfunc(after):
                s = 1
                self.var[l[posi[0]:posi[1]]] = self.exec(after, 0)
            elif isstring(after)[0]:
                s = isstring(after)
                self.var[l[posi[0]:posi[1]]] = after[s[1][0]:s[1][1]]
            elif isvar(after)[0]:
                s = isvar(after)
                self.var[l[posi[0]:posi[1]]] = self.var[after[s[1][0]:s[1][1]]]
            elif ismath(after.replace(' ', '')):
                self.var[l[posi[0]:posi[1]]] = eval(after.replace(' ', ''))
            elif isint(after.replace(' ', '')):
                self.var[l[posi[0]:posi[1]]] = int(after.replace(' ', ''))
            elif isfloat(after.replace(' ', '')):
                self.var[l[posi[0]:posi[1]]] = float(after.replace(' ', ''))


    def exec(self, function, line):
        func = ""
        function = notab(function)
        toreturn = None
        parameters = getParameters(function, self.var)
        j=0
        for i in self.functions:
            nf = i[:i.find("(")+1]+i[-1:]
            tcf = function[:function.find("(")+1]+function[-1:]
            if nf == tcf:
                func = self.functions[i]
                line = func
                script = self.script[func:]
                parametersF = getParametersF(script[0])
                script = script[1:script.index("end def")]
                if len(parameters) > len(parametersF):
                    print("Warning: too many parameters for function `{}'".format(function))
                if len(parameters) < len(parametersF):
                    print("Error: not enough parameters for function `{}'".format(function))
                    return None
                for i in range(len(parametersF)):
                    self.var[parametersF[i]] = parameters[i]
                while j != len(script):
                    i = script[j]
                    line2 = line + j
                    if i.find('=') != -1:
                        self.scanVarI(i)
                    else:
                        toreturn = self.exec(notab(i), line2)
                        if toreturn == ["__proc__", "__lScript__", "__if__", "__BreaK__"]:
                            for u in range(len(script)):
                                if script[u].find("end") != -1 and script[u].find("if") != -1:
                                    j = u
                        #toreturn = None
                    j += 1
                            
                break
        for i in self.default_function:
            nf = i[:i.find("(")+1]+i[-1:]
            tcf = function[:function.find("(")+1]+function[-1:]
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
                    if parameters [1] == "==":
                        if parameters[0] == parameters[2]:
                            script = self.script[func:]
                            parametersF = getParametersF(script[0])
                            script = script[1:script.index("end def")]
                            if len(parameters) > len(parametersF):
                                print("Warning: too many parameters for function `{}'".format(function))
                            if len(parameters) < len(parametersF):
                                print("Error: not enough parameters for function `{}'".format(function))
                                return None
                            for i in range(len(parametersF)):
                                self.var[parametersF[i]] = parameters[i]
                            while j != len(script):
                                i = script[j]
                                if i.find('=') != -1:
                                    self.scanVarI(i)
                                else:
                                    toreturn = self.exec(notab(i))
                                    if toreturn == ["__proc__", "__lScript__", "__if__", "__BreaK__"]:
                                        for u in range(len(script)):
                                            if script[u].find("end") != -1 and script[u].find("if") != -1:
                                                j = u
                                j += 1
                    elif parameters [1] == ">":
                        if parameters[0] > parameters[2]:
                            script = self.script[func:]
                            parametersF = getParametersF(script[0])
                            script = script[1:script.index("end def")]
                            if len(parameters) > len(parametersF):
                                print("Warning: too many parameters for function `{}'".format(function))
                            if len(parameters) < len(parametersF):
                                print("Error: not enough parameters for function `{}'".format(function))
                                return None
                            for i in range(len(parametersF)):
                                self.var[parametersF[i]] = parameters[i]
                            while j != len(script):
                                i = script[j]
                                if i.find('=') != -1:
                                    self.scanVarI(i)
                                else:
                                    toreturn = self.exec(notab(i))
                                    if toreturn == ["__proc__", "__lScript__", "__if__", "__BreaK__"]:
                                        for u in range(len(script)):
                                            if script[u].find("end") != -1 and script[u].find("if") != -1:
                                                j = u
                                j += 1
                    elif parameters [1] == "<":
                        if parameters[0] < parameters[2]:
                            script = self.script[func:]
                            parametersF = getParametersF(script[0])
                            script = script[1:script.index("end def")]
                            if len(parameters) > len(parametersF):
                                print("Warning: too many parameters for function `{}'".format(function))
                            if len(parameters) < len(parametersF):
                                print("Error: not enough parameters for function `{}'".format(function))
                                return None
                            for i in range(len(parametersF)):
                                self.var[parametersF[i]] = parameters[i]
                            while j != len(script):
                                i = script[j]
                                if i.find('=') != -1:
                                    self.scanVarI(i)
                                else:
                                    toreturn = self.exec(notab(i))
                                    if toreturn == ["__proc__", "__lScript__", "__if__", "__BreaK__"]:
                                        for u in range(len(script)):
                                            if script[u].find("end") != -1 and script[u].find("if") != -1:
                                                j = u
                                j += 1
                    elif parameters [1] == "!=":
                        if parameters[0] != parameters[2]:
                            script = self.script[func:]
                            parametersF = getParametersF(script[0])
                            script = script[1:script.index("end def")]
                            if len(parameters) > len(parametersF):
                                print("Warning: too many parameters for function `{}'".format(function))
                            if len(parameters) < len(parametersF):
                                print("Error: not enough parameters for function `{}'".format(function))
                                return None
                            for i in range(len(parametersF)):
                                self.var[parametersF[i]] = parameters[i]
                            while j != len(script):
                                i = script[j]
                                if i.find('=') != -1:
                                    self.scanVarI(i)
                                else:
                                    toreturn = self.exec(notab(i))
                                    if toreturn == ["__proc__", "__lScript__", "__if__", "__BreaK__"]:
                                        for u in range(len(script)):
                                            if script[u].find("end") != -1 and script[u].find("if") != -1:
                                                j = u
                                j += 1
                    elif parameters [1] == "<=":
                        if parameters[0] <= parameters[2]:
                            script = self.script[func:]
                            parametersF = getParametersF(script[0])
                            script = script[1:script.index("end def")]
                            if len(parameters) > len(parametersF):
                                print("Warning: too many parameters for function `{}'".format(function))
                            if len(parameters) < len(parametersF):
                                print("Error: not enough parameters for function `{}'".format(function))
                                return None
                            for i in range(len(parametersF)):
                                self.var[parametersF[i]] = parameters[i]
                            while j != len(script):
                                i = script[j]
                                if i.find('=') != -1:
                                    self.scanVarI(i)
                                else:
                                    toreturn = self.exec(notab(i))
                                    if toreturn == ["__proc__", "__lScript__", "__if__", "__BreaK__"]:
                                        for u in range(len(script)):
                                            if script[u].find("end") != -1 and script[u].find("if") != -1:
                                                j = u
                                j += 1
                    elif parameters [1] == ">=":
                        if parameters[0] >= parameters[2]:
                            script = self.script[func:]
                            parametersF = getParametersF(script[0])
                            script = script[1:script.index("end def")]
                            if len(parameters) > len(parametersF):
                                print("Warning: too many parameters for function `{}'".format(function))
                            if len(parameters) < len(parametersF):
                                print("Error: not enough parameters for function `{}'".format(function))
                                return None
                            for i in range(len(parametersF)):
                                self.var[parametersF[i]] = parameters[i]
                            while j != len(script):
                                i = script[j]
                                if i.find('=') != -1:
                                    self.scanVarI(i)
                                else:
                                    toreturn = self.exec(notab(i))
                                    if toreturn == ["__proc__", "__lScript__", "__if__", "__BreaK__"]:
                                        for u in range(len(script)):
                                            if script[u].find("end") != -1 and script[u].find("if") != -1:
                                                j = u
                                j += 1
                break
        if func == "":
            print("Error, function not found `{}'".format(function))
            return None
        return toreturn


def main():
    print(argv)
    reader = ls(read("test.ls"))
    reader.parse(read("test.ls"))
    reader.var["__Python__.__LS__.__sys__.__argv__"] = argv
    reader.exec("start(%__Python__.__LS__.__sys__.__argv__%)", 0)
    #print(reader.var)
    

main()
