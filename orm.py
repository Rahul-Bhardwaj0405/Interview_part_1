# 1. What is Django’s ORM, and how does it work?
# Answer: Django’s ORM (Object-Relational Mapping) allows developers to interact with databases using Python code instead of writing raw SQL. It translates Python models into database tables and provides methods to query, update, delete, and manage data using Python classes and objects. ORM works by defining models (Python classes) that represent database tables, and Django generates SQL queries under the hood to interact with the database.

# 2. How do you optimize database queries in Django?
# Answer:

# Use select_related() and prefetch_related() to reduce the number of database queries when accessing related objects.
# Avoid n+1 query problems by using the appropriate related object methods.
# Use database indexing for frequently queried fields.
# Use only() and defer() to retrieve only necessary fields from the database.
# Use values() and values_list() to fetch specific fields directly as dictionaries or lists, which is more efficient than fetching entire objects.
# Cache frequently accessed data using Django’s caching framework.
# 3. Explain the difference between select_related() and prefetch_related().
# Answer:

# select_related() is used for single-valued relationships (foreign keys, one-to-one relationships). It performs a SQL join and retrieves all the related objects in a single query.
# prefetch_related() is used for multi-valued relationships (many-to-many, reverse foreign keys). It performs separate queries for related objects and then combines the results in Python.
# 4. What is the difference between AbstractBaseUser and User in Django?
# Answer:

# User is Django’s default user model, which includes predefined fields such as username, email, password, etc. It is suitable for most use cases but may not fit custom authentication needs.
# AbstractBaseUser is a more flexible base class for creating custom user models. It provides the bare minimum functionality (like password hashing and authentication methods), allowing you to define your own fields and logic, such as removing the username field or adding custom authentication fields.
# 5. How do you handle file uploads in Django?
# Answer:

# Use Django’s FileField or ImageField in your model to handle file uploads.
# In the view, ensure the form uses enctype="multipart/form-data".
# Files are uploaded to the directory specified in the MEDIA_ROOT setting.
# Access uploaded files through request.FILES in the view.
# Use FileSystemStorage or custom storage backends to manage where files are stored.
# To ensure file security, restrict access to file URLs and consider using private media.
# 6. What are Django signals, and how do you use them?
# Answer: Django signals allow decoupled applications to communicate. They provide a way to execute certain actions when specific events occur (e.g., model save, user login). Signals can be used to trigger actions like sending an email after a model instance is created. Example:

# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import MyModel
# @receiver(post_save, sender=MyModel)
# def my_model_post_save_handler(sender, instance, created, **kwargs):
#     if created:
#         # Do something when MyModel instance is created
#         pass
# 7. How do you manage multiple databases in Django?
# Answer: Django supports multiple databases using the DATABASES setting in settings.py. You define different database connections, and use routers to route queries to specific databases. Key points include:

# Define databases in DATABASES as a dictionary.
# Create a custom database router to control which database a query should go to.
# Use using() to explicitly run queries on specific databases.
# Example configuration:

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'db.sqlite3',
#     },
#     'remote': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'remote_db',
#         'USER': 'user',
#         'PASSWORD': 'password',
#         'HOST': '192.168.1.1',
#     },
# }
# 8. What are middleware in Django, and how do you create custom middleware?
# Answer: Middleware are hooks into Django’s request/response processing. They allow you to process requests and responses globally (for all views). You can use middleware to modify requests, responses, or handle exceptions. To create custom middleware:

# class MyCustomMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#     def __call__(self, request):
#         # Code to execute for each request before the view is called
#         response = self.get_response(request)
#         # Code to execute for each response after the view is called
#         return response
# dd the middleware class to MIDDLEWARE in settings.py.

# 9. How do you handle concurrency in Django?
# Answer: Concurrency can be handled using techniques like:

# Database transactions (atomic) to ensure that multiple operations on the database are treated as a single transaction.
# Optimistic locking using version numbers or timestamps to prevent race conditions when two users try to update the same data simultaneously.
# F() expressions to perform atomic updates on model fields directly in the database, avoiding race conditions.
# Select for update to lock rows during a transaction to avoid conflicts.
# 10. How do you manage security in Django applications?
# Answer:

