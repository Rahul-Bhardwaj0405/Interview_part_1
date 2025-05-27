# Frequency of characters in string:
# def freq_count(n):
#     freaq = {}
#     for i in n:
#         if i in freaq:
#             freaq[i] += 1
#         else:
#             freaq[i] = 1
#     return freaq

# print(freq_count("RAHHUL"))

# Take 2 characters from both ends of str

# def ch_both(s):
#     if len(s)<2:
#         print("Error")
#     return (s[0:2] + s[-2:])

# print(ch_both("GREATER"))
        

# Remove the duplicate items from List:

# def dup_lis(s):
#     act_iteam = set()
#     for i in s:
#         if i not in act_iteam:
#             act_iteam.add(i)
#     return act_iteam

# print(dup_lis("KAILASHA"))


# Write a Python program to square the elements of a list using map and lambda ?


# def mix_map_lambda(s):
#     res=list(map(lambda i : i* i , s))
#     return res

# print(mix_map_lambda([3,4,5,6,7,8]))

# Write a python program to square the elements using list comprehension ?

# def mix_map_lambda(s):
#     res=[i* i for i in s]
#     return res

# print(mix_map_lambda([3,4,5,6,7,8]))



# sample_string = 'hello good morning everyone'
# output = 'everyone morning good hello'
# Reverse the order of the word in the given string ?

# def rev_order(s):
#     res = s.split()
#     out = ' '.join(reversed(res))
#     return out
# print(rev_order("hello good morning everyone"))


# Answers of above questions max salary and total salary


# employees = [
#     {"name": "Alice", "details": {"age": 30, "salary": 50000}},
#     {"name": "Bob", "details": {"age": 35, "salary": 60000}},
#     {"name": "Charlie", "details": {"age": 28, "salary": 55000}},
# ]


# emp = sum(sal['details']['salary']  for sal in employees)

# print(emp)


# employees = [
#     {"name": "Alice", "salary": 50000},
#     {"name": "Bob", "salary": 60000},
#     {"name": "Charlie", "salary": 55000},
# ]

# # emp = max(sal['salary']  for sal in employees)
# emp = max(employees, key=lambda x: x['salary'])

# print(emp)


# Filter and reduce function

# numbers = [1, 2, 3, 4, 5]

# res = filter(lambda x: x%2 ==0, numbers)

# print(res)


from functools import reduce

numbers = [1, 2, 3, 4, 5]

res = reduce(lambda x,y: x+y, numbers)

print(res)
