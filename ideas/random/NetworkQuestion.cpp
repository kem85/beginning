#include <iostream>
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
    }
int main()
{
    string ip;
    vector <int> check;
    cin>>ip;
    ipcheck(ip);
    // int decimal;
    // cin>>decimal;
    // check=toOctal(decimal);
    // for(int i=0;i<toOctal(decimal).size();i++){cout<<toOctal(decimal)[i];} //checker
    }
