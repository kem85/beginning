#include <iostream>

using namespace std;
int main() 
{
    int g=0;
    string x;
    getline(cin,x);
    for(int i=0;i<x.length();i++)
    {
        if(x[i]== ' ')
        {
            g++;
        }
    }
    cout<<"Words count: "<<x.size;
}