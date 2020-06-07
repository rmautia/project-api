from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.core.validators import MaxValueValidator, MinValueValidator


class Profile(models.Model):
    main_user = models.ForeignKey(User, on_delete = models.CASCADE)
    bio = models.TextField(max_length = 300, blank = True, default = '')
    profile_pic = models.ImageField(upload_to = 'images/', null =True, blank = True, default = '')

    def __str__(self):
        return self.main_user.username

    def save_profile(self):
        self.save()

    def delete_profile(profile_id):
        Profile.objects.get(id = profile_id).delete()

    def update_profile(profile_id, xbio):
        Profile.objects.get(id = profile_id).update(bio = xbio)

    @classmethod
    def search_users(cls,name):
        users=cls.objects.filter(main_user__username__icontains=name)
        return users

    @classmethod
    def get_profile(cls,user):
        profile=cls.objects.get(main_user=user)
        return profile

class Rating(models.Model):
    project = models.CharField(max_length = 30, default = '')
    main_user = models.ForeignKey(User,on_delete=models.CASCADE)
    usability = models.IntegerField(choices=[(i, i) for i in range(1, 11)], blank=True)
    content = models.IntegerField(choices=[(i, i) for i in range(1, 11)], blank=True)
    design = models.IntegerField(choices=[(i, i) for i in range(1, 11)], blank=True)

    def __str__(self):
        return self.main_user.username
    average = models.IntegerField(blank = True, default=0)



class Project(models.Model):
    image_path = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length = 30, default = '')
    main_user = models.ForeignKey(User, on_delete = models.CASCADE)
    description = models.TextField(blank = True)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length = 100, default = '')
    reviews = models.CharField(max_length = 30, blank = True, default = 0)
    usability = models.CharField(max_length = 30, default = 0)
    content = models.CharField(max_length = 30, default = 0)
    design = models.CharField(max_length = 30, default = 0)
    rating = models.CharField(max_length = 30, default = 0)

    def __str__(self):
        return self.caption

    def save_project(self):
        self.save()

    def delete_project(project_id):
        Project.objects.filter(id = project_id).delete()

    def update_project(project_id, xcaption):
        Project.objects.filter(id = project_id).update(description = xcaption)

    def get_project_by_id(project_id):
        project = Project.objects.get(pk = project_id)
        return project

    @classmethod
    def search_project(cls, search):
        projects = cls.objects.filter(name__icontains=search).all()
        return projects

class Review(models.Model):
    project = models.CharField(max_length = 30, default = '')
    review = models.TextField(max_length = 30)
    main_user = models.ForeignKey(User,on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.review
