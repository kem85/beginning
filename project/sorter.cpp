#include <iostream>
#include <vector>
using namespace std;
vector<vector<int>>
int main()
{
    vector<int> g{7,7,7,1,1,1,1,1,2,3,4,6,8,9};
    for(int i = 0; i < g.size() ; i ++)
    {
        for(int j = 0 ; j < g.size(); j++)
        {
            if(g[i] < g[j])
            {
                int temp = g[i];
                g[i] = g[j];
                g[j] = temp;
            }
        }
    }
    for(int i = 0; i < g.size() ; i ++)
    {
        cout<<g[i];
    }
}