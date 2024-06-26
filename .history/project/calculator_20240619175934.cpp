#include <iostream>
#include <vector>
#include "functions.cpp"
using namespace std;
string allinone(string eq)
{
    int count  = 0;
    string g,problem;
    vector<vector<int>> checked = sorter(check(eq));
    if(checked[0] == -1)
    {
        cout<<"Invaild equation";
        return 0;
    }
    bool hasbrackets = false;
    for(int i = 0 ; i < eq.length(); i++)
    {
        if(eq[i] == '(' || eq[i] == ')')
        {
            hasbrackets = true;
            break;
        }
    }
    here:
    int size = (checked[2].size() > 0) ? maxi(checked[2])+1 : 0;
    if(!hasbrackets)
    {
        count++;
        goto pablo;
    }
    for(int i = 0 ; i < size; i++)
    {
        int start = checked[0][i];
        int end = checked[1][i];
        string operation;
        for(int j = start+1 ; j<end ; j++)
        {
            operation += eq[j];
        }
        cout<<operation<<endl;
        operation = clear(operation,0,0,true);
        if(!hassign(operation)){continue;}
        else
        {
        problem = eq;
        eq = replace(eq,to_string(calc(operation)),start,end);
        i=0;
        checked = sorter(check(eq));
            count++;
            // if(i<checked[2].size()-1)
            // {
            //     cout<<"Step Number "<<count<<endl;
            // }
            // if(i<checked[2].size())
            // {
            //     cout<<eq<<endl;
            // }
        goto here;
        }

    }
    pablo:
    return to_string(calc(eq));
}
int main()
{
    string eq;
    cout<<"Enter Equation: ";
    cin>>eq;
    vector<vector<int>> checked = sorter(check(eq));
    // if(eq.length() >= 400)
    // {
    // vector<string> equations = optimize(eq,checked);
    // cout<<allinone(eq);
    // }

        cout<<allinone(eq);
    
}