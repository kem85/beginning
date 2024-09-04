#include <iostream>
using namespace std;
int power(long long int x,int y)
{
    int pow = 1;
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
    cout<<power(20,10);
}