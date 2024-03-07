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
    int g,sum;
    sum =0;
    string y,x;
    while(true)
    {
    cin>>y;
    g=y.length();
    for(int i=0;i<g;i++) //10 
    {
        sum+=(y[i]-48)*power(2,--g);
    }
    cout<<"Number:"<<sum<<endl;
    sum=0;
    }
}