# Use Django’s built-in security features such as:
# CSRF protection using csrf_token.
# SQL injection protection with Django ORM (use parameterized queries).
# Clickjacking protection using X-Frame-Options.
# XSS protection using template escaping.
# Enable SSL (HTTPS) and use SECURE_SSL_REDIRECT to redirect all HTTP traffic to HTTPS.
# Set secure headers, such as HSTS headers, using SECURE_HSTS_SECONDS.
# Use strong password storage with Django’s built-in password hashers.
# Regularly update Django to patch any known security vulnerabilities.

################################################################################################################

# How do you optimize Django ORM queries and profile performance?
# Optimizing the ORM for complex queries is crucial in Django applications. Understanding select_related, prefetch_related, and query profiling tools can make a big difference.

# 2. When are Django signals unsuitable, and how can you disable them selectively?

# While signals are useful for decoupling, they can lead to unexpected behaviors in complex apps. Knowing when and how to disable them is essential for maintaining control.

# 3. Explain atomic() and savepoints in Django transactions.

# Using atomic() ensures data integrity in multi-step operations, while savepoints allow finer control within a transaction.

# 4. How would you implement role-based access control in Django?

# RBAC offers more granular control over permissions. Understanding how to implement it beyond Django’s built-in groups and permissions is key.

# 5. Describe select_related vs prefetch_related with examples.

# Both methods optimize query performance, but knowing when to use each can significantly impact efficiency.

# 6. How do you create conditional custom middleware in Django?

# Middleware is powerful for request/response modifications. Customizing it conditionally helps target specific scenarios.

# 7. How can you implement real-time notifications in Django?

# Real-time functionality can be added via WebSockets, Django Channels, or Celery, enabling notifications and live data updates.

# 8. What’s the difference between @cached_property and @property?

# @cached_property stores the result after the first access, optimizing repeated calls, while @property recalculates each time.

# 9. How would you set up and manage multi-database support in Django?

# Multi-database setups allow distribution of data, but it requires careful management to avoid consistency issues.

# 10. How do you handle modifying a migration already applied in production?

# Modifying migrations in production requires caution. Understanding rollback and re-application strategies is critical.

# 11. How would you implement SSO in Django using OAuth2 or SAML?

# Implementing SSO with third-party providers enhances security and user experience. Configuring OAuth2/SAML requires backend adjustments.

# 12. How do you test asynchronous tasks (e.g., Celery) in Django?

# Testing async tasks involves handling retries, failures, and efficient test setup for quicker results in the test environment.

# These questions target the nuances of Django development and reflect the skills required to manage and scale Django applications effectively.

# Exercises:
# Write a Query using Django ORM to fetch all the books objects from your database.
# Ans:





# Write a Query using Django ORM to fetch title and published_date of all books from the database.
# Fetch first name and last name of all the new authors ( Authors with popularity_score = 0 are new authors ).
# Fetch first name and popularity score of all authors whose first name starts with A and popularity score is greater than or equal to 8.
# Fetch first name of all the authors with aa case insensitive in their first name.
# Fetch list of all the authors whose ids are in the list = [1, 3, 23, 43, 134, 25].
# Fetch list of all the publishers who joined after or in September 2012, output list should only contain first name and join date of publisher. Order by join date.
# Fetch ordered list of first 10 last names of Publishers, list must not contain duplicates.
# Get the signup date for the last joined Author and Publisher.
# Get the first name, last name and join date of the last author who joined.
# Fetch list of all authors who joined after or in year 2013
# Fetch total price of all the books written by authors with popularity score 7 or higher.
# Fetch list of titles of all books written by authors whose first name starts with ‘A’. The result should contain a list of the titles of every book. Not a list of tuples.
# Get total price of all the books written by author with pk in list [1, 3, 4]
# Produce a list of all the authors along with their recommender.
# Produce list of all authors who published their book by publisher pk = 1, output list should be ordered by first name.
# Create three new users and add in the followers of the author with pk = 1.
# Set the followers list of the author with pk = 2, with only one user.
# Add new users in followers of the author with pk = 1.
# Remove one user from the followers of the author with pk = 1.
# Get first names of all the authors, whose user with pk = 1 is following. ( Without Accessing Author.objects manager )
# Fetch list of all authors who wrote a book with “tle” as part of Book Title.
# Fetch the list of authors whose names start with ‘A’ case insensitive, and either their popularity score is greater than 5 or they have joined after 2014. with Q objects.
# Retrieve a specific object with primary key= 1 from the Author table.
# Retrieve the first N=10 records from an Author table.
# Retrieve records from a table that match this condition, popularity score = 7. And get the first and last record of that list.
# Retrieve all authors who joined after or in the year 2012, popularity score greater than or equal to 4, join date after or with date 12, and first name starts with ‘a’ (case insensitive) without using Q objects.
# Retrieve all authors who did not join in 2012.
# Retrieve Oldest author, Newest author, Average popularity score of authors, sum of price of all books in database.
# Retrieve all authors who have no recommender, recommended by field is null.
# Retrieve the books that do not have any authors, where the author is null. Also, retrieve the books whose authors are present, but do not have a recommender, where the author is not null and the author’s recommender is null. (Note that if the condition for the author not being null is not specified and only the condition for the recommender being null is mentioned, all books with both author null and author’s recommender null will be retrieved.)
# Total price of books written by author with primary key = 1. ( Aggregation over related model ), oldest book written by author with pk = 1, latest book written by author with pk = 1.
# Among the publishers in the Publishers table what is the oldest book any publisher has published.
# Average price of all the books in the database.
# Maximum popularity score of publisher among all the publishers who published a book for the author with pk = 1. (Reverse Foreign Key hop)
# Count the number of authors who have written a book which contains the phrase ‘ab’ case insensitive.
# Get all the authors with followers more than 216.
# Get average popularity score of all the authors who joined after 20 September 2014.
# Generate a list of books whose author has written more than 10 books.
# Get the list of books with duplicate titles.

