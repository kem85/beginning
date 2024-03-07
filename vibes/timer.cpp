#include <iostream>
#include <limits>
#include <ctime> // time_t, difftime, time
using namespace std;

int main ()
{
    time_t pasttime=time(nullptr);
    time_t currentime;
    double seconds=0;
    while(seconds<5)
    {
    time(&currentime);
    seconds = difftime(pasttime,currentime);
    cout<<seconds;
    }
        
}
/*#include <iostream>
#include <limits>
#include <ctime> // time_t, difftime, time

int main ()
{
    //we just started the program, so let's take a snapshot of the time
    std::time_t startTime = std::time(nullptr);

    //we'll use this time_t variable to take future snapshots of the time to compare them
    //to when we started
    std::time_t currentTime;
    double seconds;

    std::cout << "Input something...";
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    std::time(&currentTime); //get the time now that the user has entered something and stick it in currentTime

    seconds = std::difftime(currentTime, startTime);
    std::cout << "It took you " << seconds << " seconds to enter something.\n";

    std::cout << "Input something else...";
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    std::time(&currentTime);

    seconds = std::difftime(currentTime, startTime);
    std::cout << "It has now been " << seconds << " seconds since you started the program.\n";

    return 0;
}*/