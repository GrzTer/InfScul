#include <iostream>

using namespace std;

int main()
{
    int n,a,b; cin>>n;
    int k[n+1];
    int p[n+1];
    p[0]=0;
    for (int i=1;i<=n; ++i)
    {
        cin>>k[i];
        p[i]=p[i-1]+k[i];
    }
    int m; cin>>m;
    for (int i=0; i<m; ++i)
        {
            cin>>a; cin>>b;
            cout<<p[b]-p[a-1]<<endl;
        }
    return 0;
}
