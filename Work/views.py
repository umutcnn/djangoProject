from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from Work.models import BasvuruForm, Basvuru
from django.http import HttpResponse


def index(request):
    return HttpResponse("Work Page")


@login_required(login_url='/login')
def addbasvuru(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST': #form post edildiyse
        form = BasvuruForm(request.POST)
        if form.is_valid():
            current_user = request.user
            data = Basvuru()
            data.user_id = current_user.id
            data.work_id = id
            #data.job = form.cleaned_data['job']
            #data.cv = form.cleaned_data['cv']
            data.referans = form.cleaned_data['referans']
            data.firmaHakkindaDusunduklerin = form.cleaned_data['firmaHakkindaDusunduklerin']
            data.save()
            messages.success(request, "Yorumunuz başarı ile gönderilmiştir. Teşekkür ederiz.")
            return HttpResponseRedirect(url)
    messages.error(request, "Kaydedilme işlemi gerçekleştirilemedi. Lütfen kontrol ediniz.")
    return HttpResponseRedirect(url)

