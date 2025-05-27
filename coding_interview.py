#  Reversing a String using an Extended Slicing Technique

# string = "Python Programming"

# result = string[::-1]

# print(result)

# Reverse a String without slicing technique

# def rev_str(strn):
#     res = ""
#     for i in strn:
#         res =  i + res
#     return res

# print(rev_str("PYTHON PRO"))

#  Counting Vowels in a Given Word

# def count_vowel(word):
#     vowel = ['a', 'e', 'i', 'o', 'u']
#     c = 0
#     for i in word:
#         if i in vowel:
#             c += 1
#         else:
#             print("Not a vowel")
#     return c

# print(count_vowel("Rahul"))


# Counting Consonants in a Given Word

# def count_vowel(word):
#     vowel = ['a', 'e', 'i', 'o', 'u']
#     c = 0
#     for i in word:
#         if i in vowel:
#             print(" A vowel")
#         else:
#             c += 1
#     return c

# print(count_vowel("Rahul"))


# or


# vowel = ['a', 'e', 'i', 'o', 'u']
# word = "programming"
# count = 0
# for character in word:
#     if character not in vowel:
#         count += 1
# print(count)


#  Counting the Number of Occurrences of a Character in a String

# def occurrences_char(ch):
#     char_count = {}
#     for i in ch:
#         if i in char_count:
#             char_count[i] += 1
#         else:
#             char_count[i] = 1
#     return char_count

# print(occurrences_char("RRRAhul"))
        

# Writing Fibonacci Series

# def fibo_series(fib):
#     a, b = 0, 1
#     print(a, b, end=" ")
#     for _ in range(2, fib):
#         c = a + b
#         print(c, end=" ")
#         a, b = b, c
    
# print(fibo_series(10))

# Finding the Maximum Number in a List

# def max_no_list(l):
#     if not l:
#         return None
#     max = l[0]
#     for i in l:
#         if i>l[0]:
#             max = i
#     return max

# print(max_no_list([12,23,45,6,99]))

# def max_no_list(l):
#     if not l:
#         return None
#     return max(l)

# print(max_no_list([12,23,45,6,99]))


# Finding the Minimum Number in a List

# def min_no_list(l):
#     if not l:
#         return None
#     minimum = l[0]
#     for i in l:
#         if i<l[0]:
#             minimum  = i
#     return  minimum 

# print(min_no_list([12,23,45,6,99]))

#  Finding the Middle Element in a List


def find_middle_element(l):
    if not l:
        return None  # Return None for empty lists
    middle_index = len(l) // 2
    print(f"Middle Index: {middle_index}")
    return l[middle_index]

print(f"Middle Element: {find_middle_element([34, 20, 3, 4])}")
