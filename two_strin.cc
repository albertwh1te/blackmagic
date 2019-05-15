#include <iostream>
#include <string>
using namespace std;

bool check(string a, string b, int start)
{
    for (int i = 0; i < a.size() - b.size(); i++)
    {
        if (a[i + start] != b[i])
        {
            return false;
        }
    }
    return true;
}

bool two_same(string a, string b, int length)
{
    string all = a + a;
    for (int i = 0; i < length; i++)
    {
        if (check(all, b, i))
        {
            return true;
        }
    }
    return false;
}

int main()
{
    cout << two_same("babbbbb", "bbbbbba", 7) << endl;
    cout << two_same("bcbbbbb", "bbbbbbc", 7) << endl;
    cout << two_same("bcwwwww", "bbbbbbc", 7) << endl;
    return 0;
}