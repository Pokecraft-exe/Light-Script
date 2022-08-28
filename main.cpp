#include "Light Script.h"
using namespace std;


string any_to_string(any some_any) {
	std::stringstream ss;
	// Since the list is a data structure we have to add each element one by one 
	ss << some_any.first.first << " " << some_any.first.second << " " << some_any.second.first;
	for (auto val : some_any.second.second) {
		ss << " " << val;
	}
	return ss.str();
}
void replaceAll(string& s, const string& search, const string& replace) {
    for (size_t pos = 0; ; pos += replace.length()) {
        // Locate the substring to replace
        pos = s.find(search, pos);
        if (pos == string::npos) break;
        // Replace by erasing and inserting
        s.erase(pos, search.length());
        s.insert(pos, replace);
    }
}

string read(string file) {
    std::ifstream myfile; myfile.open(file.c_str());
    string c;
    myfile >> c;
    return c;
}

void write(string file, string towrite) {
    ofstream outfile(file.c_str());
    outfile << towrite;
}

int search_one(string str, char chr) {
    bool isinstring = 0;
    char first;
    int N = str.length();
    for (int i = 0; i < N; i++) {
        if (str[i] == '"') {
            if (isinstring == 1) {
                if (str[i] == first) {
                    isinstring = 0;
                }
            }
            else {
                isinstring = 1;
                first = '"';
            }
        }
        else if (str[i] == '\'') {
            if (isinstring == 1) {
                if (str[i] == first) {
                    isinstring = 0;
                }
            }
            else {
                isinstring = 1;
                first = '\'';
            }
        }
        if (str[i] == chr && isinstring == 0) {
            return i;
        }
    }
    return -1;
}

int search(const string& str, const string& pattern)
{
    int isinstring = 0;
    char first;
    int M = pattern.length();
    int N = str.length();

    for (int i = 0; i <= N - M; i++)
    {
        int jj = 0;

        if (str[i] == '"')
        {
            if (isinstring == 1)
            {
                if (str[i] == first)
                {
                    isinstring = 0;
                }
            }
            else
            {
                isinstring = 1;
                first = '"';
            }
        }
        else if (str[i] == '\'')
        {
            if (isinstring == 1)
            {
                if (str[i] == first)
                {
                    isinstring = 0;
                }
            }
            else
            {
                isinstring = 1;
                first = '\'';
            }
        }

        for (int j = 0; j < M; j++)
        {
            if (str[i + j] != pattern[j])
            {
                break;
            }

            jj = j;
        }

        if (jj == M - 1 && isinstring == 0)
        {
            return i;
        }
    }

    return -1;
}

int lastline(string s, string sub) {
    vector<string> args;
    int alist = 0;
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == '\n') {
            args.push_back("");
            alist = alist + 1;
        }
        else {
            args[alist] = args[alist] + s[i];
        }
    }
    for (int i = 0; i < args.size() - 1; i++) {
        if (search(args[i], sub) != -1) {
            return i;
        }
    }
}

string getline(string s, int line) {
    vector<string> args;
    int alist = 0;
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == '\n') {
            args.push_back("");
            alist = alist + 1;
        }
        else {
            args[alist] = args[alist] + s[i];
        }
    }
    return args[line];
}

vector<string> getAllLines(string s) {
    vector<string> args;
    int alist = 0;
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == '\n') {
            args.push_back("");
            alist = alist + 1;
        }
        else {
            args[alist] = args[alist] + s[i];
        }
    }
    return args;
}

bool isstring(string str) {
    int pos1 = -1, pos2 = -1;
    char tosearch = '"';

    if (str.find('"') < str.find("'")) {
        tosearch = '\'';
    }

    if ((pos1 = str.find(tosearch)) != -1) {
        pos2 = str.find(tosearch, pos1 + 1);
        return 1;
    }
    else {
        return false;
    }
}

