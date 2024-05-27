#include <iostream>
#include <vector>
using namespace std;
int main()
{
    vector<string> adder(2);
    string eq;
    char sign;
    int index;
    cin>>eq;
    int size = eq.length();
    cout<<eq[((eq.length()/2)-2)]<<endl;
    for(int i = 0 ; i < size/2 ; i++)
    {
        if(eq[i] == '+' ||eq[i] == '-' ||eq[i] == '*' ||eq[i] == '/')
        {
            sign == eq[i];
        }
        adder[0] += eq[i];
    }
    for(int i = size/2 ; i < size ; i++)
    {
        adder[1] += eq[i];
    }
    cout<<adder[0]<<endl<<adder[1];
}