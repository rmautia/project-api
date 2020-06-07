from django import forms
from .models import *

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['main_user', 'profile', 'upload_date', 'reviews', 'usability', 'content', 'design', 'rating']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude=['main_user','project', 'upload_date']

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['main_user']

class RateForm(forms.ModelForm):
    class Meta:
        model=Rating
        exclude=['main_user', 'project', 'average']
