#include <iostream>
#include <fstream>
using namespace std;
int main()
{ifstream dane ("liczby.txt");
int i,j,d,ile=0;
string s;
for (i=0;i<999;i++)
  { dane>>s;
    d=s.size();
    j=0;
    while (j<d && s[j]!='0') j++;
    if (j==d && s[d-1]=='4') ile++;
  }
	cout<<ile;
return 0;
}

