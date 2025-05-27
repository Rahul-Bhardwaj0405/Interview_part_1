#  Converting a List into a String

# def list_to_str(l):
#     result = ','.join(l)
#     return result

# print(list_to_str(["fhdh", "uuu"]))

# Vice-versa of just above solution


# def str_to_list(l):
#     result = l.split(',')
#     return result

# print(str_to_list("jhiokok"))

#  Adding Two List Elements Together

# l_one = [2,5,7]
# l_two = [8,9,10]

# result = list(zip(l_one, l_two))
# print(result)


# def add_list(l1, l2):
#     if len(l1)!=len(l2):
#         raise ValueError("Both list must be of same length")
#     else:
#         result = [x + y for x, y in zip(l1, l2)]
#     return result

# output = add_list([2,5,7], [8,9,10])

# print(output)

# Another Way:

# def add_list(l1, l2):
#     out = []
#     if len(l1)!=len(l2):
#         raise ValueError("Both list must be of same length")
#     else:
#         for i in range(0, len(l1)):
#             out.append(l1[i] + l2[i])
#     return out

# output = add_list([2,5,7], [8,9,10])

# print(output)


#  Comparing Two Strings for Anagrams:

# from collections import Counter


# def angram(str1, str2):
#     return Counter(str1) == Counter(str2)

# result = angram("Listen".lower(), "Silent".lower())

# print(result)


# Checking for Palindrome Using Extended Slicing Technique

# import re


# def check_palindrome(s):
#     check_s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
#     return check_s == check_s[::-1]

# out = check_palindrome("madam")
# print(out)


# Counting the White Spaces in a String

# string_one = "P r ogramm in g "
# print(string_one.count(' '))

#  Counting Digits, Letters, and Spaces in a String

# import re


# def count_dls(str_one):
#     d = re.sub(r'[^0-9]', '', str_one)
#     l = re.sub(r'[^a-zA-Z]', '', str_one)
#     s = re.findall("\n", str_one)

#     cd= len(d)
#     cl = len(l)
#     cs = len(s)
#     return cd, cl, cs

# out = count_dls("Python is 1")
# print(out)

# Counting Special Characters in a String


# import re

# def special_char(s):
#     spec = re.findall(r'\D', s)
#     return len(spec)

# out = special_char("!@#$%^&*()")
# print(out)

# Removing All Whitespace in a String
# import re

# def rem_whitespace(s):
#     white_space = re.compile(r'\s+')
#     space = re.sub(white_space, '', s)
#     return space

# print(rem_whitespace("C O D E"))


# Randomizing the Items of a List in Python

# from random import shuffle

# lst = ['DDD', 'QWE', 'YTRE']
# shuffle(lst)
# print(lst)

# Factorial of a Number

# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact(n-1)

#  Find the First Non-Repeating Character

# def first_non(ch):
#     for i in ch:
#         if ch.count(i) == 1:
#             return i
#     return None
    


# print(first_non("AAHHRUL"))


# How do you implement a singleton pattern in Python?


# Magic methods (or dunder methods) are special methods with double underscores at the beginning and end. They enable the customization of behavior for standard operations

# __init__: Constructor
# __str__: String representation
# __add__: Addition operator


#  How do you handle multi-threading in Python?

# import threading

# def print_number():
#     for i in range(10):
#         print(i)

# thread = threading.Thread(target=print_number)
# thread.start()
# thread.join()

# 🧠 Summary:
# This code:

# Defines a function that prints 0 to 9.

# Runs that function in a separate thread.

# Waits for the thread to finish before continuing.

# Even though in this small example you don’t gain much from threading, it's a foundational pattern for I/O-bound or concurrent tasks — like handling multiple requests, background processing, or interacting with external APIs.

#  Example: Sending Multiple Emails Concurrently (Using Threads)
# Imagine you're writing a Django view or admin action that sends notification emails to many users. Using threads, you can do it concurrently instead of sequentially.

# 🔹 utils/email_threader.py
# python
# Copy
# Edit
# import threading
# from django.core.mail import send_mail

# class EmailThread(threading.Thread):
#     def __init__(self, subject, message, recipient_email):
#         threading.Thread.__init__(self)
#         self.subject = subject
#         self.message = message
#         self.recipient_email = recipient_email

#     def run(self):
#         send_mail(
#             self.subject,
#             self.message,
#             'noreply@example.com',
#             [self.recipient_email],
#             fail_silently=False,
#         )
# 🔹 Usage in a Django View or Management Command
# python
# Copy
# Edit
# from utils.email_threader import EmailThread

# def notify_users(user_emails):
#     threads = []

#     for email in user_emails:
#         thread = EmailThread(
#             subject="Update Notification",
#             message="Hello, we have an update for you.",
#             recipient_email=email,
#         )
#         thread.start()
#         threads.append(thread)

#     # Wait for all threads to finish
#     for thread in threads:
#         thread.join()

#     print("All emails sent!")
# ✅ Why This Is Useful in Production:
# It doesn't block the main process (e.g., view return or next logic).

# Good for non-critical, quick async-like operations.

# Especially helpful in:

# Admin actions

# Management commands

# Low-traffic background scripts

# Situations where Celery isn’t set up yet

##################################################################################
# How to Use multiprocessing Module:

# import multiprocessing

# def print_squr(num):
#     return num * num


# if __name__ == '__main__':
#     process = multiprocessing.Process(target=print_squr, args=(4,))
#     process.start()
#     process.join()

# 🔍 Explanation:
# multiprocessing.Process creates a new process.

# target is the function it should run.

# args passes arguments to that function.

# start() launches the process.

# join() waits for it to finish.



# from multiprocessing import pool

# def squr_ant(n):
#     return n * n

# if __name__ == '__main__':
#     with pool(4) as p:
#         result = p.map(squr_ant, [2,3,4,5])
#     print(result)

#  Best for:
# Parallel data processing (e.g., filtering, transformations).

# Data science workloads.

# CPU-intensive image processing, encryption, etc.


# 🧠 Use Cases in Django or Python Projects
# In Django, you typically don’t use multiprocessing directly inside views — instead, you delegate heavy tasks to:

# Celery (preferred for production task queues)

# Background scripts or management commands

# Parallel scripts for batch processing (e.g., reconciliation jobs)

# Coroutine Basics
# A coroutine function is defined using async def. It can await other async functions to pause and resume execution.

# 🧪 Basic Example:
# python
# Copy
# Edit
# import asyncio

# async def fetch_data():
#     print("Start fetching")
#     await asyncio.sleep(2)  # Simulate a network call
#     print("Done fetching")
#     return {'data': 123}
# To run this, you'd use await fetch_data() inside another coroutine or use an event loop (like asyncio.run(fetch_data())).

# ⚙️ Example in a Django Production Context
# ✅ Use Case: Async View to Call an External API
# Suppose you're building a Django app that fetches data from an external payment gateway.

# 1. Enable async view in Django

# In Django (3.1+), you can define async views:

# python
# Copy
# Edit
# # views.py

# import httpx  # An async HTTP client
# from django.http import JsonResponse

# async def get_payment_status(request):
#     async with httpx.AsyncClient() as client:
#         response = await client.get('https://api.paymentgateway.com/status')
#         data = response.json()
#     return JsonResponse(data)
# This view is a coroutine function because it uses async def and await.

# 2. Configure Django for async

# You don’t need to change much — Django supports async views out-of-the-box. Just ensure your server (like Uvicorn, Daphne, or ASGI-based deployment) supports async.

