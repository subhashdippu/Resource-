#include<iostream>
using namespace std;

class baseClass
{
public:
  baseClass()
  {
    cout << "I am baseClass constructor" << endl;
  }
  
  ~baseClass()
  {
    cout << "I am baseClass destructor" << endl;
  }
};

class derivedClass: public baseClass
{
public:
  derivedClass()
  {
    cout << "I am derivedClass constructor" << endl;
  }
  
  ~derivedClass()
  {
    cout <<"I am derivedClass destructor" << endl;
  }
};

int main()
{
  derivedClass D;
  return 0;
}