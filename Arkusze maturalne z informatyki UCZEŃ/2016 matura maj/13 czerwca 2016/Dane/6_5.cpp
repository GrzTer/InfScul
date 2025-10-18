#include <iostream>
#include <fstream>
using namespace std;
long long zamiana(string s)
{ int p,k,d=s.size();
  long long w=0;p=(int)s[d-1]-48;
  for (k=0;k<d-1;k++)
    { w=w*p+(int)s[k]-48;
	}
  return w;
}
int main()
{ifstream dane ("liczby.txt");
int i,j,d;
long long p,min=10000000,maks=0;
string s,w1,w2;

for (i=0;i<999;i++)
  { dane>>s;
    p=zamiana(s);
    if (p<min) { min=p ;w1=s;  }
     else if (p>maks) { maks=p ;w2=s;  }
  }
cout<<"min="<<min<<"(10) "<<w1<<endl;
cout<<"maks="<<maks<<"(10) "<<w2<<endl;
return 0;
}

