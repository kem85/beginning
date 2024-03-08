#include <iostream>
using namespace std;
int main()
{
    int num;string prime;
    cout<<"Enter Your Number:";
    cin>>num;
    for(int i=1;i<=num;i++)
    {
        if(num%i==0&&i!=1&&num!=i||num==1)
        {
            prime="is not prime";break;
        }
        else
        {
            prime="is prime";
        }
    }
    cout<<prime;
}