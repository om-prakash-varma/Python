'''
Problem statement
Given a number N, print sum of all even numbers from 1 to N.

Constraints :
 1 <= N <= 10ˆ4

Sample Input 1 :
 6
Sample Output 1 :
12
Explanation of Sample Input 1:
The even numbers from 1 to 6 are: 2, 4, 6, So adding these 3 numbers give a sum of 12.
'''
n = int(input())
ans = 0
for i in range (1,n+1):
    if i%2 == 0:
        ans = ans + i
print(ans)
