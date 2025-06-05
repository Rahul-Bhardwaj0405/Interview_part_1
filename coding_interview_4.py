# 1. Iterable
# An iterable is any Python object you can loop over.

# 📦 Examples:

# list, tuple, dict, set, str

# Any object that implements __iter__() or __getitem__()

# python
# Copy
# Edit
# data = [1, 2, 3]  # This is an iterable
# for i in data:
#     print(i)
# 🔄 2. Iterator
# An iterator is an object with a state that keeps track of where it is during iteration.

# It implements:

# __iter__() → returns the iterator object itself

# __next__() → returns the next item or raises StopIteration

# 📦 You get an iterator from an iterable:

# python
# Copy
# Edit
# data = [1, 2, 3]
# it = iter(data)  # This is now an iterator

# print(next(it))  # 1
# print(next(it))  # 2
# ⚙️ 3. Generator
# A generator is a special kind of iterator created using a function and yield instead of return.

# It doesn’t store all values in memory — it yields one item at a time, making it super memory efficient.

# python
# Copy
# Edit
# def my_gen():
#     yield 1
#     yield 2
#     yield 3

# gen = my_gen()
# print(next(gen))  # 1
# print(next(gen))  # 2
# 🌱 4. yield keyword
# Used inside a function to turn it into a generator.

# When the function is called, it doesn't run immediately — it returns a generator object.

# On each next(), it resumes where it left off.

# 🧠 Summary Table:
# Concept	What it is	Key Methods	Memory Efficient?	Example
# Iterable	Can be looped over	__iter__()	❌ (loads all)	List, Tuple
# Iterator	Tracks position in loop	__next__()	❌ (unless using generator)	iter(list)
# Generator	Custom iterator using yield	__next__(), __iter__()	✅ Yes	def gen(): yield ...
# 💼 When to Use generator / yield in Django Production
# ✅ When dealing with large datasets or streaming responses, for memory efficiency:
# 1. Processing large querysets (no .all() or .values() all at once)
# python
# Copy
# Edit
# def process_large_queryset():
#     for obj in MyModel.objects.iterator():  # Efficient iterator, no full load
#         yield obj.some_field
# 2. Streaming CSV/Excel file downloads
# python
# Copy
# Edit
# from django.http import StreamingHttpResponse

# def generate_csv():
#     yield 'Name, Age\n'
#     for user in User.objects.iterator():
#         yield f'{user.name}, {user.age}\n'

# def download_csv(request):
#     response = StreamingHttpResponse(generate_csv(), content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="users.csv"'
#     return response
# ✅ Memory efficient: doesn’t load the full CSV in memory.

# 3. Custom pagination or batch processing
# python
# Copy
# Edit
# def chunked_queryset(qs, chunk_size=1000):
#     offset = 0
#     while True:
#         chunk = qs[offset:offset + chunk_size]
#         if not chunk:
#             break
#         yield chunk
#         offset += chunk_size



# import operator


# d = {1: -2, 3: 4, 4: 3, 2: 1, 0: 0}

# out = sorted(d.items(), key = operator.itemgetter(1), reverse=True)

d = {1: -2, 3: 4, 4: 3, 2: 1, 0: 0}
out = sorted(d.items(), key=lambda item: item[1], reverse=True)


# print(out)

# Remove the key from the dictionary:

# def rem_key(s, k):
#     if k in s:
#         del s[k]
#         print(s[k])
#     else:
#         print("Pass the Key or Wrong key selected")

# print(rem_key({'R': 1, 'A': 2, 'G': 4}))


# keys = ['red', 'green', 'blue']

# values = ['#FF0000', '#008000', '#0000FF']

# out = dict(zip(keys, values))

# print(out)

## Remove duplicacy in dictionary:


def dup_dic(d):
    act_val = set()
    act_item = {}
    for key, value in d.items():
        if value not in act_val:
            act_val.add(value)
            act_item[key]= value
    return act_item

print(dup_dic({'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}))
