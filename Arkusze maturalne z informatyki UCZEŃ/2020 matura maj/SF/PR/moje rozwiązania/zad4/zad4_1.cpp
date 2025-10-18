#include <bits/stdc++.h>
using namespace std;
bool pierwsza(int n)
{ if (n<2) return false;
  if (n==2)return true;
  int d=0;
  for (int i=1;i*i<=n;i++)
   if (n%i==0) d++;
   
   if (d==1)return true;
   else return false;
}
 int main()
{ ifstream dane ("dane.txt");
  ofstream wynik ("wyniki4_1.txt");
int n,maks=0,mini=100001, ile=0;
  for (int i=0;i<5000;i++)
     {dane>>n;
      if (pierwsza(n)==true)
         {ile++;
          if (n>maks) maks=n;
          if (n<mini) mini=n;
		 }
	 }
	cout<<"ile pierwszych: "<<ile<<endl;
	wynik<<"ile pierwszych: "<<ile<<endl;
	cout<<"najwieksza pierwsza: "<<maks<<endl;
	wynik<<"najwieksza pierwsza: "<<maks<<endl;
	cout<<cout<<"najmniejsza pierwsza: "<<mini<<endl;
	wynik<<cout<<"najmniejsza pierwsza: "<<mini<<endl;
}