int* getstring(string str) {
    int pos[2];
    char tosearch = '"';

    if (str.find('"') < str.find("'")) {
        tosearch = '\'';
    }

    if ((pos[0] = str.find(tosearch)) != -1) {
        pos[1] = str.find(tosearch, pos[0] + 1);
        return pos;
    }
    else {
        return pos;
    }
}

bool isvar(string str) {
    int pos[2] = { 0, 0 };
    if (search(str, "%") != -1) {
        pos[0] = search(str, "%") + 1;
        string str2 = str.substr(search(str, "%") + 1);
        if (search(str2, "%") != -1) {
            pos[1] = search(str2, "%") + str.length() - str2.length();
            return 1;
        }
        else {
            return 0;
        }
    }
    else {
        return 0;
    }
}

int* getvar(string str) {
    int pos[2];
    if (search(str, "%") != -1) {
        pos[0] = search(str, "%") + 1;
        string str2 = str.substr(search(str, "%") + 1);
        if (search(str2, "%") != -1) {
            pos[1] = search(str2, "%") + str.length() - str2.length();
            return pos;
        }
        else {
            return pos;
        }
    }
    else {
        return pos;
    }
}

int iscond(string str)
{
    int pos[2];
    if (search(str, "$") != -1)
    {
        pos[0] = search(str, "$") + 1;
        string str2 = str.substr(search(str, "$") + 1);
        if (search(str2, "$") != -1)
        {
            pos[1] = search(str2, "$") + str.length() - str2.length();
            return 1;
        }
        else
        {
            return 0;
        }
    }
    else
    {
        return 0;
    }
}

int* getcond(string str)
{
    int pos[2];
    if (search(str, "$") != -1)
    {
        pos[0] = search(str, "$") + 1;
        string str2 = str.substr(search(str, "$") + 1);
        if (search(str2, "$") != -1)
        {
            pos[1] = search(str2, "$") + str.length() - str2.length();
            return pos;
        }
        else
        {
            return pos;
        }
    }
    else
    {
        return pos;
    }
}

bool isfunc(string s) {
    int pos = -1;
    if ((pos = s.find('(')) != -1) {
        if (s.find(')') != -1) {
            return true;
        }
        else {
            return false;
        }
    }
    else {
        return false;
    }
}

bool isfloat(string s) {
    try {
        s = stof(s);
        return true;
    }
    catch (...) {
        return false;
    }
}

bool isint(string s) {
    try {
        s = stoi(s);
        return true;
    }
    catch (...) {
        return false;
    }
}

string replacevar(string s, dict var) {
    int i = isvar(s);
    int* posi = getvar(s);
    while (i) {
        string toreplace = s.substr(posi[0] - 1, posi[1] + 1);
        replaceAll(s, toreplace, any_to_string(var[toreplace.substr(1, toreplace.length() - 2)]));
        i = isvar(s);
        posi = getvar(s);
    }
    return s;
}

any scanCondType(string after) {
    if (after.find("==") != string::npos) {
        return "==";
    }
    else if (after.find(">") != string::npos) {
        return ">=";
    }
    else if (after.find("<") != string::npos) {
        return "<";
    }
    else if (after.find("!=") != string::npos) {
        return "!=";
    }
    else if (after.find("<=") != string::npos) {
        return "<=";
    }
    else if (after.find(">=") != string::npos) {
        return ">=";
    }
    else {
        return -1;
    }
}

any scanOperator(string after) {
    if (after.find("**") != string::npos) {
        return "**";
    }
    else if (after.find("*") != string::npos) {
        return "*";
    }
    else if (after.find("+") != string::npos) {
        return "+";
    }
    else if (after.find("-") != string::npos) {
        return "-";
    }
    else if (after.find("//") != string::npos) {
        return "=";
    }
    else if (after.find("/") != string::npos) {
        return "/";
    }
    else if (after.find("%") != string::npos && isvar(after) == -1) {
        return "%";
    }
    else if (after.find("=") != string::npos) {
        return "=";
    }
    else {
        return -1;
    }
}

