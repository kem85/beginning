#include <iostream>
#include <vector>
#include "functions.cpp"
#include <iomanip>
#include <fstream>
using namespace std;
string allinone(string eq,bool hasbracket)
{
    if(!hasbracket)
    {
        return calc(eq);
    }
    int count  = 0;
    string g;
    vector<vector<int>> checked = sorter(check(eq));
    if(checked[0][0] == -1)
    {
        return "E1";
    }
    here:
    int size = (checked[2].size() > 0) ? maxi(checked[2])+1 : 0;
    for(int i = 0 ; i < size; i++)
    {
        int start = checked[0][i];
        int end = checked[1][i];
        string operation;
        for(int j = start+1 ; j<end ; j++)
        {
            operation += eq[j];
        }
        operation = clear(operation,0,0,true); //clears brackets
        if(!hassign(operation)){continue;}
        else
        {
        if(lead(operation)=='1')
        {
            return "C";
        }
        bool haspower= false;
        if(end+1 != eq.length()-1&& eq[end+1] == '^')
        {
            haspower=true;
            cout<<operation<<endl;
        }
        eq = replace(eq,calc(operation),start,end);
        i=0;
        checked = sorter(check(eq));           
        count++;
        goto here;
        }

    }
    return calc(eq);
}
int main()
{
    here:
    int x = 1;
    if(x != 1)
    {ifstream file("C:/Users/kem7/Desktop/problem.txt");
    stringstream ggbuddy;
    ggbuddy << file.rdbuf();
    file.close();
    string eq = ggbuddy.str();}
    string eq;
    while(x == 1)
    {
    cin>>eq;
    if(lead(eq)=='1')
    {
        goto here;
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
    string answer = allinone(eq,hasbrackets);
    if(answer[0] == 'E') //error handling
    {
        if(answer=="E1")
        {
         cout<<"Invaild Equation [missing bracket]"<<endl;
        }
        else if(answer=="E2")
        {
        cout<<"Invaild Equation [Can't divide by zero]"<<endl;
        }
        else if(answer=="E3")
        {
        cout<<"Invaild Equation [E3]"<<endl;
        }
    }
    else if(answer[0]!='C'){
    cout<<setprecision(5)<<stof(answer)<<endl;}
    }
}