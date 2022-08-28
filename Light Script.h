#pragma once

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <utility>
#include <cstdlib>
using namespace std;

typedef vector<pair<pair<int,float>, pair<string, vector<pair<pair<int,float>, string> > > > > list; //used
typedef pair<pair<int,float>, pair<string, list> > any; // used
typedef map<string, any> dict; // used

string any_to_string(any any_);
void replaceAll(string& s, const string& search, const string& replace);
string read(string file);
void write(string file, string towrite);
int search_one(string str, char chr);
int search(const string& str, const string& pattern);
int lastline(string s, string sub);
string getline(string s, int line);
vector<string> getAllLines(string s);
bool isstring(string str);
int* getstring(string str);
bool isvar(string str);
int* getvar(string str);
int iscond(string str);
int* getcond(string str);
bool isfunc(string s);
bool isfloat(string s);
bool isint(string s);
string replacevar(string s, dict var);
any scanCondType(string after);
any scanOperator(string after);
int calculate(string s);
bool ismath(string str, dict var);
int findchar(string s, char chr);
bool bislist(string str);
int* islist(string str);
string notab(string str);
list getlist(string str, dict var);
list getParametersF(std::string function);
list getParameters(string function, dict var);

class ls {
private:
    vector<string> script;
    map<string, int> functions;
    map<string, int> label;
    map<string, int> default_function;
    map<string, string> condition;
public:
    dict var;

    ls(string script);
    void parse();
    any typescan(string after);
    void scanVarI(string l);
    void scanCondI(string l);
    any condI(string l, int line);
    any exec_(string i, int line, list parameters, string function, bool one = 0);
    any exec(string function, int line);
};
