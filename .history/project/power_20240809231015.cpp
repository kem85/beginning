#include <iostream>
using namespace std;
int power(int x,int y)
{
    int pow;
    for(int i = 1;i<y;i++)
    {
        cout<<i<<endl;
        pow *= x;
    }
    return pow;
}
int main(){
    cout<<power(5,2);
}