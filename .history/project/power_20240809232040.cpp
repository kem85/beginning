#include <iostream>
using namespace std;
float power(float x,float y)
{
    float pow = 1;
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
    cout<<power(2,100);
}