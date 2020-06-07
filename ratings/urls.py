from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns=[
        url('^$', views.index, name = 'index'),
        url(r'^home$', views.home, name = 'home'),
        url(r'^accounts/profile/$', views.profile, name = 'profile'),
        url(r"^search/",views.search,name="search"),
        url(r'^review/(\d+)/$',views.review,name='review'),
        url(r'^rate/(\d+)/$',views.rate,name='rate'),
        url(r'^api/profiles/$', views.ProfilesList.as_view()),
        url(r'api/profile/profile-id/(?P<pk>[0-9]+)/$',
        views.ProfileDescription.as_view()),
        url(r'^api/projects/$', views.ProjectsList.as_view()),
        url(r'api/project/project-id/(?P<pk>[0-9]+)/$',
        views.ProjectDescription.as_view()),
    ]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
