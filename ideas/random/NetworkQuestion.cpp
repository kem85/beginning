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
    int ipcheck(string ip)
    {
        char rep='y';
        int repeat,g=0,subnet,s=0,op=0,p=0;
        int xaxis[2]{0,0},yaxis[2]{0,0},dynamic[4][3],memory[4];
        int gaga;
        int newip[4];
        int octal[8]{128,64,32,16,8,4,2,1};
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
//                cout<<dynamic[xaxis[1]][yaxis[1]]<<"."; //12[5].45[6].674
                ips[g]+=to_string(dynamic[xaxis[1]][yaxis[1]]);
                yaxis[1]=0;
                xaxis[1]++;
                g++;
            }
//            cout << dynamic[xaxis[1]][yaxis[1]];
            ips[g]+=to_string(dynamic[xaxis[1]][yaxis[1]]);

            yaxis[1]++;
        }
        for(int i=0;i<xaxis[0]+1;i++)
        {
            newip[i]= stoi(ips[i]);
        }
        for(int i=0;i<xaxis[0]+1;i++)
        {
            //change decimal to octal then octal to binary... all this to change ip to binary, then we get subnet and do && and ||
        }
    }
int main()
{
    string ip;
    cin>>ip;
    ipcheck(ip);
}