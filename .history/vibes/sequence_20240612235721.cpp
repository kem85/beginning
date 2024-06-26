#include <iostream>
#include <array>
#include <vector>
#include <random>  
using namespace std;
int rando (int x,int g) //random function
    {
    random_device rand;  
    mt19937 gen(rand());  
    uniform_int_distribution<>dis(x, g);  
    return dis(gen);
    }
    vector <int> pluss () 
    {
        vector <int> vec ;
     int plusin = rando(rando(2,50),(55,100)),
     starter = rando(rando(2,50),rando(55,100));
     int answer;
    for(int i = 0;i <4;i++)
     {
         vec.push_back(starter);
         starter = (starter + plusin);
            if (i == 3)
                {
                    answer = starter;
                    vec.push_back(answer);
                }
    }
        return vec;
    }
    vector <int> devi (int admin) 
    {
        vector <int> vec ,memory;
     long long int devi,starter,answer,x=0,o=0,g=0,
     plus=0;
     long long int temp2,temp1;
        Againn: //delay 
        Again: //if starter % div != 0
        starter=rando(rando(6,6000),rando(6001,800000)); //the fun arena
        devi=rando(rando(10,15),rando(16,20));
        // cout<<starter<<" "<<devi<<" "<<endl; 
        temp1=starter;  //temp1 = starter
        Start: //if starter%div == 031
        // cout<<starter<<" "<<devi<<endl;
        temp2=temp1%devi; //temp2 = starter % devi
        if(temp2==0&&x<4)
        {
            x++; //i
            if(x==4){goto LetsGo;} //if x=4 means divison works
            temp1=temp1/devi; //temp1/dev for next divison
            goto Start;
        }
        if(o==200){o=0;goto Againn;} //delay //34789 //6
        else if(temp2!=0)
        {
            x=0;
            memory.push_back(starter);
            memory.push_back(devi);
            memory.push_back(x);
            o++;goto Again;
        } //starter%dev !=0, i=0
    LetsGo:
    for(int i=0;i <4;i++)
     {
         vec.push_back(starter);
         starter = (starter / devi);
            if (i == 3)
                {
                    answer = starter;
                    vec.push_back(answer);
                }
        }
      if(admin==1)
      {
        for(int i=0;i<memory.size();i++)
        {
            if(memory[((i+2)+g)]==0)
            {
                cout<<"[Failed] "<<memory[i]<<" "<<memory[i+1]<<endl;
            }
            if(plus==0){plus=3;}
        }
      }
        if(admin==1)
        {
             for (int i = 0 ;i<4 ;i++)
        {
            cout <<"[Passed] "<<vec[i]<<" "<<devi<<endl;
        }
        }
        return vec;
    }
   vector <int> multi()
    {
    vector <int> vec ;
    int first,seq1;
    seq1=rando(rando(2,6),rando(6,20));
    first=rando(rando(2,5),rando(6,7));
    for (int i=0;i<4;i++)
        {
            vec.push_back(seq1);
            seq1 = (seq1 * first);
            if(i==3){vec.push_back(seq1);}
        }
        return vec;
    }
    vector <int> minuss()
    {
    vector <int> vec ;
    int first,seq1;
    seq1=rando(rando(60,80),rando(85,100));
    first=rando(rando(2,50),rando(55,100));
    for (int i=0;i<4;i++)
        {
            vec.push_back(seq1);
            seq1 = (seq1 - first);
            if(i==3){vec.push_back(seq1);}
        }
        return vec;
    }
int main()   
{
vector <int> vect1,vect2,vect3,vect4;
int answer1,answer2,answer3,answer4,repition,x=0,points=0;
cout<<"How many rounds?"<<endl;;
cin>>repition;;
while(x<repition)
{
int random=4;
    if(random==1)
    {
        cout<<"Round "<<x+1<<endl;
         vect1 = pluss(); 

      for (int i = 0 ;i<4 ;i++)
        {
            cout << vect1[i]<< " || ";
            if (i == 3)
                {
                    cin >> answer1;
                        if (answer1 == vect1[i+1])
                            {
                                points++;
                                cout << "You've won this round";
                            }
                                 else cout << "You've lost this round";
                }
        }
}
else if(random==2)
{
        cout<<"Round "<<x+1<<endl;
         vect2 = multi(); 

      for (int i = 0 ;i<4 ;i++)
        {
            cout << vect2[i]<< " || ";
            if(i==3)
            {
                cin>>answer2;
                if(vect2[i+1]==answer2)
                {
                    cout<<"You've won this round";
                    points++;
                }
                else{cout<<"You've lost this round";}
            }
        }
}
else if(random==3)
{
                cout<<"Round "<<x+1<<endl;
    vect4 = minuss(); 

      for (int i = 0 ;i<4 ;i++)
        {
            cout << vect4[i]<< " || ";
            if(i==3)
            {
                cin>>answer4;
                if(vect4[i+1]==answer4)
                {
                    cout<<"You've won this round";
                    points++;
                }
                else{cout<<"You've lost this round";}
            }
        }
}
else if(random==4)
{
                cout<<"Round "<<x+1<<endl;
vect3 = devi(0); //divison

      for (int i = 0 ;i<4 ;i++)
        {
            cout << vect3[i]<< " || ";
            if(i==3)
            {
                cin>>answer3;
                if(answer3==9997)
                {
                    devi(1);
                }
                if(vect3[i+1]==answer3&&answer3!=9997)
                {
                    cout<<"You've won this round";
                    points++;
                }
                else if(answer1!=9997){cout<<"Youve lost this round";}
            }
        }
}
x++;
cout<<endl;
}
cout<<"You've earned "<<points<<" points";
}