# Ans:

# from main.models import *
# import datetime
# from django.db.models import Count, Avg, Sum, Max, Min
# from django.db.models import Q, F
# 1. Fetch title and published_date of all books

# Books.objects.values('title', 'published_date')
# 2. Fetch first name and last name of all new authors (popularity_score = 0)

# Author.objects.filter(popularity_score=0).values('firstname', 'lastname')
# 3. Fetch first name and popularity score of authors whose first name starts with 'A' and popularity score is >= 8

# Author.objects.filter(firstname_istartswith='A', popularity_score_gte=8).values('firstname', 'popularity_score')
# 4. Fetch first name of authors with 'aa' (case-insensitive) in their first name

# Author.objects.filter(firstname__icontains='aa').values('firstname')
# 5. Fetch authors whose IDs are in the list [1, 3, 23, 43, 134, 25]

# Author.objects.filter(id__in=[1, 3, 23, 43, 134, 25])
# 6. Fetch publishers who joined after or in September 2012, showing first name and join date, ordered by join date

# Publisher.objects.filter(joindate__gte='2012-09-01').order_by('joindate').values('firstname', 'joindate')
# 7. Fetch ordered list of first 10 last names of publishers, without duplicates

# Publisher.objects.values('lastname').distinct().order_by('lastname')[:10]
# 8. Get the signup date for the last joined Author and Publisher

# last_author_signup = Author.objects.latest('joindate').joindate
# last_publisher_signup = Publisher.objects.latest('joindate').joindate
# ans9 = [last_author_signup, last_publisher_signup]
# 9. Get first name, last name, and join date of the last author who joined

# Author.objects.latest('joindate').values('firstname', 'lastname', 'joindate')
# 10. Fetch authors who joined after or in the year 2013

# Author.objects.filter(joindate_year_gte=2013)
# 11. Fetch total price of all books written by authors with popularity score 7 or higher

# from django.db.models import Sum
# Books.objects.filter(author_popularity_score_gte=7).aggregate(total_price=Sum('price'))
# 12. Fetch titles of all books written by authors whose first name starts with 'A', as a flat list

# Books.objects.filter(author_firstname_istartswith='A').values_list('title', flat=True)
# 13. Get total price of all books written by authors with primary keys in [1, 3, 4]

# Books.objects.filter(author_id_in=[1, 3, 4]).aggregate(total_price=Sum('price'))
# 14. Produce a list of all authors along with their recommender

# Author.objects.select_related('recommendedby').values('firstname', 'lastname', 'recommendedby_firstname', 'recommendedby_lastname')
# 15. Produce list of authors who published their book by publisher with primary key = 1, ordered by first name

# Author.objects.filter(books__publisher_id=1).order_by('firstname').distinct()
# 16. Create three new users and add them as followers of the author with primary key = 1

