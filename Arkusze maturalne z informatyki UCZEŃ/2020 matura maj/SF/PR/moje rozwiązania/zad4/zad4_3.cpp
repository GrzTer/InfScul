#include <bits/stdc++.h>
using namespace std;
int tab[5000];
int tab2[10],tab3[10];
bool pary(int a, int b)
{
	for (int i=0;i<10;i++) {tab2[i]=0;tab3[i]=0;}
	while(a>0)
	  {int c=a%10;
	   tab2[c]++;
	   a=a/10;
	  }
	while(b>0)
	  {int c=b%10;
	   tab3[c]++;
	   b=b/10;
	  }
	int i=0;
	while (i<10)
	{if (tab2[i]==0 && tab3[i]!=0) return false;
	 if (tab3[i]==0 && tab2[i]!=0) return false;
	 i++;
	}
	return true;
}
 int main()
{ ifstream dane ("dane.txt");
  ofstream wynik ("wyniki4_3.txt");
int n,ile=0;

  for (int i=0;i<5000;i++) dane>>tab[i];
  
  for (int i=0;i<5000-1;i++)
  	for (int j=i+1;j<5000;j++)
  	   	{ int a=tab[i];
  	   	  int b=tab[j];
  	   	  if (pary(a,b)==true) ile++;
		}
   cout<<ile;
   wynik<<ile;
}