int calculate(string s) {
    int res = 0;
    char sign = '+';
    int num = 0;
    int n = s.size();
    for (int i = 0; i < n; i++) {
        if (s[i] >= '0' && s[i] <= '9') {
            num = num * 10 + s[i] - '0';
        }
        else if (s[i] == '(') {
            int j = i, cnt = 0;
            for (; i < n; i++) {
                if (s[i] == '(') cnt++;
                if (s[i] == ')') cnt--;
                if (cnt == 0) break;
            }
            num = calculate(s.substr(j + 1, i - j));
        }
        if (s[i] == '+' || s[i] == '-' || s[i] == '*' ||
            s[i] == '/' || s[i] == '%' || i == n - 1) {
            switch (sign) {
            case '+': res += num; break;
            case '-': res -= num; break;
            case '*': res *= num; break;
            case '/': res /= num; break;
            case '%': res %= num; break;
            }
            num = 0;
            sign = s[i];
        }
    }
    return res;
}

bool ismath(string str, dict var) {
    string s;
    if (scanOperator(str) != -1) {
        try {
            s = calculate(replacevar(str, var));
            return 1;
        }
        catch (...) {
            return 0;
        }
    }
    return 0;
}

int findchar(string s, char chr) {
    int count = 0;

    for (int i = 0; i < s.size(); i++)
        if (s[i] == chr) count++;

    return count;
}

bool bislist(string str)
{
    int pos = 0;
    if (search(str, "]") != -1)
    {
        pos = search(str, "]");
        str = str.substr(search(str, "[") + 1);
        if (search(str, "]") != -1)
        {
            return 1;
        }
        else
        {
            return 0;
        }
    }
    else
    {
        return 0;
    }
}

int* islist(string str)
{
    int pos[2];
    if (search(str, "]") != -1)
    {
        pos[0] = search(str, "]");
        str = str.substr(search(str, "[") + 1);
        if (search(str, "]") != -1)
        {
            pos[1] = search(str, "]");
            return pos;
        }
        else
        {
            return (0, 0);
        }
    }
    else
    {
        return (0, 0);
    }
}

string notab(string str) {
    bool isinstring = 0;
    char first;
    string nstr = "";
    for (int i; i < str.length(); i++) {
        if (str[i] == ' ') {
            if (isinstring == 1) {
                nstr = nstr + str[i];
            }
        }
        else {
            if (str[i] == '"') {
                if (isinstring == 1) {
                    if (str[i] == first) {
                        isinstring = 0;
                    }
                }
                else {
                    isinstring = 1;
                    first = '"';
                    nstr = nstr + str[i];
                }
            }
            else {
                if (str[i] == '\'') {
                    if (isinstring == 1) {
                        if (str[i] == first) {
                            isinstring = 0;
                        }
                    }
                    else {
                        isinstring = 1;
                        first = '\'';
                        nstr = nstr + str[i];
                    }
                }
                else {
                    nstr = nstr + str[i];
                }
            }
        }
    }
    return nstr;
}

