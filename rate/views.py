from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
import datetime as dt
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer, ProjectSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly

@login_required(login_url="/accounts/login/")
def index(request):
    '''
    view function to display landing page
    '''
    current_user=request.user
    profile=Profile.objects.filter(main_user = current_user).all()

    if profile:
        return redirect('home')

    else:
        if request.method == 'POST':
            current_user = request.user
            form = ProfileForm(request.POST, request.FILES)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.main_user = current_user
                profile.save()
            return redirect('profile')
        else:
            form = ProfileForm()

    return render(request, 'register.html',{"form":form})

@login_required(login_url='/accounts/login/')
def home(request):
    '''
    view function to feeds page
    '''
    current_user=request.user
    projects = Project.objects.all()
    users = Profile.objects.all()

    form=ReviewForm()

    return render(request, 'home.html',{'projects':projects,'current_user':current_user, "users":users, "form":form})

@login_required(login_url="/accounts/login/")
def profile(request):
    title = request.user.username
    try:
        current_user=request.user
        projects=Project.objects.filter(main_user=current_user).all()
        profile=Profile.get_profile(current_user)

        if request.method == 'POST':
            form = ProjectForm(request.POST, request.FILES)
            if form.is_valid():
                project = form.save(commit=False)
                user_profile = Profile.get_profile(current_user)
                project.main_user = current_user
                project.profile = user_profile
                project.save()
            return redirect('profile')
        else:
            form = ProjectForm()

    except Exception as e:
        raise Http404()

    return render(request,"profile.html",{'profile':profile, "title":title, "projects":projects,"form":form})

@login_required(login_url='/accounts/login/')
def search(request):
    if 'project' in request.GET and request.GET['project']:
        name=request.GET.get("project")
        projects=Project.search_project(name)
        message=f'{name}'

        return render(request,'search.html',{'message':message,'projects':projects,"name":name})
    else:
        message="You did not search any project please input a project name"
        return render(request,"search.html",{"message":message})

@login_required(login_url='/accounts/login/')
def review(request,project_id):
    try:
        project=Project.objects.get(id=project_id)
    except Exception as e:
        raise  Http404()

    if request.method=='POST':
        current_user=request.user
        form=ReviewForm(request.POST)
        if form.is_valid:
            reviews=form.save(commit=False)
            reviews.main_user=current_user
            reviews.project= project_id
            reviews.save()
    else:
        form=ReviewForm()

    ratings = Rating.objects.filter(project = project_id).all()

    total = 0
    number = len(ratings)

    for rating in ratings:
        total += rating.average
        rate = total/number
        project.rating = rate

    reviews = Review.objects.filter(project = project_id).all()
    return render(request,"review.html",{"project":project,'form':form,"reviews":reviews, "ratings":ratings})

@login_required(login_url='/accounts/login/')
def rate(request, project_id):
    try:
        project=Project.objects.get(id=project_id)
    except Exception as e:
        raise  Http404()

    if request.method=='POST':
        current_user=request.user
        check = Rating.objects.filter(main_user = current_user, project = project_id).all()
        form=RateForm(request.POST)
        if form.is_valid:
            if len(check) < 1:
                ratings=form.save(commit=False)
                if ratings.usability < 11 or ratings.content < 11 or ratings.design < 11:
                    ratings.main_user=current_user
                    ratings.project= project_id
                    ratings.average = (ratings.usability + ratings.content + ratings.design)/3
                    ratings.save()
                else:
                    message = 'Rating failed! One value is not within the defined range'
                    return redirect('rate', {"message":message})
            else:
                Rating.objects.filter(main_user = current_user, project = project_id).delete()
                ratings=form.save(commit=False)
                if ratings.usability < 11 or ratings.content < 11 or ratings.design < 11:
                    ratings.main_user=current_user
                    ratings.project= project_id
                    ratings.average = (ratings.usability + ratings.content + ratings.design)/3
                    ratings.save()
                else:
                    message = 'Rating failed! One value is not within the defined range'
                    return redirect('rate', {"message":message})

            return redirect('review', project_id)

    else:
        form=RateForm()

    return render(request,"rate.html",{"project":project,'form':form})

class ProjectsList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)

        return Response(serializers.data)

    def post(self, request, format = None):
        serializers = ProjectSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status = status.HTTP_201_CREATED)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfilesList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)

        return Response(serializers.data)

    def post(self, request, format = None):
        serializers = ProfileSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status = status.HTTP_201_CREATED)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_profile(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profile = self.get_profile(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProjectDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_project(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        project = self.get_project(pk)
        serializers = ProjectSerializer(project)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        project = self.get_project(pk)
        serializers = ProjectSerializer(project, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        project = self.get_project(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
