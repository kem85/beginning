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
int getcount(string str,bool neg)
{
    int count = 0;
    for(int i = 0 ; i < str.length() ; i ++)
    {
        if(str[i] == '/'||str[i] == '-'||str[i] == '+'||str[i] == '*')
        {
            count++;
        }
    }
    if(neg)
    {
        count--;
    }
    return count;
}
int main()
{
    while(true){
    bool neg,uni = false;
    int cal=0;
    int l,r,start,end = 1;
    string num="",store; 
    cin>>num;
    neg = (num[0]=='-'? true : false);
    int countr = getcount(num,neg);
    for(int z = 0 ; z < countr ; z++)
    {
        for(int i = 0 ; i < num.length() ; i ++)
        {
            if(neg&&i==0){uni=true;}
            else{uni=false;}
            if((num[i] == '+' || (num[i] == '-'&&!uni)) && l != 2)
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
                    else if(num[j] == '+' || (num[j] == '-'&&!uni))
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
                    else if(num[j] == '+' || (num[j] == ('-')&&!uni))
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
                    num.erase(start,end-start);
                    if(neg)
                    {
                        cal = (-stoi(ladd) + stoi(radd));
                    }
                    else
                    {
                    cal = (stoi(radd) + stoi(ladd));
                    neg = (cal < 0 ? true : false);
                    }
                        num =  to_string(stoi(ladd) + stoi(radd)) + num;
                    break;
                }
                else
                {
                    cal = (stoi(ladd) - stoi(radd));
                    neg = (cal < 0 ? true : false);
                    num.erase(start,(end-start)+1);
                    num =  to_string(stoi(ladd) - stoi(radd)) + num;
                    break;
                }

            }
            else if(num[i] == '*' || num[i] == '/')
            {
                //left
                string ladd = "";
                for(int j = i-1 ;j >= 0;j--)
                {
                    if(num[j] == '+' || (num[j] == '-' &&!uni))
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
                    if(num[j] == '*' || num[j] == '/' ||num[j] == '+' || (num[j] == '-' &&!uni) )
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
                cal = (num[i] == '*' ? stoi(ladd)*stoi(radd) : stoi(ladd)/stoi(radd));
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
                    for(int b = start,k = 0 ; b < start+(to_string(cal).length()) ; b ++,k++)
                    {
                        num = to_string(cal)[k] + num;
                    }
                }
                l=1;
                i=0;
            }
        }
    }
    cout<<cal<<endl;
    }
}
