# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile,Project,User
from .forms import UserUpdateForm,ProfileUpdateForm,ProjectsForm
# Create your views here.
def landing(request):
    return render(request,'landing.html')

@login_required(login_url='/accounts/login/')
def projects(request):
    project = Project.objects.all()
    return render(request,'projects.html',{"project":project})

def register(request):
    return render(request,'registration/register_form.html')

@login_required(login_url='/accounts/login/')
def postprojects(request):
    projform = ProjectsForm()
    if request.method == "POST":
        projform = ProjectsForm(request.POST,request.FILES)
        if projform.is_valid():
           projform.save()
           return render (request,'projects.html')
        else:
           projform=ProjectsForm(request.POST,request.FILES)

    return render(request,'projects_form.html',{"projform":projform})

@login_required(login_url='/accounts/login/')
def profile(request):
    profile=Profile.objects.all()
    return render(request,'profile.html',{"profile":profile})

@login_required(login_url='/accounts/login/')
def editdp(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request,'edit.html',context)