# user1 = User.objects.create(username='user1', email='user1@example.com')
# user2 = User.objects.create(username='user2', email='user2@example.com')
# user3 = User.objects.create(username='user3', email='user3@example.com')
# author = Author.objects.get(pk=1)
# author.followers.add(user1, user2, user3)
# 17. Set the followers list of the author with primary key = 2, to only one user

# author = Author.objects.get(pk=2)
# author.followers.set([user1])  # Assuming user1 is already created
# 18. Add new users to the followers of the author with primary key = 1

# new_users = [user4, user5]  # Assuming user4 and user5 are already created
# author = Author.objects.get(pk=1)
# author.followers.add(*new_users)
# 19. Remove one user from the followers of the author with primary key = 1

# author = Author.objects.get(pk=1)
# author.followers.remove(user1)  # Assuming user1 is already created
# 20. Get first names of all authors whom the user with primary key = 1 is following

# User.objects.get(pk=1).followed_authors.values_list('firstname', flat=True)
# 21. Fetch authors who wrote a book with "tle" in the title

# Author.objects.filter(books_title_icontains='tle').distinct()
# 22. Fetch authors whose names start with 'A' (case-insensitive), and either their popularity score is greater than 5 or they joined after 2014, using Q objects

# from django.db.models import Q
# Author.objects.filter(
#     Q(firstname__istartswith='A') &
#     (Q(popularity_score_gt=5) | Q(joindateyear_gt=2014))
# )
# 23. Retrieve a specific object with primary key = 1 from the Author table

# Author.objects.get(pk=1)
# 24. Retrieve the first N=10 records from the Author table

# Author.objects.all()[:10]
# 25. Retrieve records with popularity score = 7, and get the first and last record of that list

# authors = Author.objects.filter(popularity_score=7)
# first_author = authors.first()
# last_author = authors.last()
# 26. Retrieve all authors who joined after or in 2012, popularity score >= 4, join date after 12th, and first name starts with 'a' (case-insensitive), without using Q objects

# Author.objects.filter(
#     joindate_year_gte=2012,
#     popularity_score__gte=4,
#     joindate_day_gt=12,
#     firstname__istartswith='a'
# )
# 27. Retrieve all authors who did not join in 2012

# Author.objects.exclude(joindate__year=2012)
# 28. Retrieve oldest author, newest author, average popularity score of authors, sum of price of all books

# from django.db.models import Avg, Sum
# oldest_author = Author.objects.earliest('joindate')
# newest_author = Author.objects.latest('joindate')
# avg_popularity = Author.objects.aggregate(Avg('popularity_score'))
# total_price = Books.objects.aggregate(Sum('price'))
# 29. Retrieve all authors who have no recommender (recommendedby is null)

# Author.objects.filter(recommendedby__isnull=True)
# 30. Retrieve books that do not have any authors (author is null), or books whose authors are present but do not have a recommender (author is not null and author's recommender is null)

# Books.objects.filter(
#     Q(author__isnull=True) |
#     Q(author_recommendedby_isnull=True)
# )
# 31. Total price of books written by author with primary key = 1, oldest book, and latest book

# from django.db.models import Sum
# books = Books.objects.filter(author_id=1)
# total_price = books.aggregate(Sum('price'))
# oldest_book = books.earliest('published_date')
# latest_book = books.latest('published_date')
# 32. Among the publishers, what is the oldest book any publisher has published

# Books.objects.order_by('published_date').first()
# 33. Average price of all books in the database

# Books.objects.aggregate(Avg('price'))
# 34. Maximum popularity score of publishers who published a book for the author with primary key = 1

# Publisher.objects.filter(books__author_id=1).aggregate(Max('popularity_score'))
# 35. Count the number of authors who have written a book containing the phrase 'ab' (case-insensitive) in the title

# Author.objects.filter(books_title_icontains='ab').distinct().count()
# 36. Get all authors with more than 216 followers

# Author.objects.annotate(follower_count=Count('followers')).filter(follower_count__gt=216)
# 37. Get average popularity score of authors who joined after 20th September 2014

# Author.objects.filter(joindate__gt='2014-09-20').aggregate(Avg('popularity_score'))
# 38. Generate a list of books whose author has written more than 10 books

# from django.db.models import Count
# Books.objects.filter(author_bookscount_gt=10)
# 39. Get the list of books with duplicate titles

# Books.objects.values('title').annotate(title_count=Count('title')).filter(title_count__gt=1)
