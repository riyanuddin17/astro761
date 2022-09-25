from django.contrib import admin                     #This is copied from urls.py Internship so that the path is proveded from Internshipp(Project) to Home(App)
from django.urls import path
from Home import views
urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("news",views.news,name='news'),
    path("contact",views.contact,name='contact'),
]