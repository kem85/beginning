#include <iomanip>
#include <iostream>
#include <stdlib.h>
#include <unistd.h>

using namespace std;

int hours = 0;
int minutes = 0;
int seconds = 0;
void timer() 
{
    while (true)
     {
        sleep(1);
        seconds++;

        if (seconds == 60) {
            minutes++;

            if (minutes == 60) {
                hours++;
                minutes = 0;
            }

            seconds = 0;
        }
    }
}

int main() {

    timer();
}
/*#include <iostream>
#include <random> 
#include <iomanip>
#include <iostream>
#include <stdlib.h>
#include <unistd.h> 
using namespace std;
int hours = 0;
int minutes = 0;
int seconds = 0;
char x='y';string s;
int repeat,g;
int rando (int x,int g) //random function
    {
    random_device rand;  
    mt19937 gen(rand());  
    uniform_int_distribution<>dis(x, g);  
    return dis(gen);
    }
int question()
{
    sdsd:
    g=rando(1,3);
    if(g==repeat){goto sdsd;}
    else{
    s=(g==1) ? "A" : (g==2) ? "B":"C";
    cout<<rando(1,255)<<"."<<rando(30,155)<<"."<<rando(20,90)<<"."<<rando(1,255)<<endl;
     cout<<"Class: "<<s<<endl;
        cin>>x;
    }
    repeat=g;
    cout<<"You finished in: "<<minutes<<" minutes "<<seconds<<" seconds"<<endl;
    minutes=0;seconds=0;
    return 1;
}
    void timer() 
{
    while (true)
     {
        question();
        sleep(1);
        seconds++;

        if (seconds == 60) {
            minutes++;

            if (minutes == 60) {
                hours++;
                minutes = 0;
            }

            seconds = 0;
        }
    }
}
int main()
{
    timer();
}*/