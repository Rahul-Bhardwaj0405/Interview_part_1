from django.db import models

# Create your models here.

from django.db import models

class Author(models.Model):
  firstname = models.CharField(max_length=100)
  lastname = models.CharField(max_length=100)
  address = models.CharField(max_length=200, null=True)
  zipcode = models.IntegerField(null=True)
  telephone = models.CharField(max_length=100, null=True)
  recommendedby = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='recommended_authors', related_query_name='recommended_authors', null=True)
  joindate = models.DateField()
  popularity_score = models.IntegerField()
  followers = models.ManyToManyField('User', related_name='followed_authors', related_query_name='followed_authors')
  def __str__(self):
    return f"{self.id} {self.firstname} {self.lastname}, {self.address}, Zip: {self.zipcode}, Phone: {self.telephone}, Recommended By: {self.recommendedby}, Joined: {self.joindate}, Popularity: {self.popularity_score}"

class Books(models.Model):  
  title = models.CharField(max_length=100)
  genre = models.CharField(max_length=200)
  price = models.IntegerField(null=True)
  published_date = models.DateField()
  author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='books', related_query_name='books')
  publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE, related_name='books', related_query_name='books')
  def __str__(self):
    return f"{self.title} ({self.genre}) - ₹{self.price or 'N/A'}, Published: {self.published_date or 'Unknown'}, Author: {self.author.firstname if self.author else 'N/A'}, Publisher: {self.publisher.firstname if self.publisher else 'N/A'}"

class Publisher(models.Model):
  firstname = models.CharField(max_length=100)
  lastname = models.CharField(max_length=100)
  recommendedby = models.ForeignKey('Publisher', on_delete=models.CASCADE, null=True)
  joindate = models.DateField()
  popularity_score = models.IntegerField()
  def __str__(self):
    return f"{self.firstname} {self.lastname}, Recommended By: {self.recommendedby}, Joined: {self.joindate}, Popularity: {self.popularity_score}"

class User(models.Model):
  username = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  def __str__(self):
    return f"{self.username} ({self.email})"
