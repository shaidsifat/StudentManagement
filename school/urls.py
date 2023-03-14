
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from school.views import (ListofclassApiView,ListofclassApideleteView,FilterApiview)

urlpatterns = [

    path('ListofclassApiView/', ListofclassApiView.as_view(),name=' ListofclassApiView'),
    path('ListofclassApiUpdateDeleteView/<str:pk>', ListofclassApideleteView.as_view(),name=' ListofclassApiViewdelte'),
    path('FilterForsubject/',FilterApiview.as_view(),name='FilterApiview'),
]