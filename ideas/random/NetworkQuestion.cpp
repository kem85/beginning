#include <iostream>
<<<<<<< Updated upstream
#include <random>
#include <string>
using namespace std;
int rando (int num1,int num2) //random function
{
    random_device rand;
    mt19937 gen(rand());
    uniform_int_distribution<> dis(num1, num2);
    return dis(gen);
}
int power(int b,int p)
{
    int c=1;
    for(int i=0;i<p;i++)
    {
        c=c*b;
    }
    return c;
    
}
vector<int> tobinary(int g) //this converts deciaml to binary and puts it in an array
{
    int s=0,op=0,p=0;
    vector <int>binary;
    op=g;
    while(true)
    {
        if(op==0)
        {
            break;
        }
        else{op/=2;s++;} 
    }
 int data[s];
    for (int i=0;i<s;i++) //
    {
        if(p==0)
        {
        data[i]=g%2; //1250  0521
        g/=2;
        if(i==s-1){p=1;i=s-2;}
        }
         else{for(int j=s-1;j>=0;j--){binary.push_back(data[j]);}
        }
    }
    return binary;
}
vector <int> toOctal(int g)//same with binary
{
    vector <int> octal;
    int op=0,s=0,p=0;
    op=g;
        while(true)
    {
        if(op==0)
        {
            break;
        }
        else{op/=8;s++;} 
    }
    int data[s];
    for (int i=0;i<s;i++) //s=6  5
    {
        if(p==0)
        {
        data[i]=g%8;
        g/=8;
        if(i==s-1){p=1;i=s-2;}
        }
         else{for(int j=s-1;j>=0;j--){octal.push_back(data[j]);}}
    } 
return octal;
}
   int ipcheck(string ip)
    {
        int g=0;
        int xaxis[2]{0,0},yaxis[2]{0,0},dynamic[4][3],memory[4];
        int newip[4];
        vector <int> octal,binary;
        string ips[4];
        for(int i=0;i<ip.length();i++)
        {
            if(ip[i]=='.')
            {
                memory[g]=dynamic[xaxis[0]][yaxis[0]-1];
                xaxis[0]++;
                dynamic[xaxis[0]][yaxis[0]]=ip[i]-48;
                g++;
                yaxis[0]=0;
            }
            else
            {
                dynamic[xaxis[0]][yaxis[0]]=ip[i]-48;
                yaxis[0]++;
            }
        }
        g=0;
        for(int i=0;i<(ip.length()-xaxis[0]*2);i++)
        {
            if(memory[g]==dynamic[xaxis[1]][yaxis[1]])
            {
                ips[g]+=to_string(dynamic[xaxis[1]][yaxis[1]]);
                yaxis[1]=0;
                xaxis[1]++;
                g++;
            }
            ips[g]+=to_string(dynamic[xaxis[1]][yaxis[1]]);

            yaxis[1]++;
        }
        for(int i=0;i<xaxis[0]+1;i++)
        {
            newip[i]= stoi(ips[i]);
        }
        for(int i=0;i<xaxis[0]+1;i++)
        {
            octal=toOctal(newip[i]);
            binary=tobinary(octal);
            cout<<octal<<endl;
            for(int i=0;i<toOctal(decimal).size();i++){cout<<toOctal(decimal)[i];} //checker
        }
=======
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
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
    string ip;
    vector <int> check;
    cin>>ip;
    ipcheck(ip);
    // int decimal;
    // cin>>decimal;
    // check=toOctal(decimal);
    // for(int i=0;i<toOctal(decimal).size();i++){cout<<toOctal(decimal)[i];} //checker
    }
=======
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
>>>>>>> Stashed changes
