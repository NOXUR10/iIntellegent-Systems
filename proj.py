import math

# 1. Write a program to swap the value of two variables.

# var1 = 5
# vart2 = 4
# var1, vart2 = vart2, var1
# print(var1, vart2)

# 2. Write a program that finds the largest among three numbers.

# nums = [100, 200, 300]
# max = nums[0]
# for n in nums:
#     if n > max:
#         max = n
# print(max)

# 3. Write a program that prints the following pattern:
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

# for i in range(5, 0, -1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

# 4. Write a program to print all odd numbers from n to 1.

# n = int(input("Enter A Number: "))
# for i in range(n, 0, -1):
#     if i % 2 != 0:
#         print(i, end=" ")

# 5. Write a program to check if input string is palindrome.

# palword = input("Enter a palindrome word: ")

# if palword == palword[::-1]: #reverse word
#     print(palword, " is a palindrome.")
# else:
#     print(palword, " is not a palindrome.")

# 6. Write a program to get a string made of the first 2 and the last 2 chars from a given a string.
#  If the string length is less than 2, return instead of the empty string.

# Sample String: 'Hello World'
# Expected Result: 'Held'

# word = input("Enter A String: ")
# if len(word) >= 2:
#     result = word[:2] + word[len(word)-2:len(word)]
# else:
#     result = ""
# print(result)

# 7. Write a Python program to remove the nth index character from a nonempty string.

# s = input("Write A String: ")
# n = int(input("Enter The nth Index You Want To Delete: "))

# new_s = s[:n] + s[n+1:]
# print(new_s)

# 8. Write a function to check whether a number is Prime or not
#  then call the function to check the user’s input and print the result.

# def isPrime(num):
#     if num <= 1:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
        
# num = int(input("Enter the number: "))          
# if (isPrime(num)): print(num, "is a prime number.")
# else: print(num, "is not a prime number.")

graph = {
    'S': {'A':5, 'B':2, 'C':4},
    'A': {'D':9, 'E':4},
    'B': {'G':6},
    'C': {'F':2},
    'D': {'H':7},
    'E': {'G':6},
    'G': {},
    'F': {'G':1},
    'H': {}
    }

import queue as q
def uniform_cost(graph, start, end):
    queue = q.PriorityQueue()
    queue.put((0, [start]))
    while not queue.empty():
        node = queue.get()
        current = node[1][-1]
        if end == current:
            print('path found' + str(node[1]) + " cost " + str(node[0]))
            break
        cost = node[0]
        for child in graph[current]:
            path = node[1][:]
            path.append(child)
            queue.put((cost + graph[current][child], path))

def greedy(graph, start, end):
    queue = q.PriorityQueue()
    queue.put((0, [start]))
    while not queue.empty():
        node = queue.get()
        current = node[1][-1]
        if end == current:
            print('path found' + str(node[1]) + " cost " + str(node[0]))
            break
        cost = node[0]
        for child in graph[current]:
            path = node[1][:]
            path.append(child)
            queue.put((graph[current][child], path))

uniform_cost(graph, 'S', 'G')
