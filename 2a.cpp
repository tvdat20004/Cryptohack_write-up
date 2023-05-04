#include <bits/stdc++.h>
using namespace std;
int main()
{
	string plaintext;
	int shift;

	// nhập plaintext
	cout<<"Enter plaintext:";
	getline(cin,plaintext);

	// nhập giá trị shift pattern
	cout<<"Enter shift pattern:";
	cin>>shift;
	// xử lí khi giá trị shift âm
	while (shift < 0) shift += 26;
	for (int i = 0; i < plaintext.length(); ++i)
	{
		int base; // giá trị base = 'a' nếu là chữ cái thường, bằng 'A' nếu là chữ hoa
		if (plaintext[i] >= 'a' && plaintext[i] <= 'z') base = (int)'a';
		else if(plaintext[i] >= 'A' && plaintext[i] <= 'Z') base = (int)'A';
		else continue;
		// công thức dịch chuyển: c = (c + shift) % 26 trong đó c = plaintext[i] - base
		plaintext[i] = (plaintext[i] - base + shift) % 26 + base;
	}
	// in ra kết quả
	cout<<"Encrypted text:"<<plaintext;
	return 0;
}
