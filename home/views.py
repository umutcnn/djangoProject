from django.http import HttpResponse
from django.shortcuts import render

from Work.models import work, Category, Images
from home.models import Setting


# Create your views here.
def index(request):
    setting = Setting.objects.get(pk = 1)
    sliderdata= work.objects.all().order_by('-id')[:4]
    categorydata = Category.objects.all()
    randomwork = work.objects.all().order_by('?')[0:4]
    newWork =work.objects.order_by('-create_at')[0:4]
    context= {'setting': setting, 'page': 'home','sliderdata': sliderdata,'newWork':newWork,'categorydata': categorydata,'randomwork': randomwork}
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
    setting = Setting.objects.get(pk=1)
    categorydata = Category.objects.all()
    selectedCategory = Category.objects.filter(pk=id)
    works = work.objects.filter(category_id=id)
    context = {'setting': setting,
               'selectedCategory': selectedCategory,
               'works': works,
               'categorydata': categorydata}
    return render(request, 'category_work.html', context)


def ilan(request):
    setting = Setting.objects.get(pk = 1)
    sliderdata= work.objects.all()[:]
    categorydata = Category.objects.all()
    context= {'setting': setting, 'page': 'ilan','sliderdata': sliderdata,'categorydata': categorydata}
    return render(request, 'ilan.html', context)



def work_detail(request, id, slug):
    setting = Setting.objects.get(pk=1)
    categorydata = Category.objects.all()
    selectedCategory = Category.objects.filter(pk=id)
    works = work.objects.filter(category_id=id)
    category = Category.objects.all()
    selectedwork = work.objects.filter(pk=id)
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
            query = form.cleaned_data['query']
            works = work.objects.filter(title__icontains=query)
            setting = Setting.objects.get(pk=1)
            context = {'works': works,
                       'category': category,
                       'setting': setting}
            return render(request, 'work_search.html',context)
    return HttpResponse('/')