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
        int repeat,g=0,subnet;
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

        }


        }
    }
int main()
{
    string ip;
    cin>>ip;
    ipcheck(ip);
}
//     x=0;
//     for(int i=0;i<ip.length();i++)
//     {
//         cout<<dynamic[x][i]<<endl;
//         if(i){x++;}
//     }
//     while(true)
//     {
//         repeat:
//         g = rando(1, 3);
//         if (g == repeat) { goto repeat; }
//         else
//         {
//               s = (g == 1) ? 'A' : (g == 2) ? 'B' : 'C';
//               subnet = (g == 1) ? rando(8, 32) : (g == 2) ? rando(16, 32) : rando(24, 32);
//               cout << rando(1, 255) << "." << rando(20, 200) << "." << rando(10, 140) << "." << rando(1, 255) << "/"<< subnet << endl;
//               cout << "Class: " << s << endl;
//               cin >> x;
//         }
//         repeat = g;
//     }