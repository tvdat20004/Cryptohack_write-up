#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define randomize mt19937_64 mt(chrono::steady_clock::now().time_since_epoch().count())
randomize;
bool get_mask(int x,int y)
{
    return (x>>y)&1;
}
void mahoa()
{
    string s;
    cin>>s;
    for(char c:s)
    {
        int type=mt()%2;
        int value=c-'A';
        int new_value=(!type)?(int)1:(int)-1;
        new_value=new_value*13;
        value=(value+new_value+26)%26;
        cout<<(char)(value+'A');
    }
}
void giaima()
{
    string s;
    cin>>s;
    int n=(int)s.size();
    for(int mask=0;mask<=(1<<n)-1;mask++)
    {
        string ans;
        for(int node=1;node<=n;node++)
        {
            int value=s[node-1]-'A';
            int type=get_mask(mask,node-1);
            int new_value=(!type)?(int)1:(int)-1;
            new_value=new_value*13;
            value=(value+new_value+26)%26;
            char c=(char)('A'+value);
            ans.push_back(c);
            bool ok;
            cin>>ok;
            if(ok)
            {
                cout<<ans;
                break;
            }
        }
    }
}
int main()
{
    string type;
    cin>>type;
    if(type=="MAHOA")mahoa();
    else giaima();
}

