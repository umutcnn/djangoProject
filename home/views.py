from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from Work.models import Work, Category, Images, BasvuruForm, Basvuru
from home.forms import SignUpForm
from home.models import Setting
from django.contrib import messages


# Create your views here.
def index(request):
    setting = Setting.objects.get(pk = 1)
    sliderdata= Work.objects.all().order_by('?')[0:7]
    categorydata = Category.objects.all()
    randomwork = Work.objects.all().order_by('?')[0:4]
    newWork = Work.objects.order_by('-create_at')[0:4]
    context= {'setting': setting, 'page': 'home','sliderdata': sliderdata,'newWork':newWork,'categorydata': categorydata,'randomwork': randomwork}
    return render(request, 'index.html', context)



def sss(request):
    setting = Setting.objects.get(pk = 1)
    sliderdata= Work.objects.all().order_by('?')[0:4]
    categorydata = Category.objects.all()
    context= {'setting': setting,'page': 'sss', 'sliderdata': sliderdata,'categorydata': categorydata}
    return render(request, 'sss.html', context)


def hakkimizda(request):
    setting = Setting.objects.get(pk = 1)
    categorydata = Category.objects.all()
    context = {'setting': setting, 'page': 'hakkimizda','categorydata': categorydata}
    return render(request, 'hakkimizda.html', context)

def iletisim(request):
    setting = Setting.objects.get(pk = 1)
    categorydata = Category.objects.all()
    context = {'setting': setting, 'page': 'iletisim','categorydata': categorydata}
    return render(request, 'iletisim.html', context)


def category_work(request,id):
    setting = Setting.objects.get(pk=1)
    categorydata = Category.objects.all()
    selectedCategory = Category.objects.filter(pk=id)
    works = Work.objects.filter(category_id=id)
    context = {'setting': setting,
               'selectedCategory': selectedCategory,
               'works': works,
               'categorydata': categorydata}
    return render(request, 'category_work.html', context)


def ilan(request):
    setting = Setting.objects.get(pk = 1)
    sliderdata= Work.objects.all()[:]
    categorydata = Category.objects.all()
    context= {'setting': setting, 'page': 'ilan','sliderdata': sliderdata,'categorydata': categorydata}
    return render(request, 'ilan.html', context)



def work_detail(request, id, slug):
    setting = Setting.objects.get(pk=1)
    categorydata = Category.objects.all()
    selectedCategory = Category.objects.filter(pk=id)
    works = Work.objects.filter(category_id=id)
    category = Category.objects.all()
    selectedwork = Work.objects.filter(pk=id)
    workImages = Images.objects.filter(work_id=id)
    context = {'setting': setting,
               'category': category,
               'selectedwork': selectedwork,
               'workImages': workImages,
               'selectedCategory': selectedCategory,
               'works': works,
               'categorydata': categorydata}
    return render(request, 'work_detail.html', context)


def work_search(request):
    if request.method == 'POST':
        from home.forms import searchs
        form = searchs(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            categorydata = Category.objects.all ()
            query = form.cleaned_data['query']
            works = Work.objects.filter(title__icontains=query)
            setting = Setting.objects.get(pk=1)
            context = {'works': works,
                       'category': category,
                       'categorydata': categorydata,
                       'setting': setting}
            return render(request, 'work_search.html',context)
    return HttpResponse('/')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/login')
    category = Category.objects.all()
    context = {'category': category, }
    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')



def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
        return HttpResponseRedirect('/')
    form = SignUpForm()
    category = Category.objects.all()
    context = {'category': category,
               'form': form, }
    return render(request, 'signup.html', context)









