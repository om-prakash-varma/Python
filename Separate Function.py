'''
Problem statement:
Take the person's name and age as input and print out the name and age as specified in the output format.

Input Format:
The first line of input contains a single string(name), representing the name of the person.
The second line of input contains a single integer(age), representing the age of the person.

Output Format: The only line of output prints the name and age by sticking to the sample input format. Mind that the output string won't have preceding or trailing spaces.

Sample Input 1:
Ali
30

Sample Output 1:
The name of the person is Ali and the age is 30.

Explanation of Sample Input 1:
The input name is Ali and the input age is 30 which is printed in the specified format.
'''
name = input()
age = int(input())

print('The name of the person is ',name,' and the age is ',age,'.',sep='')
