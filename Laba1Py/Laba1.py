import sys

# Визначити, скільки повних годин(h) і повних хвилин(m)
# пройшло з початку доби до k-ої її секунди

print("Input the number of seconds")
seconds = int(input())
if seconds
#include <iostream>
#include <cmath>
using namespace std;

/*
Визначити, скільки повних годин(h) і повних хвилин(m)
пройшло з початку доби до k-ої її секунди
*/


int main()
{
	int s, h, m; // вводимо змінні (секунди, години, хвилини)
	cout << "Enter the number of seconds" << endl;
	cin >> s;
	if (s > 86400 || s < 0)
	{
		cout << "There are only 86400 seconds in a single day" << endl;
		return 0;
	}
	h = s / 3600;   // ділимо секунди на їх к-сть в одній годині
	m = s % 3600 / 60;  // залишок секунд ділимо на їх к-сть в одній хвилині
	cout << "The number of hours is " << h << endl;
	cout << "The number of minutes is " << m << endl;
	return 0;

}

	> or seconds < 0:
    print("There are only 86400 seconds in a single day. Please try again.")
    sys.exit()
hours = seconds // 3600
minutes = int(seconds % 3600 / 60)
print(f"The number of hours is {hours}, the number of minutes is {minutes}")

