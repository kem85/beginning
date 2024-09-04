#include <iostream>
using namespace std;
int power(int x,int y)
{
    int pow = 1;
    for(int i = 1;i<=y;i++)
    {
        pow *= x;
    }
    return pow;
}
int main(){
    cout<<power(20,10);
}