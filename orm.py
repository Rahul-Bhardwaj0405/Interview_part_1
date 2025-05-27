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
# ans1 = Books.objects.all()
# ans2 = Books.objects.all().values_list('title', 'published_date')
# ans3 = Authors.objects.all().filter(popularity_score=0).values_list('firstname', 'lastname')
# ans4 = Authors.objects.all().filter(firstname__startswith='a', popularity_score__gte=8).values_list('firstname', 'popularity_score')
# ans5 = Authors.objects.all().filter(firstname__icontains='aa').values_list('firstname')
# ans6 = Authors.objects.all().filter(pk__in=[1, 3, 23, 43, 134, 25])
# ans7 = Authors.objects.all().filter(joindate__gte=datetime.date(year=2012, month=9, day=1)).order_by('joindate').values_list('firstname', 'joindate')
# ans8 = Publishers.objects.all().order_by('lastname').values_list('lastname').distinct()[:10]
# ans9 = [Authors.objects.all().order_by('joindate').last(),
# Publishers.objects.all().order_by('-joindate').first()]
# ans10 = Authors.objects.all().order_by('-joindate').values_list('firstname', 'lastname', 'joindate').first()
# ans11 = Authors.objects.all().filter(joindate__year__gte=2013)
# ans12 = Books.objects.all().filter(author__popularity_score__gte=7).aggregate(total_book_price=Sum('price'))
# ans13 = Books.objects.all().filter(author__firstname__contains='a').values_list('title', flat=True)
# ans14 = Books.objects.all().filter(author__pk__in=[1, 3, 4]).aggregate('price')
# ans15 = Authors.objects.all().values_list('firstname', 'recommendedby__firstname')
# ans16 = Authors.objects.all().filter(books__publisher__pk=1)
# user1 = Users.objects.create(username='user1', email='user1@test.com')
# user2 = Users.objects.create(username='user2', email='user2@test.com')
# user3 = Users.objects.create(username='user3', email='user3@test.com')
# ans17 = Authors.objects.get(pk=1).followers.add(user1, user2, user3)
# ans18 = Authors.objects.get(pk=2).followers.set(user1)
# ans19 = Authors.objects.get(pk=1).followers.add(user1)
# ans20 = Authors.objects.get(pk=1).followers.remove(user1)
# ans21 = Users.objects.get(pk=1).followed_authors.all().values_list('firstname', flat=True)
# ans22 = Authors.objects.all().filter(books__title__icontains='tle')
# ans23 = Authors.objects.all().filter(Q(firstname__istartswith='a') and ( Q(popularity_score__gt=5) or Q(joindate__year__gt=2014)))
# ans24 = Authors.objects.all().get(pk=1)
# ans25 = Authors.objects.all()[:10]
# qs = Authors.objects.all().filter(popularity_scre=7)
# author1 = qs.first()
# author2 = qs.last()
# ans26 = [author1, author2]
# ans27 = Authors.objects.all().filter(joindate__year__gte=2012, popularity_score__gte=4, joindate__day__gte=12, firstame__istartswith='a')
# ans28 = Authors.objects.all().exclude(joindate__year=2012)
# oldest_author = Authors.objects.all().aggregate(Min('joindate'))
# newest_author = Authors.objects.all().aggregate(Max('joindate'))
# avg_pop_score = Authors.objects.all().aggregate(Avg('popularity_score'))
# sum_price = Books.objects.all().aggregate(Sum('price'))
# ans29 = [oldest_author, newest_author, avg_pop_score, sum_price]
# ans30 = Authors.objects.all().filter(recommendedby__isnull=True)
# one = Books.objects.all().filter(author__isnull=False)
# two = Books.objects.all().filter(author__isnull=False, author__recommender__isnull=True)
# ans31 = [one, two]
# ans32 = Books.objects.all().filter(author__pk=1).aggregate(Sum('price'))
# ans33 = Books.objects.all().order_by('published_date').last().title
# ans34 = Books.objects.all().aggregate(Avg('price'))
# ans35 = Publishers.objects.filter(books__author__pk=1).aggregate(Max('popularity_score'))
# ans36 = Authors.objects.filter(books__title__icontains='ab').count()
# ans37 = Authors.objects.annotate(f_count=Count('followers')).filter(f_count__gt=216)
# ans38 = Authors.objects.filter(joindate__gt=datetime.date(year=2014, month=9, day=20)).aggregate(Avg('popularity_score'))
# ans39 = Books.objects.all().annotate(bk_count=Count('author__books')).filter(bk_count__gt=10).distinct()
# ans40 = Books.objects.all().annotate(count_title=Count('title')).filter(count_title__gt=1)
