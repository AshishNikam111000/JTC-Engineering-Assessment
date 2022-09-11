arr = list(map(int, input().split()))
n = len(arr)

for i in range(0, n, 2):
    temp = arr.pop(-1)
    arr.insert(i, temp)
print(arr)

'''

URL that contains the solution in programming
language of your choice (recommended:
Typescript or JavaScript)

Time complexity (Big O notation) of your
solution: O(N/2)

Space complexity (Big O notation) of your
solution: O(1)

List all possible test cases:
1. 2 4 6 8 10
-> 10 2 8 4 6

2. 2 4 6 8
-> 8 2 6 4

3. -1 0 1 2 3 5 7 9
-> 9 -1 7 0 5 1 3 2

4. -3 -2 -1 0 1 2 3
-> 3 -3 2 -2 1 -1 0

'''
