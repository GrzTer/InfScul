#include <bits/stdc++.h>
using namespace std;
string na2 (int n)
{ string w="";
  while (n>0)
    {int r=n%2;
         w=(char)(r+48)+w;
         n=n/2;
	}
return w;
}
bool palindrom(string s)
{ int i=0, d=s.size();
  while (i<d/2 && s[i]==s[d-1-i])i++;
  if (i==d/2) return true;
  else return false;
}
bool prawie(string s)
{   
	int d=s.size();
	int i=d-1, ileZer=0;
	while (s[i]=='0' and i>0) {ileZer++;i--;}
	for (int i=0;i<ileZer;i++) s='0'+s;
	if (palindrom(s)==true) return true;
	else return false;
	
}
 int main()
{ ifstream dane ("dane.txt");
  ofstream wynik ("wyniki4_2.txt");
int n;
string s;
int ilepali=0, ileprawie=0;

  for (int i=0;i<5000;i++)
     {dane>>n;
      s=na2(n);
      if (palindrom(s)==true) ilepali++;
      else 
      if (prawie(s)==true) ileprawie++;
	 }
 cout<<ilepali+ileprawie;
 wynik<<ilepali+ileprawie;
}

