'''

Take a String say s, which is to be analysed.
For the specified integer say k, which denotes the length of the substring.
Make sure that string s consists of a contiguous block of characters k.
For each substring, remove the subsequent occurrences of any element in that particular substring.
The resultant substrings are to be placed in a llist.

Input : AABCAAADA 3
where s = 'AABCAAADA' and k =3.

Output : ['AB', 'CA', 'AD']

'''

def SubstringOfString(s, k):
    "Write your logic here."