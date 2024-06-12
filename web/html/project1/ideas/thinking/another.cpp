#include <iostream>
using namespace std;
void tasklist()
{
    for(int i = 0; i < 3;i++)
    {
        string s ="    - [ ] 1 ";
         cout<<s<<endl;
    }
}
int main()
{
    int select;
    cin>>select;
    string user;
    int count,day,month;
    if(select==1)
    {
        cout<<"Enter Count - Month - Day - User"<<endl<<">";
        cin>>count>>month>>day>>user;
        cout<<"---"<<endl;
        cout<<"#  Standup"<<" #"<<count<<((count==1) ? "st " : (count==2) ? "nd " : (count==3) ? "rd " : (count>3) ? "th " : "null ")<<"#2024/"<<month<<"/"<<day<<" #"<<user<<endl;
        cout<<"- **[Yesterday]:**"<<" [2024/"<<month<<"/"<<day-1<<"]"<<endl;
        tasklist();
        cout<<"- **[Today]:**"<<" [2024/"<<month<<"/"<<day<<"]"<<endl;
        tasklist();
    }
    else{
        cout<<"Enter Count - Month - Day"<<endl<<">";
        cin>>count>>month>>day;
        cout<<"---"<<endl;
        cout<<"#  Standup"<<" #"<<count<<((count==1) ? "st " : (count==2) ? "nd " : (count==3) ? "rd " : (count>3) ? "th " : "null ")<<"#2024/"<<month<<"/"<<day<<endl;
        cout<<"1. Abdullah Osama"<<endl;
        string g = "    - [ ] 1 ";
        cout<<g<<endl;
        cout<<"2. Yara Khairat"<<endl;
        cout<<g<<endl;
        cout<<"3. Ali Morgan"<<endl;
        cout<<g<<endl;
        cout<<"## General Statements"<<endl;
        g = "    -";
        cout<<g<<"suggestions/bugs: "<<endl<<g<<"1";
    }
}