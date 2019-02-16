
"""E_GenomeServer URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from news.views import news_feed
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from startup.views import startupLogin
from committee.views import *
from investors.views import *
from mentor.views import *



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    ##News
    url(r'^news/$', news_feed, name="news_feed"),
    ##startup
    url(r'^startup_login/$', startupLogin, name="startupLogin"),
    #committee
    url(r'^committee_login/$', committeeLogin, name="committeeLogin"),
    url(r'^committee_registration/$', committeeRegistration, name="committeeRegistration"),
    url(r'^committee_list/$', committeeList, name="committeeList"),
    #investors
    url(r'^investor_login/$', investorLogin, name="investorLogin"),
    url(r'^investor_registration/$', investorRegistration, name="investorRegistration"),
    url(r'^investors/$', investorList, name="investorList"),
    #Mentors
    url(r'^mentor_login/$', mentorLogin, name="mentorLogin"),
    url(r'^mentor_registration/$', mentorRegistration, name="mentorRegistration"),
    url(r'^mentor_list/$', mentorList, name="mentorList"),


]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
