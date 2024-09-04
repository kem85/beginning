#include <iostream>
using namespace std;
int power(x,y)
{
    for(int i = 1;i<y;i++)
    {
        x *= x;
    }
}
int main(){
    cout<<power()
}