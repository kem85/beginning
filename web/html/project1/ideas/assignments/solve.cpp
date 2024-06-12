
#include <iostream>
using namespace std;
		
int main()
{
	int x[5];
	int y[5];
	int total = 0;
	cout << "Enter the elements : ";
	for (int i = 0; i < 5; i++)
	{
		
		cin >> x[i];
		y[i] = x[i];	
	}
	cout << "The elements reversed : ";
	for (int j = 4; j < 5 && j>=0; j--)
	{
		total = total + y[j];
		cout << y[j] << " ";
	}
	cout <<"The average is : " << total / 5;
}

