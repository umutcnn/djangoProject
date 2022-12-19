from django.http import HttpResponse
from django.shortcuts import render

from Work.models import work, Category, Images
from home.models import Setting


# Create your views here.
def index(request):
    setting = Setting.objects.get(pk = 1)
    sliderdata= work.objects.all()[:4]
    categorydata = Category.objects.all()
    context= {'setting': setting, 'page': 'home','sliderdata': sliderdata,'categorydata': categorydata}
    return render(request, 'index.html', context)


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
    categorydata = Category.objects.all()
    selectedCategory = Category.objects.filter(pk=id)
    works = work.objects.filter(category_id=id)
    context = {'selectedCategory': selectedCategory,
               'works': works,
               'categorydata': categorydata}
    return render(request, 'category_work.html', context)


def work_detail(request, id):
    category = Category.objects.all()
    selectedwork = work.objects.filter(pk=id)
    workImages = Images.objects.filter(work_id=id)
    context = {'category': category,
               'selectedwork': selectedwork,
               'workImages': workImages}
    return render(request, 'work_detail.html', context)



def ilan(request):
    setting = Setting.objects.get(pk = 1)
    sliderdata= work.objects.all()[:]
    categorydata = Category.objects.all()
    context= {'setting': setting, 'page': 'ilan','sliderdata': sliderdata,'categorydata': categorydata}
    return render(request, 'ilan.html', context)