from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from tablib import Dataset
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings

from recsys.models import User_Detail
from recsys.forms import SignUpForm
from recsys.resources import ArticleResource

def index(request):
    if request.user.is_authenticated:
        # return 'Hello world'
        return render(request, 'test.html')
    return render(request, 'home.html')
    # return 'Hello World!'

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            password = form.cleaned_data.get('password2')

            
            # return email
            if raw_password == password:
                user = authenticate(username=username, password=raw_password)
                User_Detail.objects.create(username=user,
                                        dob=form.cleaned_data.get('dob'),
                                        passport=form.cleaned_data.get('passport'),
                                        countryid=form.cleaned_data.get('countryid') )
                login(request, user)
                return redirect('index')
            else:
                return render(request, 'register.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def simple_upload(request):
    if request.method == 'POST':
        article_resource = ArticleResource()
        dataset = Dataset()
        new_persons = request.FILES['/Users/Alishbah/Desktop/ARS/ARS/recsys/data.csv']

        imported_data = dataset.load(new_articles.read())
        result = article_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            article_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html')

@login_required
def home(request, user, user_det):
    return render(request, 'home.html')