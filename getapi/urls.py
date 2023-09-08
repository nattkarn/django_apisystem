from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.home, name='home'),
    path('api/v1/get_data',views.view_api, name='view_api'),
    
]


urlpatterns += staticfiles_urlpatterns()