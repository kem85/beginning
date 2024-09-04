#include <iostream>
using namespace std;
float power(float x,float y)
{
    float pow = 1;
    for(int i = 1;i<=y;i++)
    {
        cout<<i<<endl;
        pow *= x;
    }
    return pow;
}
int main(){
    cout<<power(2,100);
}