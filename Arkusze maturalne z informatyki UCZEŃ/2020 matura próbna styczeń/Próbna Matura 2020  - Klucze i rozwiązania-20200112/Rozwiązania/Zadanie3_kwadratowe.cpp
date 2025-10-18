#include <iostream>

using namespace std;

int main()
{
    int n,a,b; cin>>n;
    int k[n+1];
    int p[n+1];
    p[0]=0;
    for (int i=1;i<=n; ++i) cin>>k[i];
    int m; cin>>m;
    for (int i=0; i<m; ++i)
        {   int s=0;
            cin>>a; cin>>b;
            for (int j=a; j<=b; ++j) s=s+k[i];
            cout<<s;
        }
    return 0;
}
