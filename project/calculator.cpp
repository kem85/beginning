#include <iostream>
#include <vector>
#include <string>
using namespace std;
string reverse(string str)
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
int getcount(string str)
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
int main()
{
    while(true){
    float cal=0;
    int l,r,start,end = 1;
    string num="",store; 
    cin>>num;
    int countr = getcount(num);
    for(int z = 0 ; z < countr ; z++)
    {
        for(int i = 0 ; i < num.length() ; i ++)
        {
            if((num[i] == '+' || (num[i] == '-')) && l != 2)
            {
                //left
                string ladd = "";
                for(int j = i-1 ;j >= 0;j--)
                {
                    if(num[j] == '*' || num[j] == '/')
                    {
                        l = 2;
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
                    ladd+=num[j];
                }
                //right
                string radd = "";
                for(int j = i+1 ;j < num.length();j++)
                {
                    if(num[j] == '*' || num[j] == '/')
                    {
                        l = 2;
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
                    radd+=num[j];
                }
                ladd = reverse(ladd);
                if(l == 2)
                {
                    break;
                }
                if(num[i] == '+')
                {
                    num.erase(start,(end-start)+1);
                    num =  to_string(stof(ladd) + stof(radd)) + num;
                    cal = (stof(radd) + stof(ladd));
                    break;
                }
                else
                {
                    cal = (stof(ladd) - stof(radd));
                    num.erase(start,(end-start));
                    num =  to_string(stof(ladd) - stof(radd)) + num;
                    break;
                }

            }
            else if(num[i] == '*' || num[i] == '/')
            {
                //left
                string ladd = "";
                for(int j = i-1 ;j >= 0;j--)
                {
                    if(num[j] == '+' || (num[j] == '-' ))
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
                string radd = "";
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
                cal = (num[i] == '*' ? stof(ladd)*stof(radd) : stof(ladd)/stof(radd));
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
                l=1;
                i=0;
            }
        }
    }
    cout<<cal<<endl;
    }
}
