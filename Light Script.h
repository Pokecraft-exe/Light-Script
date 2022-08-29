#pragma once

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <cstdlib>
#include <type_traits>
#include <utility>
#include <typeinfo>
#include <cassert>
#include <bitset>
using namespace std;

template <class T>
using StorageType = typename decay<T>::type; 
struct Any
{
    bool is_null() const { return !ptr; }
    bool not_null() const { return ptr; }

    template<typename U> Any(U&& value)
        : ptr(new Derived<StorageType<U>>(forward<U>(value)))
    {

    }

    template<class U> bool is() const
    {
        typedef StorageType<U> T;

        auto derived = dynamic_cast<Derived<T>*> (ptr);

        return derived;
    }

    template<class U>
    StorageType<U>& as()
    {
        typedef StorageType<U> T;

        auto derived = dynamic_cast<Derived<T>*> (ptr);

        if (!derived)
            throw bad_cast();

        return derived->value;
    }

    template<class U>
    operator U()
    {
        return as<StorageType<U>>();
    }

    Any()
        : ptr(nullptr)
    {

    }

    Any(Any& that)
        : ptr(that.clone())
    {

    }

    Any(Any&& that)
        : ptr(that.ptr)
    {
        that.ptr = nullptr;
    }

    Any(const Any& that)
        : ptr(that.clone())
    {

    }

    Any(const Any&& that)
        : ptr(that.clone())
    {

    }

    Any& operator=(const Any& a)
    {
        if (ptr == a.ptr)
            return *this;

        auto old_ptr = ptr;

        ptr = a.clone();

        if (old_ptr)
            delete old_ptr;

        return *this;
    }

    Any& operator=(Any&& a)
    {
        if (ptr == a.ptr)
            return *this;

        swap(ptr, a.ptr);

        return *this;
    }
    
    void* print() {
    	if (is<int>()) {cout << as<int>();}
		if (is<float>()) {cout << as<float>();}
		if (is<string>()) {cout << as<string>();}
	}

    ~Any()
    {
        if (ptr)
            delete ptr;
    }

private:
    struct Base
    {
        virtual ~Base() {}

        virtual Base* clone() const = 0;
    };

    template<typename T>
    struct Derived : Base
    {
        template<typename U> Derived(U&& value) : value(forward<U>(value)) { }

        T value;

        Base* clone() const { return new Derived<T>(value); }
    };

    Base* clone() const
    {
        if (ptr)
            return ptr->clone();
        else
            return nullptr;
    }

    Base* ptr;
};

template<std::size_t N>
bool operator<(const std::bitset<N>& x, const std::bitset<N>& y)
{
    for (int i = N-1; i >= 0; i--) {
        if (x[i] ^ y[i]) return y[i];
    }
    return false;
}

template<std::size_t N>
bool operator>(const std::bitset<N>& x, const std::bitset<N>& y)
{
    for (int i = N-1; i >= 0; i--) {
        if (y[i] ^ x[i]) return x[i];
    }
    return false;
}

template<std::size_t N>
bool operator<=(const std::bitset<N>& x, const std::bitset<N>& y)
{
    if (x < y || x == y) {return true;}
    return false;
}

template<std::size_t N>
bool operator>=(const std::bitset<N>& x, const std::bitset<N>& y)
{
    if (x > y || x == y) {return true;}
    return false;
}

typedef vector<Any> list;
typedef map<string, Any> dict;

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
string scanCondType(string after);
string scanOperator(string after);
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
    Any typescan(string after);
    void scanVarI(string l);
    void scanCondI(string l);
    Any condI(string l, int line);
    Any exec_(string i, int line, list parameters, string function, bool one = 0);
    Any exec(string function, int line);
};
