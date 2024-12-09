from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('newreview/', views.add_review, name='new'),

]