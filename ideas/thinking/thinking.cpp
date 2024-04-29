#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{	
<<<<<<< Updated upstream
    cout<<"pablo";
=======
    string inp;
    vector<char> sign,bracket;
    vector<int> indect[2];
    cin>>inp;
    for(int i=0;i<inp.length();i++)
    {
        sign.push_back((inp[i]=='*') ? '*' : (inp[i]=='+') ? '+': (inp[i]=='-') ? '-': (inp[i]=='/') ? '/': '0');
        bracket.push_back((inp[i] == '(') ? '(' : (inp[i] == ')') ? ')' : '0');
        if(sign[i] != '0')
        {
            indect[0].push_back(i);
        }
        if(bracket[i] != '0')
        {
            indect[1].push_back(i);
        }
    }

    for(int i = 0; i < sign.size(); i++)
    {
        cout<<sign[i];
    }
>>>>>>> Stashed changes
}