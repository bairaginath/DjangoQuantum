from django.db import models

__author__ = 'bairagi'




class UserDB(models.Model):
      email=models.EmailField(max_length=255,unique=True)
      password=models.CharField(max_length=255)
      firstName=models.CharField(max_length=255,null=True)
      lastName=models.CharField(max_length=255,null=True)



# The name of the table, myapp_person

#Once you have defined your models, you need to tell Django you are going to use those models. Do this by editing your settings file and
# changing the INSTALLED_APPS setting to add the name of the module that contains your models.py.

class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)



class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)


#ForeignKey concept
class Album(models.Model):
    artist = models.ForeignKey(Musician)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    release_date = models.DateField()
    num_stars = models.IntegerField()

# ALTER TABLE `DjangoQuantumApp_album` ADD CONSTRAINT `artist_id_refs_id_3bd17fd9` FOREIGN KEY (`artist_id`) REFERENCES `DjangoQuantumApp_musician` (`id`);


#id = models.AutoField(primary_key=True) This is an auto-incrementing primary key.
#first_name = models.CharField("person's first name", max_length=30) #Verbose field names


class Topping(models.Model):
    # ...
    pass

class Pizza(models.Model):
    # ...
    toppings = models.ManyToManyField(Topping)


# CREATE TABLE `DjangoQuantumApp_pizza_toppings` ( `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,`pizza_id` integer NOT NULL,`topping_id` integer NOT NULL, UNIQUE (`pizza_id`, `topping_id`);
#ALTER TABLE `DjangoQuantumApp_pizza_toppings` ADD CONSTRAINT `topping_id_refs_id_b32e63f0` FOREIGN KEY (`topping_id`) REFERENCES `DjangoQuantumApp_topping` (`id`);
#ALTER TABLE `DjangoQuantumApp_pizza_toppings` ADD CONSTRAINT `pizza_id_refs_id_86283cca` FOREIGN KEY (`pizza_id`) REFERENCES `DjangoQuantumApp_pizza` (`id`);


class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person)
    group = models.ForeignKey(Group)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)



class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)




class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):              # __unicode__ on Python 2
        return self.title

    class Meta:
        ordering = ('title',)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    def __str__(self):              # __unicode__ on Python 2
        return self.headline

    class Meta:
        ordering = ('headline',)


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):              # __unicode__ on Python 2
        return self.headline