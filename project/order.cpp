#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std; 
int main() 
{ 
    string eq;
    cin>>eq;
    vector<string> brac;
    vector<int> filter,index;
    vector<vector<int>> checked(3);
    int count = 0;
    for(int i = 0; i < eq.length() ; i++)
    {
        if(eq[i] == '(')
        {
            brac.push_back("o"+ to_string(++count));
            index.push_back(i);
        }
        if(eq[i] == ')')
        {
            brac.push_back('b'+ to_string(count--));
            index.push_back(i);
        }
    }
    for(int i = 0; i < brac.size() / 2; i++)
    {
    if(brac[i][0] == 'o') 
    {
            for(int j = 0 ; j < brac.size(); j++)
            {
                if(brac[i][1] == brac[j][1] && brac[j][0] == 'b' && !(binary_search(filter.begin(), filter.end(), index[i])))
                {
                    checked[0].push_back(index[i]);
                    checked[1].push_back(index[j]);
                    filter.push_back(index[i]);
                    filter.push_back(index[j]);
                } 
            }
    }
    }
    for(int i = 0; i < checked[0].size() ;i++)
    {
        cout<<checked[0][i]<<" "<<checked[1][i];
    }
} 