#include <iostream>
using namespace std;
int main()
{
  int y[3]={0,0,0};
  int size=0;
  int l=0;
  string seq;
  cin>>seq;
  size=seq.length();
  int x[size];
  for(int i=0;i<size;i++)
  {
    if(y[2]==0)
    {
    x[i]=seq[i]-48;
    if(i==(size-1)){y[2]=1;i=-1;}
    }
else if(y[2]==1)
{
  for(int j=0;j<size;j++)
  {
    if(x[i]<x[j]&&x[i]!=x[j]) //2
    {

      cout<<x[i]<<" "<<x[j]<<" "<<j<<endl;//{4,1}{1,3}{3,2}
    }
    // if(y[0]==(size-1)){cout<<x[i];}
  }
}
  }
} 
  //4513

  //1345