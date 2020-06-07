from django.test import TestCase
from .models import *
import datetime as dt
# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.user = User(id = 5, username = 'photolee', password = 'Qwerty123', email = 'photolee@gmail.com')
        self.profile = Profile(id = 5, profile_pic = 'fuaad.png', main_user = self.user, bio = 'photo fo passports')

    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()

    def test_instance(self):
        self.user.save()
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_profile(self):
        self.user.save()
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_profile(self):
        self.user.save()
        self.profile.save_profile()
        Profile.delete_profile(self.profile.id)
        profiles = Profile.objects.all()
        self.assertEqual(len(profiles), 0)

    def test_search_users(self):
        self.user.save()
        self.profile.save_profile()
        profile = Profile.search_users('photolee')
        self.assertEqual(len(profile), 1)

class ProjectTestClass(TestCase):

    def setUp(self):
        self.user = User(id = 5, username = 'photolee', password = 'Qwerty123', email = 'photolee@gmail.com')
        self.profile = Profile(id = 5, profile_pic = 'fuaad.png', main_user = self.user, bio = 'photo fo passports')
        self.project = Project(id = 5, image_path = 'fuaad.png', name = 'fuaad', main_user = self.user, description = 'photo fo passports', reviews = 0, usability = 0, upload_date=dt.datetime.today(), content = 0, design = 0, profile = self.profile)

    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
        Project.objects.all().delete()

    # Testing instance
    def test_instance(self):
        self.user.save()
        self.profile.save_profile()
        self.assertTrue(isinstance(self.project, Project))

    def test_save_project(self):
        self.user.save()
        self.profile.save_profile()
        self.project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)

    def test_delete_project(self):
        self.user.save()
        self.profile.save_profile()
        self.project.save_project()
        Project.delete_project(self.project.id)
        projects = Project.objects.all()
        self.assertEqual(len(projects), 0)

    def test_get_project_by_id(self):
        self.user.save()
        self.profile.save_profile()
        self.project.save_project()
        project = Project.get_project_by_id(self.project.id)
        self.assertEqual(self.project, project)

    def test_update_project(self):
        self.user.save()
        self.profile.save_profile()
        Project.update_project(self.project.id, 'fuaad.png')
        self.assertEqual(self.project.image_path, 'fuaad.png')
