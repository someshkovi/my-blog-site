from django.urls import path, re_path
from mysite import views

urlpatterns = [

    # The home page
    path('', views.index, name='mysite'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
