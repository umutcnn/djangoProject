from django.http import HttpResponse
from django.shortcuts import render

from Work.models import work, Category
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
    context = {'setting': setting, 'page': 'hakkimizda'}
    return render(request, 'hakkimizda.html', context)

def iletisim(request):
    setting = Setting.objects.get(pk = 1)
    context = {'setting': setting, 'page': 'iletisim'}
    return render(request, 'iletisim.html', context)