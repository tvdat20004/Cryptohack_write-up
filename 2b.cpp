#include<bits/stdc++.h>
using namespace std;

string shift(string &ciphertext)
{
	for (int i = 0; i < ciphertext.length(); ++i)
	{
		int base;
		if (ciphertext[i] >= 'a' && ciphertext[i] <= 'z') base = (int)'a';
		else if (ciphertext[i] >= 'A' && ciphertext[i] <= 'Z') base = (int)'A';
		else continue;
		ciphertext[i] = (ciphertext[i] - base + 1) % 26 + base;
	}
	return ciphertext;
}
int main()
{
	string ciphertext;
	cout<<"Enter encrypted text:";
	getline(cin,ciphertext);
	for (int i = 1; i <= 26; ++i)
	{
		cout<<"Shift:"<< i <<"\nPlaintext:"<< shift(ciphertext)<<'\n';
	}
	return 0;
}