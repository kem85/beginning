#include <iostream>
using namespace std;
int main()
{
    int choose;
    string user[2]={"pablo",""},password[2]={"333",""};
    while(true){
    again:
    cout<<"[1] Login\n[2] Register\n";
    cin>>choose;
    if(choose==2)
    {
    cin>>user[0]>>password[0];
    goto again;
    }
    else
    {
        cin>>user[1]>>password[1];
        if(user[1]==user[0]&&password[0]==password[1])
        {
            cout<<"Login success\n";
        }
        
    }
    }s
}
