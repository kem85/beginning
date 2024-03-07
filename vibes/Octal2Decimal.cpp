#include <iostream>
using namespace std;
int power(int b,int p)
{
    int c=1;
    for(int i=0;i<p;i++)
    {
        c=c*b;
    }
    return c;
    
}
int main()
{
    int o,sum=0;
    string y;
    cin>>y;
    o=y.length();
    for(int i=0;i<y.length();i++) 
    {
        sum+=(y[i]-48)*power(8,--o); //-2
    }
    cout<<sum;
}