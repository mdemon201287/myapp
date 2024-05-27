# app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from .models import Member
from .serializers import MemberSerializer

def home(request):
    return render(request, 'home.html')

@login_required
def index(request):
    mem = Member.objects.filter(user=request.user)
    return render(request, 'index.html', {'mem': mem})

@csrf_exempt
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@csrf_exempt
def signin_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form})

@login_required
def signout_view(request):
    logout(request)
    return redirect('home')

@login_required
@csrf_exempt
def add(request):
    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        country = request.POST['country']
        Member.objects.create(user=request.user, name=name, subject=subject, country=country)
        return redirect('index')
    return render(request, 'add.html')

@login_required
@csrf_exempt
def update(request, id):
    mem = Member.objects.get(id=id)
    if request.method == 'POST':
        mem.name = request.POST['name']
        mem.subject = request.POST['subject']
        mem.country = request.POST['country']
        mem.save()
        return redirect('index')
    return render(request, 'update.html', {'mem': mem})

@login_required
def delete(request, id):
    mem = Member.objects.get(id=id)
    mem.delete()
    return redirect('index')

class MemberViewSet(viewsets.ModelViewSet):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()

    def get_queryset(self):
        return Member.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
