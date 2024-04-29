#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <random>
using namespace std;
int rando (int x,int g)
{
    random_device rand;
    mt19937 gen(rand());
    uniform_int_distribution<>dis(x, g);
    return dis(gen);
}
vector<string> readip(string ip)
{
    vector<string> sp;
    string adding;
    int index=0;
    for (int i = 0; i < ip.size()+1; i++)
    {
        if(ip[i]=='.'||ip[i]=='/'||i==ip.size())
        {
            index++;
            sp.push_back(adding);
            adding.erase();
            continue;
        }
        adding+=ip[i];
    }
    return sp;
}
vector<string> subnetmask(int subnetmask)
{
    string add;
    int count = (subnetmask)+1;
    vector<string> subb;
    while(--count)
    {
        add.push_back('1');
        if(add.length()>=8)
        {
            subb.push_back(add);
            add.erase();
        }
    }
    count=33-subnetmask;
    while(--count)
    {
        add.push_back('0');
        if(add.length()>=8)
        {
            subb.push_back(add);
            add.erase();
        }
    }
    subb.push_back(add);
    return subb;
}
string binary(int decimal)
{
    int bin;
    string binary;
    for(int i = 0 ;; i++)
    {
        if(decimal % 2 == 0)
        {
            binary.push_back('0');
        }
        else
        {
            binary.push_back('1');
        }
        decimal /= 2;
        if(decimal==0){break;}
    }
    reverse(binary.begin(),binary.end());
    while(binary.length()<8)
    {
        binary.push_back('0');
        rotate(binary.rbegin(), binary.rbegin() + 1, binary.rend());
    }
    return binary;
}
string decimal(vector<string> binary)
{
    vector<int> decimal;
    string returner;
    int add=0,count=7;
    for(int i = 0 ; i < 4 ; i++)
    {
        for(int j = 0; j <= 7 ; j++)
        {
            add += (binary[i][j]-48)* pow(2, count--);
        }
        decimal.push_back(add);
        add=0;
        count=7;
    }
    for(int i = 0 ; i < 4 ; i++)
    {
        returner+=to_string(decimal[i]);
        if(i!=3){returner+=".";}
    }
    return returner;
}
vector<string> solution(vector<string> mask , vector<string> ip)
{
    vector<string> network,notmask,broadcast,solve;
    notmask.assign(mask.begin(), mask.end());
    string add;
    for(int i = 0 ; i < 4 ; i++)
    {
        for(int j = 0 ; j < 8 ; j ++)
        {
            if(mask[i][j]=='1'&&ip[i][j]=='1')
            {
                add.push_back('1');
                if(add.length()>=8)
                {
                    network.push_back(add);
                    add.erase();
                }
            }
            else
            {
                add.push_back('0');
                if(add.length()>=8)
                {
                    network.push_back(add);
                    add.erase();
                }
            }
        }
    }
    for(int i = 0 ; i < 4 ; i++)
    {
        for(int j = 0 ; j < 8 ; j++)
        {
            if(notmask[i][j]=='1')
            {
                notmask[i][j]='0';
            }
            else
            {
                notmask[i][j]='1';
            }
        }
    }
    for(int i = 0 ; i < 4 ; i++)
    {
        for(int j = 0 ; j < 8 ; j ++)
        {
            if(notmask[i][j]=='1'||ip[i][j]=='1')
            {
                add.push_back('1');
                if(add.length()>=8)
                {
                    broadcast.push_back(add);
                    add.erase();
                }
            }
            else
            {
                add.push_back('0');
                if(add.length()>=8)
                {
                    broadcast.push_back(add);
                    add.erase();
                }
            }
        }
    }
    solve.push_back(decimal(network));
    solve.push_back(decimal(broadcast));
    return solve;
}
string randomip(string classe)
{
    int all[5];
    string constru;
    if(classe=="a"||classe=="A") {
        all[0]=rando(1,126);
        for (int i = 1; i < 5; i++)
        {
        if (i == 4)
        {
            all[i] = rando(8, 32);
            break;
        }
        all[i] = rando(1, 223);
        }
        for(int i =0;i<5;i++)
        {
            if(i==4)
            {
                constru+="/";
                constru+=to_string(all[i]);
                break;
            }
            constru+=to_string(all[i]);
            if(i!=3){constru+=".";}
        }
    }
    else if(classe=="b"||classe=="B")
    {
        all[0]=rando(128,191);
        for (int i = 1; i < 5; i++)
        {
            if (i == 4)
            {
                all[i] = rando(8, 32);
                break;
            }
            all[i] = rando(1, 223);
        }
        for(int i =0;i<5;i++)
        {
            if(i==4)
            {
                constru+="/";
                constru+=to_string(all[i]);
                break;
            }
            constru+=to_string(all[i]);
            if(i!=3){constru+=".";}
        }
    }
    else if(classe=="c"||classe=="C")
    {
        all[0]=rando(192,223);
        for (int i = 1; i < 5; i++)
        {
            if (i == 4)
            {
                all[i] = rando(8, 32);
                break;
            }
            all[i] = rando(1, 223);
        }
        for(int i =0;i<5;i++)
        {
            if(i==4)
            {
                constru+="/";
                constru+=to_string(all[i]);
                break;
            }
            constru+=to_string(all[i]);
            if(i!=3){constru+=".";}
        }
    }
    return constru;
}
void answerr(string ip)
{
    vector<string> comp;
    vector<string> sp = readip(ip);
    vector<int> num, sub;
    for (int i = 0; i < 5; i++) {
        string str = sp[i];
        num.push_back(stoi(str));
        comp.push_back(binary(num[i]));
    }
    vector<string> subnett = subnetmask(num[4]);
    vector<string> collect = solution(subnett, comp);
    cout << "Network: " << collect[0] << endl;
    cout << "Broadcast: " << collect[1] << endl;
    cout << "SubnetMask: " << decimal(subnett) << endl;
    string clas = (num[0]>=1&&num[0]<=126) ? "A" : (num[0]>=128&&num[0]<=191) ? "B" : (num[0]>=192&&num[0]<=223) ? "C" : "invaild";
    cout << "Class: "<<clas<<endl<<endl;
}
int main()
{
    string answer;
    while(true) {
        string ip;
        int selector;
        cout<<"[1] Select\n[2] Random\n";
        cin>>selector;
        if(selector==1)
        {
        cin >> ip;
        answerr(ip);
        }
        else
        {
        string clas,randoip;
        cout<<"Class:";
        cin>>clas;
        randoip=randomip(clas);
        cout<<randoip<<endl;
        cin>>answer;
        answerr(randoip);
        }
    }
}