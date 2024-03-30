from django.db import models
from category.models import Category
from ckeditor.fields import RichTextField

from django.utils.text import slugify
from django.db.models.signals import pre_save



# Create your models here.
class Section(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    



    

class Product(models.Model):
    total_quantity = models.IntegerField()
    Availability = models.IntegerField()
    featured_image = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    discount = models.IntegerField()
    Product_information = RichTextField()
    model_name = models.CharField(max_length=100)

    categories = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.CharField(max_length=100)
    Description = RichTextField()
    section = models.ForeignKey(Section,on_delete=models.CASCADE)
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)
    tax = models.IntegerField(null = True)
    packing_cost = models.IntegerField(null=True)

    def __str__(self):
        return self.product_name
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("product_details", kwargs={'slug': self.slug})

    class Meta:
        db_table = "product_Product"
        
def create_slug(instance, new_slug=None):
    slug = slugify(instance.product_name)
    if new_slug is not None:
        slug = new_slug
    qs = Product.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, Product)


class Coupon_Code(models.Model):
    code = models.CharField(max_length=100)
    discount = models.IntegerField()
    max_use = models.IntegerField()
    total_used = models.IntegerField()

    def __str__(self):
        return self.code

class Product_Image(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image_url = models.CharField(max_length=200)

class Additional_Information(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    specification = models.CharField(max_length=100)
    details =models.CharField(max_length=100)