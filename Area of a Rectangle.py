'''
Problem statement:

Take the length(L) and breadth(B) of the rectangle as input and find its area.
Note: Length and breadth must be an integer value and the area will always be in the range of integers.

Detailed Explenation:

Input Format: The first line of input contains two intergers, both seperated by a sigle space denoting the length and breadth respectively.
Output Format: The only line of output prints the area of the rectangle.

Sample Input 1: 4 20
Sample Output 1: 80

Explanation of Sample Input 1:
Length of the rectangle is 4 and breadth is 20. 
Hence the area of the rectangle is (length*breadth). 
So the answer is 4*20=80.
'''

l,b = input().split()
l = int(l)
b = int(b)

a = l*b

print(a)
