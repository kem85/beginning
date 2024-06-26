#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
vector<vector<int>> check(string eq) //checks brackets and numbers
{
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
     if(count > 0 || count < 0)
     {
        checked[0].push_back(-1);
        return checked;
     }
    for(int i = 0; i < brac.size()/2; i++)
    {
    if(brac[i][0] == 'o') 
    {
            for(int j = 0 ; j < brac.size(); j++)
            {
                cout<<i<<endl;
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
    return checked;
}
vector<vector<int>> sorter(vector<vector<int>> checked) //sorts for use brackets
{
    checked[2].clear();
    for(int i = 0 ; i < checked[0].size() ; i++)
    {
        int count=0;
        for(int j = 0 ; j < checked[0].size() ; j++)
        {
            if(checked[0][j] > checked[0][i] && checked[1][j] < checked[1][i])
            {
                count++;
            }
        }
        checked[2].push_back(count);
    }
    for(int i = 0 ; i < checked[0].size() ; i++)
    {
        for(int j = 0 ; j < checked[0].size(); j++)
        {
            if(checked[2][i] < checked[2][j])
            {
                swap(checked[0][i], checked[0][j]);
                swap(checked[1][i], checked[1][j]);
                swap(checked[2][i], checked[2][j]);
            }
        }
    }
    return checked;
}
string reverse(string str) //reverses string
{
    if(str.length() >= 2)
    {
     string l;
     for (int i = str.length() - 1; i >= 0; i--)
         l += str[i];
     return l;
    }
    return str;
}
int getcount(string str) //gets count for loop size
{
    int count = 0;
    for(int i = 0 ; i < str.length() ; i ++)
    {
        if(str[i] == '/'||str[i] == '-'||str[i] == '+'||str[i] == '*')
        {
            count++;
        }
    }
    return count;
}
string clear(string str,int start,int end,bool blear = false) //clears without replacing
{
    int g = str.length();
    if(!blear)
    {
    str.erase(start,(end-start)+1);
    return str;
    }
    else
    for(int i = 0 ; i < g; i++)
    {
        if(str[i] == '(' || str[i] == ')')
        {
            str.erase(i,1);
            i--;
        }
    }
    return str;
}
bool hassign(string eq) //checks boolean sign
{
    for(int i = 0 ; i < eq.length() ; i++)
    {
        if(eq[i] == '+' ||eq[i] == '-' ||eq[i] == '*' ||eq[i] == '/')
        {
            return true;
        }
    }
    return false;
}
string replace(string str,string rep,int start, int end) //replacer
{
    string store;
    str = clear(str,start,end);
    start--;
    end = start+1;
    for(int i = end ; i < str.length()+1 ; i ++)
    {
        store+=str[i];
    }
    str = clear(str,end,str.length());
    return (str + rep + store);
}
int maxi(vector<int> vec) //max indicator
{
    int max = vec[0];
    for(int i = 0; i < vec.size(); i ++)
    {
        if(max<vec[i])
        {
            max = vec[i];
        }
    }
    return max;
}
string calc(string num) //actual calculator
{
    if(!hassign(num))
    {
        return num;
    }
    num = clear(num,0,0,true);
    bool skip = false;
    int g = num.length();
    float cal= 0;
    int r,start,end = 1;
    string store; 
    int countr = getcount(num);
    for(int z = 0 ; z < countr ; z++)
    {
        for(int i = 0 ; i < num.length() ; i ++)
        {
            if((num[i] == '+' || (num[i] == '-')) && !skip)
            {
                //left
                string ladd = "";
                for(int j = i-1 ;j >= 0;j--)
                {
                    if(num[j] == '*' || num[j] == '/')
                    {
                        skip = true;
                        break; // dont do it man
                    }
                    else if(num[j] == '+' || (num[j] == '-'))
                    {
                        start = j+1;
                        break;
                    }
                    else if(j == 0)
                    {
                        start = 0;
                        ladd+=num[j];
                    }
                    else
                    {
                    ladd+=num[j];
                    }
                }
                //right
                string radd = "";
                for(int j = i+1 ;j < num.length();j++)
                {
                    if(num[j] == '*' || num[j] == '/')
                    {
                        skip = true;
                        break; // dont do it man
                    }
                    else if(num[j] == '+' || (num[j] == ('-')))
                    {
                        end = j-1;
                        break;
                    }
                    else if(j == num.length()-1)
                    {
                        end = j;
                        radd+=num[j];
                    }
                    else
                    {
                    radd+=num[j];
                    }
                }
                if(skip)
                {
                    break;
                }
                ladd = reverse(ladd);
                cal = (num[i] == '+') ? (stof(radd) + stof(ladd)) : (stof(ladd) - stof(radd));
                num.erase(start,(end-start)+1);
                num =  to_string(cal) + num;
                break;
            }
            else if(num[i] == '*' || num[i] == '/')
            {
                //left
                string ladd;
                for(int j = i-1 ;j >= 0;j--)
                {
                    if(num[j] == '+' || (num[j] == '-' ))
                    {
                        start = j+1;
                        break;
                    }
                    if(num[j] == '*' || num[j] == '/' ||num[j] == '+' || (num[j] == '-' ) )
                    {
                        start = j+1;
                        break;
                    }
                    else if(j == 0)
                    {
                        start = 0;
                        ladd+=num[j];
                    }
                    else
                    ladd+=num[j];
                }
                //right
                string radd;
                for(int j = i+1 ;j < num.length();j++)
                {
                    if(num[j] == '*' || num[j] == '/' ||num[j] == '+' || (num[j] == '-' ) )
                    {
                        end = j-1;
                        break;
                    }
                    else if(j == num.length()-1)
                    {
                        end = j;
                        radd+=num[j];
                    }
                    else
                    radd+=num[j];
                }
                ladd = reverse(ladd);
                string errorer= (num[i] == '*' ? to_string(stof(ladd)*stof(radd)) : (radd != "0") ? to_string(stof(ladd)/stof(radd)) :"c");
                if(errorer[0] == 'c')
                {
                    return "cant divide by zero";
                }
                else{
                    cal=stof(errorer);
                }
                num.erase(start,(end-start)+1);
                if(start!=0)
                {
                for(int k = start ; k < num.length() ; k++)
                {
                    store += num[k];
                }
                num.erase(start,(num.length()-2));
                for(int b = start,k = 0 ; b < start+(to_string(cal).length()) ; b ++,k++)
                {
                    num += to_string(cal)[k];
                }
                num += store;
                }
                else
                {
                    store = num;
                    for(int b = start,k = to_string(cal).length()-1; b < start+(to_string(cal).length()) ; b ++,k--)
                    {
                        num = to_string(cal)[k] + num;
                    }
                }
                store.clear();
                skip=false;
                i=0;
            }
        }
    }
    return to_string(cal);
}