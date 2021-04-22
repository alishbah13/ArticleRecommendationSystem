from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from tablib import Dataset
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from recsys.models import User_Detail, Article, User_Search
from recsys.forms import SignUpForm
from recsys.resources import ArticleResource
from recsys.sim import d2v

def index(request):
    if request.user.is_authenticated:
        # print(request.user)
        # user = request.user
        # print(user)
        # us = User_Detail.objects.filter(username=user.username).values('approved')
        # if us:
         # return 'Hello world'
        if request.method == 'GET': 
            search_query = request.GET.get('q')
            if search_query:
                quer = request.GET['q']
                # print(quer)
                abst = list( Article.objects.all().values_list('abstract'))
                p_ids = list( Article.objects.all().values_list('paper_id')) 

                curr =  User_Detail.objects.filter(username=request.user.username)
                cuur_i = request.user.id

                print('^^^^^^^^^^^^^^ ', curr, cuur_i)

                recommendations = d2v(quer, abst, p_ids)
                recs = []
                art = Article.objects.filter(paper_id__in= recommendations )
                # User_Search.objects.create(
                #                         query=quer,
                #                         results=art,
                #                         username=)
            else:
                art = ''
            return render(request, 'search.html', {'recs':art})
        else:
            return render(request, 'search.html')
        # else:
        #     return render(request, 'wait.html')
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
            email = form.cleaned_data.get('email')

            # return email
            if raw_password == password:
                user = authenticate(username=username, password=raw_password)
                User_Detail.objects.create(username=user,
                                        dob=form.cleaned_data.get('dob'),
                                        passport=form.cleaned_data.get('passport'),
                                        countryid=form.cleaned_data.get('countryid') )
                
                current_site = get_current_site(request)
                mail_subject = 'We will verify your account.'
                message = render_to_string('email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                })
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(
                            mail_subject, message, to=[to_email]
                )
                # email.send()

                # login(request, user)
                # return redirect('index')
                return render(request, 'wait.html')
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



