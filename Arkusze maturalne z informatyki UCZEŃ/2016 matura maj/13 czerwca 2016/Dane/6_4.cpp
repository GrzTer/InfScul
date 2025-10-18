#include <iostream>
#include <fstream>
using namespace std;
long long zamiana(string s)
{ int k,d=s.size();
  long long w=0;
  for (k=0;k<d-1;k++)
    { w=w*8+(int)s[k]-48;
	}
  return w;
}
int main()
{ifstream dane ("liczby.txt");
int i,j,d;
long long p,ile=0;
string s;

for (i=0;i<999;i++)
  { dane>>s;
     d=s.size();
    if (s[d-1]=='8') 
      {p=zamiana(s);
        ile=ile+p;
	  }
  }
	cout<<ile;

return 0;
}

