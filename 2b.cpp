#include<bits/stdc++.h>
using namespace std;
// hàm shift là hàm mã hóa bằng caesar cipher với giá trị shift = 1
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
	// nhập ciphertext
	cout<<"Enter encrypted text:";
	getline(cin,ciphertext);
	// thực hiện brute-force với plaintext với các giá trị shift từ 1 tới 26 
	for (int i = 1; i <= 26; ++i)
	{
		cout<<"Shift:"<< i <<"\nPlaintext:"<< shift(ciphertext)<<'\n';
	}
	return 0;
}
