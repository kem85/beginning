#include <iostream>
using namespace std;
int main()
{
    int op,g,s=0,l=0;
    cin>>g;
    op=g;
    for(;;)
    {
        if(op==0)
        {
            break;
        }
        else{op/=8;s++;} 
    }
    int data[s];
    for (int i=0;i<s;i++) //i=4 s=6
    {
        if(l==0)
        {
        data[i]=g%8;
        g/=8;
        if(i==s-1){l=1;i=s-2;}
        }
         else{for(int j=s-1;j>=0;j--){cout<<data[j];}}
    } 
}