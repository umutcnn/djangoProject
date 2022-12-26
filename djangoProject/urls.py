"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', include('home.urls')),
    path('hakkimizda/', views.hakkimizda, name='hakkimizda'),
    path('iletisim/', views.iletisim, name='iletisim'),
    path('home/', include('home.urls')),
    path('work/', include('Work.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('category/<int:id>', views.category_work, name='category_work'),
    path('work/<int:id>/<slug:slug>', views.work_detail, name='work_detail'),
    path('ilan/', views.ilan, name='ilan'),
    path('search/', views.work_search, name='work_search'),
    path('login/',views.login_view,name='login_view'),
    path('logout/',views.logout_view,name='logout_view'),
    path('user/', include('user.urls')),
    path('sss/', views.sss, name='sss'),
    path('signup/', views.signup_view, name='signup_view'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)

