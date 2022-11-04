#pragma once

#include <iostream>
#include <sstream>
#include <fstream>
#include <math.h>
#include <string>
#include <vector>
#include <map>
# define M_PI (float)3.141592653589793
using namespace std;

class LSobject {
private:
	string s = "0";
	vector<LSobject> l;
	char type = 'i';
public:
	LSobject() {
		s="0";
	}
	LSobject(long int new_int) {
		s = to_string(new_int);
		l = {};
		type = 'i';
	}
	LSobject(int new_int) {
		s = to_string(new_int);
		l = {};
		type = 'i';
	}
	LSobject(double new_float) {
		s = to_string(new_float);
		l = {};
		type = 'f';
	}
	LSobject(float new_float) {
		s = to_string(new_float);
		l = {};
		type = 'f';
	}
	LSobject(string new_string) {
		s = new_string;
		l = {};
		type = 's';
	}
	LSobject(const char* new_string) {
		s = new_string;
		l = {};
		type = 's';
	}
	LSobject(vector<LSobject> new_vector) {
		s = "0";
		l = new_vector;
		type = 'l';
	}
	LSobject(initializer_list<LSobject> new_vector) {
		s = "0";
		l = new_vector;
		type = 'l';
	}
	void append(LSobject o){
		s = "0";
		l.push_back(o);
		type = 'l';
	}
	void replace(int index, LSobject o){
		s = "0";
		l[index] = o;
		type = 'l';
	}
	void no_null(){
		s = "0";
		l.push_back(0);
		type = 'i';
	}
	bool is(char t) {if (t == type) {return 1;}return 0;}
    vector<LSobject> as_list() {return l;}
    string print() {
    	string ss;
		if (type == 'l') {
			ss += '[';
			int size = this->l.size();
    		for(int x = 0; x < size-1; x++){
    			ss += this->l[x].str() + ", ";
  			}
  			ss += this->l[size-1].str();
  			return ss + ']';
		} else {
			return this->s;
		}
		return ss;
	}
    float asf() {
    	if (type == 'i') {
    		return (float)stoi(s);
		} else if (type == 's') {
			return stof(s);
		} else if (type == 'f'){
			return stof(s);
		} else {
			return 0.0;
		}
	}
	long int as_int() {return (long int)asf();}
	string str() {return print();}
	bool operator==(LSobject b) {
		if ((is('i') || is('f')) && (b.is('i') || b.is('f'))) {
			if (asf() == b.asf()) {return 1;}
		} else if (is('s') && b.is('s')) {
			if (str() == b.str()) {return 1;}
		}
		return 0;
	}
	bool operator!=(LSobject b) {
		if ((is('i') || is('f')) && (b.is('i') || b.is('f'))) {
			if (asf() == b.asf()) {return 0;}
		} else if (is('s') && b.is('s')) {
			if (str() == b.str()) {return 0;}
		}
		return 1;
	}
	bool operator>=(LSobject b) {
		if ((is('i') || is('f')) && (b.is('i') || b.is('f'))) {
			if (asf() >= b.asf()) {return 1;}
		}
		return 0;
	}
	bool operator<=(LSobject b) {return !(asf() >= b.asf());}
	bool operator>(LSobject b) {
		if ((is('i') || is('f')) && (b.is('i') || b.is('f'))) {
			if (asf() > b.asf()) {return 1;}
		}
		return 0;
	}
	bool operator<(LSobject b) {return !(asf() > b.asf());}
};

typedef map<string, LSobject> dict;

void replaceAll(string& s, const string& search, const string& replace);
vector<string> read(string file);
void write(string file, string towrite);
int search_one(string str, char chr);
int search(string str, string pattern);
int lastline(string s, string sub);
string getline(string s, int line);
vector<string> getAllLines(string s);
bool isstring(string str);
vector<unsigned int> getstring(string str);
bool isvar(string str);
vector<int> getvar(string str);
int iscond(string str);
vector<int> getcond(string str);
bool isfunc(string s);
bool isfloat(string s);
bool isint(string s);
bool isbin(string s);
string getbin(long int a);
template< typename T >
string to_hex( T i );
bool ishex(string s);
string replacevar(string s, dict var);
LSobject scankeyType(string after);
LSobject scanCondType(string after);
LSobject scanOperator(string after);
long int calculate(string s);
bool ismath(string str, dict var);
int findchar(string s, char chr);
bool bislist(string str);
vector<int> islist(string str);
string notab(string str);
vector<string> getParametersF(std::string function);

class ls {
private:
    vector<string> script;
    map<string, int> functions;
    map<string, int> label;
    map<string, int> default_function;
    map<string, string> condition;
public:
    dict var;

    ls(vector<string> script_);
    void parse();
    LSobject typescan(string after, int line);
    LSobject typescan_test(string after);
    LSobject tokeytype(string keytype, string after, int line);
    void scanVarI(string l, int line);
    LSobject getParameters(string function, int line);
    LSobject getlist(string str, int line);
    void scanCondI(string l);
    void scanPointI(string l, int line);
    LSobject condI(string l, int line);
    LSobject exec_(string i, int line, LSobject parameters, string function, bool one = 0);
    LSobject exec(string function, int line);
};
