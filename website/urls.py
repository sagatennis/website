"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
import home.views
import about.views
import athletics.views
import education.views
import work.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home.views.home,name='home'),
    path('blog/',include('blog.urls')),
    path('about/',about.views.about,name='me'),
    path('athletics/',athletics.views.tennis,name='tennis'),
    path('education/',education.views.education,name='uni'),
    path('work/',work.views.work,name='job'),







] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
