#include <iostream>
using namespace std;
int main()
{
    int num;
    cin>>num;
    for(int i=num;i>=1;i--)
    {
         again:
        for(int j=1;j<=i;j++)
        {
        if(i%j==0&&j!=1&&i!=j||i==1)
        {
            i--;
            goto again;
        }
        else if(i==j)
        {
            cout<<i<<" ";
            break;
        }
        
        }
    }
}