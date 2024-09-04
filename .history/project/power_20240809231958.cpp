#include <iostream>
using namespace std;
long long int power(long long int x,long long int y)
{
    long long int pow = 1;
    if(x > 30 || y > 15)
    {

    }
    for(int i = 1;i<=y;i++)
    {
        pow *= x;
    }
    return pow;
}
int main(){
    cout<<power(80,10);
}