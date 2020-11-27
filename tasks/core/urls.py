from django.urls import path

from . import views

app_name = 'core' 

urlpatterns = [
    path('',views.test_view,name='test'),
    path('time/',views.current_datetime, name='time'),
]