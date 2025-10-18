#include <iostream>
#include <fstream>
using namespace std;
int main()
{
	ifstream dane ("dane_6_2.txt");
	ofstream wynik ("wynik_6_2.txt");
	string s,w;
	int d,i,j,p,k;
	char znak;
	for (i=0;i<700;i++)
		{ dane>>s>>k;
		  w="";
		  d=s.size();
		  k=k%26;
		  for (j=0;j<d;j++)
		  	{ p=(int)s[j]-k;
		  	  if (p<65) p=p+26;
		  	  w=w+(char)p; 
		  	  
		  	}
	   wynik<<w<<endl;
		}
		
		return 0;
}
