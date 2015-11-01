__author__ = 'veradocs-web'


from django.db import models

#  Abstract Inheritance
# ======================

# Abstract base classes are useful when you want to put some common information into a number of other models.
# You write your base class and put abstract=True in the Meta class. This model will then not be used to create any database table.
# Instead, when it is used as a base class for other models, its fields will be added to those of the child class. It is an error to have
# fields in the abstract base class with the same name as those in the child (and Django will raise an exception).



# CREATE TABLE `DjangoQuantumApp_student` (
#     `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
#     `name` varchar(100) NOT NULL,
#     `age` integer UNSIGNED NOT NULL,
#     `home_group` varchar(5) NOT NULL
# )
# ;



class CommonInfo1(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True

class Student(CommonInfo1):
    home_group = models.CharField(max_length=5)


#Meta Inheritance
# ==================

# CREATE TABLE `student_info` (
#     `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
#     `name` varchar(100) NOT NULL,
#     `age` integer UNSIGNED NOT NULL,
#     `home_group` varchar(5) NOT NULL
# )
# ;

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    class Meta:
        abstract = True
        ordering = ['name']

class Student(CommonInfo):
    home_group = models.CharField(max_length=5)
    class Meta(CommonInfo.Meta):
        db_table = 'student_info'





#proxy Inheritance
# ==================

# CREATE TABLE `DjangoQuantumApp_person2` (
#     `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
#     `first_name` varchar(30) NOT NULL,
#     `last_name` varchar(30) NOT NULL
# )
# ;

# The MyPerson class operates on the same database table as its parent Person class.
# In particular, any new instances of Person will also be accessible through MyPerson, and vice-versa:

# A proxy model must inherit from exactly one non-abstract model class.
# You can’t inherit from multiple non-abstract models as the proxy model doesn’t provide any connection
# between the rows in the different database tables. A proxy model can inherit from any number of abstract model
# classes, providing they do not define any model fields.

class Person2(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class MyPerson(Person2):
    class Meta:
        proxy = True

    def do_something(self):
        # ...
        pass

# Now normal MyPerson queries will be unordered and OrderedPerson queries will be ordered by last_name.
class OrderedPerson(Person2):
        class Meta:
            ordering = ["last_name"]
            proxy = True


# Multi-table inheritance
# ==========================

# CREATE TABLE `DjangoQuantumApp_place` (
#     `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
#     `name` varchar(50) NOT NULL,
#     `address` varchar(80) NOT NULL
# )
# ;
# CREATE TABLE `DjangoQuantumApp_restaurant` (
#     `place_ptr_id` integer NOT NULL PRIMARY KEY,
#     `serves_hot_dogs` bool NOT NULL,
#     `serves_pizza` bool NOT NULL
# )
# ;
# ALTER TABLE `DjangoQuantumApp_restaurant` ADD CONSTRAINT `place_ptr_id_refs_id_c294c6cf` FOREIGN KEY (`place_ptr_id`) REFERENCES `DjangoQuantumApp_place` (`id`);

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)


# If the parent has an ordering and you don’t want the child to have any natural ordering, you can explicitly disable it:
class ParentMode(models.Model):
    class Meta:
        ordering = ['name']

class ChildModel(ParentMode):
    # ...
    class Meta:
        # Remove parent's ordering effect
        ordering = []


# Inheritance and reverse relations
# ====================================

# #CREATE TABLE `DjangoQuantumApp_place1` (
#     `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
#     `name` varchar(50) NOT NULL,
#     `address` varchar(80) NOT NULL
# )
# ;
# CREATE TABLE `DjangoQuantumApp_supplier` (
#     `place1_ptr_id` integer NOT NULL PRIMARY KEY
# )
# ;
# ALTER TABLE `DjangoQuantumApp_supplier` ADD CONSTRAINT `place1_ptr_id_refs_id_45477b8f` FOREIGN KEY (`place1_ptr_id`) REFERENCES `DjangoQuantumApp_place1` (`id`);
#



class Place1(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

class Supplier(Place1):
    # customers = models.ManyToManyField(Place1) #Reverse query name for m2m field 'customers' clashes with related field 'Place1.supplier'. Add a related_name argument to the definition for 'customers'.
    models.ManyToManyField(Place, related_name='provider')




# Multiple inheritance
# =======================

# CREATE TABLE `DjangoQuantumApp_article` (
#     `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
#     `headline` varchar(50) NOT NULL,
#     `body` longtext NOT NULL
# )
# ;
# CREATE TABLE `DjangoQuantumApp_book` (
#     `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
#     `title` varchar(50) NOT NULL
# )
# ;
# CREATE TABLE `DjangoQuantumApp_bookreview` (
#     `article_ptr_id` integer NOT NULL UNIQUE,
#     `book_ptr_id` integer NOT NULL PRIMARY KEY
# )
# ;
# ALTER TABLE `DjangoQuantumApp_bookreview` ADD CONSTRAINT `book_ptr_id_refs_id_b5a67756` FOREIGN KEY (`book_ptr_id`) REFERENCES `DjangoQuantumApp_book` (`id`);
# ALTER TABLE `DjangoQuantumApp_bookreview` ADD CONSTRAINT `article_ptr_id_refs_id_6638ec27` FOREIGN KEY (`article_ptr_id`) REFERENCES `DjangoQuantumApp_article` (`id`);


class Article(models.Model):
    headline = models.CharField(max_length=50)
    body = models.TextField()

class Book(models.Model):
    title = models.CharField(max_length=50)

class BookReview(Book, Article):
    pass


# Field name “hiding” is not permitted

# In normal Python class inheritance, it is permissible for a child class to override any attribute from the parent class.
# In Django, this is not permitted for attributes that are Field instances (at least, not at the moment). If a base class has a
#  field called author, you cannot create another model field called author in any class that inherits from that base class.

class World(models.Model):
      country=models.CharField()

class India(World):
      # country = models.CharField() #django.core.exceptions.FieldError: Local field 'country' in class 'India' clashes with field of similar name from base class 'World'
      pass