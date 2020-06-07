from rest_framework import serializers
from .models import Profile, Project

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'main_user', 'bio', 'profile_pic')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'image_path', 'name', 'main_user', 'description', 'profile', 'upload_date', 'reviews', 'usability', 'content', 'design')
