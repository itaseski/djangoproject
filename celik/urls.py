from django.urls import path

from . import views

app_name = 'celik'
urlpatterns = [
    path('', views.index, name='index'),
    path('cookies/', views.cookies, name='cookies'),
    # picles
    path('picles/', views.pikles, name='pikles'),
    path('picles/red-onion', views.red_onion, name='red-onion'),
    # docs
    path('docs/', views.docs_index, name='docs_index'),    
    path('docs/getting-started/required-apps/', views.docs_gs_required_apps, name='docs_gs_required-apps'),
]