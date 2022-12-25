from Work.models import Category, Work, Images

from home.models import Setting, UserProfile

from django.shortcuts import render


def index(request):
    if request.user.id is not None:
        user = UserProfile.objects.get(user_id=request.user.id)
        settings = Setting.objects.filter(pk=0)
        categorydata = Category.objects.all ()
        setting = Setting.objects.get (pk=1)
        category = Category.objects.all ()

        context = {'category': category,
                   'user': user,
                   'settings': settings,
                   'setting': setting,
                   'categorydata': categorydata
                   }
        return render(request, 'user_profile.html', context)
