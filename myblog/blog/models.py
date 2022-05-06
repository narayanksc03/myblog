from datetime import datetime

from django.db import models

# Create your models here.
class AppUser(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True,blank = True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    profile = models.FileField(upload_to='images/profile/',null=True)
    verification_code = models.CharField(max_length=20)
    is_active =  models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_removed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now())
    updated_at = models.DateTimeField(null=True)
    removed_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'app_user'
class Category:
    category = models.CharField(max_length=100)
    parent_id = models.BigIntegerField(null=True)

    class meta:
        db_table = 'app_categories'
class posts(models.Model):
    post_title =  models.CharField(max_length=100)
    post_description = models.TextField(max_length=300)
    slug = models.CharField(max_length=100)
    category_id = models.BigIntegerField(null=True)
    post_image = models.FileField('images/post/')
    user_id =  models.BigIntegerField(null=True)
    post_status = models.CharField(max_length=100)
    is_removed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now())
    updated_at = models.DateTimeField(null=True)
    removed_at = models.DateTimeField(null=True)
