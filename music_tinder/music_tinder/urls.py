"""music_tinder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from registration import views as rg
from app import views as ap

urlpatterns = [
    url(r'^register/', rg.register, name='register'),
    url(r'^$', ap.index, name='index'),
    url(r'^profile/$', ap.profile, name='profile'),
    url(r'^nice/(?P<user_id>\d+)$', ap.nice, name='nice'),
	url(r'^nope/(?P<user_id>\d+)$', ap.nope, name='nope'),
	url(r'^', include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)