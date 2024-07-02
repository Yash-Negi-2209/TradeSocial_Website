from django.db import models

# Create your models here.

class Provider(models.Model):
    business_name = models.CharField(max_length=255)
    street_number = models.CharField(max_length=20)
    street_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    business_tagline = models.TextField(blank=True)
    business_description = models.TextField(blank=True)

    provider_username = models.CharField(max_length=150, unique=True)
    provider_name = models.CharField(max_length=150)
    provider_email = models.EmailField(unique=True)
    provider_mobile = models.CharField(max_length=15)
    provider_password = models.CharField(max_length=128)  

    website_link = models.URLField(blank=True)

    class Meta:
        db_table = "Users"