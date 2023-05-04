#include <bits/stdc++.h>
using namespace std;
int main()
{
	string plaintext;
	int shift;
	cout<<"Enter plaintext:";
	getline(cin,plaintext);
	cout<<"Enter shift pattern:";
	cin>>shift;
	while (shift < 0) shift += 26;
	for (int i = 0; i < plaintext.length(); ++i)
	{
		int base;
		if (plaintext[i] >= 'a' && plaintext[i] <= 'z') base = (int)'a';
		else if(plaintext[i] >= 'A' && plaintext[i] <= 'Z') base = (int)'A';
		else continue;
		plaintext[i] = (plaintext[i] - base + shift) % 26 + base;
	}
	cout<<"Encrypted text:"<<plaintext;
	return 0;
}