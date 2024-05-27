#include <iostream>
#include <vector>
#include "functions.cpp"
using namespace std;
int main()
{
    while(true)
    {
    cout<<"Final Step [1]"<<endl<<"Detailed Steps[2]"<<endl;
    int step;
    cin>>step;
    int count  = 0;
    string eq,g;
    cout<<"Enter Equation: ";
    cin>>eq;
    vector<vector<int>> checked = sorter(check(eq));
    bool hasbrackets = false;
    int size = (checked[2].size() > 0) ? maxi(checked[2]) : 1;
    for(int i = 0 ; i < checked[2].size(); i++)
    {
        if(eq[i] == '(' || eq[i] == ')')
        {
            hasbrackets = true;
            break;
        }
    }
    if(!hasbrackets)
    {
        goto pablo;
    }
    for(int i = 0 ; i < checked[0].size(); i++)
    {
        int start = checked[0][i];
        int end = checked[1][i];
        string operation;
        for(int j = start+1 ; j<end ; j++)
        {
            operation += eq[j];
        }
        bool isyes = false;
        operation = clear(operation,0,0,true);
        for(int i = 0 ; i < operation.length(); i++)
        {
            if(operation[i] == '+' ||operation[i] == '-' ||operation[i] == '*' ||operation[i] == '/')
            {
                isyes = true;
                break;
            }
        }
        if(!isyes){continue;}
        else
        {
        eq = replace(eq,to_string(calc(operation)),start,end);
        i=0;
        checked = sorter(check(eq));
        count++;
        if(step == 2)
        {
            cout<<"Step Number "<<count<<endl;
            if(i<checked[2].size()-1)
            {
                cout<<eq<<endl;
            }
        }
        }

    }
    pablo:
    cout<<eq<<" = "<<calc(eq)<<endl<<"Number of operations: "<<count<<endl;
    }
}