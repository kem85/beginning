#include <iostream>
#include <string>
#include <cmath>
using namespace std;

struct rec {
    int points[3];
    int area;
}rect1;

int main()
{

    int arr[4];
    int p1,p4;
    
    for (int i = 0; i <= 3; i++) {
        cin >> arr[i];
    }
    rect1.points[0]= arr[0]; //p1 x axis
    rect1.points[1] = arr[1]; //p1 y axis
    rect1.points[2] = arr[2]; //p4 x axis
    rect1.points[3] = arr[3]; //p4 y axis
    cout<<"Enter area:";
    cin>>arr[4];  
    cout << "p2=(" << rect1.points[2] << "," << rect1.points[1] << ")"<<endl;
    cout << "p3=(" << rect1.points[0] << "," << rect1.points[3] << ")";

}