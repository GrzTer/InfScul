#include <iostream>
#include <fstream>
using namespace std;
int main()
{ifstream dane ("liczby.txt");
int i,d,ile=0;
string s;
for (i=0;i<999;i++)
  { dane>>s;
    d=s.size();
    if (s[d-1]=='8') ile++;
  }
	cout<<ile;
return 0;
}

