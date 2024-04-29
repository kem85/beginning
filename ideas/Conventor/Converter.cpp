#include <iostream>
using namespace std;
int power(int b,int p)
{
    int c=1;
    for(int i=0;i<p;i++)
    {
        c=c*b;
    }
    return c;
    
}
int main()
{
    char again='y';
    while(again=='y'||again=='Y')
    {
int o=0,sum=0,g,s=0,op=0,l,p=0;
string y,x;
again='n';
cout<<"\n[0] Decimal to Binary\n[1] Binary to Decimal\n[2] Decimal to Octal\n[3] Octal to Decimal\n";
    cin>>l;
    if(l==0)
    {
    cout<<"Enter Decimal:";
    cin>>g;
    cout<<"Binary: ";
    op=g;
    for(int i=0;;)
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
         else{for(int j=s-1;j>=0;j--){cout<<data[j];} }
    } 
    }
    else if(l==1)
    {
    cout<<"Enter Binary:";
    cin>>y;
    cout<<"Decimal: ";
    o=y.length();
    for(int i=0;i<y.length();i++) 
    {
        sum+=(y[i]-48)*power(2,--o); //-2
    }
    cout<<"Number:"<<sum<<endl;
    }
    else if(l==2)
    {
        cout<<"Enter Decimal:";
        cin>>g;
        cout<<"Octal: ";
        op=g;
        for(int i=0;;)
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
         else{for(int j=s-1;j>=0;j--){cout<<data[j];} }
    } 
    }
    else if(l==3)
    {
    cout<<"Enter Octal:";
    cin>>y;
    cout<<"Decimal: ";
    o=y.length();
    for(int i=0;i<y.length();i++) 
    {
        sum+=(y[i]-48)*power(8,--o); //-2
    }
    cout<<sum;
    }
    cout<<"\nCalculate again?\nY/N\n";
    cin>>again;
    }
}