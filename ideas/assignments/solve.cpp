#include <iostream>
using namespace std;
int main()
{
int nummer,posstiivee = 0,negaativeee = 0;
char repeeattterrr = 'Y';
cout << "Enter The Number" << endl;
while (repeeattterrr == 'Y')
{
    cin >> nummer;
        if(nummer > 0)
            {
                posstiivee++;
            }
        else negaativeee++;

        cout << "Do You Want To Continue Y/N" << endl;
        cin >> repeeattterrr;
    }
        

cout << "Positive Counter: " <<posstiivee << endl;
cout << "Negative Counter: " <<negaativeee ;
}