#include <iostream>
using namespace std;
float power(float x,float y)
{
    float pow = 1;
    for(int i = 1;i<=y;i++)
    {
        pow *= x;
    }
    return pow;
}
int main(){
    long long int x = 5;
    int y = 10;
    cout<<x*y;
}