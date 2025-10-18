#include <iostream>
#include <fstream>
using namespace std;
int main()
{
	ifstream dane ("dane_6_3.txt");
	ofstream wynik ("wynik_6_3.txt");
	string s,szyfr,w;
	int d,i,j,p1,p2,k,p;
	  for (i=0;i<3000;i++)
		{ dane>>s>>szyfr;
		  w="";
		  d=s.size();
		  p1=(int)s[0]; p2=(int)szyfr[0]; 
		  k=p2-p1;
		  if (k<0)k=k+26;
		 for(j=0;j<d;j++)
			{ p=(int)s[j]+k;
		 	 if (p>90) p=p-26;
		 	 w=w+(char)p;
			}
	  	 if (szyfr!=w)
			wynik<<s<<endl;
		}
		
		return 0;
}