list getlist(string str, dict var) {
    list pos;
    int passed;
    str = str.substr(search(str, "[") + 1);
    int s;
    for (int i; i < findchar(str, ','); i++) {
        s = search(str, ",");
        if (s == -1) {
            if (passed >= 1) {
                return pos;
            }
            else {
                passed += 1;
            }
        }
        if (isfunc(str.substr(0, s))) {
            cout << "Error, can't directly set function return as list value" << endl;
            string passstr = str;
            passed = 0;
        }
        else if (isstring(str.substr(0, s))) {
            int* f = getstring(str.substr(0, s));
            pos.push_back(str.substr(f[0], f[1]));
            str = str.substr(search(str, ",") + 1);
            string passstr = str;
            passed = 0;
        }
        else if (ismath(str.substr(0, s), var)) {
            pos.push_back(calculate(replacevar(str.substr(0, s), var)));
            str = str.substr(search(str, ",") + 1);
            string passstr = str;
            passed = 0;
        }
        else if (isvar(str.substr(0, s))) {
            int* f = getvar(str.substr(0, s));
            pos.push_back(var[str.substr(f[0], f[1])]);
            str = str.substr(search(str, ",") + 1);
            string passstr = str;
            passed = 0;
        }
        else if (isint(str.substr(0, s))) {
            pos.push_back(stoi(str.substr(0, s)));
            str = str.substr(search(str, ",") + 1);
            string passstr = str;
            passed = 0;
        }
        else if (isfloat(str.substr(0, s))) {
            pos.push_back(stof(str.substr(0, s)));
            str = str.substr(search(str, ",") + 1);
            string passstr = str;
            passed = 0;
        }
        else {
            list l = getlist(str.substr(0, search(str, "]") + 1), var);
            pos.push_back(l);
            string passstr = str.substr(search(str, ",") + 1);
            for (int j; j <= pos[pos.size() - 1].size(); j++) {
                str = str.substr(search(str, ",") + 1);
            }
        }
    }
    return pos;
}

list getParametersF(std::string function) {
    list parameters;
    std::string after = function.substr(function.find("(") + 1, -2);
    int pos = 1;
    while (pos) {
        if (isvar(after)) {
            pos = 1;
            int* s = getvar(after);
            parameters.push_back(after.substr(s[0], s[1]));
            if (search(after, ",") == -1) {
                after = after.substr(0, -1);
            }
            after = after.substr(search(after, ",") + 1);
        }
        else {
            pos = 0;
        }
    }
    return parameters;
}

list getParameters(string function, dict var) {
    list parameters;
    bool pos = 1;
    string l = function;
    string after = l.substr(search(l, "(") + 1, l.length() - 1);
    while (pos) {
        if (bislist(after) && (getvar(after)[0] > islist(after)[0] || isvar(after) == 0)) {
            pos = 1;
            parameters.push_back(getlist(after, var));
        }
        else if (isstring(after)) {
            pos = 1;
            int* s = getstring(after);
            parameters.push_back(after.substr(s[0], s[1]));
        }
        else if (isfunc(after)) {
            pos = 1;
        }
        else if (ismath(after, var)) {
            pos = 1;
            parameters.push_back(calculate((replacevar(after, var))));
        }
        else if (isint(after)) {
            parameters.push_back(std::stoi(after));
        }
        else if (isfloat(after)) {
            parameters.push_back(std::stof(after));
        }
        else if (isstring(after)) {
            parameters.push_back(after.substr(1, after.length() - 2));
        }
        else if (isvar(after)) {
            std::string varName = after.substr(0, after.find("["));
            std::string index = after.substr(after.find("[") + 1, after.find("]") - after.find("[") - 1);
            parameters.push_back(var.at(varName)[std::stoi(index)]);
        }
        else {
            pos = 0;
        }
        if (search(after, ",") == -1) {
            after = after.substr(0, after.length() - 1);
        }
        after = after.substr(after.find(",") + 1, after.length());
    }
    return parameters;
}

vector<string> sub(vector<string> vec, int pos1, int pos2) {
    vector<string> vec2;
    for (int i; i < vec.size(); i++) {
        if (i >= pos1 && i <= pos2) {
            vec2.push_back(vec[i]);
        }
    }
    return vec2;
}

int index(vector<string> vec, string str) {
    for (int i; i < vec.size(); i++) {
        if (vec[i] == str) {
            return i;
        }
    }
}

ls::ls(string script_) {
    default_function[""] = -1;
    default_function["print(%string%)"] = 0;
    default_function["os.file.write(%file%, %string%)"] = 1;
    default_function["os.file.read(%file%)"] = 2;
    default_function["input(%string%)"] = 3;
    default_function["return(%to_return%)"] = 4;
    default_function["free(%variable%)"] = 5;
    default_function["goto(%name%)"] = 6;
    default_function["label(%name%)"] = 7;
    for (string& i : getAllLines(script_)) {
        if (search(i, "#") != -1) {
            script.push_back(i.substr(0, search(i, "#")));
        }
        else {
            script.push_back(i);
        }
    }
}

