#include <iostream>
#include <fstream>
using namespace std;
int main()
{
	ifstream dane ("dane_6_1.txt");
	ofstream wynik ("wynik_6_1.txt");
	string s,w;
	int d,i,j,p,k;
	
	for (i=0;i<100;i++)
	{ dane>>s;
	  w="";
	d=s.size();
	k=107%26;
	for(j=0;j<d;j++)
		{ p=(int)s[j]+k;
		  if (p>90) p=64+p-90;  //mo¿na zapisaæ jako p=p-26
		  w=w+(char)p;
		  
		}
		wynik<<w<<endl;
	}
	return 0;
}
