'''
Problem statement
Write a program to find the factorial of a number.

Factorial of n is:

n! = n * (n-1) * (n-2) * (n-3)....* 1

Output the factorial of 'n'. If it does not exist, output 'Error'.

Input format: The only line of input contains a single integer.
Output format: The only line of output prints the Factorial of the number or "Error" if it doesn't exist.

Constraints: -10<= n <= 12

Sample Input 1 :
5
Sample Output 1 :
120
Explanation of Sample Input 1:
5!=5*4*3*2*1=120
Sample Input 2 :
0
Sample Output 2 :
1
Explanation of Sample Input 2:
Its a fact that 0!=1
Sample Input 3 :
-2
Sample Output 3 :
Error
Explanation of Sample Input 3:
It's a fact that we can't find the factorial of a negative number.
'''
n = int(input())
ans = 1
if n==0:
    print(1)
elif n<0:
    print("Error")
else:
    for i in range(1,n+1):
        ans = ans * i
    print(ans)
