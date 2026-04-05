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

