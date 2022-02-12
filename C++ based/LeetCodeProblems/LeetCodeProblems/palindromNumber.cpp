#include<iostream>
#include<string>
#include<typeinfo>
using namespace std;

bool isPalindrome(int passed_number)
{
	//cout << "The passed number is : "<<passed_number;
	//To convert string to number
	string returned_string = to_string(passed_number);
	int size = returned_string.size();
	//for (int i = 0; i < returned_string.size(); i++)
	//{
	//	size++;
	//}
	//cout << "Size of string is : " << size;
	string reversed_string;
	//cout << "\nTraversing in reverse"<<endl;
	for (int i = size-1; i >=0; i--)
	{
		reversed_string.push_back(returned_string[i]);
	}
	/*cout << "\nReversed String: " << reversed_string;*/
	for (int i = 0; i < size; i++)
	{
		if (returned_string[i] != reversed_string[i])
		{
			return false;
		}
	}
	return true;
}

int main() {
	int palindrom_number =  1122;
	bool answer = isPalindrome(palindrom_number);
	//cout << "The number : " << palindrom_number << " is: " << answer;
	string check;
	check.push_back('A');
	check.push_back('B');
	check.push_back('C');
	cout << "check is : " << check;
}