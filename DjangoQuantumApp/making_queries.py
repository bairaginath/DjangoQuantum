from datetime import date
from DjangoQuantumApp.models import Person, Group, Membership, Publication, Article, Blog, Entry, Author

__author__ = 'veradocs-web'


def my_queries():
    # Creating objects
    blog = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')
    blog.save()
    #update
    blog.name = 'New name'
    blog.save()
    author=Author(name='bairagi',email='bairagi@gmail.com')
    author.save()
    entry=Entry(blog =blog,headline ="world is not enough",body_text ="james bond",pub_date=date(1962, 8, 16),mod_date=date(1963, 8, 16),n_comments=66,n_pingbacks=98,rating=8)
    entry.save()
    entry.authors.add(author)
    #Retrive all Objects
    all_entries=Entry.objects.all()
    #to read more queries
    # https://docs.djangoproject.com/en/1.8/topics/db/queries/
    #Retrieving specific objects with filters¶
    #exclude(**kwargs)
    #Chaining filters
    #Each time you refine a QuerySet, you get a brand-new QuerySet that is in no way bound to the previous QuerySet. Each refinement creates a separate and distinct QuerySet that can be stored, used and reused.
    #QuerySets are lazy
    #Retrieving a single object with get
    # read more about queryset APIs https://docs.djangoproject.com/en/1.8/ref/models/querysets/#queryset-api
    # Limiting QuerySets
    # Field lookups (double underscore)
    # Filters can reference fields on the model ( F expressions) (compare the value of a model field with another field on the same model)
    # The pk lookup shortcut
    # like statement
    # Caching and QuerySets (Each QuerySet contains a cache to minimize database access)
    #Complex lookups with Q objects
    # Comparing objects
    # Deleting objects
    # Copying model instances
    # Updating multiple objects at once(Be aware that the update() method is converted directly to an SQL statement. It is a bulk operation for direct updates)
    # Related objects(an Entry object e, e.blog and Blog object b,b.entry_set.all())( forword and backword relations)
    # Additional methods to handle related objects¶
    # Many-to-many relationships
    # One-to-one relationships
    # How are the backward relationships possible?
    #





def many_to_many_relation():
    p1 = Publication(title='The Python Journal')
    p1.save()
    p2 = Publication(title='Science News')
    p2.save()
    p3 = Publication(title='Science Weekly')
    p3.save()

    a1 = Article(headline='Django lets you build Web apps easily')
    a1.save()
    # Associate the Article with a Publication
    a1.publications.add(p1)

    a2 = Article(headline='NASA uses Python')
    a2.save()
    a2.publications.add(p1, p2)
    a2.publications.add(p3)
    # Create and add a Publication to an Article in one step using create()
    # new_publication = a2.publications.create(title='Highlights for Children')
    print (a1.publications.all())
    print (a2.publications.all())
    # Publication objects have access to their related Article objects
    print(p2.article_set.all())
    print(p1.article_set.all())
    print(Publication.objects.get(id=3).article_set.all())

    # Many-to-many relationships can be queried using lookups across relationships
    #https://docs.djangoproject.com/en/1.8/topics/db/examples/many_to_many/


def many_to_many_relation_through():
    ringo = Person.objects.create(name="Ringo Starr")
    paul = Person.objects.create(name="Paul McCartney")
    beatles = Group.objects.create(name="The Beatles")
    m1 = Membership(person=ringo, group=beatles,date_joined=date(1962, 8, 16),invite_reason="Needed a new drummer.")
    m1.save()
    print(beatles.members.all())
    print(ringo.group_set.all())
    m2 = Membership.objects.create(person=paul, group=beatles,date_joined=date(1960, 8, 1),invite_reason="Wanted to form a band.")
    print(beatles.members.all())
    # Unlike normal many-to-many fields, you canot use add, create, or assignment (i.e., beatles.members = [...]) to create relationships:
    # THIS WILL NOT WORK
   # beatles.members.add(Person.objects.create(name="john"))
    # NEITHER WILL THIS
    #beatles.members.create(name="George Harrison")
    # AND NEITHER WILL THIS
    #beatles.members = [Person.objects.create(name="john"), paul, ringo]
    # Beatles have broken up


    # the clear() method can be used to remove all many-to-many relationships for an instance
    beatles.members.clear()
    #Note that this deletes the intermediate model instances
    Membership.objects.all()


    # Find all the groups with a member whose name starts with 'Paul'
    Group.objects.filter(members__name__startswith='Paul')

    # Find all the members of the Beatles that joined after 1 Jan 1961
    Person.objects.filter(group__name='The Beatles',membership__date_joined__gt=date(1961,1,1))

    # you may do so by directly querying the Membership model
    ringos_membership = Membership.objects.get(group=beatles, person=ringo)

    # querying the many-to-many reverse relationship from a Person object
    ringos_membership = ringo.membership_set.get(group=beatles)