void ls::parse() {
    for (int l = 0; l < script.size() - 1; l++) {
        string subscript = script[l];
        if (subscript.find("def") != std::string::npos && subscript.find(":") != std::string::npos) {
            functions[subscript.substr(4, subscript.find(':') - 4)] = l;
        }
    }
}

any ls::typescan(string after) {
    if (bislist(after) && (getvar(after)[0] > islist(after)[0] || isvar(after) == 0)) {
        return getlist(after, var);
    } else if (isfunc(after)) {
        return exec(after, 0);
    } else if (isstring(after)) {
        int* s = getstring(after);
        return after.substr(s[0], s[1]);
    } else if (ismath(after, var)) {
        return calculate(replacevar(after, var));
    } else if (isvar(after)) {
        if (getvar(after)[0] < islist(after)[0]){
            list index = getlist(after, var);
            int* s = getvar(after);
            return var[after.substr(s[0], s[1])][index];
        }
        int* s = getvar(after);
        return var[after.substr(s[0], s[1])];
    } else if (isint(after)) {
        return stoi(after);
    }
    else if (isfloat(after)){
     return stof(after);
    }
}

void ls::scanVarI(string l) {
    int* pos = getvar(l);
    string after = l.substr(search(l, "=") + 1);
    var[l.substr(pos[0], pos[1])] = typescan(after);
}

void ls::scanCondI(string l) {
    int* pos = getcond(l);
    string after = l.substr(search(l, "=") + 1);
    condition[l.substr(pos[0], pos[1])] = notab(after);
}

any ls::condI(string l, int line) {
    bool pos = iscond(l);
    int* posi = getcond(l);
    bool iselse = false;
    string c;
    if (pos) {
        posi = getcond(l);
        string f = notab(l.substr(posi[1] + 1));
        if (search(l, "!") == posi[0]) {
            iselse = 1;
            c = condition[l.substr(posi[0] + 1, posi[1])];
        }
        else {
            c = condition[l.substr(posi[0], posi[1])];
        }
        any after = typescan(c.substr(search(c, "=") + 1));
        any before = typescan(c.substr(0, search(c, "=")));
        if (search(c, "==") != -1) {
            if (before == after) {
                if (!iselse) {
                    return exec_(f, line, {}, f, 1);
                }
            } else {
                if (iselse) {
                    return exec_(f, line, {}, f, 1);
                }
            }
        } else if (search(c, ">") != -1) {
            if (before > after) {
                if (!iselse) {
                    return exec_(f, line, {}, f, 1);
                }
            } else {
                if (iselse) {
                    return exec_(f, line, {}, f, 1);
                }
            }
        } else if (search(c, "<") != -1) {
            if (before < after) {
                if (!iselse) {
                    return exec_(f, line, {}, f, 1);
                }
            } else {
                if (iselse) {
                    return exec_(f, line, {}, f, 1);
                }
            }
        } else if (search(c, "!=") != -1) {
            if (before != after) {
                if (!iselse) {
                    return exec_(f, line, {}, f, 1);
                }
            } else {
                if (iselse) {
                    return exec_(f, line, {}, f, 1);
                }
            }
        } else if (search(c, "<=") != -1) {
            if (before <= after) {
                if (!iselse) {
                    return exec_(f, line, {}, f, 1);
                }
            } else {
                if (iselse) {
                    return exec_(f, line, {}, f, 1);
                }
            }
        } else if (search(c, ">=") != -1) {
            if (before < after) {
                if (!iselse) {
                    return exec_(f, line, {}, f, 1);
                }
            } else {
                if (iselse) {
                    return exec_(f, line, {}, f, 1);
                }
            }
        }
    }
}

