#include <iostream>
#include <random>  
using namespace std;
int rando (int x,int g) //random function
    {
    random_device rand;  
    mt19937 gen(rand());  
    uniform_int_distribution<>dis(x, g);  
    return dis(gen);
    }
int main()
{
    char x='y';string s;
    int repeat,g;
    while(true)
    {
    sdsd:
    g=rando(1,3);
    if(g==repeat){goto sdsd;}
    else{
    s=(g==1) ? "A" : (g==2) ? "B":"C";
    cout<<rando(1,255)<<"."<<rando(30,155)<<"."<<rando(20,90)<<"."<<rando(1,255)<<"/"<<rando(8,32)<<endl;
     cout<<"Class: "<<s<<endl;
        cin>>x;
    }
    repeat=g;
    }
}