#include <iostream>
#include <random>
using namespace std;
<<<<<<< Updated upstream
int main()
{
    cout<<"pass";
=======
int rando (int x,int g) //random function
    {
    random_device rand;  
    mt19937 gen(rand());  
    uniform_int_distribution<>dis(x, g);  
    return dis(gen);
    }
main()
{                                            //Simple Calculator.
    int num1, num2, type, shady;
    cout << "Please enter your first number : ";
    cin >> num1;
    cout << "Please enter your secound number : ";
    cin >> num2;
    cout << "=============================================================================="<<endl;
    cout << "for + => [1]  \nfor - => [2]  \nfor * => [3]  \nfor / => [4] \nfor shady => [5]  " << endl;
    cout << "=============================================================================="<<endl;
    cin >> type;

    if (type == 1) {
        cout << "Your sum is : " << num1 + num2;
    }
    else if (type == 2) {
        cout << "Your minus is : " << num1 - num2;
    }
    else if (type == 3) {
        cout << "Your multi is : " << num1 * num2;
    }
    else if (type == 4) {
        cout << "Your divide is : " << num1 / num2;
    }
    else if (type == 5) {
        while (true) 
        {
            if(rando(1,3)==3)
            {
                cout<<"we";
            }
            if(rando(1,3)==2)
            {
                cout<<"elll"<<endl;
            }
              if(rando(1,3)==1)
            {
                cout<<rando(100,10000);
            }
        }
    }
>>>>>>> Stashed changes
}