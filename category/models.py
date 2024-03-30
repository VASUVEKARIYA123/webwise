from django.db import models

# Create your models here.
class Main_Category(models.Model):
    name = models.CharField(max_length = 100)
    hot = models.BooleanField(default = False)
    new = models.BooleanField(default = False)

    def __str__(self):
        return self.name

class Category(models.Model):
    main_category = models.ForeignKey(Main_Category,on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name + "--" + self.main_category.name
    
class Sub_Category(models.Model):
    category = models.ForeignKey(Category,on_delete = models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name + "--" + self.category.name + "--" + self.category.main_category.name 