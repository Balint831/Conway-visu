#include <vector>
#include <iostream>

int main()
{
    std::vector<char> a = {1,2,3,4,5,6,7,8,9,10};
    for (char i = 0; i < a.size(); ++i)
        if ( a[i] > 3 ) std::cout << "yess" << std::endl;

    return 0;
}

