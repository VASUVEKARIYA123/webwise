from django.db import models

# Create your models here.
class slider(models.Model):
    DISCOUNT_DEAL = {
        ('HOT DEALS','HOT DEALS'),
        ('New Arraivels','New Arraivels'),
    }
    Image = models.ImageField(upload_to = 'media/slider_imgs')
    discount_deal = models.CharField(choices = DISCOUNT_DEAL, max_length=100 )
    SALE = models.IntegerField()
    Brand_Name = models.CharField(max_length = 200)
    Discount = models.IntegerField()
    Link = models.CharField(max_length = 200)

    def __str__(self):
        return self.Brand_Name
    
class banner_area(models.Model):
    Image = models.ImageField(upload_to='media/banner_img')
    discount_deal = models.CharField(max_length=100)
    Quote = models.CharField(max_length = 100)
    Discount_quote = models.CharField(max_length = 100)
    Link = models.CharField(max_length = 200, null = True)

    def __str__(self):
        return self.Quote
    