any ls::exec_(string i, int line, list parameters, string function, bool one = 0) {
    any toreturn;
    if (!one) {
        int j = 0;
        string end = "end def";
        int func = functions[i];
        int line = func;
        vector<string> script_ = sub(script, func, script.size());
        list parametersF = getParametersF(script[0]);
        vector<string>::iterator itr = find(script_.begin(), script_.end(), end);
        script_ = sub(script_, 1, index(script_, end));
        if (parameters.size() > parametersF.size()) {
            cout << "Error: too many parameters for function `" << function << "', at line " << line << endl;
        }
        if (parameters.size() > parametersF.size()) {
            cout << "Error: not enough parameters for function `" << function << "', at line " << line << endl;
            return nullptr;
        }
        for (int i; i < parametersF.size(); i++) {
            var[parametersF[i]] = parameters[i];
        }
        while (j != script_.size()) {
            int line2 = line + j;
            string i = script_[j];
            if (!iscond(i) && isvar(i) && scanOperator(i) != -1) {
                scanVarI(i);
            }
            else if (iscond(i) && scanCondType(i) != -1) {
                scanCondI(i);
            }
            else if (iscond(i)) {
                toreturn = condI(i, line2);
            }
            else {
                toreturn = exec(i, line2);
            }
            try {
                if (toreturn[0] == "__Python__.__ls__.__sys__.__ goto__") {
                    j = toreturn[1] - line;
                    toreturn = nullptr;
                }
            }
            catch (...) {
                j += 1;
            }
            return toreturn;
        }
    }
    else {
        int line2 = line;
        if (!iscond(i) && isvar(i) && scanOperator(i) != -1) {
            scanVarI(i);
        } else if (iscond(i) && scanCondType(i) != -1) {
            scanCondI(i);
        } else if (iscond(i)) {
            toreturn = condI(i, line2);
        } else {
            toreturn = exec(i, line2);
        }
    }
    return toreturn; 
}

any ls::exec(string function, int line) {
    any func = "";
    string function_ = notab(function);
    any toreturn;
    any parameters = getParameters(function, var);
    for (std::map<string, int>::iterator it = functions.begin(); it != functions.end(); ++it) {
        string i = it->first;
        string nf = i.substr(0, search(i, "(") + 1) + i.substr(-1);
        string tcf = function.substr(0, search(function, "(") + 1) + function.substr(-1);
            if (nf == tcf) {
                func = i;
                    toreturn = exec_(i, line, parameters, function);
                    break;
            }
    }
    for (std::map<string, int>::iterator it = default_function.begin(); it != default_function.end(); ++it) {
        string i = it->first;
        string nf = i.substr(0, search(i, "(") + 1) + i.substr(-1);
        string tcf = function.substr(0, search(function, "(") + 1) + function.substr(-1);
        if (nf == tcf) {
            func = i;
            func = default_function[func];
            if (func == 0) {
                cout << parameters[0];
            }
            else if (func == 1) {
                write((string)parameters[0], (string)parameters[1]);
            }
            else if (func == 2) {
                toreturn = read((string)parameters[0]);
            }
            else if (func == 3) {
                cout << parameters[0];
                cin >> toreturn;
            }
            else if (func == 4) {
                toreturn = parameters[0];
            }
            else if (func == 5) {
                bool f = 1;
            }
            else if (func == 6) {
                toreturn = { "__Python__.__ls__.__sys__.__goto__", label[parameters[0]] };
            }
            else if (func == 7) {
                label[parameters[0]] = line + 1;
            }
            break;
        } 
    }
    if (func == "") {
        cout << "Error, function not found `" << function << "' at line " << line << endl;
            return nullptr;
    }
    return toreturn;
}

int main(int argc, char* argv[])
{
    ls reader = ls(read(argv[1]));
    reader.parse();
    reader.var["__Python__.__LS__.__swys__.__argv__"] = argv;
    reader.exec("start(%__Python__.__LS__.__sys__.__argv__%)", 0);
	return 0;
}
