from django.db import models


class Category(models.Model):
    # models.Model - initilaizing a category database table

    #column in catergory table
    name = models.CharField(max_length=99)

    #displays name of catogory object
    def __str__(self):
        return self.name

class Tag(models.Model):
    #models.Model - initilaizing a tag database table

    name = models.CharField(max_length=99)

    #displays name of tag object
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)

    # we need search so product decription
    description = models.TextField()


    price = models.DecimalField(max_digits=10, decimal_places= 2)

    # use Foriegn Key to make column id of whichever category , ondelete deletes all products in the category
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    #product can have many tags, and tag can have many products/ True cause not all products have tags
    tags = models.ManyToManyField(Tag, blank=True)


    def __str__(self):
        return self.name
