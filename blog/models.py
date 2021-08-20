from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField #import django-ckeditor

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name 
    
    def get_absolute_url(self):
        # return reverse("detail", kwargs={"pk": self.pk})
          return reverse('home')

#this s for database it will come like categorys to override that we use verbose_name
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

# for profile with the user (djangomodel) -in members/edit_profile
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to = 'images/profile/',blank=True, null=True)
    website_url = models.CharField(max_length = 150, blank=True, null=True)
    facebook_url= models.CharField(max_length = 150, blank=True, null=True)
    twitter_url= models.CharField(max_length = 150, blank=True, null=True)
    pinterest_url = models.CharField(max_length = 150, blank=True, null=True)


    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
          return reverse('home')
    
    
class Post(models.Model):
    title = models.CharField(max_length = 150)
    header_image = models.ImageField(blank=True, null=True, upload_to = 'images') #image folder will create automatically
    title_tag = models.CharField(max_length = 150, default="common")
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    body = RichTextField(blank=True, null=True)
    # body = models.TextField()
    post_date = models.DateField(auto_now_add = True)
    category = models.CharField(max_length=255, default='coding')
    likes  = models.ManyToManyField(User, related_name = 'blog_post')
    

    #counting total likes 
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + " | "+ str(self.author)
    
    def get_absolute_url(self):
        # return reverse("detail", kwargs={"pk": self.pk})
          return reverse('home')
    

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Post'


class comment(models.Model):
    post = models.ForeignKey(Post, related_name = 'comments', on_delete = models.CASCADE)
    name = models.CharField(max_length = 250)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return '%s -%s' %(self.post.title, self.name)

    # def get_absolute_url(self):
    #     return reverse("detail", kwargs={"pk": self.kwargs['pk'] })
    #     # return reverse('home') 
    

 