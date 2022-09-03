from tkinter import *
from tkinter.filedialog import *
from sys import argv

global file
global text_
text_ = ""
file = "NewFile"
root = Tk(className = " Light Script IDE - NewFile")
root['bg'] = 'black'
frame = Frame(root)
frame.pack(pady=5, expand=True, fill='both')
frame.configure(background = 'black')
text = Text(frame, insertbackground="white", selectbackground="gray", background="black", foreground='white', undo=True)
text.pack(expand=True, fill='both')
text_ = text.get("1.0", END)
tags = []
menubar = Menu(root)

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


menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Open", command=openFile)
menu1.add_command(label="Save", command=saveFile)
menu1.add_separator()
menu1.add_command(label="Exit", command=exit)
menubar.add_cascade(label="File", menu=menu1)

root.config(menu=menubar)


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


def search_one(string, char):
    string = string + " "
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
    string = string + " "
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
    string = string + " "
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
            return i+M-1
    return -1
    

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


def findchar(lists, char):
  find=0
  for i in range(len(lists)-1):
    if lists[i] == char:
      find=find+1
  return find


def isfunc(string):
    pos = 0
    if search(string, ')') != -1:
        pos = search(string, ')')
        string = string[search(string, '(')+1:]
        if search(string, '(') != -1:
            return (1, (pos, search(string, ')')))
        else:
            return (0, (0, 0))
    else:
        return (0, (0, 0))


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

    
def exec_():
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
        exec_()
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
        print("Argument must be a path to a file")
else:
    if len(argv) > 2:
        print("LSide only take 1 argument")
        
root.mainloop()
